"""Evidence sources for the simulator API. Standard library only.

* LogTail   - follows the Connections app's log.txt from its current end; turns lines into events:
                ("sent",  signal, value)   the app sent a control value to the cloud
                ("cloud", signal, value)   the cloud sent a value back
                ("app",   what,  detail)   app milestones (bridge connected, sign-in, display up...)
* GameFile  - polls VehicleInfo.xml (what the app tells Farming Simulator) -> ("game", field, value)
* Armrest   - the virtual armrest's scripted port: commands, plus its event stream
                ("control", id, value), ("led", id, value), ("link", state, "")

Every event is a tuple (time, kind, name, value) with time = time.time() on this PC.
"""
import glob
import json
import os
import re
import socket
import threading
import time
import xml.etree.ElementTree as ET
from datetime import datetime

APP_DIR = r"C:\Simulator\Apr20_LTTS_FS25_ConnectionsApp_2\net8.0-windows"
LOG_PATH = os.path.join(APP_DIR, "log.txt")
GAME_PATH = os.path.join(os.path.expanduser("~"), "Documents", "My Games", "FarmingSimulator2025",
                         "mods", "DeereVehicleControl", "src", "VehicleInfo.xml")
ARMREST_PORT = 47800

_TS = re.compile(r"^(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d),(\d{3}) ")
_SENT = re.compile(r'SendVIOData\(\): ActiveMQ data to send to EC2\. Data: \{"signal":"([^"]+)","value":"([^"]*)"\}')
_CLOUD = re.compile(r"OnStompMessageReceived\(\): ActiveMQ data received from EC2: (\{.*\})\s*$")
_APP = [
    (re.compile(r"MainWindow\.MainWindow\(\): InitializeComponent complete"), "app", "started"),
    (re.compile(r"MainWindow\.ExitApp\(\): Exiting"), "app", "exited"),
    # Aug 26 build (SimulatorConnections 3.2.0)
    (re.compile(r"MainWindow\.MainWindow\(\): Starting Connections App"), "app", "started"),
    (re.compile(r"MainWindow\.OnAppExit\(\): Initiating MainWindow application exit"), "app", "exited"),
    (re.compile(r"HandleSimulatorBridgeConnected\(\): Subscribing to SBM notifications"), "bridge", "connected"),
    (re.compile(r"DisplayStreamingManager\.LaunchDisplay\(\): Launching display"), "display", "launched"),
    (re.compile(r"HandleMonitorDaemonAvailableResponseAsync\(\): No devices available"), "bridge", "no armrest found"),
    (re.compile(r"Connect to Simulator Bridge button pressed"), "bridge", "connect pressed"),
    (re.compile(r"Disconnect from Simulator Bridge button pressed"), "bridge", "disconnect pressed"),
    (re.compile(r"SBM detected at COM port (\S+)"), "bridge", "box found"),
    (re.compile(r"Launch Machine Simulator button pressed"), "machine_sim", "launch pressed"),
    (re.compile(r"Shutdown Machine Simulator"), "machine_sim", "shutdown pressed"),
    (re.compile(r"Sign in complete"), "sign_in", "complete"),
    (re.compile(r"Established Stomp connection"), "cloud_link", "up"),
    (re.compile(r"Launching display with URL"), "display", "launched"),
    (re.compile(r"ActiveMQ connection closed|remote party closed"), "cloud_link", "down"),
    (re.compile(r"Launch Farming Simulator button pressed"), "farming_sim", "launch pressed"),
]


def _line_time(line):
    m = _TS.match(line)
    if not m:
        return None
    return datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").timestamp() + int(m.group(2)) / 1000


def parse_log_line(line):
    """Return a list of events for one log line (usually zero or one)."""
    t = _line_time(line)
    if t is None:
        return []
    m = _SENT.search(line)
    if m:
        return [(t, "sent", m.group(1), m.group(2))]
    m = _CLOUD.search(line)
    if m:
        try:
            body = json.loads(m.group(1))
        except ValueError:
            return []
        sigs = body.get("signals") or body.get("Signals") or []
        out = [(t, "cloud", s.get("signal"), str(s.get("value"))) for s in sigs if isinstance(s, dict)]
        if "display_init" in body:
            out.append((t, "app", "display", "init " + str(body["display_init"])))
        return out
    for rx, what, detail in _APP:
        if rx.search(line):
            return [(t, "app", what, detail)]
    return []


