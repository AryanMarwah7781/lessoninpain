"""Lesson checker: proves a lesson file works against the real app + virtual armrest.

For each step it
  1. (if the step defines a mistake) makes that mistake through the armrest and checks the engine catches it,
  2. performs the step the right way ("show_me") and checks the engine sees it done, without false mistakes.
It also validates the file: every control id, signal and hint highlight must exist in controls.json.

Needs: the app with "Connect to Simulator Bridge" pressed and SBMEmulator.exe running. Works offline
(steps that can only be judged with the cloud are reported as "online only").

Run:  python -I lessons/check_lesson.py lessons/field-ready-r4045.json
"""
import datetime as dt
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from simapi.sources import Armrest, GameFile, LogTail          # noqa: E402
from simapi.store import Store                                   # noqa: E402
from simapi.lesson import LessonRun, TRUE, UNKNOWN, describe    # noqa: E402

STEP_TIMEOUT = 15.0     # the app's log can reach the file a few seconds late
WRONG_TIMEOUT = 10.0


def walk_checks(check, out):
    if isinstance(check, dict):
        for k in ("all", "any", "then", "before"):
            if k in check:
                for c in check[k]:
                    walk_checks(c, out)
                return out
        if "not" in check:
            return walk_checks(check["not"], out)
        out.append(check)
    return out


def validate(lesson, catalogue):
    # controls the simulator's armrest knows, plus 612R-only controls the lesson declares itself
    ids = {c["id"] for c in catalogue["controls"]} | set((lesson.get("extra_controls") or {}).keys())
    vios = {c.get("vio") for c in catalogue["controls"] if c.get("vio")}
    leds = {c["led"]["vio"] for c in catalogue["controls"] if c.get("led")}
    known_cloud = vios | leds | {"VIO_DCU_VehicleGroundSpeed", "PLT_RoadWheelAngleDeg", "PLT_GPS_SteerLeft",
                                 "PLT_NeutralSlotStatus", "PLT_SteeringWheelAngleDeg"}
    game_fields = {"wheelAngle", "wheelSpeed", "hydroHandlePosition", "nozzleOnOffStatus", "boomUnfolded",
                   "boomHeight", "cameraView", "ladderRaised"}
    problems, used = [], set()
    seen_ids = set()
    for sec in lesson["sections"]:
        for st in sec["steps"]:
            sid = st.get("id")
            if sid in seen_ids: problems.append(f"{sid}: duplicate step id")
            seen_ids.add(sid)
            for k in ("say", "done"):
                if k not in st: problems.append(f"{sid}: missing '{k}'")
            for cid in st.get("controls", []):
                (used.add(cid) if cid in ids else problems.append(f"{sid}: unknown control '{cid}'"))
            for h in st.get("hints", []):
                for cid in h.get("highlight", []):
                    if cid not in ids: problems.append(f"{sid}: hint highlights unknown control '{cid}'")
            prev = -1
            for h in st.get("hints", []):
                if h["after_s"] <= prev: problems.append(f"{sid}: hints not in time order")
                prev = h["after_s"]
            leaves = walk_checks(st["done"], []) + [l for w in st.get("wrong", []) for l in walk_checks(w["if"], [])]
            for leaf in leaves:
                for key in ("sent", "now_sent"):
                    if key in leaf and leaf[key] not in vios | {"PLT_NeutralSlotStatus", "PLT_GPS_SteerLeft"}:
                        problems.append(f"{sid}: app never sends '{leaf[key]}'")
                if "cloud" in leaf and leaf["cloud"] not in known_cloud:
                    problems.append(f"{sid}: unknown cloud signal '{leaf['cloud']}'")
                if "game" in leaf and leaf["game"] not in game_fields:
                    problems.append(f"{sid}: unknown game field '{leaf['game']}'")
                if "control" in leaf and leaf["control"] not in ids:
                    problems.append(f"{sid}: unknown control '{leaf['control']}'")
            for cmd in st.get("show_me", []) + st.get("wrong_demo", []):
                parts = cmd.split()
                if parts[0] != "wait" and (len(parts) < 2 or parts[1] not in ids):
                    problems.append(f"{sid}: bad armrest command '{cmd}'")
            if st.get("wrong") and not st.get("wrong_demo"):
                pass  # allowed: some mistakes can't be produced on purpose
    return problems, used


