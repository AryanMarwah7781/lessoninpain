"""Build manual/figure-map.json: which manual figure shows each armrest control and screen target.

Figures come from the 612R operator manual (OMKK105338, 400R-616R) on spark-bf0b
(~/jd_rag_612R/vault/attachments/figures), copied to manual/figures. The simulated machine is a 2019 R4045,
so every entry says how sure we are:
  manual   the manual names this exact function on this figure or button
  likely   the manual shows the function, but which of two similar figures is left/right is our reading
  inferred the 612R handle has no such button; position chosen by function (left/right) only
Run: python -I manual/build_figure_map.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# control id -> (handle letter or None, [figures, best first], certainty, where to find it, in words)
CONTROLS = {
    # multi-function lever (MHC). Letters from the manual's table, p. 30-19/30-20 (NX707642).
    "master_spray":         ("I", ["N152644", "NX711654"], "manual", "Multi-function lever, yellow button low on the right"),
    "hms":                  ("A", ["N152638", "NX711654"], "manual", "Multi-function lever, top right, marked HMS"),
    "left_boom_raise":      ("F", ["N152642", "NX711654"], "likely", "Multi-function lever, left rocker in the middle, push the top"),
    "left_boom_lower":      ("E", ["N152642", "NX711654"], "likely", "Multi-function lever, left rocker in the middle, push the bottom"),
    "right_boom_raise":     ("C", ["N152643", "NX711654"], "likely", "Multi-function lever, right rocker in the middle, push the top"),
    "right_boom_lower":     ("D", ["N152643", "NX711654"], "likely", "Multi-function lever, right rocker in the middle, push the bottom"),
    "section_left_enable":  ("H", ["N152636", "NX711654"], "manual", "Multi-function lever, wide rocker near the top, left half"),
    "section_right_enable": ("G", ["N152637", "NX711654"], "manual", "Multi-function lever, wide rocker near the top, right half"),
    "section_reset":        ("N", ["N152635", "NX711654"], "manual", "Multi-function lever, angled button top left (IBS Reset)"),
    "centre_boom_raise":    ("M", ["N152641", "N153424"], "manual", "Multi-function lever, round pad on the left, push up"),
    "centre_boom_lower":    ("K", ["N152641", "N153021"], "manual", "Multi-function lever, round pad on the left, push down"),
    "foam_marker_left":     ("L", [], "inferred", "Round pad on the left, push left (the 612R handle has no foam marker)"),
    "foam_marker_right":    ("J", [], "inferred", "Round pad on the left, push right (the 612R handle has no foam marker)"),
    "boomtrac":             ("Z", ["N152646", "NX711654"], "manual", "Multi-function lever, bottom right of the middle group (BoomTrac Resume)"),
    "switch_4":             ("O", ["N152645", "NX711654"], "manual", "Multi-function lever, bottom left of the middle group, marked AUTO (AutoTrac Resume)"),
    "warning_switch":       ("V", ["N152634", "NX711654"], "manual", "Multi-function lever, the button on top (Quick Stop)"),
    "reconfig_a":           ("P", ["N152648", "NX707641"], "manual", "Multi-function lever, right side, top right button (A)"),
    "reconfig_b":           ("Q", ["N152648", "NX707641"], "manual", "Multi-function lever, right side, bottom right button (B)"),
    "reconfig_c":           ("R", ["N152648", "NX707641"], "likely", "Multi-function lever, right side, top rocker (C), right half"),
    "reconfig_d":           ("S", ["N152648", "NX707641"], "likely", "Multi-function lever, right side, top rocker (C), left half"),
    "reconfig_e":           ("T", ["N152648", "NX707641"], "likely", "Multi-function lever, right side, bottom rocker (D), right half"),
    "reconfig_f":           ("U", ["N152648", "NX707641"], "likely", "Multi-function lever, right side, bottom rocker (D), left half"),
    "speed_dial":           ("XY", ["N166440", "NX707641"], "manual", "Thumb wheel under the multi-function lever (speed range)"),
    "dial_push":            ("XY", ["N166440", "NX707641"], "likely", "Press the thumb wheel under the multi-function lever"),
    # armrest switch panel (DCM)
    "engine_low_idle":      (None, ["N166477"], "manual", "Right-hand console, Low Idle switch (B in the photo)"),
    "engine_high_idle":     (None, ["N137031"], "manual", "Right-hand console, High Idle switch"),
    "park_brake":           (None, ["N137032"], "manual", "Right-hand console, Park Brake switch (P)"),
    "ladder":               (None, ["N154889"], "likely", "Ladder switch; the ladder is on the left side of the machine"),
    # sprayer keypad (SCM)
    "solution_pump":        (None, ["N155117"], "manual", "Right-hand console keypad, Solution Pump switch (A)"),
    "rate_1":               (None, ["N155118"], "likely", "Right-hand console keypad, rate control switches (A)"),
    "rate_2":               (None, ["N155118"], "likely", "Right-hand console keypad, rate control switches (A)"),
    "rate_3":               (None, ["N155118"], "likely", "Right-hand console keypad, rate control switches (A)"),
    "camera_toggle":        (None, ["N152939C"], "likely", "Camera key; the display shows the camera view"),
    # lever, wheel, foot switch
    "lever":                (None, ["N166439", "N152958"], "manual", "Multi-function lever: push forward to drive, pull back to slow"),
    "park_slot":            (None, ["N152958", "N166439"], "manual", "Multi-function lever park position (the gate at the end of its travel)"),
    "steering":             (None, ["N151293"], "manual", "Steering wheel"),
    "foot_switch":          (None, ["N153424"], "manual", "Boom Fold/Unfold floor switch (A in the photo), hold it down with your foot"),
}

# screen target id -> figure showing the same thing in the manual
SCREEN = {
    "run.softkey.hms": "N120151",
    "pdu.speed": "PC29666",
    "pdu.rpm": "PC29665",
    "pdu.gear": "PC29668",
}


def main():
    figs = {}
    for line in open(os.path.join(HERE, "figures.jsonl"), encoding="utf-8"):
        d = json.loads(line)
        figs[d["key"]] = d
    caps = {}
    for line in open(os.path.join(HERE, "captions.jsonl"), encoding="utf-8"):
        d = json.loads(line)
        caps[d["key"]] = d["caption"]
    manual_caps = {}
    tsv = os.path.join(HERE, "figure-captions.tsv")
    if os.path.isfile(tsv):
        for line in open(tsv, encoding="utf-8"):
            k, _, c = line.rstrip("\n").partition("\t")
            if k and c and k not in manual_caps:
                manual_caps[k] = c
    # many manual figures carry no caption line but a heading right under them ("**Figure N152646**" then
    # "BoomTrac Resume"): use that heading
    import glob
    import re
    for path in glob.glob(os.path.join(HERE, "612r", "topics", "*.md")):
        lines = [l.strip() for l in open(path, encoding="utf-8") if l.strip()]
        for i, l in enumerate(lines[:-1]):
            m = re.match(r"^\*\*Figure ([A-Z0-9]+)\*\*$", l)
            if m and m.group(1) not in manual_caps:
                nxt = lines[i + 1]
                if len(nxt) <= 60 and not nxt.startswith(("!", "**", "#", "NOTE", "IMPORTANT", "CAUTION")) and "—UN—" not in nxt:
                    manual_caps[m.group(1)] = nxt
    controls_json = json.load(open(os.path.join(HERE, "..", "virtual-commandarm", "controls.json"), encoding="utf-8"))
    known = {c["id"] for c in controls_json["controls"]}

    used, missing = {}, []

    def fig(key):
        path = os.path.join(HERE, "figures", key + ".png")
        if not os.path.isfile(path):
            missing.append(key)
            return None
        f = figs.get(key, {})
        callouts = f.get("callouts") or {}
        used[key] = {"page": f.get("pdf_page"), "callouts": callouts,
                     "caption": manual_caps.get(key) or (caps.get(key) or "").replace("Figure %s shows " % key, "").strip()}
        return key

    out_controls = {}
    for cid, (letter, keys, certainty, where) in CONTROLS.items():
        if cid not in known:
            raise SystemExit("unknown control id in map: " + cid)
        out_controls[cid] = {"handle": letter, "figures": [k for k in (fig(k) for k in keys) if k],
                             "certainty": certainty, "where": where}
    out_screen = {t: fig(k) for t, k in SCREEN.items() if fig(k)}
    hotspots = json.load(open(os.path.join(HERE, "handle-hotspots.json"), encoding="utf-8"))
    fig(hotspots["figure"])

    out = {
        "source": "John Deere 612R operator manual OMKK105338 (400R-616R), via the RAG vault on spark-bf0b",
        "machine_note": "Pictures are from the 612R manual; the simulated machine is a 2019 R4045, so some layouts may differ.",
        "handle": hotspots,
        "controls": out_controls,
        "screen": out_screen,
        "figures": used,
    }
    json.dump(out, open(os.path.join(HERE, "figure-map.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"{len(out_controls)} controls mapped ({sum(1 for c in out_controls.values() if c['figures'])} with a photo), "
          f"{len(out_screen)} screen targets, {len(used)} figures used")
    if missing:
        print("missing figure files:", ", ".join(sorted(set(missing))))


if __name__ == "__main__":
    main()
