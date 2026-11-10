"""Simulator API: one local service the lesson panel and the chatbot talk to, instead of log files.

    python -I -m simapi.server [--log udp|tail] [--port 47900]     (run from the lesson-studio folder)

It listens on 127.0.0.1 only and sends no cross-origin headers, so other websites in the browser
can't call it. Endpoints (JSON):

  GET  /api/health             sources, online/offline, armrest link
  GET  /api/state              current machine state (game file, last values sent/returned, lights, controls)
  GET  /api/events?since=T     events after time T (epoch seconds); /api/stream for live Server-Sent Events
  GET  /api/lessons            lesson files available
  POST /api/lesson/start       {"id": "field-ready-r4045"}
  GET  /api/lesson             what the panel should show now (step, hint due, mistakes, progress)
  POST /api/lesson/skip        skip the current step
  POST /api/lesson/showme      perform the current step through the virtual armrest
  GET  /api/chatbot-context    what to hand the RAG chatbot for the current step
  POST /api/armrest            {"cmd": "press master_spray 300"} pass-through to the virtual armrest
  GET  /api/manual/figure-map  which 612R manual figure shows each control and screen target, plus handle hotspots
  GET  /api/manual/<KEY>.png   one manual figure (from manual/figures)
"""
import argparse
import glob
import json
import os
import queue
import re
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from .lesson import LessonRun
from .sources import Armrest, GameFile, LogTail, LogUdp
from .store import Store

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSON_DIR = os.path.join(ROOT, "lessons")


CONTROLS_PATH = os.path.join(ROOT, "virtual-commandarm", "controls.json")
SCREEN_MAP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screens", "apr20-r4045.json")
MANUAL_DIR = os.path.join(ROOT, "manual")
FIGURE_MAP_PATH = os.path.join(MANUAL_DIR, "figure-map.json")
FIGURE_KEY = re.compile(r"^[A-Z0-9]{3,16}$")
OPS_DIR = os.path.join(ROOT, "operations")
OPS_TYPES = {".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8",
             ".js": "text/javascript; charset=utf-8", ".png": "image/png"}


