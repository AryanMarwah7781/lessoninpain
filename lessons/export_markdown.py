"""Export lessons to one shareable Markdown file, with the manual figures they use.

    python -I lessons/export_markdown.py OUT_DIR [PATTERN] [TITLE]

PATTERN defaults to "612r-*.json" (lessons/ folder). Writes OUT_DIR/<name>.md, OUT_DIR/figures/*.png and
OUT_DIR.zip. Standard library only.
"""
import glob
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MANUAL = os.path.join(ROOT, "manual")

# the order a trainee would take them in; anything else follows alphabetically
ORDER = ["612r-controls-tour", "612r-drive-transport", "612r-fill-load", "612r-boom-handling",
         "612r-field-spraying", "612r-no-spray-fault", "612r-full-shift"]

MODES = {"learn": "Learn", "practice": "Practice", "assess": "Assessment"}
OPS = {"eq": "=", "gte": "≥", "lte": "≤", "gt": ">", "lt": "<"}


def load_captions():
    """Figure captions: the manual's own caption or heading first, the machine-written caption last."""
    caps = {}
    tsv = os.path.join(MANUAL, "figure-captions.tsv")
    if os.path.isfile(tsv):
        for line in open(tsv, encoding="utf-8"):
            k, _, c = line.rstrip("\n").partition("\t")
            if k and c and k not in caps:
                caps[k] = c
    for path in glob.glob(os.path.join(MANUAL, "612r", "topics", "*.md")):
        lines = [l.strip() for l in open(path, encoding="utf-8") if l.strip()]
        for i, l in enumerate(lines[:-1]):
            m = re.match(r"^\*\*Figure ([A-Z0-9]+)\*\*$", l)
            if m and m.group(1) not in caps:
                nxt = lines[i + 1]
                if len(nxt) <= 60 and not nxt.startswith(("!", "**", "#", "NOTE", "IMPORTANT", "CAUTION")) and "—UN—" not in nxt:
                    caps[m.group(1)] = nxt
    vlm = os.path.join(MANUAL, "captions.jsonl")
    if os.path.isfile(vlm):
        for line in open(vlm, encoding="utf-8"):
            d = json.loads(line)
            if d["key"] not in caps and d.get("caption"):
                c = d["caption"].replace(f"Figure {d['key']} shows ", "").split(". ")[0].rstrip(".")
                caps[d["key"]] = c[:1].upper() + c[1:]
    return caps


def load_controls():
    data = json.load(open(os.path.join(ROOT, "virtual-commandarm", "controls.json"), encoding="utf-8"))["controls"]
    by_id = {c["id"]: c["label"] for c in data}
    by_vio = {c["vio"]: c["label"] for c in data if c.get("vio")}
    # signals that are not a single armrest button
    by_vio.update({"PLT_HydroHandlePosition": "Multi-function lever position",
                   "PLT_NeutralSlotStatus": "Lever in Park",
                   "PLT_MHC_Encoder": "Speed dial",
                   "PLT_SteeringWheelAngleDeg": "Steering wheel"})
    return by_id, by_vio


def check_text(check, by_vio):
    """A check in plain words, with the signal name kept for whoever wires the simulator."""
    for key, sep in (("all", " **and** "), ("any", " **or** "), ("then", ", **then** ")):
        if key in check:
            return sep.join(check_text(c, by_vio) for c in check[key])
    if "before" in check:
        a, b = check["before"]
        return f"{check_text(a, by_vio)} **before** {check_text(b, by_vio)}"
    if "not" in check:
        return f"**not** ({check_text(check['not'], by_vio)})"
    if "confirm" in check:
        return f"trainee ticks “{check['confirm']}”"
    for src, who in (("sent", "simulator sees"), ("now_sent", "simulator sees"), ("cloud", "machine reports"),
                     ("game", "game shows"), ("control", "armrest shows")):
        if src in check:
            sig = check[src]
            tests = [f"{OPS[k]} {check[k]}" for k in OPS if k in check]
            if "between" in check:
                tests.append(f"between {check['between'][0]} and {check['between'][1]}")
            if "outside" in check:
                tests.append(f"outside {check['outside'][0]} to {check['outside'][1]}")
            label = by_vio.get(sig)
            name = f"{label} (`{sig}`)" if label else f"`{sig}`"
            return f"{who} {name} {' '.join(tests)}".strip()
    return "?"


