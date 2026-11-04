# Writing brief: 612R lessons (3 Nov 2026)

You are writing lessons for **Lesson Studio**, a trainer that runs beside a John Deere sprayer simulator. The user
asked for seven 612R lessons: six of 15-20 minutes and one long one of 1-2 hours. They must be complex and realistic
(ordering, decisions, recovery, fault finding), not "get in the cab" basics.

## Who takes them

Customers and operators at a demo table (often first time on a CommandARM) and students at a training centre. Plain
words, one action per step, the reason in one line. Not John Deere staff.

## Files to read first

- `lessons/FORMAT.md`: the lesson file format, including the **0.2 additions** at the end (`extra_controls`, section
  `mode` and `checkpoint`, step `est_s`, `source`, `figure`, the `confirm` check, confidence `"manual"`).
- `lessons/headland-hms.json` and `lessons/no-spray-fault.json`: two existing lessons; copy their style and density.
- `virtual-commandarm/controls.json`: the simulator armrest's controls. Each has an `id`, `label`, and (when the app
  sends something) a `vio` signal name. **Only these signals exist** for `sent` checks; `led.vio` names exist for
  `cloud` checks; game fields are listed in FORMAT.md.
- `manual/figure-map.json`: which manual figure shows each control, and the handle buttons by letter.

## The manual (your only source of machine facts)

The 612R operator's manual, OMKK105338 (400R-616R), compiled into local files:

- `manual/612r/index.md`: every topic with its manual page, grouped in 52 sections.
- `manual/612r/topics/<name>.md`: verbatim manual text of each topic, with `**Figure Nxxxx**` references and pages.
- `manual/612r/wiki/procedures|components|troubleshooting|safety|settings/*.md`: compiled step-by-step pages with
  warnings and figure references.
- Figures: any key in `manual/figures.jsonl` may be used as a step `figure` (captions in `manual/captions.jsonl`).

Every instruction, warning, number and name must come from the manual. Cite it in each step's `source`
(`{"pages": ["30-19"], "topic": "<topic file name without .md>"}`). Never invent a procedure, a setting, a
specification or a figure. If the manual does not say something you need, leave it out or mark the step
`"confidence": "draft"` and say why in your report.

## What the simulator can see, and the `confirm` check

The lessons run on the Display and CommandARM Simulator (Connections app). It sees the **CommandARM**: every control in
`controls.json` with a `vio` signal (multi-function lever buttons, armrest keypad, switch panel, lever, steering,
speed dial, foot switch), plus a game file (`boomUnfolded`, `cameraView`, `ladderRaised`, ...). It can **not** see the
display pages, the corner post, the fill station, anything outside the cab, or 612R-only switches.

- Use a sensed check (`sent`, `game`, `control`, `cloud`) whenever the action is on the simulator's CommandARM.
  Use the control **by function**: e.g. HMS is `hms` (`PLT_MHC_HMS`), master spray is `master_spray`, centre boom
  raise is `centre_boom_raise`, the boom fold floor switch is `foot_switch`.
- Use `{"confirm": "<short text for the Done button>"}` for everything else, and declare any 612R control that is not
  in `controls.json` under `extra_controls` (label, where, figure, source).
- Aim for a mix: in cab/field lessons most steps should be sensed; in walk-around, filling and maintenance lessons
  `confirm` is expected.

## Every step

- `say`: one action, plain language, at most about 20 words.
- `why`: one line, from the manual's reasoning or warnings.
- `controls`: ids involved (catalogue or `extra_controls`).
- `done`: the check. Ordering matters? Use `then` / `before`.
- `wrong[]`: realistic mistakes with a check and a plain explanation, wherever a mistake is sensable (wrong order,
  wrong button, skipping a safety step). At least one per lesson section on average.
- `hints[]`: two, escalating (`after_s` 20, then 45), the second naming exactly where the control is.
- `show_me`: armrest commands that do the step (sensed steps only; commands are in FORMAT.md, ids from controls.json).
- `ask`: the question a trainee would ask the chatbot here.
- `est_s`: seconds a first-timer needs. `figure`: best manual figure key. `source`: manual pages and topic.
- `confidence`: `"manual"` when it is the manual's own instruction, `"draft"` when adapted for the simulator.

## Structure and length

- Short lessons: 15-20 minutes in total `est_s` (900-1200 s), usually 14-24 steps, 2-4 sections. End with a short
  `practice` or `assess` section that repeats the key skill without hand-holding.
- The long lesson: 60-120 minutes (3600-7200 s), at least 6 sections, every section `"checkpoint": true`, at least one
  `practice` section and a final `assess` section.
- Top level: `schema` "lesson/0.2", `id` (prefix `612r-`), `title`, `machine` ("612R Sprayer · CommandCenter display ·
  CommandARM"), `build` ("612R operator's manual OMKK105338; runs on the Apr 20 Display and CommandARM Simulator"),
  `manual`, `level`, `minutes`, `objective`, `procedure_source`, `setup` (`armrest` commands using catalogue ids only,
  and `trainer` text), `chatbot` (what the RAG chatbot should know about the whole lesson), `sections`.

## Done means

Run `python -I lessons/check_lesson.py --validate lessons/<id>.json` and fix until it prints OK. Do not run the
simulator, the API or the armrest, and do not edit any file except your own lesson files.

In your final report give, per lesson: id, title, sections, steps, minutes, how many steps are sensed vs confirmed,
the manual topics you used, and every place you were unsure of a fact or adapted the manual.
