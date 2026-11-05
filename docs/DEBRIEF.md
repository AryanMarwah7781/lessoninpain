# Lesson Studio debrief

5 Nov 2026 · exported from the "Lesson Studio debrief" doc (the live, editable version)

Lesson Studio turns the John Deere sprayer simulator into guided lessons that check themselves: 13 lessons are written (7 for the 612R, 6 for the R4045), and on 4 November the whole chain ran on the real rig for the first time. Next is proving the lessons with the real armrest, then expert review, then building toward a full training product inside the display simulator app.

## Lesson plans

A lesson is a list of steps a trainee does on the real armrest and display. Each step shows what to do and why, the operator's-manual figure of the control, and a ring on an armrest drawing; it gives timed hints and ticks itself off when the simulator sees it done. Steps the simulator cannot see (a walk-around, reading a gauge) have a Done button. Sections are Learn, Practice or Assessment (no hints), and long lessons can be resumed at marked points.

| Machine | Lesson | Time | Steps |
| --- | --- | --- | --- |
| 612R | Know your 612R cab: CommandARM, multi-function lever and corner post | 16 min | 24 |
| 612R | Drive in Auto mode and transport safely | 17 min | 23 |
| 612R | Fill the solution tank and load chemicals safely | 18 min | 27 |
| 612R | Unfold, level and protect the boom | 16 min | 22 |
| 612R | Start spraying right: rates, sections, HMS headlands and AutoTrac | 16 min | 22 |
| 612R | No spray or the wrong rate: find the fault and recover | 19 min | 23 |
| 612R | A full spraying day: from daily checks to parked and rinsed | 107 min | 110 |
| R4045 | Field-ready: from the yard to spraying and back | 40 min | 41 |
| R4045 | Headland turn with HMS, done in the right order | 15 min | 7 |
| R4045 | Field zones: rates, speeds and sections on the go | 15 min | 7 |
| R4045 | Boom folded mid-pass: recover safely | 15 min | 6 |
| R4045 | Obstacle on the right: protect the boom | 15 min | 5 |
| R4045 | No spray at the nozzles: find the fault | 20 min | 6 |

The 612R lessons (251 steps, about 3.5 h) are written from operator's manual OMKK105338 and cite its pages; 133 steps check themselves, the rest use Done. 47 steps are marked draft because they use a button whose simulator mapping is unconfirmed. The R4045 lessons (72 steps, about 2 h) come from the Apr 20 app's own procedures and wait for the R4045 manual. None has yet been reviewed by an experienced operator.

## How it fits together

![How Lesson Studio fits the simulator: the armrest (real or virtual) feeds the Connections app, which talks to the cloud machine and writes the Farming Simulator game files; the simulator API reads the app log, replay log, game file and virtual armrest, and feeds the Lesson Studio window](debrief-architecture.png)

Every press goes through the Connections app to the cloud machine. Lesson Studio never sits in that path: it reads what the app, the replay log and the game report, so it cannot slow or break the simulator.

## Where we are now

The software is built and runs on the rig; what is left is proving the lessons with the real armrest and getting them reviewed.

