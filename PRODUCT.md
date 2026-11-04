# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

The Connections app's own stack, because the lesson panel will eventually become part of that app (user, 3 Nov 2026): WPF on .NET 8 (`net8.0-windows`), C# and XAML, Newtonsoft.Json, WebView2 for WPF where web content is needed; no third-party UI library (the app has none). Built as a UserControl the app can host, inside a standalone window for the trainee's second monitor. Data still comes from the local simulator API (`simapi/server.py`, `127.0.0.1:47900`). (An earlier choice of plain HTML/CSS/JS was replaced by this.)

## Users

- Primary: customers and operators at a demo table, often on a CommandARM for the first time, and students at a training centre, sometimes with an instructor nearby. Mixed experience.
- Not the target: John Deere staff.
- Situation: the trainee sits at the simulator rig with the Gen 4 display simulator and corner post on one screen, the lesson panel on a second monitor, and a CommandARM (real, or the virtual armrest on this PC) under their right hand.
- Job: work through a lesson step by step on the real controls, find the right button without hunting, recover from mistakes, and come away able to do it on the machine.

## Product Purpose

Lesson Studio teaches the John Deere R4045 sprayer (2019, Gen 4 display, CommandARM) on the Display and CommandARM Simulator (Connections app, Apr 20 build). The lesson panel tells the trainee what to do, shows exactly which control to press on the armrest and where to touch or look on the display, checks what they actually did through the simulator API, and helps when they are stuck. Success: a trainee finishes a complex lesson (fault finding, recovery, ordering) without an instructor pointing at buttons.

## Positioning

The panel knows what the trainee actually pressed and what the machine did, from the simulator itself (armrest presses, cloud signals, game state), not from self-reported checkboxes. It points at the real control: the manual's own photo of the button, a live CommandARM that lights up the target, and a ring on the live display.

## Operating Context

- Rig: Connections app with the Gen 4 display window and corner-post window; CommandARM through the SBM box or the virtual armrest (`virtual-commandarm/SBMEmulator.exe`); optional Farming Simulator 25 with the DeereVehicleControl mod.
- Online needs the trainee's John Deere sign-in, which they do themselves; offline, only the armrest and game side are checked.
- The panel is a full-screen page on its own monitor, used for 15 to 40 minutes per lesson, read at arm's length while hands are on the armrest.
- Instructor may stand behind the trainee and glance at the same screen.

## Capabilities and Constraints

- Data comes from the simulator API: `/api/lesson` (step, hints, mistakes, armrest and screen targets), `/api/stream` (live events), `/api/state`, `/api/screen/<display|pdu>.png` (live captures), `/api/lesson/start|skip|showme|setup`, `/api/chatbot-context`.
- Six lessons today (`lessons/*.json`), format in `lessons/FORMAT.md`.
- Manual figures come from the 612R operator manual (OMKK105338, 400R-616R), `manual/figures`; the simulated machine is a 2019 R4045, so some layouts may differ; mark uncertain ones.
- The handle button positions follow the manual's lettered figure (NX711654/NX707642); some app keys are inferred.
- The RAG chatbot exists on the user's other machine and is not connected yet; the panel prepares the context to send it.
- Undecided: whether the display ring is also drawn on top of the real display window (overlay) or only on the mirror.

## Brand Commitments

None confirmed. The machine's own interfaces (Gen 4 display, corner post, CommandARM) are the trainee's reference world. Do not invent John Deere logos or marks.

## Evidence on Hand

- Lessons: `lessons/*.json`; results in `lessons/results`.
- Control catalogue: `virtual-commandarm/controls.json` (62 controls).
- Screen map: `simapi/screens/apr20-r4045.json` (40 targets on the Run page and corner post).
- Manual figures and captions: `manual/figures`, `manual/figures.jsonl`, `manual/captions.jsonl`.
- No user testing, trainee feedback, or completion data yet; do not invent any.

## Product Principles

1. Point at the real thing: the trainee should never have to translate a description into a location.
2. Truth from the machine: a step is done when the simulator says so, and the panel says what it saw.
3. Calm under pressure: mistakes are explained, not punished; the next action is always obvious.
4. Readable from the seat: hands are on the armrest, eyes move between three screens.
5. Honest about uncertainty: when a layout or name is inferred, say so.

## Accessibility & Inclusion

Mixed-experience adults, some first-time computer-at-a-machine users; large type and high contrast at arm's length; never rely on colour alone for state; respect reduced motion.
