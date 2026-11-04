---
module_id: ch177nn,1738309063983-19-03FEB25
title: AutoTrac Turn Automation
section: AutoTrac Tuning, AutoTrac RowSense, and AutoTrac Vision
page_labels:
- 140-8
- 140-9
pdf_pages:
- 819
- 820
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: procedure
components:
- display
- steering
conditions:
- temperature
signal_words:
- NOTE
figures:
- PC28762
- PC613045
- PC661533
generic: false
title_inferred: false
parent_module_id: null
---

# AutoTrac Turn Automation

PC28762—UN—25AUG22

![[PC28762.png]]
**Figure PC28762**

AutoTrac Turn Automation
The AutoTrac Turn Automation application automates end turns in equipped machines. This automation allows the operator to focus on other tasks instead of coordinating end turns.
It is recommended to use the default settings when initially setting up AutoTrac Turn Automation. The default settings provide a starting point that performs well with many machine and implement configurations. With some configurations, it may be necessary to adjust the AutoTrac Turn Automation advanced settings to fine-tune performance. For example, if a tractor is made wider by adding triple tires or the turn radius is affected by adjusting steering stops, then the Maximum Turn
Radius and Maximum Turn Angle values may need adjustment.
Navigate to AutoTrac Turn Automation
1. Select Menu.
2. Select Applications tab.
3. Select AutoTrac Turn Automation application.
Mapping
AutoTrac Turn Automation map module displays information about upcoming turns, such as distance to the turn and direction of the turn. Use the Onscreen Help for more information about the Mapping application.
AutoTrac Turn Automation Compatibility
AutoTrac Turn Automation is compatible with the following displays and receivers:
NOTE: Update software to the latest version.
- 4600 CommandCenter Display
- 4640 Universal Display
- G5 CommandCenter Display
- G5 Universal Display
- StarFire 3000 Receiver
- StarFire 6000 Receiver
- StarFire 7000 Receiver
- StarFire 7500 Receiver
AutoTrac Turn Automation is not compatible with the following displays:
- 4200 CommandCenter
- 4600 CommandCenter version 1 processor
- 4240 Universal Display
- Original GreenStar Display
- GreenStar 2 1800 Display
- GreenStar 2 2600 Display
- GreenStar 3 2630 Display when used with a 4600 CommandCenter or a 4640 Universal Display
Skip Turn Recommendation
PC613045—UN—20FEB24

![[PC613045.png]]
**Figure PC613045** — A: No Skip; B: Skip Turn

Skip Turn Recommendation
AutoTrac Turn Automation suggests to skip a turn as needed when track spacing is less than machine minimum turn diameter. This feature is implemented only when U-Type turns are selected.
Select OK on the Skip Turn Recommendation message to accept the skip turn. Close the message or select Cancel to dismiss the recommendation and continue without performing a skip turn.
NOTE: The selections are retained during cold and warm boot cycles.
NOTE: Recommendation shall re-appear when changing fields and track spacing is less than turn diameter.
Intelligent Turn Sizing
When the track spacing is equal to or larger than machine's minimum turn diameter, the application will plan an efficient U-turn.
When the track spacing is less than machine's minimum turn diameter, the turn shape will be a light bulb shape which takes more space to complete.
NOTE: If Skip turn is accepted, the application disregards the intelligent turn sizing feature.
Impassable Boundaries
PC661533—UN—30JAN25

![[PC661533.png]]
**Figure PC661533**

Impassable Boundaries
Impassable boundaries warning can be disabled by selecting the checkbox in AutoTrac Turn Automation Advanced Settings. The checkbox sets to default state (warning enabled) in the following conditions:
- Change of field
- Operator is out of seat
- Key cycle

> Source: OMKK105338 p. 140-8, 140-9 · module ch177nn,1738309063983-19-03FEB25