class LogTail(threading.Thread):
    """Follows the app's log. `path` may be a function returning the file to follow now (the Aug 26 build writes a
    new daily file per start); `aliases` maps the build's signal names to the canonical (Apr 20) ones."""

    def __init__(self, sink, path=LOG_PATH, poll=0.25, from_start=False, aliases=None):
        super().__init__(daemon=True, name="log-tail")
        self.path_fn = path if callable(path) else (lambda: path)
        self.path = self.path_fn()
        self.aliases = aliases or {}
        self.sink = sink if not self.aliases else (lambda ev: sink(self._alias(ev)))
        self.poll = poll
        self.pos = 0 if from_start else (os.path.getsize(self.path) if os.path.exists(self.path) else 0)
        self.buf = b""
        self.stop = False
        self._last_resolve = 0.0

    def _alias(self, ev):
        t, kind, name, value = ev
        return (t, kind, self.aliases.get(name, name), value)

    def _resolve(self):
        """Switch to a newer log file (new day or new app start); read the new one from its start."""
        if time.time() - self._last_resolve < 2:
            return
        self._last_resolve = time.time()
        p = self.path_fn()
        if p != self.path:
            self.path, self.pos, self.buf = p, 0, b""

    def catch_up(self, max_bytes=12 * 1024 * 1024):
        """Replay the app milestones (sign-in, cloud link, display) of the app's current run, so an
        API started after sign-in still knows it's online. Only 'app' events; past presses are not replayed."""
        if not self.pos:
            return
        try:
            with open(self.path, "rb") as fh:
                fh.seek(max(0, self.pos - max_bytes))
                data = fh.read(self.pos - fh.tell())
        except OSError:
            return
        events = []
        for raw in data.split(b"\n"):
            line = raw.decode("utf-8", "replace").rstrip("\r")
            if "SendVIOData" in line or "Found ports" in line:
                continue
            for ev in parse_log_line(line):
                if ev[1] != "app":
                    continue
                if ev[2] == "app" and ev[3] == "started":
                    events = []           # an app restart wipes the earlier run's milestones
                events.append(ev)
        for ev in events:
            self.sink(ev)

    def run(self):
        self.catch_up()
        while not self.stop:
            try:
                self._resolve()
                size = os.path.getsize(self.path)
                if size < self.pos:          # log rotated
                    self.pos, self.buf = 0, b""
                if size > self.pos:
                    with open(self.path, "rb") as fh:
                        fh.seek(self.pos)
                        chunk = fh.read(size - self.pos)
                    self.pos = size
                    data = self.buf + chunk
                    lines = data.split(b"\n")
                    self.buf = lines.pop()       # keep a partial last line
                    for raw in lines:
                        for ev in parse_log_line(raw.decode("utf-8", "replace").rstrip("\r")):
                            self.sink(ev)
            except OSError:
                pass
            time.sleep(self.poll)


class LogUdp(threading.Thread):
    """Live log lines pushed by the app itself, once its log4.config has the UdpAppender (see API.md).
    Same line format as log.txt, so the same parser applies; nothing is read from disk."""

    def __init__(self, sink, port=47901):
        super().__init__(daemon=True, name="log-udp")
        self.sink, self.port = sink, port
        self.received = 0
        self.stop = False

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("127.0.0.1", self.port))
        s.settimeout(1.0)
        while not self.stop:
            try:
                data, _ = s.recvfrom(65535)
            except socket.timeout:
                continue
            self.received += 1
            for line in data.decode("utf-8", "replace").splitlines():
                for ev in parse_log_line(line):
                    self.sink(ev)


def _mp_unpack(b, i=0):
    """Minimal MessagePack decoder (what the SBM sends: arrays, maps, short strings, ints, bools, floats)."""
    import struct
    t = b[i]
    if t <= 0x7f: return t, i + 1
    if t >= 0xe0: return t - 0x100, i + 1
    if 0xa0 <= t <= 0xbf: n = t & 0x1f; return b[i + 1:i + 1 + n].decode("utf-8", "replace"), i + 1 + n
    if 0x90 <= t <= 0x9f or 0x80 <= t <= 0x8f:
        n, i, is_map = t & 0x0f, i + 1, t < 0x90
        return _mp_items(b, i, n, is_map)
    if t == 0xc0: return None, i + 1
    if t == 0xc2: return False, i + 1
    if t == 0xc3: return True, i + 1
    fixed = {0xcc: ">B", 0xcd: ">H", 0xce: ">I", 0xcf: ">Q", 0xd0: ">b", 0xd1: ">h", 0xd2: ">i", 0xd3: ">q",
             0xca: ">f", 0xcb: ">d"}
    if t in fixed:
        fmt = fixed[t]; n = struct.calcsize(fmt)
        return struct.unpack(fmt, b[i + 1:i + 1 + n])[0], i + 1 + n
    if t in (0xd9, 0xda, 0xdb):
        w = {0xd9: 1, 0xda: 2, 0xdb: 4}[t]; n = int.from_bytes(b[i + 1:i + 1 + w], "big")
        return b[i + 1 + w:i + 1 + w + n].decode("utf-8", "replace"), i + 1 + w + n
    if t in (0xdc, 0xdd, 0xde, 0xdf):
        w = 2 if t in (0xdc, 0xde) else 4; n = int.from_bytes(b[i + 1:i + 1 + w], "big")
        return _mp_items(b, i + 1 + w, n, t in (0xde, 0xdf))
    raise ValueError(f"unsupported MessagePack type 0x{t:02x}")


