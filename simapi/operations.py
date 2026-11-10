"""The 612R lessons as the Connections app's Operations panel shows them.

The page itself lives in lesson-studio/operations. The API serves it at /operations/ (live: it follows the running
lesson), and tools/operations_panel.py copies it into the app's HTML/SprayerOp/OperatingProcedure folder, where it
lists the same lessons from a written-out copy of this data until the API is reachable.
"""
import glob
import json
import os

from .lesson import _leaves

# The order a trainee takes the 612R lessons in (the same order as Lesson Studio's chooser).
COURSE_612R = ["612r-controls-tour", "612r-drive-transport", "612r-fill-load", "612r-boom-handling",
               "612r-field-spraying", "612r-no-spray-fault", "612r-full-shift"]


def step_figure(step, lesson, figure_map):
    """The manual figure that best shows a step: the step's own `figure`, else the first photo of its first control
    that has one, else the figure of a screen target it names."""
    if step.get("figure"):
        return step["figure"]
    extra = (lesson or {}).get("extra_controls") or {}
    for cid in step.get("controls", []):
        if cid in extra and extra[cid].get("figure"):
            return extra[cid]["figure"]
        figs = ((figure_map.get("controls") or {}).get(cid) or {}).get("figures") or []
        if figs:
            return figs[0]
    for tid in step.get("display") or []:
        if (figure_map.get("screen") or {}).get(tid):
            return figure_map["screen"][tid]
    return None


def lessons(lesson_dir, figure_map, prefix="612r-"):
    """Every lesson whose file name starts with `prefix`, in course order, with what the panel lists."""
    out = []
    for path in glob.glob(os.path.join(lesson_dir, prefix + "*.json")):
        try:
            with open(path, encoding="utf-8") as fh:
                L = json.load(fh)
        except (OSError, ValueError):
            continue
        out.append({
            "id": L["id"], "title": L["title"], "minutes": L.get("minutes"), "objective": L.get("objective"),
            "trainer": (L.get("setup") or {}).get("trainer"),
            "sections": [{
                "title": s["title"], "mode": s.get("mode", "learn"), "checkpoint": bool(s.get("checkpoint")),
                "steps": [{
                    "id": st["id"], "say": st["say"], "why": st.get("why"),
                    "figure": step_figure(st, L, figure_map), "draft": st.get("confidence") == "draft",
                    "confirm": [leaf["confirm"] for leaf in _leaves(st["done"]) if "confirm" in leaf],
                } for st in s["steps"]],
            } for s in L["sections"]],
        })

    def rank(lesson):
        return COURSE_612R.index(lesson["id"]) if lesson["id"] in COURSE_612R else 100 + (lesson["minutes"] or 0)
    return sorted(out, key=rank)


def lessons_js(lesson_dir, figure_map):
    """lessons.js for the Operations page."""
    data = lessons(lesson_dir, figure_map)
    return "window.OPS_LESSONS = " + json.dumps(data, ensure_ascii=True, separators=(",", ":")) + ";\n"


def figures_used(lesson_dir, figure_map):
    return sorted({st["figure"] for L in lessons(lesson_dir, figure_map)
                   for s in L["sections"] for st in s["steps"] if st["figure"]})
