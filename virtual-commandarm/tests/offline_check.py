"""Offline check of the virtual CommandARM against the real Apr 20 Connections app.

Needs: the app running with "Connect to Simulator Bridge" pressed (no sign-in needed) and
SBMEmulator.exe running. Every control in controls.json is driven through the scripted port
(127.0.0.1:47800). The oracle is the app itself:
  * cloud controls   -> the app's own log line "SendVIOData ... {signal, value}" (logged even offline)
  * game controls    -> VehicleInfo.xml, reported by the armrest's "watch" stream
  * not-sent keys    -> no new signal at all while pressed

Run:  python -I tests/offline_check.py   (writes tests/results/offline-<time>.json and .md)
"""
import datetime as dt
import json
import os
import re
import socket
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LOG = r"C:\Simulator\Apr20_LTTS_FS25_ConnectionsApp_2\net8.0-windows\log.txt"
PORT = 47800
GAP = 0.7          # seconds between test cases, so log windows don't overlap
SLACK = 0.6        # extra seconds a signal may arrive after the action finished

CAT = json.load(open(os.path.join(ROOT, "controls.json"), encoding="utf-8"))
CTL = {c["id"]: c for c in CAT["controls"]}


# ---------------------------------------------------------------- armrest client
class Arm:
    def __init__(self):
        self.s = socket.create_connection(("127.0.0.1", PORT), timeout=10)
        self.f = self.s.makefile("rw", encoding="utf-8", newline="\n")

    def cmd(self, line):
        self.f.write(line + "\n"); self.f.flush()
        reply = self.f.readline().strip()
        if not reply.startswith("ok"):
            raise RuntimeError(f"{line!r} -> {reply!r}")
        return reply


class Watch(threading.Thread):
    """Collects armrest events (game file changes, lights, link) with local timestamps."""
    def __init__(self):
        super().__init__(daemon=True)
        self.events = []
        self.s = socket.create_connection(("127.0.0.1", PORT), timeout=None)
        self.f = self.s.makefile("rw", encoding="utf-8", newline="\n")
        self.f.write("watch\n"); self.f.flush()
        self.f.readline()

    def run(self):
        for line in self.f:
            line = line.strip()
            if line.startswith("evt "):
                parts = line.split(" ", 3)   # evt HH:MM:SS.fff kind rest
                self.events.append((time.time(), parts[2], parts[3] if len(parts) > 3 else ""))


# ---------------------------------------------------------------- log reading
LINE = re.compile(r"^(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d),(\d{3}) .*SendVIOData\(\): ActiveMQ data to send to EC2\. Data: "
                  r"\{\"signal\":\"([^\"]+)\",\"value\":\"([^\"]*)\"\}")


def read_log_from(offset):
    with open(LOG, "rb") as fh:
        fh.seek(0, 2)
        end = fh.tell()
        if end < offset:
            offset = 0
        fh.seek(offset)
        data = fh.read().decode("utf-8", "replace")
    out = []
    for ln in data.splitlines():
        m = LINE.match(ln)
        if m:
            t = dt.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").timestamp() + int(m.group(2)) / 1000
            out.append((t, m.group(3), m.group(4)))
    return out


