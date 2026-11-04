# Lesson Studio

Guided lessons for the John Deere sprayer simulator (the Display and CommandARM Simulator Connections app with
Farming Simulator 22). Each step shows the trainee what to press on the armrest and the display, with the
operator's-manual picture beside it, gives timed hints, and ticks itself off when the simulator sees it done.

- **612R (2025):** 7 lessons, about 3½ hours, written from operator's manual OMKK105338.
- **R4045 (2019):** 6 lessons, about 2 hours.

> This repository contains John Deere operator's-manual text and figures and details of the simulator app.
> Keep it **private**.

---

## 1. What the PC needs

| | What | Where it comes from |
|---|---|---|
| 1 | Windows 10 or 11 | |
| 2 | **Connections app**, Aug 26 test build v4 (`SimulatorConnections.exe`, 3.2.0) | the `Aug26_Sprayer612R_TestBuild_v4.zip` build (not in this repo); the rig PC may already have it |
| 3 | **Farming Simulator 22**, standard edition | GIANTS store (installs where the app expects it) or Steam |
| 4 | **Git**, **Python 3.12**, **.NET 8 Desktop Runtime** | `winget`, step 2 below |

The armrest box (SBM) with the CommandARM, the steering wheel and the display hardware are the rig's.

## 2. Install the tools (once)

Open **PowerShell** and run:

```powershell
winget install --id Git.Git -e
winget install --id Python.Python.3.12 -e
winget install --id Microsoft.DotNet.DesktopRuntime.8 -e
```

Close PowerShell, open a new one, and check:

```powershell
git --version
python --version          # Python 3.12.x  (or: py -3 --version)
dotnet --list-runtimes    # a line "Microsoft.WindowsDesktop.App 8.0.x"
```

No other Python packages are needed. Lesson Studio itself comes ready-built in `dist\LessonStudio`.

## 3. Get Lesson Studio

```powershell
cd $env:USERPROFILE\Documents
git clone https://github.com/AryanMarwah7781/lessoninpain.git lesson-studio
```

GitHub asks you to sign in the first time (the repository is private). To update later:

```powershell
cd $env:USERPROFILE\Documents\lesson-studio
git pull
```

## 4. Set up the Connections app and the game (once)

