"""Switch the Aug 26 Connections app between the REAL armrest box and the VIRTUAL armrest.

    python -I tools/armrest_mode.py real|virtual|show [APP_FOLDER]

real     DevelopmentSettings:UseSBMEmulator = false: the app finds the box through monitor_daemon (as shipped).
virtual  UseSBMEmulator = true: the app talks to SBMEmulator.exe (lesson-studio/virtual-commandarm) over the pipe.
Restart the Connections app afterwards; it reads the setting at start. The first change keeps the original file as
appsettings.local.json.orig. APP_FOLDER defaults to the copy in Documents/jd_resources.
"""
import json
import os
import shutil
import sys

DEFAULT = os.path.join(os.path.expanduser("~"), "Documents", "jd_resources", "Aug26_Sprayer612R_TestBuild_v4",
                       "net8.0-windows")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("real", "virtual", "show"):
        raise SystemExit(__doc__)
    folder = sys.argv[2] if len(sys.argv) > 2 else DEFAULT
    path = os.path.join(folder, "appsettings.local.json")
    if not os.path.isfile(path):
        raise SystemExit(f"not found: {path}")
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