# ---------------------------------------------------------------- test plan
def plan():
    """Each case: (name, control ids covered, list of (op, args), expectations)."""
    cases = []

    def press_case(cid):
        c = CTL[cid]
        exp = []
        if c["dest"] == "cloud":
            exp = [("vio_seq", c["vio"], ["1", "0"])]
        elif c["dest"] == "none":
            exp = [("no_vio",)]
        cases.append((f"press {cid}", [cid], [("press", cid)], exp))

    # every plain cloud / not-sent button, module by module
    for c in CAT["controls"]:
        if c["kind"] == "button" and c["dest"] in ("cloud", "none") and c["id"] not in ("centre_boom_raise", "centre_boom_lower"):
            press_case(c["id"])

    # centre boom, normal: raises/lowers the boom in the cloud sim
    cases.append(("centre boom raise (no foot switch)", ["centre_boom_raise"], [("press", "centre_boom_raise")],
                  [("vio_seq", "PLT_MHC_CenterBoomRaise", ["1", "0"])]))
    cases.append(("centre boom lower (no foot switch)", ["centre_boom_lower"], [("press", "centre_boom_lower")],
                  [("vio_seq", "PLT_MHC_CenterBoomLower", ["1", "0"])]))

    # fold / unfold: foot switch held turns centre raise/lower into a game-only fold
    cases.append(("fold boom: foot switch + centre raise", ["foot_switch", "centre_boom_raise"],
                  [("switch", "foot_switch", 1), ("wait", 0.4), ("press", "centre_boom_raise"), ("wait", 0.4)],
                  [("game", "boomUnfolded", "0"), ("no_vio_named", "PLT_MHC_CenterBoomRaise")]))
    cases.append(("unfold boom: foot switch + centre lower", ["foot_switch", "centre_boom_lower"],
                  [("press", "centre_boom_lower"), ("wait", 0.4), ("switch", "foot_switch", 0)],
                  [("game", "boomUnfolded", "1"), ("no_vio_named", "PLT_MHC_CenterBoomLower")]))

    # game-only keys
    cases.append(("ladder toggle up", ["ladder"], [("press", "ladder"), ("wait", 0.5)], [("game", "ladderRaised", "1"), ("no_vio",)]))
    cases.append(("ladder toggle down", ["ladder"], [("press", "ladder"), ("wait", 0.5)], [("game", "ladderRaised", "0"), ("no_vio",)]))
    cases.append(("camera 1/2", ["camera_toggle"], [("press", "camera_toggle"), ("wait", 0.5)], [("game", "cameraView", "2"), ("no_vio",)]))
    cases.append(("camera 3", ["camera_3"], [("press", "camera_3"), ("wait", 0.5)], [("game", "cameraView", "3"), ("no_vio",)]))
    cases.append(("camera 4", ["camera_4"], [("press", "camera_4"), ("wait", 0.5)], [("game", "cameraView", "4"), ("no_vio",)]))
    cases.append(("camera back to 1", ["camera_toggle"], [("press", "camera_toggle"), ("wait", 0.5)], [("game", "cameraView", "1"), ("no_vio",)]))

    # switches
    cases.append(("warning switch on/off", ["warning_switch"], [("switch", "warning_switch", 1), ("wait", 0.5), ("switch", "warning_switch", 0)],
                  [("vio_seq", "PLT_MHC_Warning", ["1", "0"])]))
    cases.append(("foot switch alone sends nothing", ["foot_switch"], [("switch", "foot_switch", 1), ("wait", 0.5), ("switch", "foot_switch", 0)],
                  [("no_vio",)]))

    # speed dial
    cases.append(("speed dial up 4 steps, back to 0", ["speed_dial"], [("set", "speed_dial", 4), ("wait", 0.5), ("set", "speed_dial", 0)],
                  [("vio_seq", "PLT_MHC_Encoder", ["3000", "1000"])]))

    # lever
    cases.append(("lever out of park slot", ["park_slot"], [("switch", "park_slot", 0), ("wait", 0.4)],
                  [("vio_seq", "PLT_NeutralSlotStatus", ["0"])]))
    # (125 is only sent here on a fresh app: the app sends a value only when it differs from the last one it sent)
    cases.append(("lever to 175, 75, neutral", ["lever"],
                  [("set", "lever", 175), ("wait", 0.5), ("set", "lever", 75), ("wait", 0.5), ("set", "lever", 125)],
                  [("vio_seq", "PLT_HydroHandlePosition", ["175", "75", "125"])]))
    # (the game file's hydroHandlePosition and wheelSpeed come from the cloud's echo, so they're online-only checks)
    cases.append(("lever back into park slot", ["park_slot"], [("switch", "park_slot", 1), ("wait", 0.4)],
                  [("vio_seq", "PLT_NeutralSlotStatus", ["1"])]))

    # steering: 450 deg left, 450 deg right, centre
    cases.append(("steer left 450 deg", ["steering"], [("set", "steering", 450), ("wait", 1.2)],
                  [("vio_last", "PLT_SteeringWheelAngleDeg", "17.5"), ("vio_last", "PLT_GPS_SteerLeft", "1")]))
    cases.append(("steer right 450 deg", ["steering"], [("set", "steering", -450), ("wait", 1.6)],
                  [("vio_last", "PLT_SteeringWheelAngleDeg", "-17.5"), ("vio_last", "PLT_GPS_SteerLeft", "0")]))
    cases.append(("steer back to centre", ["steering"], [("set", "steering", 0), ("wait", 1.2)],
                  [("vio_last", "PLT_SteeringWheelAngleDeg", "0")]))
    return cases


