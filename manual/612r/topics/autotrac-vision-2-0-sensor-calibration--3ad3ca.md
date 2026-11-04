---
module_id: az06166,1748614901810-19-27APR26
title: AutoTrac Vision 2.0 Sensor Calibration
section: AutoTrac Vision and RowSense
page_labels:
- 25-O-4
- 25-O-5
pdf_pages:
- 278
- 279
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: procedure
components:
- boom
- camera
- display
- steering
- wheel
conditions: []
signal_words:
- NOTE
figures:
- PC28688
- PC28717
- PC15305
- PC654363
- PC654364
- PC654365
- PC639350
- PC654366
- PC669738
- PC659259
- PC654368
generic: false
title_inferred: false
parent_module_id: null
---

# AutoTrac Vision 2.0 Sensor Calibration

AutoTrac Vision 2.0 calibration may be needed in following conditions:
- When vision cameras are replaced.
- When undesired guidance performance is experienced while utilizing RowSense in vision mode.
Perform the following procedure to calibrate RowSense stereo vision:
1. Select Menu.
PC28688—UN—25AUG22

![[PC28688.png]]
**Figure PC28688**

Menu Button
2. Select Guidance.
PC28717—UN—25AUG22

![[PC28717.png]]
**Figure PC28717**

Guidance Application
3. Select Settings icon.
PC15305—UN—19MAR13

![[PC15305.png]]
**Figure PC15305**

Settings Icon
4. Select Status and Settings.
PC654363—UN—25NOV24

![[PC654363.png]]
**Figure PC654363**

Status and Settings
5. Ensure that RowSense is enabled.
6. Select Sensor Settings & Calibration.
PC654364—UN—25NOV24

![[PC654364.png]]
**Figure PC654364**

Sensor Settings & Calibration
7. Select CAL.
PC654365—UN—25NOV24

![[PC654365.png]]
**Figure PC654365**

CAL
8. Select Begin.
PC639350—UN—18JUL24

![[PC639350.png]]
**Figure PC639350**

Begin Calibration
NOTE: Phases 1 and 2 both need to be completed for a successful calibration.
9. Select calibration phase and follow the onscreen instructions to perform calibration procedure.
PC654366—UN—25NOV24

![[PC654366.png]]
**Figure PC654366** — A: Phase 1: Static Calibration; B: Phase 2: Dynamic Calibration

Vision 2.0 Sensor Calibration
Phase 1—Static Calibration
Before performing static calibration, ensure the following:
- Machine is parked in a flat area but not in row crops.
- No obstacles in the field of view of camera (9 m [27 ft]).
- Machine is not moving.
- Boom (if equipped) is out of camera view.
- Ladder (if equipped) should be down.
- Wheels must be fully treaded in.
Vertical Alignment: Using the controls on the display, center the target line to the lowest point of contact between the rim and the tire.
Horizontal Alignment: Using the controls on the display, center the target line to the lowest point of the suspension cylinder.
At the end of calibration, the region of interest is shown inside green borders. Ensure that the region of interest is loading correctly into the display.
PC669738—UN—09APR25

![[PC669738.png]]
**Figure PC669738**

Calibration Completed
Phase 2—Dynamic Calibration
Before performing dynamic calibration, ensure the following:
- Machine is aligned to straight row crops.
- Machine is in a flat terrain.
- Boom (if equipped) is completely unfolded.
- Wheels must be fully treaded in.
PC659259—UN—14JAN25

![[PC659259.png]]
**Figure PC659259**

Row Spacing
Row spacing input is required for dynamic calibration. On sensor calibration page, input row spacing value (50 cm [20 in]—100 cm [40 in]) and follow onscreen instructions to perform calibration.
Drive the machine as instructed on the display to complete the calibration procedure. System can pause if:
- Machine speed is out of range.
- Machine is not on a flat terrain.
- Crop detection is challenging.
The confidence indicator will turn from gray to green once both phases of calibration are successful and sufficient crop is detected.
PC654368—UN—25NOV24

![[PC654368.png]]
**Figure PC654368**

Confidence

> Source: OMKK105338 p. 25-O-4, 25-O-5 · module az06166,1748614901810-19-27APR26
