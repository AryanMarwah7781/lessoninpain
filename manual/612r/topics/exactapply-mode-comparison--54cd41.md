---
module_id: ouo6092,1778690708032-19-13MAY26
title: ExactApply Mode Comparison
section: ExactApply Nozzle Control System (If Equipped)
page_labels:
- 125-4
pdf_pages:
- 698
models:
- all
options:
- ExactApply
engine_tier: null
topic_type: description
components:
- boom
- commandarm
- display
- nozzle
- spray tip
conditions: []
signal_words: []
figures: []
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply Mode Comparison

The following table aids in easy comparison of the ExactApply operation modes.
ExactApply Mode Comparison
Nozzles 4, 5, or 6 in the Front Position
Combined A + B —Pulsing OFF
Combined A + B —Automatic Pulsing
A Only or B Only —Automatic Pulsing
Nozzles 1, 2, or 3 in the Front Position
A + B—Automatic Pulsing
Automatic— Pulsing OFF
Automatic— Pulsing ON
Speed Range | Base | Better | Best | Best | Good | Besta
Curve Compensation
Not applicable | Good | Best | Best | Goodb | Best
Boost | Not applicable | Good | Best | Best | Not applicable | Best
Pressure Selection Not applicable | Target | Target | Target | Target Range | Target
Coverage | Best | Best | Good | Best | Best | Best
High Application Rates
Best | Better | Good | Best | Best | Best
Manual Nozzle Selection using the Display or CommandARM
No | No | Yes | Yes | Yesc | No (see comment
for Automatic-
Pulsing OFF)
Multirate Perfomance
Not applicable | Good | Better | Better | Marginald | Best
S&S Variable Rate Supported
Not applicable | Good | Good | Better | Not applicable | Best
Notes | a, i | b, i | c, d, e, i | f, g | h, i
aThe range is better than A+B with pulsing. bNon-pulsed curve comp is supported in auto mode. cOnly from the display as part of setup. The armrest buttons do not affect active/available tip dThere is no averaging between adjacent tips (e.g. -03 and -05 on adjacent tips looks like -04 on the ground). Multirate is limited to 3 rates across the boom. Each meter would be as close as it could be for one of the three tip options available.
Notes:
- a—One nozzle supplied by two solenoids with alternating pulses
- b—One nozzle supplied by one solenoid
- c—Supplies two nozzles with one solenoid each with alternating pulses.
- d—Different spray tip sizes can be used on both turret positions. Spray tips must be 02 or larger.
- e—Dual fan pattern possible
- f—Uses a small and a large spray tip. The large spray tip cannot be more than double the size of the small spray tip.
- g—Sprays without pulsing, automatically switching between the front, rear, or both nozzles within an operator set pressure range.
- h—Sprays with pulsing, automatically switching between front, rear, or both nozzles to maintain target pressure. Switching is done at the individual nozzle level, not for the entire boom.
- i—Requires automatic pulsing to support per-nozzle flow adjustments to the requested target rate for MultiRate or S&S Variable Rate.

> Source: OMKK105338 p. 125-4 · module ouo6092,1778690708032-19-13MAY26