def check_kind(check):
    leaves = []

    def walk(c):
        for k in ("all", "any", "then", "before"):
            if k in c:
                for x in c[k]:
                    walk(x)
                return
        if "not" in c:
            walk(c["not"])
            return
        leaves.append(c)
    walk(check)
    confirm = sum(1 for l in leaves if "confirm" in l)
    if confirm == len(leaves):
        return "Trainee confirms"
    return "Automatic" if not confirm else "Automatic + trainee confirms"


def pages(source):
    p = (source or {}).get("pages") or []
    return ("page " if len(p) == 1 else "pages ") + ", ".join(p) if p else ""


def minutes(lesson):
    s = sum(st.get("est_s", 0) for sec in lesson["sections"] for st in sec["steps"])
    return round(s / 60) if s else lesson.get("minutes")


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    out = os.path.abspath(sys.argv[1])
    pattern = sys.argv[2] if len(sys.argv) > 2 else "612r-*.json"
    title = sys.argv[3] if len(sys.argv) > 3 else "John Deere 612R sprayer: lesson plans"
    files = glob.glob(os.path.join(HERE, pattern))
    lessons = [json.load(open(f, encoding="utf-8")) for f in files]
    lessons.sort(key=lambda l: (ORDER.index(l["id"]) if l["id"] in ORDER else 99, l["id"]))
    caps = load_captions()
    by_id, by_vio = load_controls()
    figs_dir = os.path.join(out, "figures")
    os.makedirs(figs_dir, exist_ok=True)
    used = set()

    def figure(key, width=280):
        if not key:
            return ""
        src = os.path.join(MANUAL, "figures", key + ".png")
        if not os.path.isfile(src):
            return f"*Manual figure {key}*"
        used.add(key)
        cap = caps.get(key, "")
        alt = f"Manual figure {key}" + (f": {cap}" if cap else "")
        return f'<img src="figures/{key}.png" width="{width}" alt="{alt}">'

    total_steps = sum(len(sec["steps"]) for l in lessons for sec in l["sections"])
    total_min = sum(minutes(l) or 0 for l in lessons)
    md = [f"# {title}", ""]
    manuals = sorted({l.get("manual", "") for l in lessons if l.get("manual")})
    drafts = sum(1 for l in lessons for s in l["sections"] for st in s["steps"] if st.get("confidence") == "draft")
    md += [f"{len(lessons)} lessons, {total_steps} steps, about {total_min // 60} h {total_min % 60} min in all. "
           f"Written from the operator's manual, {'; '.join(manuals)}; every step names the manual pages it comes from.", "",
           "**Status: draft for review.** The steps follow the manual but have not yet been reviewed by an experienced "
           f"612R operator. {drafts} steps are marked **(draft)**: they use a button whose simulator mapping is not "
           "confirmed yet, or a drill the manual does not describe.", "",
           "The lessons run in Lesson Studio beside the John Deere Display and CommandARM Simulator: the panel shows each "
           "step with its manual figure, rings the control to press, gives timed hints, and checks the step itself "
           "where the simulator can see it.", ""]

    md += ["## Contents", "", "| # | Lesson | Level | Time | Sections | Steps |", "|---|---|---|---|---|---|"]
    for i, l in enumerate(lessons, 1):
        anchor = f"lesson-{i}"
        n = sum(len(s["steps"]) for s in l["sections"])
        md.append(f"| {i} | [{l['title']}](#{anchor}) | {l.get('level', '')} | {minutes(l)} min | {len(l['sections'])} | {n} |")
    md += ["", "## How to read a lesson", "",
           "- **Sections** are marked **Learn** (hints and *Show me* available), **Practice** (hints come later and "
           "there are fewer) or **Assessment** (no hints, no *Show me*, scored). A **resume point** is a section a long "
           "lesson can be restarted from.",
           "- Each **step** gives the instruction the trainee sees, *why* it matters, the controls involved and an "
           "estimated time for a first-timer.",
           "- **Check** says how the step is marked done: **Automatic** when the simulator can see it (signal names "
           "in `code`), **Trainee confirms** when it can't (a walk-around, a reading on a gauge), and the trainee ticks "
           "a box instead.",
           "- **If they get it wrong** lists the mistakes the panel watches for and what it tells the trainee.",
           "- **Hints** appear after the given number of seconds on the step.",
           "- **Manual** gives the operator's manual pages and the figure shown beside the step (the figures are in "
           "the `figures` folder next to this file).", ""]

    for i, l in enumerate(lessons, 1):
        n = sum(len(s["steps"]) for s in l["sections"])
        md += ["---", "", f'<a id="lesson-{i}"></a>', "", f"## {i}. {l['title']}", "",
               f"**{l.get('level', '')}** · about **{minutes(l)} min** · {len(l['sections'])} sections · {n} steps", "",
               f"**Objective:** {l.get('objective', '')}", ""]
        if l.get("procedure_source"):
            md += [f"**From the manual:** {l['procedure_source']}", ""]
        trainer = (l.get("setup") or {}).get("trainer")
        if trainer:
            md += [f"**Before you start (trainer):** {trainer}", ""]
        for si, sec in enumerate(l["sections"], 1):
            mode = MODES.get(sec.get("mode", "learn"), sec.get("mode", ""))
            tags = [mode] + (["resume point"] if sec.get("checkpoint") else [])
            md += [f"### {sec['title']}", "", f"*{' · '.join(tags)}*", ""]
            for ti, st in enumerate(sec["steps"], 1):
                extra = l.get("extra_controls") or {}
                ctl = [extra.get(c, {}).get("label") or by_id.get(c, c) for c in st.get("controls", [])]
                head = f"**{si}.{ti}  {st['say']}**"
                if st.get("est_s"):
                    head += f"  *(~{st['est_s']} s)*"
                if st.get("confidence") == "draft":
                    head += "  **(draft)**"
                md += [head, ""]
                fig = figure(st.get("figure"))
                if fig:
                    md += [fig, ""]
                rows = []
                if st.get("why"):
                    rows.append(f"- **Why:** {st['why']}")
                if ctl:
                    rows.append(f"- **Controls:** {', '.join(ctl)}")
                if st.get("done"):
                    rows.append(f"- **Check ({check_kind(st['done'])}):** {check_text(st['done'], by_vio)}")
                for w in st.get("wrong", []):
                    rows.append(f"- **If they get it wrong:** {w['say']}")
                if st.get("hints") and sec.get("mode") != "assess":
                    hs = " ".join(f"*{h.get('after_s', 0)} s:* {h['say']}" for h in st["hints"])
                    rows.append(f"- **Hints:** {hs}")
                src = pages(st.get("source"))
                if src or st.get("figure"):
                    bits = [b for b in (src, f"figure {st['figure']}" + (f" ({caps[st['figure']]})" if caps.get(st.get('figure')) else "") if st.get("figure") else "") if b]
                    rows.append(f"- **Manual:** {' · '.join(bits)}")
                md += rows + [""]

    name = re.sub(r"[^A-Za-z0-9]+", "-", title.split(":")[0]).strip("-") + "-lesson-plans"
    name = "612R-lesson-plans" if pattern.startswith("612r") else name
    md_path = os.path.join(out, name + ".md")
    with open(md_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(md).rstrip() + "\n")
    for f in os.listdir(figs_dir):
        if f[:-4] not in used:
            os.remove(os.path.join(figs_dir, f))
    for key in used:
        shutil.copy2(os.path.join(MANUAL, "figures", key + ".png"), figs_dir)
    zip_path = shutil.make_archive(out, "zip", os.path.dirname(out), os.path.basename(out))
    print(f"{md_path}\n{len(lessons)} lessons, {total_steps} steps, {len(used)} figures\n{zip_path}")


if __name__ == "__main__":
    main()
