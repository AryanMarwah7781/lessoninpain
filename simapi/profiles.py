"""Build profiles: what differs between the Connections app builds the API can watch.

Lessons and the store always use one set of signal names (the Apr 20 build's, "canonical"). A profile says where the
build keeps its log and game files, which names it uses instead, and where "the app sent X" evidence comes from.

  apr20  Display and CommandARM Simulator 3.2.0.7 (Apr 20 2026), R4045 2019, FS25. Logs every SendVIOData line.
  aug26  SimulatorConnections 3.2.0 (Aug 26 2026 test build v4), 612R (2025) Premium, FS22 by default.
         Logs no control values at all (report sprayer612R/reports/02 §1.2), so "sent" evidence comes from the
         virtual armrest while it is linked to the app. Signal names from sprayer612R/reports/04 §3.
"""
import glob
import os

DOCS = os.path.join(os.path.expanduser("~"), "Documents", "My Games")


def _game_path(year):
    return os.path.join(DOCS, f"FarmingSimulator{year}", "mods", "DeereVehicleControl", "src", "VehicleInfo.xml")


PROFILES = {
    "apr20": {
        "label": "Apr 20 build (R4045, Display and CommandARM Simulator 3.2.0.7)",
        "process": "Online - Display and CommandARM Simulator",
        "app_dir": r"C:\Simulator\Apr20_LTTS_FS25_ConnectionsApp_2\net8.0-windows",
        "log": "log.txt",
        "game_year": 2025,
        "aliases": {},                 # actual name -> canonical name
        "armrest_as_sent": False,      # the app logs every value it sends
        "steer_full_lock_deg": 900,    # wheel degrees for 35 degrees of road wheel
        "extra_game_fields": [],
    },
    "aug26": {
        "label": "Aug 26 test build v4 (612R, SimulatorConnections 3.2.0)",
        "process": "SimulatorConnections",
        "app_dir": r"C:\Simulator\Aug26_Sprayer612R_TestBuild_v4\net8.0-windows",
        "log": "logs/ConnectionsApp_*.log",
        "game_year": 2022,             # FarmingSimulatorPath defaults to FS22; 2025 when pointed at FS25
        "aliases": {
            # armrest keypad (SCM) and switch panel (DCM) send generic button names on the 612R
            "PLT_SCMButton_1ab": "PLT_AIC_SolutionPump",
            "PLT_SCMButton_2c": "PLT_AIC_Rate1Control",
            "PLT_SCMButton_3ab": "PLT_AIC_Rate2Control",
            "PLT_SCMButton_3c": "PLT_AIC_Rate3Control",
            "PLT_SCMButton_6ab": "PLT_AIC_ResetA",
            "PLT_SCMButton_6c": "PLT_AIC_ResetB",
            "PLT_AIC_DCMButton_01": "PLT_AIC_EngineLowIdle",
            "PLT_AIC_DCMButton_03": "PLT_AIC_EngineHighIdle",
            "PLT_AIC_DCMButton_08": "PLT_AIC_ParkBrake",
            "PLT_SWITCH_23": "PLT_MHC_Warning",
            # lights the cloud sets
            "PLT_AIC_SCMIndicator_1ab": "PLT_AIC_SolutionPumpIndicator",
            "PLT_AIC_SCMIndicator_2c": "PLT_AIC_Rate1ControlIndicator",
            "PLT_AIC_SCMIndicator_3ab": "PLT_AIC_Rate2ControlIndicator",
            "PLT_AIC_SCMIndicator_6ab": "PLT_AIC_ResetAIndicator",
            "PLT_AIC_SCMIndicator_6c": "PLT_AIC_ResetBIndicator",
            "PLT_AIC_SCMIndicator_3c": "PLT_AIC_Rate3ControlIndicator",
            "PLT_AIC_DCMIndicator_01": "PLT_AIC_EngineLowIdleSpeedIndicator",
            "PLT_AIC_DCMIndicator_03": "PLT_AIC_EngineHighIdleSpeedIndicator",
            "PLT_AIC_DCMIndicator_08": "PLT_AIC_ParkBrakeIndicator",
            "VIO_DCU_VehicleGroundSpeed_mph": "VIO_DCU_VehicleGroundSpeed",
        },
        "armrest_as_sent": True,
        "steer_full_lock_deg": 450,    # 612R: wheel clamped to +-450 degrees, x35/450
        "extra_game_fields": ["raiseBoomStatus", "leftBoomStatus", "rightBoomStatus", "seeAndSpray",
                              "nozzleStatus_Group1", "nozzleStatus_Group2", "nozzleStatus_Group3", "nozzleStatus_Group4",
                              "nozzleStatus_Group5", "nozzleStatus_Group6", "nozzleStatus_Group7", "nozzleStatus_Group8"],
    },
}


def get(name):
    if name not in PROFILES:
        raise SystemExit(f"unknown build '{name}'; choose one of: {', '.join(PROFILES)}")
    p = dict(PROFILES[name], name=name)
    p["game_path"] = _game_path(p["game_year"])
    return p


def detect():
    """The build whose app is running now (Aug 26 first), else Apr 20."""
    try:
        import subprocess
        out = subprocess.run(["tasklist", "/fo", "csv", "/nh"], capture_output=True, text=True, timeout=10).stdout
    except Exception:
        out = ""
    for name in ("aug26", "apr20"):
        if f'"{PROFILES[name]["process"]}.exe"' in out:
            return name
    return "apr20"


_running_cache = {}


def running_dir(process_name, max_age=10.0):
    """Folder of the running copy of `process_name` (any copy the user extracted), else None. Cached briefly."""
    import time
    hit = _running_cache.get(process_name)
    if hit and time.time() - hit[0] < max_age:
        return hit[1]
    found = None
    try:
        import ctypes
        from ctypes import wintypes
        psapi, k32 = ctypes.WinDLL("psapi"), ctypes.WinDLL("kernel32")
        k32.OpenProcess.restype = wintypes.HANDLE
        k32.OpenProcess.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
        k32.CloseHandle.argtypes = (wintypes.HANDLE,)
        k32.QueryFullProcessImageNameW.argtypes = (wintypes.HANDLE, wintypes.DWORD, wintypes.LPWSTR,
                                                   ctypes.POINTER(wintypes.DWORD))
        pids = (wintypes.DWORD * 8192)()
        got = wintypes.DWORD()
        psapi.EnumProcesses(pids, ctypes.sizeof(pids), ctypes.byref(got))
        want = process_name.lower() + ".exe"
        for pid in pids[: got.value // ctypes.sizeof(wintypes.DWORD)]:
            h = k32.OpenProcess(0x1000, False, pid)        # PROCESS_QUERY_LIMITED_INFORMATION
            if not h:
                continue
            try:
                buf = ctypes.create_unicode_buffer(1024)
                size = wintypes.DWORD(1024)
                if k32.QueryFullProcessImageNameW(h, 0, buf, ctypes.byref(size)) and \
                        os.path.basename(buf.value).lower() == want:
                    found = os.path.dirname(buf.value)
                    break
            finally:
                k32.CloseHandle(h)
    except (OSError, AttributeError):
        pass
    _running_cache[process_name] = (time.time(), found)
    return found


def log_path(profile):
    """The log file to follow now: in the folder of the copy that is running (else the profile's folder); for
    daily, per-start files, the newest matching file."""
    pattern = os.path.join(running_dir(profile["process"]) or profile["app_dir"], profile["log"])
    if "*" not in pattern:
        return pattern
    files = glob.glob(pattern)
    return max(files, key=os.path.getmtime) if files else pattern.replace("*", "none")
