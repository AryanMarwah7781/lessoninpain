# AGENTS.md — rules for compiling the wiki (Milestone 4)

This vault holds the John Deere OMKK105338 operator's manual as extracted (`topics/`), plus a
compiled layer (`wiki/`) that makes retrieval and reasoning easier. You are compiling `wiki/`.

The wiki never replaces the topics. A wiki page is a map into the manual: it gathers what is
scattered, states what the manual says with a link to where it says it, and is explicit about what
the manual does **not** say.

---

## 1. Hard rules

1. **`topics/`, `specs/` and `attachments/` are read-only.** Write only the files assigned to you
   in `wiki/_plan.md`. Never edit another page, `index.md`, a folder index, or `wiki/_log.md`.
2. **Every fact links to its source topic note**: `[[note-stem|Topic Title]]` at the end of the
   sentence or list item that carries it. No link → the sentence doesn't belong on the page.
3. **Numbers are copied exactly as printed**, with both units as they appear
   ("16 km/h (10 mph)", "531 N·m (392 lb·ft)", "207—414 kPa (2—4 bar) (30—60 psi)"), each with its
   source link. Never convert, round, reformat or combine units. If you need a value that isn't in
   a source you link, leave it out and say what determines it.
4. **Signal-word text is copied verbatim** (DANGER / WARNING / CAUTION / IMPORTANT / NOTE), in a
   `> [!warning]` callout, with its source link. Never paraphrase or shorten it. If a procedure you
   describe has a warning in any source topic, the page carries it, above the steps.
5. **Conflicts are reported, never resolved.** If two sources disagree, write both, link both, and
   add a `> [!conflict]` callout naming the disagreement. Note when one side is a generic Deere-wide
   module (`generic: true` in the note's frontmatter), because those can contradict machine-specific
   text. Do not pick a winner.
6. **Anything not directly stated in a source is an inference**: put it in a `> [!inference]`
   callout with your reasoning. Prefer not inferring at all for anything safety-related.
7. **Applicability is explicit.** State the models, options and engine tiers a page applies to,
   taken from the source notes' frontmatter (`models`, `options`, `engine_tier`). If sources differ
   in applicability, say so per step rather than averaging them.
8. **The product label and local law govern chemical application.** Any page about spraying
   chemicals says so.
9. **No outside knowledge.** Everything comes from this vault. You are not allowed to fill a gap
   from general knowledge, ever, and especially not a value, an interval or a limit.
10. **Write for an operator standing at the machine**: plain sentences, no marketing, no "simply".

---

## 2. Frontmatter (every wiki page)

```yaml
---
type: procedure | component | settings | safety | troubleshooting
title: "Fill the solution tank from a nurse tank"
models: [all]              # or [600R, 612R, 616R]
options: []                # [ExactApply], [See & Spray], …
engine_tier: null
components: [solution tank, fill valve]
requires: [park-machine-safely, relieve-spray-pressure]   # procedure pages: prerequisite pages
sources: ["ouo6092,1763565405881-19-27APR26", …]          # module IDs of every topic used
reviewed: false            # only a human sets this to true
compiled: 2026-09-23
---
```

`reviewed: false` pages are indexed with a lower prior, so never set `reviewed: true` yourself.

---

## 3. Page types

- **components/** — what it is, where it is (embed the figure from the source topic), related
  procedures, settings, warnings and troubleshooting entries. Link every related page.
- **procedures/** — a task from start to finish, composed from several topics. Prerequisites first
  (engine off, pressure relieved, parked safely, PPE), then numbered steps, each with its source
  link and the figures from the source topic. Warnings above the steps.
- **settings/** — one condition per page (wind and drift, speed changes, rate changes, boom height,
  pulsing modes, droplet size). Structure: the condition · the manual's hard limits · the levers the
  operator controls, with the exact display page and setting names · what the manual says each lever
  does · **what the manual does not specify** · what overrides it (the product label, the tip chart,
  the dealer). These pages answer questions like "what setting for 10 mph wind", so being explicit
  about the gaps matters more than being comprehensive.
- **safety/** — warnings indexed by component and by task, verbatim, each linked.
- **troubleshooting/** — symptom → causes ordered cheapest-to-check-first → check → fix, each node
  linked. Only causes the manual supports; anything else is an `> [!inference]`.

Specs stay in `specs/`. Link to them; never copy a number without its link.

---

## 4. Working method

1. Read `wiki/_plan.md` and take only your assigned pages.
2. For each page, first collect the source topics: search the vault, read the whole note (not an
   excerpt), and list the module IDs you will cite.
3. Write the page. Every sentence that states a fact ends with its link.
4. Re-read your page against the sources and check: numbers identical, warnings verbatim,
   applicability stated, no unlinked claim, conflicts surfaced.
5. Return a summary: pages written, module IDs read, conflicts found, gaps where the manual is
   silent, and anything you could not source.

The main session runs `uv run python -m sprayer_rag.wiki.lint` (every link resolves, every number
appears verbatim in a linked source, `requires` targets exist, no orphan pages, conflict callouts
have two sources), then regenerates the indexes and appends to `wiki/_log.md`.

---

## 5. House style learned in wave 1 (components)

- **Links:** a bare stem (`[[nozzle]]`) or a path (`[[components/nozzle]]`) both resolve. Topic notes
  by stem (`[[wet-system-valves--2f14aa|Wet System Valves]]`). Spec tables may be linked from
  `specs/`, but prefer the spec *topic note* — it carries the same verbatim numbers and a module ID.
- **Short warnings:** put the source link on the same callout line, after the verbatim text, or in
  the callout title (`> [!warning] IMPORTANT — [[note|Title]]`). The linter strips `> ` prefixes and
  stops the quoted text at the first `[[`.
- **Printed oddities are copied as printed:** a stray space in a wrapped range (`457— 559 mm`), a
  misprinted unit (170-3 "8000 kPa (80 bar) (1160 bar)"). Never tidy them.
- **Numbers in topic titles** ("…—250 Hours (6.8 L Engine)") count as printed text for the linter.
- **Always run the linter yourself** on your pages before reporting: `uv run python -m
  sprayer_rag.wiki.lint --pages wiki/<type>/<page>.md`. A path that matches no page is reported as an
  error, never as a clean result.
- **Model applicability:** the 408R is the only 6.8 L machine; every other model is 9.0 L. Several
  values split by model group — state which group each value applies to.

## 6. Example

```markdown
Rotate the strainer/flowmeter shutoff valve handle parallel to the solution hose to open it
[[wet-system-valves--2f14aa|Wet System Valves]].

> [!warning] CAUTION
> CAUTION: Escaping fluid under pressure can penetrate the skin causing serious injury. [[relieve-pressure--ab12cd|Relieve Pressure]]

> [!conflict] Maximum solution pressure
> The generic chemical-safety module says not to operate above 345kPa (3.5 bar) (50 psi)
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]],
> while most flat fan tips are designed for 207—414 kPa (2—4 bar) (30—60 psi)
> [[flat-fan-spray-tip--xxxxxx|Flat Fan Spray Tip]]. Confirm the limit for your machine with your dealer.
```
