# Simulator API (local)

One small service on the trainee's PC that the lesson panel and the RAG chatbot talk to, so nothing
else ever reads log files. Standard-library Python, no installs. Listens on `127.0.0.1:47900` only.

```
 virtual armrest ──(scripted port 47800: presses, lights, link)──┐
 Connections app ──(log lines: tail log.txt  OR  live UDP 47901)──┼──► Store (state + events) ──► Lesson engine
 VehicleInfo.xml ──(game file, polled every 200 ms)───────────────┘            │                       │
                                                                               └──── HTTP API :47900 ◄─┘
                                                                         lesson panel · chatbot · tests
```

## What it knows

| Kind | From | Example |
|---|---|---|
| `sent` | the app, every control value it sends to the cloud | `PLT_MHC_MasterSprayOnOff = 1` |
| `cloud` | the app, every value the cloud sends back (online only) | `PLT_AIC_SolutionPumpIndicator = 1`, `VIO_DCU_VehicleGroundSpeed = 62` |
| `app` | milestones in the app | bridge connected, sign-in complete, display launched, cloud link down |
| `game` | VehicleInfo.xml | `boomUnfolded = 0`, `cameraView = 2`, `wheelSpeed` |
| `control` | virtual armrest (when used) | `foot_switch = 1`, `lever = 175` |
| `led` | virtual armrest: lights the cloud switched on | `solution_pump = 1` |
| `lesson` | the lesson engine | step advanced, mistake seen |

With the real armrest box instead of the virtual one, everything except `control` and `led` still works.

## Endpoints