def main(path):
    lesson = LessonRun.load(path)
    catalogue = json.load(open(os.path.join(ROOT, "virtual-commandarm", "controls.json"), encoding="utf-8"))
    problems, used = validate(lesson, catalogue)

    arm = Armrest()
    if not arm.available():
        sys.exit("Virtual armrest not reachable on 127.0.0.1:47800.")
    st = arm.state()
    if not st.get("connected"):
        sys.exit("Armrest is not connected to the app: press 'Connect to Simulator Bridge'.")

    store = Store()
    now = time.time()
    # seed the armrest's current state so 'control' checks work before the first change
    store.add((now, "control", "foot_switch", "1" if st["footSwitch"] else "0"))
    store.add((now, "control", "park_slot", "1" if st["parked"] else "0"))
    store.add((now, "control", "lever", str(st["lever"])))
    store.add((now, "control", "steering", str(int(st["wheelTarget"]))))
    store.add((now, "control", "speed_dial", str(st["speedDial"])))
    LogTail(store.add).start()
    GameFile(store.add).start()
    arm.watch(store.add)
    time.sleep(1.0)

    # setup: armrest commands, then make the toggles match what the lesson expects
    arm.run_script(lesson.get("setup", {}).get("armrest", []))
    expect = lesson.get("setup", {}).get("expect", {}).get("game", {})
    time.sleep(1.0)
    for field, cmd in (("ladderRaised", "press ladder 300"), ("cameraView", "press camera_toggle 300")):
        if field in expect and store.game.get(field, ("?",))[0] != expect[field]:
            arm.run_script([cmd, "wait 0.6"])
    time.sleep(0.5)
    setup_state = {k: store.game.get(k, ("?",))[0] for k in expect}

    run = LessonRun(lesson, store, online=None, armrest=True)
    rows = []
    print(f"{lesson['title']}: {len(run.steps)} steps, online={store.online()}")
    while not run.finished:
        si, section, step = run.steps[run.index]
        row = {"section": section, "step": step["id"], "say": step["say"], "check": describe(step["done"]),
               "confidence": step.get("confidence")}

        # 1. the mistake, on purpose
        if step.get("wrong") and step.get("wrong_demo"):
            run.restart_step()
            arm.run_script(step["wrong_demo"])
            caught, deadline = None, time.time() + WRONG_TIMEOUT
            while time.time() < deadline:
                v = run.poll()
                if v.get("advanced"):
                    caught = "STEP COMPLETED BY THE MISTAKE"
                    break
                if v["mistakes"]:
                    caught = v["mistakes"][0]
                    break
                time.sleep(0.25)
            row["mistake_caught"] = caught is not None and not caught.startswith("STEP COMPLETED")
            row["mistake_message"] = caught
            if caught and caught.startswith("STEP COMPLETED"):
                rows.append(row | {"result": "FAIL", "why": "the mistake completed the step"})
                continue

        # 2. the right way
        run.restart_step()
        t0 = time.time()
        arm.run_script(step.get("show_me", []))
        # what the simulator can't sense, the trainee confirms: press Done for each item, as the panel would
        for leaf in walk_checks(step.get("done", {}), []):
            if "confirm" in leaf:
                store.add((time.time(), "confirm", leaf["confirm"], step["id"]))
        result, deadline, last = None, time.time() + STEP_TIMEOUT, None
        while time.time() < deadline:
            last = run.poll()
            if last.get("advanced"):
                result = "PASS"
                break
            time.sleep(0.25)
        if result is None:
            if last and last["done_status"] == UNKNOWN:
                result = "ONLINE ONLY"
                run.skip("needs the cloud")
            else:
                result = "FAIL"
                run.skip("not detected")
        row["result"] = result
        row["seconds"] = round(time.time() - t0, 1)
        row["false_mistakes"] = [m for m in (last or {}).get("mistakes", [])] if result == "PASS" else []
        if row["false_mistakes"]:
            row["result"] = "FAIL"
            row["why"] = "a mistake fired during the correct attempt"
        rows.append(row)
        print(f"  {row['result']:<11} {step['id']:<20} {row['seconds']:>5}s" +
              (f"   mistake caught: {row['mistake_caught']}" if "mistake_caught" in row else ""))

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    outdir = os.path.join(ROOT, "lessons", "results")
    os.makedirs(outdir, exist_ok=True)
    controls_all = {c["id"] for c in catalogue["controls"] if c["dest"] != "none"}
    summary = {
        "lesson": lesson["id"], "when": stamp, "online": store.online(), "setup_state": setup_state,
        "steps": len(rows), "passed": sum(r["result"] == "PASS" for r in rows),
        "online_only": sum(r["result"] == "ONLINE ONLY" for r in rows),
        "failed": sum(r["result"] == "FAIL" for r in rows),
        "mistakes_tested": sum("mistake_caught" in r for r in rows),
        "mistakes_caught": sum(r.get("mistake_caught", False) for r in rows),
        "file_problems": problems,
        "controls_used": sorted(used), "controls_not_used": sorted(controls_all - used),
        "rows": rows,
    }
    json.dump(summary, open(os.path.join(outdir, f"{lesson['id']}-{stamp}.json"), "w", encoding="utf-8"), indent=2)
    md = [f"# Lesson check: {lesson['title']}", "",
          f"{stamp} · {'online' if summary['online'] else 'offline (no sign-in)'} · "
          f"{summary['passed']} of {summary['steps']} steps passed, {summary['online_only']} online-only, {summary['failed']} failed · "
          f"mistakes caught {summary['mistakes_caught']} of {summary['mistakes_tested']}", "",
          f"File problems: {', '.join(problems) if problems else 'none'}", "",
          f"Controls used ({len(used)}): {', '.join(sorted(used))}", "",
          f"Controls not used ({len(summary['controls_not_used'])}): {', '.join(summary['controls_not_used'])}", "",
          "| # | Section | Step | Checked by | Result | Mistake test |", "|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        mt = "" if "mistake_caught" not in r else ("caught: " + (r["mistake_message"] or "") if r["mistake_caught"] else "NOT caught")
        md.append(f"| {i} | {r['section']} | {r['say']} | {r['check']} | {r['result']} | {mt} |")
    mpath = os.path.join(outdir, f"{lesson['id']}-{stamp}.md")
    open(mpath, "w", encoding="utf-8").write("\n".join(md) + "\n")
    print(f"\n{summary['passed']}/{summary['steps']} passed, {summary['online_only']} online-only, {summary['failed']} failed; "
          f"mistakes caught {summary['mistakes_caught']}/{summary['mistakes_tested']}; file problems: {len(problems)}")
    print("Report:", mpath)


def validate_only(path):
    """Static check of a lesson file (format 0.2): no simulator needed. Exit code 1 when anything is wrong."""
    lesson = LessonRun.load(path)
    catalogue = json.load(open(os.path.join(ROOT, "virtual-commandarm", "controls.json"), encoding="utf-8"))
    problems, used = validate(lesson, catalogue)
    figs = set()
    fpath = os.path.join(ROOT, "manual", "figures.jsonl")
    if os.path.isfile(fpath):
        figs = {json.loads(l)["key"] for l in open(fpath, encoding="utf-8")}
    for k in ("id", "title", "machine", "minutes", "objective", "sections"):
        if k not in lesson: problems.append(f"lesson: missing '{k}'")
    for cid, c in (lesson.get("extra_controls") or {}).items():
        for k in ("label", "where"):
            if not c.get(k): problems.append(f"extra control {cid}: missing '{k}'")
        if c.get("figure") and figs and c["figure"] not in figs: problems.append(f"extra control {cid}: unknown figure {c['figure']}")
    total, steps, confirms, sensed = 0, 0, 0, 0
    for sec in lesson["sections"]:
        if sec.get("mode", "learn") not in ("learn", "practice", "assess"):
            problems.append(f"section '{sec.get('title')}': mode must be learn, practice or assess")
        for st in sec["steps"]:
            steps += 1
            total += st.get("est_s", 0)
            if not st.get("est_s"): problems.append(f"{st.get('id')}: missing est_s (estimated seconds)")
            if st.get("figure") and figs and st["figure"] not in figs: problems.append(f"{st.get('id')}: unknown figure {st['figure']}")
            leaves = walk_checks(st.get("done", {}), [])
            if any("confirm" in l for l in leaves): confirms += 1
            if any("confirm" not in l for l in leaves): sensed += 1
            for l in leaves:
                if "confirm" in l and not str(l["confirm"]).strip(): problems.append(f"{st.get('id')}: empty confirm text")
    print(f"{lesson.get('title')}: {len(lesson['sections'])} sections, {steps} steps, about {round(total / 60)} min "
          f"(file says {lesson.get('minutes')}); {sensed} steps checked by the simulator, {confirms} confirmed by the trainee")
    for p in problems:
        print("  PROBLEM:", p)
    print("OK" if not problems else f"{len(problems)} problems")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--validate":
        validate_only(sys.argv[2])
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "lessons", "field-ready-r4045.json"))
