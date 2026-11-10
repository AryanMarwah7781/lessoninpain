"""Put the 612R lessons into the Connections app's Operations panel, or put the app's own page back.

    python -I tools/operations_panel.py install|remove|show [APP_FOLDER]

install  copies lesson-studio/operations (the page, its script and style, the app's own scenario pictures), the 612R
         lessons (lessons.js) and their manual figures (images/manual) into the app's
         HTML/SprayerOp/OperatingProcedure folder. The app's own page is kept as OperatingProcedure.orig.html (and
         refreshed if an app update brought a new one). Safe to run again: only changed files are written.
remove   puts the app's own page back and deletes what install added.
show     says which page the app will show.

The app loads the page when a 612R session opens its window, so the next Launch Machine Simulator shows it.
APP_FOLDER (the folder with SimulatorConnections.exe, or one above it) defaults to the copy armrest_mode.py finds;
a running copy elsewhere (another build on the rig) gets it too.
"""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]

from armrest_mode import find_app_folder  # noqa: E402
from simapi import operations  # noqa: E402

PAGE = "OperatingProcedure.html"
ORIG = "OperatingProcedure.orig.html"
OURS = ("operations.js", "operations.css", "lessons.js")
MARK = b'data-lesson-studio="operations"'
SRC = os.path.join(ROOT, "operations")
FIGURES = os.path.join(ROOT, "manual", "figures")


def panel_dir(app_folder):
    return os.path.join(app_folder, "HTML", "SprayerOp", "OperatingProcedure")


def ours(path):
    try:
        with open(path, "rb") as fh:
            return MARK in fh.read()
    except OSError:
        return False


def write_if_changed(dst, data):
    try:
        with open(dst, "rb") as fh:
            if fh.read() == data:
                return False
    except OSError:
        pass
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "wb") as fh:
        fh.write(data)
    return True


def copy_if_changed(src, dst):
    with open(src, "rb") as fh:
        return write_if_changed(dst, fh.read())


def install(folder):
    op = panel_dir(folder)
    page = os.path.join(op, PAGE)
    if not os.path.isfile(page):
        raise SystemExit(f"No Operations page in {op}\nPass the 612R app's folder (the one with SimulatorConnections.exe).")
    changed = 0
    if not ours(page):                      # the app's own page (first install, or an app update replaced ours)
        shutil.copy2(page, os.path.join(op, ORIG))
        changed += 1
    for name in (PAGE, "operations.js", "operations.css"):
        changed += copy_if_changed(os.path.join(SRC, name), os.path.join(op, name))
    for name in os.listdir(os.path.join(SRC, "images")):
        changed += copy_if_changed(os.path.join(SRC, "images", name), os.path.join(op, "images", name))
    fmap = json.load(open(os.path.join(ROOT, "manual", "figure-map.json"), encoding="utf-8"))
    lessons_dir = os.path.join(ROOT, "lessons")
    changed += write_if_changed(os.path.join(op, "lessons.js"), operations.lessons_js(lessons_dir, fmap).encode("utf-8"))
    used = operations.figures_used(lessons_dir, fmap)
    figdir = os.path.join(op, "images", "manual")
    for key in used:
        src = os.path.join(FIGURES, key + ".png")
        if os.path.isfile(src):
            changed += copy_if_changed(src, os.path.join(figdir, key + ".png"))
    for name in os.listdir(figdir) if os.path.isdir(figdir) else []:     # figures no lesson uses any more
        if name[:-4] not in used:
            os.remove(os.path.join(figdir, name))
            changed += 1
    n = len(operations.lessons(lessons_dir, fmap))
    print(f"{folder}\n  Operations panel: Lesson Studio's, {n} 612R lessons"
          + (f" ({changed} files updated)" if changed else " (already up to date)"))


def remove(folder):
    op = panel_dir(folder)
    page, orig = os.path.join(op, PAGE), os.path.join(op, ORIG)
    if not ours(page):
        print(f"{folder}\n  Operations panel: already the app's own")
        return
    if not os.path.isfile(orig):
        raise SystemExit(f"The app's own page was not kept in {op}: copy {PAGE} from another copy of this build.")
    shutil.copy2(orig, page)
    os.remove(orig)
    for name in OURS:
        if os.path.isfile(os.path.join(op, name)):
            os.remove(os.path.join(op, name))
    shutil.rmtree(os.path.join(op, "images", "manual"), ignore_errors=True)
    print(f"{folder}\n  Operations panel: the app's own page is back")


def show(folder):
    page = os.path.join(panel_dir(folder), PAGE)
    which = "Lesson Studio's (612R lessons)" if ours(page) else "the app's own" if os.path.isfile(page) else "not found"
    print(f"{folder}\n  Operations panel: {which}")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("install", "remove", "show"):
        raise SystemExit(__doc__)
    folders = [find_app_folder(sys.argv[2] if len(sys.argv) > 2 else None)]
    if len(sys.argv) <= 2:
        try:
            from simapi.profiles import running_dir
            d = running_dir("SimulatorConnections")
            if d and os.path.isdir(panel_dir(d)) and os.path.normcase(d) != os.path.normcase(folders[0]):
                folders.append(d)
        except Exception:
            pass
    for folder in folders:
        {"install": install, "remove": remove, "show": show}[sys.argv[1]](folder)
    if sys.argv[1] != "show":
        print("  The Operations panel changes from the next Launch Machine Simulator.")


if __name__ == "__main__":
    main()
