# Lesson file format (draft 0.1)

One JSON file per lesson. You write the first five by hand; later Lesson Studio writes the same files.
Control ids and signal names come from `virtual-commandarm/controls.json`.

## Top level

| Field | Meaning |
|---|---|
| `schema` | `"lesson/0.1"` |
| `id`, `title`, `machine`, `build` | What the lesson is and which simulator build it was written for |
| `level`, `minutes`, `objective` | Shown to the trainee before they start |
| `procedure_source` | Where the steps came from. Anything not from the app's own procedures is marked `"draft: confirm with an operator"` |
| `setup` | `armrest`: commands that put the simulator in the starting state (virtual armrest only). `trainer`: the same in words, for a real rig |
| `chatbot` | What the RAG chatbot is told about the whole lesson |
| `sections[]` | Groups of steps, each with a `title` and `steps[]` |

## A step

| Field | Meaning |
|---|---|
| `id` | Short, unique in the lesson |
| `say` | The instruction the trainee reads |
| `why` | One line on why it matters (shown under the instruction) |
| `controls` | Control ids involved; the panel highlights them and "show me" uses them |
| `done` | The check that completes the step (see Checks) |
| `wrong[]` | `{ "if": check, "say": "..." }`: a mistake to catch while this step is active |
| `hints[]` | `{ "after_s": 20, "say": "...", "highlight": [ids] }`: shown when the trainee stalls |
| `show_me` | Armrest commands that perform the step (for "show me", and for the lesson checker) |
| `wrong_demo` | Armrest commands that make the mistake in `wrong` (the checker uses them to prove the mistake is caught) |
| `ask` | What to tell the chatbot if the trainee opens it on this step |
| `confidence` | `"app"` (from the app's own procedure) or `"draft"` (needs an operator to confirm) |
| `display` | optional: screen target ids from `simapi/screens/apr20-r4045.json` to ring on the display or corner post. Without it, targets are matched through `controls` |

## Checks

A check is a leaf or a combination. Leaves look at one evidence source:

| Leaf | Source | True when |
|---|---|---|
| `{"sent": SIGNAL, ...}` | the app sent this to the cloud (log line `SendVIOData`) | a matching value is sent after the step starts |
| `{"cloud": SIGNAL, ...}` | the cloud sent this back (log line `received from EC2`) | a matching value arrives after the step starts. Online only |
| `{"game": FIELD, ...}` | `VehicleInfo.xml` | the field currently has a matching value |
| `{"control": ID, ...}` | the virtual armrest's own state | the control currently has a matching value. Virtual armrest only |

Value tests on a leaf: `"eq"`, `"gte"`, `"lte"`, `"gt"`, `"lt"`, `"outside": [lo, hi]`, `"between": [lo, hi]`.
Add `"online": true` to a `game` leaf whose field only changes when the cloud is connected (`nozzleOnOffStatus`, `wheelSpeed`, `boomHeight`, `hydroHandlePosition`).

Combinations: `{"all": [...]}` every part true; `{"any": [...]}` at least one; `{"then": [...]}` the parts become true in this order.

Offline (no sign-in) a leaf that needs the cloud can't be judged. Inside `any`, such alternatives are skipped. A step whose `done` can only be judged online is marked "online only" by the checker.

## Armrest commands

The same text the virtual armrest's scripted port takes: `press <id> [ms]`, `down <id>`, `up <id>`,
`switch <id> 0|1`, `set <id> <value>`, plus `wait <seconds>` for the checker.

## Additions in 0.2 (3 Nov 2026: 612R lessons, long lessons)

`schema` is `"lesson/0.2"`. Everything above still holds.

| Where | Field | Meaning |
|---|---|---|
| top level | `extra_controls` | Controls this lesson uses that the simulator's armrest catalogue does not have (612R console switches, display keys, things outside the cab): `{ "id": { "label", "where", "figure", "source" } }`. Steps may list these ids in `controls`; their checks use `confirm` |
| top level | `manual` | The manual the lesson follows, e.g. `"OMKK105338 (400R-616R operator's manual)"` |
| section | `mode` | `"learn"` (default: hints, Show me), `"practice"` (hints later, fewer of them), `"assess"` (no hints, no Show me, scored) |
| section | `checkpoint` | `true`: a long lesson can be resumed from this section (`POST /api/lesson/start {"id", "section": n}`) |
| step | `est_s` | Estimated seconds the step takes a first-timer; the validator adds them up to the lesson length |
| step | `source` | Where in the manual the step comes from: `{ "pages": ["30-19"], "topic": "<vault topic file name without .md>" }` |
| step | `figure` | The manual figure key that shows this step best (e.g. `"N153424"`); shown beside the step |
| step | `confidence` | adds `"manual"`: the step is the manual's own instruction (cite it in `source`). `"draft"` stays for anything adapted |

New check leaf, for anything the simulator cannot sense (a walk-around item, the fill station, a page on the
display that is not mapped yet):

| Leaf | Source | True when |
|---|---|---|
| `{"confirm": "Pressure strainer clean"}` | the trainee presses the Done button with that text (`POST /api/lesson/confirm {"item": text}`) | the trainee confirms after the step starts |

A step may mix sensed leaves and `confirm` leaves (`{"all": [{"sent": ...}, {"confirm": ...}]}`). Prefer a sensed
check whenever the simulator can see the action; `confirm` is for what it cannot.

Validate a file without the simulator: `python -I lessons/check_lesson.py --validate lessons/<id>.json`.
