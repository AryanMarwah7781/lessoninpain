---
module_id: as09261,1711640467945-19-28MAR24
title: Shift Track
section: AutoTrac Tuning, AutoTrac RowSense, and AutoTrac Vision
page_labels:
- 140-8
pdf_pages:
- 819
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: procedure
components:
- steering
conditions:
- wind
signal_words:
- NOTE
figures:
- PC16665
generic: false
title_inferred: false
parent_module_id: null
---

# Shift Track

PC16665—UN—18MAR13

![[PC16665.png]]
**Figure PC16665** — A: Shift Track Center; B: Shift Track Left; C: Shift Track Right

Shift Track adjusts position of machine left, center, or right of the set track. Use Shift Track to compensate for the global positioning system (GPS) drift.
Shift Track adjusts track 0 and all guidance lines associated with the track. Guidance lines are shifted right or left to the pre-specified distance. An operator can also center a guidance line on machine.
To center line on current machine location, select Shift Track Center (A). To move line to left, select Shift Track
Left (B). To move line to right, select Shift Track Right (C).
NOTE: Shift track master defaults to ON.
Shift Track is disabled while adaptive curves recording is active.
The maximum shift increment value allowed with AutoTrac active is 30 cm (12 in). With AutoTrac inactive, operator is allowed to shift up to 914 cm (360 in).
NOTE: Drift is inherent to any satellite-based, differentially corrected GPS system.
When using SF1 differential correction (or when using RTK Quick Survey Mode), the track may drift over time or at power cycles. Shift Track can be used to compensate for GPS drift.
Shift Track is not recommended with Adaptive Curves. Shift is based on the current heading on the track, not the geometry of the entire track. Shift Track can cause some portions of the track to shift closer or further away from the desired shift. Shift Track does not compensate for inherent GPS drift when using Adaptive Curves.
The Shift Track Center button is disabled with AB Curves. Use left and right shift buttons to move and regenerate the AB Curve tracks.
Total shifts are visible when editing a straight track or circle track guidance line only. Clear shifts are eligible for all tracks.

> Source: OMKK105338 p. 140-8 · module as09261,1711640467945-19-28MAR24
