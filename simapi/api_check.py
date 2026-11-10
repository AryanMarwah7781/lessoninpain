"""End-to-end check of the simulator API, used the way the lesson panel will use it.
Needs: run_simapi.py running, the app connected to the virtual armrest. Offline is fine.
Run: python -I simapi/api_check.py
"""
import json
import time
import urllib.request

BASE = "http://127.0.0.1:47900"


def get(path):
    with urllib.request.urlopen(BASE + path, timeout=10) as r:
        return json.loads(r.read())


def post(path, body=None):
    data = json.dumps(body or {}).encode()
    req = urllib.request.Request(BASE + path, data=data, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def wait_view(pred, timeout=15):
    end = time.time() + timeout
    while time.time() < end:
        v = get("/api/lesson")
        if pred(v):
            return v
        time.sleep(0.3)
    return get("/api/lesson")


results = []


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(("PASS " if ok else "FAIL ") + name + (f"  ({detail})" if detail else ""))


h = get("/api/health")
check("health: armrest linked", h["armrest"], f"online={h['online']}")

s = post("/api/lesson/setup", {"id": "field-ready-r4045"})
check("setup puts the simulator in the lesson's starting state", s["ok"], f"now={s['now']}")
v = post("/api/lesson/start", {"id": "field-ready-r4045"})
check("lesson starts on step 1", v.get("step") == "ladder-up", v.get("say", ""))

# 1. stall on step 1 until the 20 s hint is due
time.sleep(21)
v = get("/api/lesson")["view"]
check("hint appears after 20 s on a stalled step", bool(v.get("hint")), (v.get("hint") or {}).get("say", ""))

# 2. show me completes steps 1 and 2
post("/api/lesson/showme")
v = wait_view(lambda x: x["view"].get("step") == "camera-boom-view")["view"]
check("show me completes 'ladder up' and the API advances", v.get("step") == "camera-boom-view", f"step {v.get('index')}/{v.get('of')}")
post("/api/lesson/showme")
wait_view(lambda x: x["view"].get("step") == "hold-foot-switch")
post("/api/lesson/showme")
v = wait_view(lambda x: x["view"].get("step") == "unfold")["view"]
check("reached the unfold step", v.get("step") == "unfold")

# 3. the classic mistake: Centre boom lower without the foot switch
post("/api/armrest", {"cmd": "switch foot_switch 0"})
post("/api/armrest", {"cmd": "press centre_boom_lower 400"})
v = wait_view(lambda x: bool(x["view"].get("mistakes")), timeout=10)["view"]
check("API reports the mistake while the step stays open", bool(v.get("mistakes")) and v.get("step") == "unfold",
      (v.get("mistakes") or [""])[0])

# 4. chatbot context for the step the trainee is stuck on
ctx = get("/api/chatbot-context")
check("chatbot context names the lesson, step and recent controls",
      ctx.get("step", "").startswith("Keep holding") and "centre_boom_lower" in ctx.get("last_controls", []),
      f"last_controls={ctx.get('last_controls')}, game boomUnfolded={ctx.get('game', {}).get('boomUnfolded')}")

# 5. now do it right through show me
post("/api/lesson/showme")
v = wait_view(lambda x: x["view"].get("step") == "release-foot-switch")["view"]
check("unfold done the right way advances the lesson", v.get("step") == "release-foot-switch")
post("/api/lesson/showme")

# 6. live stream delivers events
req = urllib.request.urlopen(BASE + "/api/stream", timeout=10)
post("/api/armrest", {"cmd": "press rate_3 300"})
got = []
end = time.time() + 6
while time.time() < end and len(got) < 3:
    line = req.readline().decode().strip()
    if line.startswith("data: "):
        got.append(json.loads(line[6:]))
req.close()
check("live stream (/api/stream) delivers events", bool(got), ", ".join(f"{e['kind']}:{e['name']}={e['value']}" for e in got[:3]))

c = get("/api/controls")
m = get("/api/screen-map")
check("catalogue and screen map served", len(c["controls"]) == 62 and len(m["targets"]) >= 40,
      f"{len(c['controls'])} controls, {len(m['targets'])} screen targets")
scr = get("/api/screens")
check("app windows found and told apart", "main" in scr, ", ".join(sorted(k for k in scr)))
with urllib.request.urlopen(BASE + "/api/screen/main.png", timeout=30) as r:
    png = r.read()
check("live capture of the main window is a PNG", png[:8] == b"\x89PNG\r\n\x1a\n", f"{len(png)} bytes")
post("/api/lesson/start", {"id": "headland-hms"})
time.sleep(0.8)
v = get("/api/lesson")["view"]
check("step 'press HMS' points at the HMS handle button and the HMS soft key",
      [a["id"] for a in v["armrest"]] == ["hms"] and "run.softkey.hms" in [t["id"] for t in v["screen"]["press"]],
      f"armrest={[a['id'] for a in v['armrest']]}, press={[t['id'] for t in v['screen']['press']]}")

state = get("/api/state")
check("state shows the game file and what the app sent",
      state["game"].get("boomUnfolded") == "1" and "PLT_AIC_Rate3Control" in state["sent"],
      f"boomUnfolded={state['game'].get('boomUnfolded')}, sent signals={len(state['sent'])}")

with urllib.request.urlopen(BASE + "/operations/lessons.js", timeout=10) as r:
    ops = json.loads(r.read().decode("utf-8").split("=", 1)[1].strip().rstrip(";"))
with urllib.request.urlopen(BASE + "/operations/OperatingProcedure.html", timeout=10) as r:
    page = r.read()
check("Operations panel page and its 612R lessons served", b'data-lesson-studio="operations"' in page and len(ops) == 7,
      f"{len(ops)} lessons, {sum(len(s['steps']) for L in ops for s in L['sections'])} steps")

print(f"\n{sum(r[1] for r in results)}/{len(results)} API checks passed")
