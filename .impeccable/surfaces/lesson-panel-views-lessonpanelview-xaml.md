---
version: 1
slug: "lesson-panel-views-lessonpanelview-xaml"
primary_target: "lesson-panel/Views/LessonPanelView.xaml"
related_targets: ["lesson-panel/Controls/HandleView.xaml","lesson-panel/Overlay/DisplayOverlay.xaml"]
---

## Scope

The lesson monitor of Lesson Studio: a full-screen WPF view (`LessonPanelView`) on the trainee's second monitor, plus a click-through ring overlay on the Gen 4 display's own monitor. Mode: Operate. The Gen 4 display and corner post live on another monitor; the R4045 3D model gets a slot later.

## Audience and task

Customers, operators and students, often first time on a CommandARM, hands on the armrest, reading at arm's length. Job: do each lesson step on the real controls, find the right button without hunting, recover from mistakes. The panel judges steps from what the simulator reports (simapi), never from self-report.

## Chosen direction

"Manual procedure page", picked by the user on 3 Nov 2026 from three dealt structures. Memorable moment: the manual's own photo beside every step, and the current step's buttons ringed on the manual's lettered handle drawing, turning green the instant the machine reports the press.

## Unresolved

- Chatbot (RAG) not connected yet; no Ask button until it is.
- R4045 3D model slot reserved, not shown.
- Handle drawing and photos come from the 612R manual; marked when a position is inferred.

## Direction contract

THESIS: The lesson reads like the operator's manual procedure, live: every step numbered with the manual's photo beside it and the current one opened up, so the trainee never translates words into a location. It refuses the category default of a one-step wizard with a generic progress bar.

OWN-WORLD: The Connections app's world: white title band with the green and yellow edge stripe and grey rule; grey ground; white cards, 6px radius, 1px line; Calibri on a 15/17/21/26/34/48 scale. Green carries structure and done, yellow carries the current step, the main action and every ring, red appears only for mistakes. Imagery is the manual's photos and its lettered handle drawing, nothing drawn to imitate them.

STORY: The trainee sees the whole procedure, finds their step by its yellow number, reads one action, looks at the photo and the ringed button, presses it; the panel confirms from the machine and moves on. A mistake is explained in place, in plain words, and stays visible until the step is done.

FIRST VIEWPORT: 1920x1080. Title band 64px: product name, lesson title, live link chips and step timer on the right. Left 58%: lesson title, machine and length, then sections with numbered steps; finished steps collapsed with a green check and photo thumbnail; the current step expanded with a yellow number disc, the action at 34px bold, why, mistake callout, hint when due, a row of numbered manual photo cards, Show me (yellow), Hint and Skip, and a "Watching for" line saying what the machine must report. Right 42%: one "On the armrest" card at full height with the lettered handle drawing and numbered rings (or the module's manual photo for switch-panel, keypad, lever, wheel and foot-switch steps, with their live state), and at its foot what to touch or watch on the display monitor.

FORM: dealt structure 2 on the decision page, "Manual procedure page" (position 6 on my ordered list). seed:d53d6635647fe137

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