| | | |
|---|---|---|
| GET | `/api/health` | sources, online/offline, armrest link |
| GET | `/api/state` | current state: game file, last value sent/returned per signal, lights, last 10 controls |
| GET | `/api/events?since=<epoch s>` | event history (last 500) |
| GET | `/api/stream` | live events (Server-Sent Events) |
| GET | `/api/lessons` | lesson files in `lessons/` |
| POST | `/api/lesson/setup` `{"id": "..."}` | put the simulator in the lesson's starting state (virtual armrest); returns the trainer note for real rigs |
| POST | `/api/lesson/start` `{"id": "..."}` | start a lesson |
| GET | `/api/lesson` | what the panel shows now: step, progress, hint due, mistakes, how the step is checked |
| POST | `/api/lesson/skip` | skip the current step |
| POST | `/api/lesson/showme` | perform the current step on the virtual armrest |
| GET | `/api/chatbot-context` | what to send your RAG chatbot with the trainee's question |
| POST | `/api/armrest` `{"cmd": "press master_spray 300"}` | pass-through to the virtual armrest |
| GET | `/api/controls` | the control catalogue (`virtual-commandarm/controls.json`) |
| GET | `/api/screen-map` | where things are on the app's screens (`simapi/screens/apr20-r4045.json`) |
| GET | `/api/screens` | which app windows are open: `display` (Gen 4), `pdu` (corner post + Operations + Navigation), `main`; the display also gets `picture`, the Gen 4 picture's box inside its window |
| GET | `/api/screen/<display\|pdu\|main>.png` | live capture of that window (404 until it's open). `display.png` is cropped to the 4:3 Gen 4 picture, whatever size the window is |

## Showing the button (for the UI)

`GET /api/lesson` → `view` now also carries:

- `armrest`: the step's controls with label, module ("Multi-function handle", "Armrest keypad", ...), the
  signal they send and how sure we are of the name. Light these on the armrest picture.
- `screen.press`: screen targets the trainee touches (e.g. `run.softkey.hms`).
- `screen.watch`: where to look for the result (e.g. `pdu.speed`, `run.target_rates.rate3`).

Each screen target has `window`, `rect` = `[x0, y0, x1, y1]` as fractions of that window's capture, and a
`label`. To draw a ring: fetch `/api/screen/<window>.png`, scale `rect` by the image size. Display boxes are
fractions of the Gen 4 picture (the display capture is cropped to it), so they stay right when the trainee
resizes the window: the display letterboxes its picture, and checked on 3 Nov, a 960x1032 window puts it
between dark bands above and below. Corner-post boxes are fractions of the whole window (checked at 1278x898). A step can list
its own targets in an optional `display` field; otherwise they're matched through the step's controls.
The map covers the Gen 4 **Run page** and the corner-post window (40 targets, checked against captures).
Other display pages (menus, setup) need their own entries.

No cross-origin headers, and POSTs must be JSON, so other websites in the trainee's browser can't call it.

## Hooking up the RAG chatbot

When the trainee opens the chatbot, the panel calls `GET /api/chatbot-context` and sends that JSON with
the question. It carries: what the lesson is about, the section and step text, a suggested question,
seconds on the step, the last 10 controls used, the game state and the lights that are on.
Your chatbot only needs to accept one extra JSON field next to the question.

## Builds

`python -I run_simapi.py --build apr20|aug26|auto` (default `auto`: whichever app is running). Profiles are in
`simapi/profiles.py`; `/api/health` reports the active one.

| | Apr 20 (`apr20`) | Aug 26 test build v4 (`aug26`) |
|---|---|---|
| App | Display and CommandARM Simulator 3.2.0.7, R4045 (2019) | SimulatorConnections 3.2.0, 612R (2025) Premium, also R4045, 6R/8R, SPFH |
| Folder | `C:\Simulator\Apr20_LTTS_FS25_ConnectionsApp_2` | `C:\Simulator\Aug26_Sprayer612R_TestBuild_v4` (installed 3 Nov 2026) |
| Log | `log.txt` | `logs\ConnectionsApp_yyyyMMdd.log`, a new file per day and per start (followed automatically) |
| Virtual armrest | used whenever `SBMEmulator` runs | only with `DevelopmentSettings:UseSBMEmulator=true` in `appsettings.local.json` (set on the installed copy; original kept as `.orig`), and `SBMEmulator` must run before Connect |
| "The app sent X" | from the log (`SendVIOData`) | the build logs no control values, so it comes from the virtual armrest while it is linked to the app (same decoding: lever not while parked, dial `step × 500 + 1000`, steering `wheel × 35 / 450`) |
| Signal names | canonical | translated to canonical: `PLT_SCMButton_1ab` → `PLT_AIC_SolutionPump`, `PLT_AIC_DCMButton_08` → `PLT_AIC_ParkBrake`, `PLT_SWITCH_23` → `PLT_MHC_Warning`, `VIO_DCU_VehicleGroundSpeed_mph` → `VIO_DCU_VehicleGroundSpeed`, ... |
| Game files | FarmingSimulator2025 | FarmingSimulator2022 by default (the app's `FarmingSimulatorPath`); game GPS goes to the cloud as J1939 frames |

Lessons always use canonical names, so the same lesson file runs on either build.

## Two ways to get the app's log lines

1. **Tail log.txt** (default, `--log tail`). Needs no change to the app. Measured today: presses
   show up in about 0.3 s. On start the API reads back the app's milestones since it last started
   (sign-in, cloud link, display), so it knows it's online even when started after sign-in.
2. **Live UDP from the app** (`--log udp`). The app's own logger sends every line to `127.0.0.1:47901`
   the moment it's written: no file reading, no rotation gaps. Needs one addition to
   `C:\Simulator\Apr20_LTTS_FS25_ConnectionsApp_2\net8.0-windows\log4.config` (back the file up first;
   removing the two additions undoes it):

   ```xml
   <!-- inside <log4net>, next to the RollingFileAppender -->
   <appender name="LessonStudioUdp" type="log4net.Appender.UdpAppender">
     <remoteAddress value="127.0.0.1" />
     <remotePort value="47901" />
     <layout type="log4net.Layout.PatternLayout">
       <conversionPattern value="%date [%thread] %-5level - %message%newline" />
     </layout>
   </appender>
   <!-- inside <root>, next to the existing appender-ref -->
   <appender-ref ref="LessonStudioUdp" />
   ```

   **Not applied.** Waiting for your OK (board card A2).

## Run

```
python -I run_simapi.py            # tail log.txt
python -I run_simapi.py --log udp  # after the log4.config change
python -I simapi/api_check.py      # end-to-end check (10 checks)
```