1. **Put the Connections app somewhere**, for example extract the zip to `Documents\jd_resources\`.
2. **Choose the armrest.** Double-click **`Use REAL armrest.cmd`** in the lesson-studio folder for the rig's box
   (this is how the app ships), or **`Use VIRTUAL armrest.cmd`** to practise without hardware (see section 7).
   It finds the app copy that is running, else the one in `Documents\jd_resources`. If yours is elsewhere, drag
   the app's folder onto the `.cmd` file.
3. **Farming Simulator 22:** start it once on its own and quit (the GIANTS version asks for its product key the
   first time). If it is not in `C:\Program Files (x86)\Farming Simulator 2022\`, open the Connections app's
   **Settings** and paste the full path to `FarmingSimulator2022.exe` under *Path to where Farming Simulator is
   installed*.
4. The first **Launch Farming Simulator** asks *"The following mods are out of date ... Update mods?"*: answer
   **Yes**. It installs the LTTS sprayer mods and **replaces savegame slot 1** with the sprayer savegame.

## 5. Every session

**In the Connections app:**

1. Start it and **sign in** (only you sign in; nothing in this repo does).
2. **Settings > VNC Streaming Mode:**
   - **Physical Display** if the rig's displays are wired to this PC;
   - **HTML** if not (otherwise Connect fails with *"Private (CommandARM) adapter not found"*).
   The app forgets this choice when it restarts.
3. Open **Sprayer Operator Experience** (the 612R; *Sprayer 2019 Operator Experience* is the R4045), then **Desktop**.
4. **Real armrest only:** in the developer row, tick **Message Replay Logger** *before* Connect. Lesson Studio reads
   the real armrest's presses from that log (the app writes it every 2 s, so a press can take up to 2 s to count).
5. **Connect Simulator Bridge**, then **Launch Machine Simulator**, then **Launch Farming Simulator**.

**Then Lesson Studio:**

6. Double-click **`Start Lesson Studio.cmd`**. A *Simulator API* window opens (leave it open; closing it stops the
   lessons), then Lesson Studio.
7. Choose **612R** or **R4045**, then a lesson. **Know your 612R cab** (16 min) is a good first one.

Close Chrome and other big apps first: the app, the display, the game and Lesson Studio together need several GB.

## 6. During a lesson

- The current step shows what to do, why, the manual picture, and a ring on the armrest drawing.
- **Hint** shows the next hint; **Done** buttons are for things the simulator can't see (a walk-around, reading a
  gauge); **Skip** moves on.
- In an **Assessment** section there are no hints.
- Long lessons can be resumed at their marked sections.

| | Real armrest | Virtual armrest |
|---|---|---|
| Steps judged from your presses | yes, up to 2 s late | yes, at once |
| Automatic setup of the starting state | no: follow the trainer note at the start of the lesson | yes |
| **Show me** | no | yes |

## 7. Practising without the rig (virtual armrest)

1. Double-click **`Use VIRTUAL armrest.cmd`**. It switches the app over and starts the virtual armrest
   (`virtual-commandarm\SBMEmulator.exe`); restart the Connections app afterwards.
2. In the app: sign in, **Settings > VNC Streaming Mode > HTML**, **Sprayer Operator Experience > Desktop >
   Connect**. The virtual armrest window shows **connected**.
3. **Start Lesson Studio.cmd** as usual.

Switch back with **`Use REAL armrest.cmd`** before using the rig's box.

## 8. When something is wrong

| What you see | What to do |
|---|---|
| Lesson Studio says *Simulator API not running* | The API window was closed or crashed: run `Start Lesson Studio.cmd` again and read the API window. |
| *The armrest isn't linked* with the real box | Message Replay Logger wasn't ticked before Connect: Disconnect, tick it, Connect again. |
| *The armrest isn't linked* with the virtual armrest | Start the virtual armrest **before** pressing Connect; check `Use VIRTUAL armrest.cmd` was run and the app restarted. |
| Connect fails with *Private (CommandARM) adapter not found* | Settings > VNC Streaming Mode > **HTML** (or plug in the rig's displays). |
| A press doesn't tick the step | Wait 2 s (real armrest). If it never counts, note the button and press **Skip**. |
| *Python 3 was not found* | `winget install --id Python.Python.3.12 -e`, then open a new window. |
| Lesson Studio doesn't open | Install the .NET 8 Desktop Runtime (section 2). |
| The game opens on its menu, not the sprayer | Load savegame 1 (DeereSprayerMapLF02) yourself. |
| The rings on the display don't line up | Expected on the 612R: the rings are mapped for the R4045's Gen 4 display only. |

## 9. For developers

| Task | Command |
|---|---|
| Check a lesson file | `python -I lessons/check_lesson.py --validate lessons/612r-controls-tour.json` |
| Export the 612R lessons to Markdown | `python -I lessons/export_markdown.py <out folder>` |
| Run the API on its own | `python -I run_simapi.py --build aug26` (or `apr20`, or `auto`); health at <http://127.0.0.1:47900/api/health> |
| Rebuild Lesson Studio (needs the .NET 8 SDK) | `dotnet publish lesson-panel/LessonPanel.csproj -c Release -o dist/LessonStudio --self-contained false` |
| Rebuild the virtual armrest | `virtual-commandarm\build.cmd` (uses the C# compiler that ships with Windows) |

**Layout**

```
lessons/              lesson files (*.json), FORMAT.md, validator, Markdown exporter
simapi/               simulator API (standard-library Python): app log, game file, armrest, lesson engine; API.md
lesson-panel/         Lesson Studio source (WPF, .NET 8)
dist/LessonStudio/    Lesson Studio, ready-built
virtual-commandarm/   virtual armrest (SBMEmulator.exe), controls.json, tests
manual/               612R manual text, figures and the figure map the lessons use
tools/                armrest_mode.py, find-python.cmd
*.cmd                 Start Lesson Studio, Use REAL / VIRTUAL armrest
```

## Status

Draft lessons, not yet reviewed by an experienced 612R operator. 47 of the 612R steps are marked *draft*: they use
a button whose simulator mapping is not confirmed (Quick Stop, AutoTrac Resume, Transport Lock, configurable
buttons) or a drill the manual doesn't describe. Reading the real armrest through the replay log is new and not yet
confirmed on hardware.