# ---------------------------------------------------------------- run
def main():
    arm = Arm()
    st = json.loads(arm.cmd("state")[3:])
    if not st["connected"]:
        sys.exit("The armrest is not connected: press 'Connect to Simulator Bridge' in the app first.")
    # start from a known state
    arm.cmd("switch foot_switch 0"); arm.cmd("switch warning_switch 0"); arm.cmd("switch park_slot 1")
    arm.cmd("set speed_dial 0"); arm.cmd("set steering 0")
    time.sleep(1.5)
    # the toggle cases assume ladder down and camera view 1; earlier runs may have left them otherwise
    game = json.loads(arm.cmd("state")[3:]).get("game", {})
    if game.get("ladderRaised") == "1":
        arm.cmd("press ladder 300"); time.sleep(0.8)
    if game.get("cameraView", "1") != "1":
        arm.cmd("press camera_toggle 300"); time.sleep(0.8)

    watch = Watch(); watch.start()
    offset = os.path.getsize(LOG)
    cases = plan()
    runs = []
    print(f"Running {len(cases)} cases...")
    for name, ids, ops, exp in cases:
        t0 = time.time()
        for op in ops:
            if op[0] == "press":
                arm.cmd(f"press {op[1]} 300")
            elif op[0] == "switch":
                arm.cmd(f"switch {op[1]} {op[2]}")
            elif op[0] == "set":
                arm.cmd(f"set {op[1]} {op[2]}")
            elif op[0] == "wait":
                time.sleep(op[1])
        t1 = time.time()
        runs.append({"name": name, "ids": ids, "t0": t0, "t1": t1, "exp": exp})
        time.sleep(GAP)

    print("Waiting for the app to flush its log...")
    deadline = time.time() + 30
    log = []
    while time.time() < deadline:
        time.sleep(3)
        log = read_log_from(offset)
        if log and log[-1][0] >= runs[-1]["t1"] - 2:
            break
    time.sleep(2)
    log = read_log_from(offset)

    results = []
    for r in runs:
        lo, hi = r["t0"] - 0.05, r["t1"] + SLACK
        sig = [(t, s, v) for t, s, v in log if lo <= t <= hi]
        # the armrest samples the game file every 300 ms, so a change can land a little after the action;
        # judge by the FIRST change in the window, since the next case may already have changed it again
        game = [(t, k, v) for t, kind, rest in watch.events if kind == "game" and lo <= t <= hi + 0.3
                for k, v in [rest.split(" ", 1)]]
        checks = []
        for e in r["exp"]:
            if e[0] == "vio_seq":
                got = [v for t, s, v in sig if s == e[1]]
                ok = got == e[2]
                checks.append({"check": f"{e[1]} sends {' then '.join(e[2])}", "ok": ok, "got": got})
            elif e[0] == "vio_last":
                got = [v for t, s, v in sig if s == e[1]]
                ok = bool(got) and got[-1] == e[2]
                checks.append({"check": f"{e[1]} ends at {e[2]}", "ok": ok, "got": got})
            elif e[0] == "no_vio":
                checks.append({"check": "nothing sent to the cloud", "ok": not sig, "got": [f"{s}={v}" for _, s, v in sig]})
            elif e[0] == "no_vio_named":
                got = [v for t, s, v in sig if s == e[1]]
                checks.append({"check": f"{e[1]} not sent", "ok": not got, "got": got})
            elif e[0] == "game":
                got = [v for t, k, v in game if k == e[1]]
                ok = bool(got) and (e[2] is None or got[0] == e[2])
                want = "changes" if e[2] is None else f"= {e[2]}"
                checks.append({"check": f"game {e[1]} {want}", "ok": ok, "got": got})
        results.append({"name": r["name"], "controls": r["ids"], "ok": all(c["ok"] for c in checks), "checks": checks,
                        "signals": [f"{s}={v}" for _, s, v in sig]})

    covered = sorted({cid for r in results for cid in r["controls"]})
    passed = {cid for r in results if r["ok"] for cid in r["controls"]}
    failed_ids = sorted(set(covered) - passed)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    summary = {"when": stamp, "cases": len(results), "cases_passed": sum(r["ok"] for r in results),
               "controls_in_catalogue": len(CTL), "controls_tested": len(covered),
               "controls_not_tested": sorted(set(CTL) - set(covered)), "controls_failing": failed_ids,
               "log_lines_seen": len(log), "results": results}
    jpath = os.path.join(HERE, "results", f"offline-{stamp}.json")
    json.dump(summary, open(jpath, "w", encoding="utf-8"), indent=2)

    md = [f"# Offline check {stamp}", "",
          f"{summary['cases_passed']} of {summary['cases']} cases passed; "
          f"{len(covered)} of {len(CTL)} controls exercised.", "",
          "| Case | Result | What the app did |", "|---|---|---|"]
    for r in results:
        what = "; ".join(f"{c['check']}: {'yes' if c['ok'] else 'NO (got ' + ', '.join(map(str, c['got'])) + ')'}" for c in r["checks"])
        md.append(f"| {r['name']} | {'PASS' if r['ok'] else 'FAIL'} | {what} |")
    if summary["controls_not_tested"]:
        md += ["", "Not exercised offline: " + ", ".join(summary["controls_not_tested"])]
    mpath = os.path.join(HERE, "results", f"offline-{stamp}.md")
    open(mpath, "w", encoding="utf-8").write("\n".join(md) + "\n")
    print(f"{summary['cases_passed']}/{summary['cases']} cases passed. Report: {mpath}")
    for r in results:
        if not r["ok"]:
            print("FAIL", r["name"], json.dumps(r["checks"]), r["signals"])


if __name__ == "__main__":
    main()
