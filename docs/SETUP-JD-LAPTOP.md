# Moving Lesson Studio to the JD laptop

How to set up everything on a new Windows laptop, as of 5 Nov 2026. Read `docs/DEBRIEF.md` first for what the
project is and where it stands. Steps 1 to 4 get you running; 5 to 7 bring over the rig access and the working
context.

## What is in the handoff zip

| Folder or file | What it is | Goes to |
| --- | --- | --- |
| `START-HERE.md` | This file | read it |
| `lesson-studio.bundle` | The whole git repo, all history, as one file (in case GitHub is blocked) | step 2 |
| `DEBRIEF.md`, `debrief-architecture.png` | Where the project stands | read it |
| `research\` | Earlier analysis: `sprayer612R\` (Aug 26 build reports + decompiled code), `apr20-connections\` (Apr 20 build), `controls-lesson-master.md` | `C:\Users\<you>\re\` |
| `rig-capture\2026-11-04\` | From the rig mini PC: real armrest replay logs, box settings (`monitor_settings.toml`), box firmware, app and game logs, the newer combine build's app DLL | `C:\Users\<you>\re\rig-capture\` |
| `claude-memory\` | Claude Code's notes on this project | step 7 |
| `612R-lesson-plans.zip` | The 7 612R lessons as a shareable Markdown file with manual figures | share as needed |

Not in the zip, on purpose: the Connections app builds and Farming Simulator (large; copy them separately), and
any private SSH key (make new ones, step 5).

## 1. Install the tools

In PowerShell (if winget is blocked on the JD laptop, use the download links instead):

```powershell
winget install --id Git.Git -e                       # https://git-scm.com/download/win
winget install --id Python.Python.3.12 -e            # https://www.python.org/downloads/  (3.10+ works)
winget install --id Microsoft.DotNet.DesktopRuntime.8 -e   # runs Lesson Studio
```

To **build** Lesson Studio you also need the .NET 8 SDK. A per-user install needs no admin rights:

```powershell
Invoke-WebRequest https://dot.net/v1/dotnet-install.ps1 -OutFile "$env:TEMP\dotnet-install.ps1"
& "$env:TEMP\dotnet-install.ps1" -Channel 8.0 -InstallDir "$env:LOCALAPPDATA\dotnet8-sdk"
```

Optional: GitHub CLI (`winget install --id GitHub.cli -e`) and Claude Code. Python needs no extra packages.

## 2. Get the code

```powershell
mkdir $env:USERPROFILE\re; cd $env:USERPROFILE\re
git clone https://github.com/AryanMarwah7781/lessoninpain.git lesson-studio   # private: sign in to GitHub when asked
```

GitHub blocked? Clone from the bundle in the zip, then point it back at GitHub for later:

```powershell
git clone <zip folder>\lesson-studio.bundle lesson-studio
git -C lesson-studio remote set-url origin https://github.com/AryanMarwah7781/lessoninpain.git
```

Any folder works; the scripts find their files relative to themselves.

## 3. Put the apps where the scripts look

| App | Where | Notes |
| --- | --- | --- |
| Connections app, Aug 26 test build v4 (612R) | `Documents\jd_resources\Aug26_Sprayer612R_TestBuild_v4\` (extract `Aug26_Sprayer612R_TestBuild_v4.zip`) | The lessons are written for this build. The scripts also find it under `C:\Simulator\...` |
| Connections app, Apr 20 (R4045) | `C:\Simulator\Apr20_LTTS_FS25_ConnectionsApp_2\` | Only for the R4045 lessons |
| Farming Simulator 22 | GIANTS default `C:\Program Files (x86)\Farming Simulator 2022\` | Optional at home; standard edition is enough. Start it once, then quit |

Then run **`Setup.cmd -Armrest virtual`** from the repo. It checks the tools, finds the app, switches it to the
virtual armrest, finds FS22 and offers to install the LTTS sprayer mods (savegame 1 is backed up first), and puts
a Lesson Studio shortcut on the desktop. At the rig the mini PC already has all this.

## 4. Run it

**At home (virtual armrest):**

1. Double-click `Use VIRTUAL armrest.cmd` (switches the app and starts `virtual-commandarm\SBMEmulator.exe`).
2. Connections app: sign in yourself; **Settings > VNC Streaming Mode > HTML**; **Sprayer Operator Experience >
   Desktop > Connect Simulator Bridge** (the virtual armrest window shows connected); **Launch Machine Simulator**;
   **Launch Farming Simulator** if installed.
3. `Start Lesson Studio.cmd` (the simulator API opens in its own window, then Lesson Studio). Choose 612R.

**At the rig:** the mini PC is set up; follow README section 5. Remember: tick **Message Replay Logger** before
every Connect, because the app forgets it.

## 5. Reach the rig mini PC

The mini PC is `JDSIM-SPR-001`, user `johndeere`, `192.168.1.140` on the rig Wi-Fi (PEOIT). SSH is on; key login
works, while password login for this account failed on 4 Nov, so use a key.

1. On the JD laptop: `ssh-keygen -t ed25519` (accept the defaults), then show the public key:
   `Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub`.
2. On the mini PC, in an **administrator** PowerShell (`johndeere` is an admin, so SSH reads the admin key file):
   ```powershell
   Add-Content -Path "$env:ProgramData\ssh\administrators_authorized_keys" -Value "<the public key line>" -Encoding ascii
   icacls "$env:ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"
   ```
3. From the JD laptop, on the rig Wi-Fi: `ssh johndeere@192.168.1.140 hostname` should print `JDSIM-SPR-001`.

Updating the mini PC: `git pull` in `C:\Users\JohnDeere\Documents\lesson-studio` (needs a GitHub sign-in there),
or copy a bundle over SSH (`git bundle create x.bundle main`, `scp`, then `git pull x.bundle main` on the mini PC).
Restart the API after an update with `tools\start-api.cmd`.

Optional: Tailscale on both machines would reach the mini PC from any network (an open question in the debrief).
The 612R manual vault (RAG) lives on the Spark box `spark-bf0b` (Tailscale `100.115.38.24`, user `dbw_ltts`); a new
laptop needs Tailscale and its key added there by someone with access.

## 6. Build and check

| Task | Command (from the repo folder) |
| --- | --- |
| Validate a lesson | `python -I lessons/check_lesson.py --validate lessons/612r-controls-tour.json` |
| Export the 612R lessons to Markdown | `python -I lessons/export_markdown.py <out folder>` |
| Run the API alone | `python -I run_simapi.py --build aug26` (or `apr20`, `auto`); health at http://127.0.0.1:47900/api/health |
| Rebuild Lesson Studio | `& "$env:LOCALAPPDATA\dotnet8-sdk\dotnet.exe" publish lesson-panel/LessonPanel.csproj -c Release -o dist/LessonStudio --self-contained false`, then commit `dist/` |
| Rebuild the virtual armrest | `virtual-commandarm\build.cmd` (uses the C# compiler built into Windows) |

## 7. Continue with Claude Code

Claude Code keeps per-project notes in `%USERPROFILE%\.claude\projects\<folder key>\memory\`. The key is the
project folder's path with `:` and `\` turned into `-`: for `C:\Users\jdoe\re\lesson-studio` it is
`C--Users-jdoe-re-lesson-studio`.

1. Open Claude Code once in the repo folder (this creates the projects folder).
2. Copy `claude-memory\lesson-studio\*.md` from the zip into `%USERPROFILE%\.claude\projects\<folder key>\memory\`
   (`MEMORY.md` is the index Claude loads). `claude-memory\home\` holds two older notes from the home folder; copy
   them into the same folder if you want that history too.
3. The notes mention paths from the old laptop (`C:\Users\user\...`); Claude should check a path before using it.

### Brief for the next Claude session

You are continuing Lesson Studio. Read `docs/DEBRIEF.md`, `README.md`, `simapi/API.md` and `lessons/FORMAT.md`.
Ground rules that carry over: never sign in to the John Deere account for the user (they sign in themselves); do
not touch the AWS session; do not change the Apr 20 app's `log4.config` without an explicit OK; ask before any
change to another computer; keep the GitHub repo private (it holds John Deere manual content).

Open work, in order:

1. **Replay-logger reminder:** when the app's bridge is connected to the real box but no replay log is being
   written, show "Tick Message Replay Logger, then Disconnect and Connect" in Lesson Studio (API health + panel).
2. **Button census on the rig:** a guided script that names each 612R control by its manual letter, records the
   replay log and the app's Show VIO Viewer, and writes the physical button, key and signal map; use it to fix
   `virtual-commandarm/controls.json` and confirm the 47 draft steps and the steering sign.
3. **VIO Viewer to file:** read the Show VIO Viewer window through Windows UI Automation, so the Aug 26 build gets
   the "signal sent" evidence the Apr 20 `log.txt` gives.
4. **Combine build:** decompile `rig-capture\2026-11-04\combine-build\SimulatorConnections.dll` (3 Nov) and diff
   the sprayer code against Aug 26 v4 (it may handle the G923 wheel message 1023 that v4 rejects).
5. **Virtual armrest extras** (offered, not yet asked for): a gradual drive control (hold a key to push the lever)
   and the clutch boom-fold pedal (pressed at 50 % or more, held 5 s).
6. **G5 display:** map its screens for the rings, and consider the virtual physical display (VNC) described in the
   debrief.