def _mp_items(b, i, n, is_map):
    if is_map:
        out = {}
        for _ in range(n):
            k, i = _mp_unpack(b, i); v, i = _mp_unpack(b, i); out[k] = v
        return out, i
    out = []
    for _ in range(n):
        v, i = _mp_unpack(b, i); out.append(v)
    return out, i


class ReplayTail(threading.Thread):
    """The REAL armrest on the Aug 26 build, which logs no control values. With "Message Replay Logger" ticked
    (dev tools row, before Connect) the app appends every message the SBM box sends to
    logs/ReplayLogs/SBMReplayLog_<UTC>.bin every 2 s: records of int32 elapsedMs, int32 len, then MessagePack
    [msgId, {key: value}] (report sprayer612R/reports/02 section 2.3). This follows the newest file and turns
    changes into the same ("control", id, value) events the virtual armrest gives, so lessons judge real presses
    (up to 2 s late). Decoding as the app does (reports/04 section 3): MHC buttons pressed == 1; SCM/DCM pressed when
    even and not 8; speed dial step = (y0 - y1) mod 49; hydro v/p; steering 'an' 0-359 unwrapped; pedals fs."""

    def __init__(self, sink, dir_fn, controls_doc, poll=0.3, skip=lambda: False):
        super().__init__(daemon=True, name="replay-tail")
        self.sink, self.dir_fn, self.poll, self.skip = sink, dir_fn, poll, skip
        self.modules = {m["msg"]: m for m in controls_doc["modules"]}
        self.by_key = {(c["module"], c.get("key")): c for c in controls_doc["controls"] if c.get("key")}
        self.path, self.pos, self.buf = None, 0, b""
        self.state = {}
        self.live = False
        self.wheel, self.last_an = 0.0, None
        self.stop = False

    def _emit(self, cid, value):
        value = str(value)
        if self.state.get(cid) != value:
            self.state[cid] = value
            self.sink((time.time(), "control", cid, value))

    def handle(self, msg):
        if not (isinstance(msg, list) and len(msg) == 2 and isinstance(msg[1], dict)):
            return
        mid, vals = msg
        mod = self.modules.get(mid)
        if mod is None:
            return
        m = mod["id"]
        if m in ("mhc", "scm", "dcm"):
            for k, v in vals.items():
                if not isinstance(v, int) or isinstance(v, bool):
                    continue
                c = self.by_key.get((m, k))
                if m == "mhc" and k in ("y0", "y1"):
                    if "y0" in vals and "y1" in vals:
                        self._emit("speed_dial", (int(vals["y0"]) - int(vals["y1"])) % 49)
                    continue
                if c is None:
                    continue
                if c["kind"] == "switch":                      # warning switch v1: 612R sends 3 when on
                    on = v == c.get("on", 1) or v == 3
                    self._emit(c["id"], "1" if on else "0")
                elif m == "mhc":
                    self._emit(c["id"], "1" if v == 1 else "0")
                else:
                    self._emit(c["id"], "1" if (v % 2 == 0 and v != 8) else "0")
        elif m == "hydro":
            if "p" in vals:
                self._emit("park_slot", "1" if vals["p"] else "0")
            if "v" in vals:
                self._emit("lever", int(vals["v"]))
        elif m == "steer" and "an" in vals:
            an = int(vals["an"]) % 360
            if self.last_an is not None:
                step = (an - self.last_an + 180) % 360 - 180     # shortest step; rising reading = right
                self.wheel -= step                                # armrest convention: positive = left
            self.last_an = an
            self._emit("steering", int(round(self.wheel)))
        elif m == "pedals" and "fs" in vals:
            self._emit("foot_switch", "1" if vals["fs"] else "0")

    def _newest(self):
        d = self.dir_fn()
        files = glob.glob(os.path.join(d, "SBMReplayLog_*.bin")) if d else []
        return max(files, key=os.path.getmtime) if files else None

    def step(self):
        p = self._newest()
        if p != self.path:
            if p is None:
                return
            fresh = self.path is not None or (time.time() - os.path.getmtime(p) < 120)
            self.path, self.buf, self.state, self.last_an, self.wheel = p, b"", {}, None, 0.0
            self.pos = 0 if fresh else os.path.getsize(p)    # an old file from before we started: skip it
            if fresh:
                self.live = True
                self.sink((time.time(), "link", "connected", ""))
        if self.path is None:                                # no replay file yet: the logger isn't on
            return
        size = os.path.getsize(self.path)
        if size <= self.pos:
            return
        with open(self.path, "rb") as fh:
            fh.seek(self.pos)
            data = self.buf + fh.read(size - self.pos)
        self.pos = size
        i = 0
        while len(data) - i >= 8:
            n = int.from_bytes(data[i + 4:i + 8], "little", signed=True)
            if n < 0 or n > 65536:
                i, data = 0, b""; break                     # out of step: drop the rest of this chunk
            if len(data) - i - 8 < n:
                break
            payload = data[i + 8:i + 8 + n]
            i += 8 + n
            if self.skip():
                continue
            if not self.live:
                self.live = True
                self.sink((time.time(), "link", "connected", ""))
            try:
                self.handle(_mp_unpack(payload)[0])
            except (ValueError, IndexError):
                pass
        self.buf = data[i:]

    def run(self):
        while not self.stop:
            try:
                self.step()
            except OSError:
                pass
            time.sleep(self.poll)


