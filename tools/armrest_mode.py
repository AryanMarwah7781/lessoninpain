"""Switch the Aug 26 Connections app between the REAL armrest box and the VIRTUAL armrest.

    python -I tools/armrest_mode.py real|virtual|show [APP_FOLDER]

real     DevelopmentSettings:UseSBMEmulator = false: the app finds the box through monitor_daemon (as shipped).
virtual  UseSBMEmulator = true: the app talks to SBMEmulator.exe (lesson-studio/virtual-commandarm) over the pipe.
Restart the Connections app afterwards; it reads the setting at start. The first change keeps the original file as
appsettings.local.json.orig. APP_FOLDER (the folder with SimulatorConnections.exe, or one above it) defaults to the
copy that is running, else the one in Documents/jd_resources.
"""
import json
import os
import shutil
import sys

DEFAULT = os.path.join(os.path.expanduser("~"), "Documents", "jd_resources", "Aug26_Sprayer612R_TestBuild_v4",
                       "net8.0-windows")


def find_app_folder(given):
    if given:
        for cand in (given, os.path.join(given, "net8.0-windows")):
            if os.path.isfile(os.path.join(cand, "appsettings.local.json")):
                return cand
        return given
    # A rig can hold many builds and run another one (e.g. the combine build): the lessons are for the Aug 26 v4
    # 612R build, so look for that first, then a running Aug 26 copy, then the default place.
    import glob
    home = os.path.expanduser("~")
    for pattern in (os.path.join(home, "Documents", "jd_resources", "Aug26_Sprayer612R_TestBuild_v4*", "net8.0-windows"),
                    r"C:\Simulator\*\Aug26_Sprayer612R_TestBuild_v4*\net8.0-windows",
                    r"C:\Simulator\Aug26_Sprayer612R_TestBuild_v4*\net8.0-windows",
                    os.path.join(home, "Desktop", "**", "Aug26_Sprayer612R_TestBuild_v4*", "net8.0-windows")):
        hits = [h for h in glob.glob(pattern, recursive=True) if os.path.isfile(os.path.join(h, "appsettings.local.json"))]
        if hits:
            return hits[0]
    try:
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from simapi.profiles import running_dir
        d = running_dir("SimulatorConnections")
        if d and "Aug26" in d:
            return d
    except Exception:
        pass
    return DEFAULT


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("real", "virtual", "show"):
        raise SystemExit(__doc__)
    folder = find_app_folder(sys.argv[2] if len(sys.argv) > 2 else None)
    path = os.path.join(folder, "appsettings.local.json")
    if not os.path.isfile(path):
        raise SystemExit(f"Connections app settings not found: {path}\n"
                         "Start the app first, or pass its folder (the one with SimulatorConnections.exe).")
    data = json.load(open(path, encoding="utf-8-sig"))
    dev = data.setdefault("DevelopmentSettings", {})
    if sys.argv[1] != "show":
        if not os.path.isfile(path + ".orig"):
            shutil.copy2(path, path + ".orig")
        dev["UseSBMEmulator"] = sys.argv[1] == "virtual"
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2)
    mode = "virtual armrest (SBMEmulator)" if dev.get("UseSBMEmulator") else "real armrest box (monitor_daemon)"
    print(f"{folder}\n  armrest: {mode}")
    if sys.argv[1] != "show":
        print("  Restart the Connections app for this to take effect.")


if __name__ == "__main__":
    main()
