# Lesson Studio

Guided lessons for the John Deere sprayer simulator (Display and CommandARM Simulator Connections): each step
shows what to press on the armrest and display with the operator's-manual figure beside it, gives timed hints, and
checks the step from what the simulator reports.

- `lessons/` - 7 lessons for the **612R** (written from operator's manual OMKK105338) and 6 for the **R4045**.
  `FORMAT.md` describes the file format; `python -I lessons/check_lesson.py --validate lessons/<file>.json` checks one.
- `simapi/` - the local simulator API on `127.0.0.1:47900` (standard-library Python). It follows the Connections
  app's log, the Farming Simulator game file and the armrest, and runs the lessons. See `simapi/API.md`.
- `lesson-panel/` - the Lesson Studio window (WPF, .NET 8). `dist/LessonStudio/` is a ready-built copy.
- `virtual-commandarm/` - the virtual armrest (`SBMEmulator.exe`) that stands in for the SBM box.
- `manual/` - the 612R manual text and figures the lessons show.

## Run it

Needs **Python 3.12** and the **.NET 8 Desktop Runtime** (free from Microsoft; the SDK is not needed).

1. In the Connections app (Aug 26 build): sign in, **Settings > VNC Streaming Mode**: *Physical Display* if the rig's
   displays are wired to this PC, else *HTML*.
2. **Sprayer Operator Experience > Desktop**. With the **real armrest**, tick **Message Replay Logger** in the developer
   row *before* Connect: Lesson Studio reads the real presses from that file (up to 2 s late).
3. **Connect Simulator Bridge**, **Launch Machine Simulator**, **Launch Farming Simulator**.
4. Double-click **`Start Lesson Studio.cmd`**: the simulator API opens in its own window, then Lesson Studio.
   Choose **612R** or **R4045**, then a lesson.

`Use REAL armrest.cmd` / `Use VIRTUAL armrest.cmd` switch the Connections app copy between the real box and the
virtual armrest (`tools/armrest_mode.py`; restart the app afterwards). With the virtual armrest, Lesson Studio can
also set each lesson up and "show me" a step.

## Status

Draft lessons, not yet reviewed by an experienced operator; steps marked draft use buttons whose simulator mapping is
not confirmed. Display rings are mapped for the R4045's Gen 4 display only, not yet for the 612R's G5.