class GameFile(threading.Thread):
    def __init__(self, sink, path=GAME_PATH, poll=0.2):
        super().__init__(daemon=True, name="game-file")
        self.sink, self.path, self.poll = sink, path, poll
        self.values = {}
        self.stop = False

    def run(self):
        while not self.stop:
            try:
                with open(self.path, "rb") as fh:
                    data = fh.read()
                if data.strip():
                    root = ET.fromstring(data)
                    now = time.time()
                    for child in root:
                        v = (child.text or "").strip()
                        if self.values.get(child.tag) != v:
                            self.values[child.tag] = v
                            self.sink((now, "game", child.tag, v))
            except (OSError, ET.ParseError):
                pass                      # the app rewrites the file every 80 ms; torn reads happen
            time.sleep(self.poll)


class Armrest:
    """Client for the virtual armrest's scripted port. `watch()` streams its events into `sink`."""

    def __init__(self, port=ARMREST_PORT):
        self.port = port
        self._lock = threading.Lock()
        self._sock = None
        self._file = None

    def available(self):
        try:
            return self.cmd("ping").startswith("ok")
        except OSError:
            return False

    def cmd(self, line, timeout=30):
        with self._lock:
            if self._sock is None:
                self._sock = socket.create_connection(("127.0.0.1", self.port), timeout=timeout)
                self._file = self._sock.makefile("rw", encoding="utf-8", newline="\n")
            try:
                self._file.write(line + "\n")
                self._file.flush()
                reply = self._file.readline().strip()
            except OSError:
                self._sock = None              # dead connection: reconnect on the next command
                raise
            if not reply:
                self._sock = None
                raise OSError("armrest closed the connection")
            return reply

    def state(self):
        r = self.cmd("state")
        return json.loads(r[3:]) if r.startswith("ok ") else {}

    def run_script(self, commands):
        """Run lesson-style armrest commands, including 'wait <seconds>'."""
        for c in commands:
            if c.startswith("wait "):
                time.sleep(float(c.split()[1]))
                continue
            r = self.cmd(c)
            if not r.startswith("ok"):
                raise RuntimeError(f"armrest refused {c!r}: {r}")

    def watch(self, sink, on_end=None):
        """Stream the armrest's events into `sink`; `on_end()` runs when the armrest goes away."""
        def loop():
            try:
                _stream()
            except OSError:
                pass
            finally:
                with self._lock:
                    self._sock = None
                if on_end:
                    on_end()

        def _stream():
            s = socket.create_connection(("127.0.0.1", self.port))
            f = s.makefile("rw", encoding="utf-8", newline="\n")
            f.write("watch\n"); f.flush(); f.readline()
            for line in f:
                parts = line.strip().split(" ")
                if len(parts) < 4 or parts[0] != "evt":
                    continue
                kind, rest = parts[2], parts[3:]
                now = time.time()
                if kind in ("press", "release"):
                    sink((now, "control", rest[0], "1" if kind == "press" else "0"))
                elif kind in ("switch", "set"):
                    sink((now, "control", rest[0], rest[1] if len(rest) > 1 else ""))
                elif kind == "led":
                    sink((now, "led", rest[0], rest[1]))
                elif kind == "link":
                    sink((now, "link", rest[0], ""))
                elif kind == "mode":
                    sink((now, "mode", rest[0], ""))
                # "game" events from the armrest are ignored: GameFile reads the file directly
        th = threading.Thread(target=loop, daemon=True, name="armrest-watch")
        th.start()
        return th