| Part | Status | What we know |
| --- | --- | --- |
| Lesson files (13) | Working | All pass the lesson checker; the 612R set is exported as a shareable Markdown file |
| Simulator API | Working | Follows the Apr 20 and Aug 26 builds, runs the lessons; installed on the rig mini PC |
| Lesson Studio window | Working | WPF on .NET 8 (the display simulator app's stack); 612R / R4045 chooser |
| Virtual armrest | Working | Drives the cloud machine on the Aug 26 build: lights come back, boom moves, lever took it to a steady 8.27 |
| Farming Simulator 22 link | Working | LTTS mods installed; boom and wheel speed reach the game |
| Rig mini PC | Working | Repo cloned, setup script passed, desktop shortcut; reachable by SSH on the rig network |
| Real armrest in lessons | Partly | Presses read from the app's Message Replay Logger; encodings confirmed 4 Nov; a full lesson run is still to do |
| Rings on the display | Partly | Mapped for the R4045's Gen 4 display only; the 612R's G5 is not mapped |
| Operator review | Not started | No experienced 612R operator has checked the steps yet |
| Chatbot (RAG) | Not started | The API already serves each step's context for it; not connected |
| Display atlas | Not started | Every display screen captured and explained; waiting for the R4045 manual |

## What the rig taught us on 4 November

The full chain works with real hardware, but the app has two habits every session must work around.

- **The cloud machine drives.** With the Aug 26 build, releasing the park brake, high idle and the lever above its 125 centre moved it, which never happened on the Apr 20 build.
- **The app records the real armrest only if Message Replay Logger is ticked before Connect,** and it clears that tick every time it starts. Lesson Studio should say so on screen.
- **The real box encodes keys its own way.** Keypad and side keys count presses (8 at rest, even = pressed); two side keys are status values, not buttons; the steering wheel sends its own message in degrees (±450). Lesson Studio now reads all of this.
- **Speed comes from the lever and speed dial.** The rig's accelerator pedal is ignored by the sprayer app; its clutch pedal is the boom-fold pedal.
- **Physical Display mode needs the rig's displays wired to the PC;** without them, choose HTML or Connect fails.
- **The rig holds six app builds.** The combine build (3 Nov) has newer app code than the Aug 26 v4 the lessons use; what changed is not yet checked.

## How we confirm a signal

A step is only as good as the signal it checks, so each control is confirmed in four layers; the last needs the rig and is not done yet.

| Layer | What it proves | Status |
| --- | --- | --- |
| 1. The app's code | Which raw key each armrest message carries, the signal name the app turns it into (key b1 becomes PLT_MHC_MasterSprayOnOff) and how pressed is encoded; each control is marked named or inferred | Working |
| 2. Virtual armrest, live | The press reaches the cloud machine: the Apr 20 build logs every signal it sends; on both builds the machine's light comes back and the game file changes | Working |
| 3. Real box, raw | The replay log shows exactly what the real box sends; on 4 Nov its encodings matched the app's rules | Working |
| 4. Button census on the rig | Which physical button is which key on the 612R: each button pressed once by its manual letter, with Message Replay Logger and the app's Show VIO Viewer on, gives button, key and signal name together | Not started |

The census also settles the 47 draft steps, whose buttons are only inferred today.

### Which files show a signal

On the Apr 20 build (R4045) one log proves a signal went out and what came back; the Aug 26 build (612R) logs neither, so we read both ends instead.

| Build | File | What it shows |
| --- | --- | --- |
| Apr 20 | `log.txt` in the app folder, `SendVIOData` lines | The app sent a signal to the cloud machine, e.g. `{"signal":"PLT_MHC_HMS","value":"1"}` |
| Apr 20 | `log.txt`, `OnStompMessageReceived` lines | What the cloud sent back: lights, ground speed |
| Aug 26 | `logs\ConnectionsApp_<date>.log` | No sent or received signals: on 4 Nov it held 0 `SendVIOData` lines, and its 3,557 "received from EC2" lines were all keep-alive pongs |
| Aug 26 | `logs\ReplayLogs\SBMReplayLog_*.bin` (Message Replay Logger on) | Input: exactly what the armrest box sent the app, key and value |
| Aug 26 | `VehicleInfo.xml` in the FS22 DeereVehicleControl mod folder | Output: what the app wrote to the game, such as wheel speed, boom raise and fold, lever, nozzles |
| Aug 26 | `gameToSim.xml`, same folder | What the game sent back: GPS and speed |
| Both | The armrest's lights (virtual armrest: `SBMEmulator.log`) | The cloud received a press and answered |

On the 612R no file says the app turned a key into a named signal and sent it, so Lesson Studio rebuilds those signals from the replay log with the app's own decoding rules. The one direct view is the app's **Show VIO Viewer** window, which lists signal names and values live. Next step: open it during the button census, then have Lesson Studio read its text through Windows UI Automation into a file, giving the 612R the same proof the Apr 20 `log.txt` gives.

## The plan to the end

The end state is a training product inside the display simulator app: authors build lessons with AI help, trainees run them on the real rig with on-screen guidance and a chatbot, and managers assign them and see where people get stuck. Phases 1 and 2 are under way; 3 to 5 follow the product plan drawn up in October.

1. **Prove the lessons on the rig (now).** Record every physical 612R button once (a 10-minute button census), run each 612R lesson with the real armrest, fix any key or steering mismatch, and add the Message Replay Logger reminder.
    - Done when: all 7 612R lessons run start to finish on the rig and every self-checking step ticks.
2. **Make the content right.** An experienced operator reviews every step, draft steps first; the R4045 lessons are rewritten from the R4045 manual; the G5 display is mapped so its rings line up, possibly through a virtual display over VNC for exact screens and taps; the display atlas explains every screen.
    - Done when: an operator signs off the steps and the rings line up on both displays.
3. **Complete the trainee experience.** Connect the RAG chatbot to each step's context, score the Assessment sections and keep each trainee's results.
    - Done when: a trainee can run a lesson alone, ask the chatbot and get a result.
4. **Authoring studio and admin console.** An author gives a goal and the skills to cover, AI drafts the steps and the simulator checks them; an admin console assigns lessons and shows where people get stuck (both have approved mock-ups).
    - Done when: a new lesson is written and assigned without code.
5. **Into the display simulator app.** Move the lesson window into the Connections app, which uses the same WPF and .NET 8 stack, and roll out; a marketplace for sharing lessons comes later.
    - Done when: lessons ship as part of the app.

## Open questions

- [ ] Who reviews the steps? An experienced 612R operator is needed for phase 2.
- [ ] When does the R4045 manual (RAG) arrive? The R4045 lessons and the display atlas wait for it.
- [ ] What are the "cutouts" asked for alongside the display atlas: cut-out images of each control, or something else?
- [ ] Should the lessons move to the combine build (3 Nov), which has newer app code than Aug 26 v4?
- [ ] Can Tailscale go on the rig mini PC, so it can be reached from outside the rig network?
- [ ] Is it OK to add the UDP log line to the Apr 20 app's logging settings, for live R4045 feedback?
- [ ] Where does the AI run when authoring arrives (phase 4): on our own hardware or online? A business decision, still open.

## Links

| What | Where |
| --- | --- |
| Code, lessons and setup guide (private) | [GitHub: lessoninpain](https://github.com/AryanMarwah7781/lessoninpain) |
| This debrief, live and editable | [Lesson Studio debrief](https://claude.ai/artifact/Sjbvd29a2eFuwUY76bCp4f) |
| Every lesson with its steps | [Lesson Studio Library](https://claude.ai/artifact/HZ9cyRLeixN4DfaNouU6s5) |
| How the virtual armrest was built | [SBM Emulator Build Notes](https://claude.ai/artifact/VCQJ2Hp7wzXBiLxiU6nStr) |
| Driving the machine from the game | [Simulator Drive Loop](https://claude.ai/artifact/5f9AjHRuD9bWYCc6Ab1zp5) |
| Task board | [Build board](https://claude.ai/artifact/X8UzZQjpHjr5VsMKoMbezm) |

The claude.ai pages are private until shared from their Share menu. Rig recordings (armrest replay logs, box settings, firmware) are in the handoff zip under `rig-capture\2026-11-04`.