class App:
    def __init__(self, log_mode, profile=None):
        from . import profiles
        self.profile = profile or profiles.get("apr20")
        self.controls = json.load(open(CONTROLS_PATH, encoding="utf-8"))
        self.controls_by_id = {c["id"]: c for c in self.controls["controls"]}
        self.modules = {m["id"]: m["name"] for m in self.controls["modules"]}
        self.screen_map = json.load(open(SCREEN_MAP_PATH, encoding="utf-8"))
        self.figure_map = (json.load(open(FIGURE_MAP_PATH, encoding="utf-8")) if os.path.isfile(FIGURE_MAP_PATH)
                           else {"controls": {}, "screen": {}, "figures": {}, "handle": None})
        self.figure_index = self._load_figure_index()
        self.store = Store()
        self.armrest = Armrest()
        self.log_mode = log_mode
        p = self.profile
        if log_mode == "udp":
            self.log_source = LogUdp(self.store.add)
        else:
            self.log_source = LogTail(self.store.add, path=lambda: profiles.log_path(p), aliases=p["aliases"])
        self.log_source.start()
        GameFile(self.store.add, path=p["game_path"]).start()
        if p["armrest_as_sent"]:
            # this build logs no control values: what the linked virtual armrest sends is what the app sends
            self.store.subscribe(self._armrest_to_sent)
        self.armrest_ok = False
        self.replay = None
        if p["armrest_as_sent"]:
            # the REAL armrest on this build: read from the app's Message Replay Logger file (see ReplayTail)
            from .sources import ReplayTail
            self.replay = ReplayTail(
                self.store.add, controls_doc=self.controls, skip=lambda: self.armrest_ok,
                dir_fn=lambda: os.path.join(profiles.running_dir(p["process"]) or p["app_dir"], "logs", "ReplayLogs"))
            self.replay.start()
            self.store.subscribe(self._replay_link)
        self.run = None
        self.view = None
        self.lock = threading.Lock()
        self.setup_lock = threading.Lock()
        self.streams = []
        self.store.subscribe(self._fanout)
        threading.Thread(target=self._armrest_loop, daemon=True).start()
        threading.Thread(target=self._lesson_loop, daemon=True).start()

    def _armrest_loop(self):
        while True:
            if not self.armrest_ok and self.armrest.available():
                try:
                    st = self.armrest.state()
                    now = time.time()
                    self.store.add((now, "link", "connected" if st.get("connected") else "disconnected", ""))
                    for cid, v in (("foot_switch", st["footSwitch"]), ("park_slot", st["parked"])):
                        self.store.add((now, "control", cid, "1" if v else "0"))
                    self.store.add((now, "control", "lever", str(st["lever"])))
                    self.store.add((now, "control", "steering", str(int(st["wheelTarget"]))))
                    self.store.add((now, "control", "speed_dial", str(st["speedDial"])))
                    for cid in st.get("lit", []):
                        self.store.add((now, "led", cid, "1"))
                    self.armrest.watch(self.store.add, on_end=self._armrest_lost)
                    self.armrest_ok = True
                except OSError:
                    pass
            time.sleep(2)

    @property
    def real_armrest(self):
        """The real armrest is feeding us through the replay log (and the virtual one is not running)."""
        return bool(self.replay and self.replay.live and not self.armrest_ok)

    @property
    def any_armrest(self):
        return self.armrest_ok or self.real_armrest

    def _replay_link(self, ev):
        """The app's bridge went down (Disconnect, or the app closed): the real armrest is no longer linked."""
        t, kind, name, value = ev
        if self.replay and self.replay.live and kind == "app" and (
                (name == "bridge" and value == "disconnect pressed") or (name == "app" and value == "exited")):
            self.replay.live = False
            self.store.add((t, "link", "disconnected", ""))

    def _armrest_lost(self):
        """The virtual armrest closed: say so, and stop treating its link as connected."""
        self.armrest_ok = False
        self.store.add((time.time(), "link", "disconnected", ""))

    def _lesson_loop(self):
        while True:
            with self.lock:
                if self.run is not None:
                    before = self.view.get("step") if self.view else None
                    self.view = self.run.poll()
                    if self.view.get("advanced") or self.view.get("step") != before or self.view.get("mistakes"):
                        self._fanout((time.time(), "lesson", self.view.get("step") or "finished",
                                      json.dumps({k: self.view.get(k) for k in ("index", "of", "say", "mistakes", "finished")})))
            time.sleep(0.25)

    def _armrest_to_sent(self, ev):
        """For builds that don't log what they send (Aug 26): turn the virtual armrest's control events into the
        'sent' events the Apr 20 build would have logged, using the same decoding the app applies. Only while
        the armrest is linked to the app, because only then does the app receive them."""
        t, kind, name, value = ev
        if kind != "control" or not (self.store.armrest_link and self.store.armrest_link[0] == "connected"):
            return
        sent = None
        if name == "lever":
            parked = self.store.controls.get("park_slot", ("0",))[0] == "1"
            if not parked:
                sent = ("PLT_HydroHandlePosition", value)
        elif name == "park_slot":
            sent = ("PLT_NeutralSlotStatus", "1" if value == "1" else "0")
        elif name == "speed_dial":
            try:
                sent = ("PLT_MHC_Encoder", str(int(value) % 49 * 500 + 1000))
            except ValueError:
                pass
        elif name == "steering":
            try:
                lock = self.profile["steer_full_lock_deg"]
                wheel = max(-lock, min(lock, float(value)))
                sent = ("PLT_SteeringWheelAngleDeg", f"{wheel * 35 / lock:g}")
            except ValueError:
                pass
        else:
            vio = self.controls_by_id.get(name, {}).get("vio")
            if vio:
                sent = (vio, "1" if value not in ("0", "") else "0")
        if sent:
            self.store.add((t, "sent", sent[0], sent[1]))

    def _fanout(self, ev):
        for q in list(self.streams):
            try:
                q.put_nowait(ev)
            except queue.Full:
                pass

    @staticmethod
    def _load_figure_index():
        """Page and caption of every figure in the 612R manual (manual/figures.jsonl, captions.jsonl)."""
        index = {}
        try:
            for line in open(os.path.join(MANUAL_DIR, "figures.jsonl"), encoding="utf-8"):
                f = json.loads(line)
                index[f["key"]] = {"page": f.get("pdf_page"), "callouts": f.get("callouts") or {}, "caption": ""}
            for line in open(os.path.join(MANUAL_DIR, "captions.jsonl"), encoding="utf-8"):
                c = json.loads(line)
                if c["key"] in index:
                    index[c["key"]]["caption"] = (c.get("caption") or "").replace(f"Figure {c['key']} shows ", "")
        except OSError:
            pass
        return index

    def step_figure(self, step):
        """The manual figure that best shows a step (see operations.step_figure)."""
        from .operations import step_figure
        return step_figure(step, self.run.lesson if self.run else None, self.figure_map)

    # ---- "show me where": armrest controls and screen targets for the current step
    def where(self, view):
        """Adds what the UI needs to point at things: armrest controls (with module) and screen targets.
        A step's own "display" list wins; otherwise targets are matched through the controls they relate to."""
        if not view or view.get("finished"):
            return view
        step = self.run.current() if self.run else None
        ids = view.get("controls", [])
        view = dict(view)
        fm = self.figure_map
        extra = (self.run.lesson.get("extra_controls") or {}) if self.run else {}

        def entry(i):
            if i in self.controls_by_id or i not in extra:
                return {"id": i, "label": self.controls_by_id.get(i, {}).get("label", i),
                        "module_id": self.controls_by_id.get(i, {}).get("module"),
                        "module": self.modules.get(self.controls_by_id.get(i, {}).get("module"), ""),
                        "sends": self.controls_by_id.get(i, {}).get("vio"),
                        "certainty": self.controls_by_id.get(i, {}).get("certainty"),
                        "manual": fm["controls"].get(i)}
            x = extra[i]          # a 612R control the lesson declares itself
            return {"id": i, "label": x.get("label", i), "module_id": None, "module": x.get("where", ""),
                    "sends": None, "certainty": "manual",
                    "manual": {"handle": None, "figures": [x["figure"]] if x.get("figure") else [],
                               "certainty": "manual", "where": x.get("where", "")}}

        view["armrest"] = [entry(i) for i in ids]
        explicit = (step or {}).get("display")
        if explicit:
            targets = [t for t in self.screen_map["targets"] if t["id"] in explicit]
        else:
            # matched through the step's controls: one touch target per control, two things to watch at most,
            # so the panel and the ring overlay never point at half the screen
            targets, looks = [], 0
            for c in ids:
                for kind in ("touch", "look"):
                    hit = next((t for t in self.screen_map["targets"] if t["kind"] == kind and c in t["controls"] and t not in targets), None)
                    if hit and (kind == "touch" or looks < 2):
                        targets.append(hit)
                        looks += kind == "look"
        targets = [dict(t, figure=fm["screen"].get(t["id"])) for t in targets]
        view["screen"] = {"press": [t for t in targets if t["kind"] == "touch"],
                          "watch": [t for t in targets if t["kind"] == "look"]}
        keys = [step["figure"]] if step and step.get("figure") else []
        for a in view["armrest"]:
            for k in (a["manual"] or {}).get("figures", []):
                if k not in keys:
                    keys.append(k)
        for t in targets:
            if t.get("figure") and t["figure"] not in keys:
                keys.append(t["figure"])
        view["figures"] = [dict(fm["figures"].get(k) or self.figure_index.get(k, {}), key=k) for k in keys]
        return view

    # ---- lesson actions
    def setup_lesson(self, lesson_id):
        """Put the simulator in the lesson's starting state through the virtual armrest. Holds the setup lock,
        so a lesson started meanwhile waits: setup presses must never count as the trainee's."""
        with self.setup_lock:
            return self._setup_lesson(lesson_id)

    def _setup_lesson(self, lesson_id):
        path = os.path.join(LESSON_DIR, lesson_id + ".json")
        if not os.path.isfile(path):
            raise FileNotFoundError(f"no lesson '{lesson_id}'")
        if not self.armrest_ok:
            raise RuntimeError("setup needs the virtual armrest; on a real rig follow the trainer note")
        lesson = LessonRun.load(path)
        setup = lesson.get("setup", {})
        self.armrest.run_script(setup.get("armrest", []))
        time.sleep(0.8)
        expect = setup.get("expect", {}).get("game", {})
        for field, cmd in (("ladderRaised", "press ladder 300"), ("cameraView", "press camera_toggle 300")):
            if field in expect and self.store.game.get(field, ("?",))[0] != expect[field]:
                self.armrest.run_script([cmd, "wait 0.6"])
        state = {k: self.store.game.get(k, ("?",))[0] for k in expect}
        return {"ok": state == expect, "expected": expect, "now": state, "trainer": setup.get("trainer")}

    def start_lesson(self, lesson_id, section=None):
        """Start a lesson; `section` (0-based) resumes a long lesson at that section's checkpoint."""
        with self.setup_lock:          # wait for a setup still pressing buttons
            pass
        path = os.path.join(LESSON_DIR, lesson_id + ".json")
        if not os.path.isfile(path):
            raise FileNotFoundError(f"no lesson '{lesson_id}'")
        lesson = LessonRun.load(path)
        with self.lock:
            self.run = LessonRun(lesson, self.store, online=None, armrest=self.any_armrest)
            if section:
                first = next((i for i, (si, _, _) in enumerate(self.run.steps) if si >= int(section)), None)
                if first is not None:
                    for sid in [st["id"] for _, _, st in self.run.steps[:first]]:
                        self.run.log.append((time.time(), "skipped", sid, "resumed at a later checkpoint"))
                    self.run.index = first
                    self.run.restart_step()
            self.view = self.run.poll()
        return self.view

    def confirm(self, item):
        """The trainee pressed Done on something the simulator can't sense."""
        with self.lock:
            if self.run is None or self.run.finished:
                return {"ok": False, "error": "no lesson running"}
            self.store.add((time.time(), "confirm", item or "*", self.run.current()["id"]))
        return {"ok": True}

    def show_me(self):
        with self.lock:
            step = self.run.current() if self.run else None
        if step is None:
            raise RuntimeError("no lesson step to show")
        if not self.armrest_ok:
            raise RuntimeError("show me needs the virtual armrest")
        self.armrest.run_script(step.get("show_me", []))
        return {"performed": step.get("show_me", [])}


def make_handler(app):
    class H(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            pass

        def _json(self, code, body):
            data = json.dumps(body, indent=1).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def _body(self):
            n = int(self.headers.get("Content-Length") or 0)
            if n == 0:
                return {}
            if not (self.headers.get("Content-Type") or "").startswith("application/json"):
                raise ValueError("send JSON (Content-Type: application/json)")
            return json.loads(self.rfile.read(n).decode("utf-8"))

        def do_GET(self):
            u = urlparse(self.path)
            try:
                if u.path == "/api/health":
                    return self._json(200, {
                        "ok": True, "build": app.profile["name"], "build_label": app.profile["label"],
                        "online": app.store.online(), "armrest": app.any_armrest,
                        "armrest_source": ("virtual" if app.armrest_ok else "real (replay log)" if app.real_armrest
                                           else None),
                        "armrest_link": app.store.armrest_link[0] if app.store.armrest_link else None,
                        "log_source": app.log_mode, "udp_lines": getattr(app.log_source, "received", None),
                        "events": len(app.store.events), "app": {k: v[0] for k, v in app.store.app.items()}})
                if u.path == "/api/state":
                    return self._json(200, app.store.snapshot())
                if u.path == "/api/events":
                    since = float(parse_qs(u.query).get("since", ["0"])[0])
                    return self._json(200, [list(e) for e in app.store.since(since)][-500:])
                if u.path == "/api/lessons":
                    out = []
                    for p in sorted(glob.glob(os.path.join(LESSON_DIR, "*.json"))):
                        try:
                            L = json.load(open(p, encoding="utf-8"))
                            out.append({"id": L["id"], "title": L["title"], "machine": L.get("machine"),
                                        "steps": sum(len(s["steps"]) for s in L["sections"]), "minutes": L.get("minutes")})
                        except (ValueError, KeyError):
                            continue
                    return self._json(200, out)
                if u.path == "/api/lesson":
                    with app.lock:
                        if app.run is None:
                            return self._json(200, {"running": False})
                        return self._json(200, {"running": True, "lesson": app.run.lesson["id"], "view": app.where(app.view),
                                                "log": [list(x) for x in app.run.log[-50:]]})
                if u.path == "/api/controls":
                    return self._json(200, app.controls)
                if u.path == "/api/screen-map":
                    return self._json(200, app.screen_map)
                if u.path == "/api/manual/figure-map":
                    return self._json(200, app.figure_map)
                if u.path.startswith("/api/manual/") and u.path.endswith(".png"):
                    key = u.path[len("/api/manual/"):-4]
                    path = os.path.join(MANUAL_DIR, "figures", key + ".png")
                    if not FIGURE_KEY.match(key) or not os.path.isfile(path):
                        return self._json(404, {"error": "no manual figure " + key})
                    data = open(path, "rb").read()
                    self.send_response(200)
                    self.send_header("Content-Type", "image/png")
                    self.send_header("Content-Length", str(len(data)))
                    self.send_header("Cache-Control", "max-age=86400")
                    self.end_headers()
                    self.wfile.write(data)
                    return
                if u.path == "/api/screens":
                    from . import screens
                    return self._json(200, screens.screens())
                if u.path.startswith("/api/screen/") and u.path.endswith(".png"):
                    from . import screens
                    png = screens.capture_png(u.path[len("/api/screen/"):-4])
                    if png is None:
                        return self._json(404, {"error": "that window isn't open (the display and corner post appear after Launch Machine Simulator)"})
                    self.send_response(200)
                    self.send_header("Content-Type", "image/png")
                    self.send_header("Content-Length", str(len(png)))
                    self.send_header("Cache-Control", "no-store")
                    self.end_headers()
                    self.wfile.write(png)
                    return
                if u.path in ("/", "/panel"):
                    data = open(os.path.join(os.path.dirname(__file__), "panel.html"), "rb").read()
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.send_header("Content-Length", str(len(data)))
                    self.send_header("Cache-Control", "no-store")
                    self.end_headers()
                    self.wfile.write(data)
                    return
                if u.path == "/api/lesson/plan":
                    with app.lock:
                        if app.run is None:
                            return self._json(200, {"running": False})
                        status = {}
                        for t, kind, sid, text in app.run.log:
                            if kind in ("done", "skipped"):
                                status[sid] = kind
                        return self._json(200, {
                            "running": True, "id": app.run.lesson["id"], "title": app.run.lesson["title"],
                            "machine": app.run.lesson.get("machine"), "objective": app.run.lesson.get("objective"),
                            "trainer_setup": app.run.lesson.get("setup", {}).get("trainer"),
                            "index": app.run.index,
                            "sections": [{"title": s["title"], "steps": [{"id": st["id"], "say": st["say"],
                                          "status": status.get(st["id"]), "confidence": st.get("confidence"),
                                          "controls": st.get("controls", []), "figure": app.step_figure(st)}
                                         for st in s["steps"]]} for s in app.run.lesson["sections"]]})
                if u.path == "/api/chatbot-context":
                    with app.lock:
                        if app.run is None:
                            return self._json(200, {"lesson": None, "state": app.store.snapshot()})
                        return self._json(200, app.run.chatbot_context(app.store.snapshot()))
                if u.path == "/api/stream":
                    return self._stream()
                if u.path.startswith("/operations"):
                    return self._operations(u.path)
                return self._json(404, {"error": "not found"})
            except Exception as ex:          # keep the service up whatever a request does
                return self._json(500, {"error": str(ex)})

        def do_POST(self):
            u = urlparse(self.path)
            try:
                body = self._body()
                if u.path == "/api/lesson/setup":
                    return self._json(200, app.setup_lesson(body.get("id", "")))
                if u.path == "/api/lesson/start":
                    return self._json(200, app.start_lesson(body.get("id", ""), body.get("section")))
                if u.path == "/api/lesson/confirm":
                    return self._json(200, app.confirm(body.get("item")))
                if u.path == "/api/lesson/stop":
                    with app.lock:
                        app.run, app.view = None, None
                    return self._json(200, {"ok": True})
                if u.path == "/api/lesson/skip":
                    with app.lock:
                        if app.run:
                            app.run.skip("skipped by trainee or trainer")
                    return self._json(200, {"ok": True})
                if u.path == "/api/screen/tap":
                    # {"window": "display", "x": 0.5, "y": 0.9} or {"target": "run.softkey.menu"}
                    from . import screens
                    if body.get("target"):
                        t = next((t for t in app.screen_map["targets"] if t["id"] == body["target"]), None)
                        if not t:
                            return self._json(404, {"error": "no screen target " + body["target"]})
                        r = t["rect"]
                        return self._json(200, screens.tap(t["window"], (r[0] + r[2]) / 2, (r[1] + r[3]) / 2))
                    return self._json(200, screens.tap(body.get("window", "display"), float(body["x"]), float(body["y"])))
                if u.path == "/api/lesson/showme":
                    return self._json(200, app.show_me())
                if u.path == "/api/armrest":
                    return self._json(200, {"reply": app.armrest.cmd(body["cmd"])})
                return self._json(404, {"error": "not found"})
            except (ValueError, KeyError, FileNotFoundError, RuntimeError, OSError) as ex:
                return self._json(400, {"error": str(ex)})

        def _operations(self, path):
            """The app's Operations panel, live (lesson-studio/operations). Served from here so the page and the
            API share one origin: the API stays without cross-origin headers."""
            from . import operations
            if path in ("/operations", "/operations/"):
                self.send_response(302)
                self.send_header("Location", "/operations/OperatingProcedure.html")
                self.end_headers()
                return
            if path == "/operations/lessons.js":
                data, ctype = operations.lessons_js(LESSON_DIR, app.figure_map).encode("utf-8"), OPS_TYPES[".js"]
            else:
                full = os.path.normpath(os.path.join(OPS_DIR, path[len("/operations/"):]))
                ctype = OPS_TYPES.get(os.path.splitext(full)[1].lower())
                if not full.startswith(OPS_DIR + os.sep) or not ctype or not os.path.isfile(full):
                    return self._json(404, {"error": "not found"})
                with open(full, "rb") as fh:
                    data = fh.read()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def _stream(self):
            q = queue.Queue(maxsize=1000)
            app.streams.append(q)
            try:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                while True:
                    try:
                        ev = q.get(timeout=15)
                        msg = json.dumps({"t": ev[0], "kind": ev[1], "name": ev[2], "value": ev[3]})
                        self.wfile.write(f"data: {msg}\n\n".encode("utf-8"))
                    except queue.Empty:
                        self.wfile.write(b": keep-alive\n\n")
                    self.wfile.flush()
            except OSError:
                pass
            finally:
                app.streams.remove(q)
    return H


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=47900)
    ap.add_argument("--log", choices=["tail", "udp"], default="tail",
                    help="tail = follow log.txt (no app change); udp = live lines from the app's UdpAppender")
    ap.add_argument("--build", default="auto",
                    help="which Connections app build to watch: apr20, aug26, or auto (the one running now)")
    a = ap.parse_args()
    from . import profiles
    profile = profiles.get(profiles.detect() if a.build == "auto" else a.build)
    app = App(a.log, profile)
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), make_handler(app))
    print(f"Simulator API on http://127.0.0.1:{a.port}/api/health  (build: {profile['label']}; log: {profiles.log_path(profile)}; "
          f"game file: {profile['game_path']})", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()
