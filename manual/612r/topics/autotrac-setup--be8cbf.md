---
module_id: as09261,1711638024249-19-30APR24
title: AutoTrac Setup
section: AutoTrac Tuning, AutoTrac RowSense, and AutoTrac Vision
page_labels:
- 140-1
- 140-2
- 140-3
pdf_pages:
- 812
- 813
- 814
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: procedure
components:
- steering
- wheel
conditions: []
signal_words:
- IMPORTANT
- NOTE
figures:
- PC16645
- PC16646
- PC16647
- PC16648
- N167383
- N167385
- N167384
- PC17128
- PC17129
generic: false
title_inferred: false
parent_module_id: null
---

# AutoTrac Setup

Operate Guidance Systems Safely
Read and understand Operate Guidance Systems Safely in the Safety section.
AutoTrac System
General Information
AutoTrac system relies on Global Positioning System (GPS) operated by the United States government, which is solely responsible for its accuracy and maintenance. System is subject to changes that could affect accuracy and performance of all GPS equipment.
Operator must maintain responsibility for the machine and must turn at end of each track. This system does not turn at the end of a track unless equipped with iTEC Pro.
AutoTrac basic system is an assistance tool to mechanical markers. Operator must evaluate overall system accuracy to determine specific field operations where assisted steering is used. This evaluation is necessary because accuracy required for various field operations differs depending on farming operation. Because AutoTrac uses StarFire differential correction network along with GPS, slight shifts in position may occur over time.
AutoTrac Accuracy— Overall AutoTrac system accuracy is dependent upon many variables. Equation looks like:
AutoTrac System Accuracy = Signal accuracy + Vehicle Setup + Implement Setup + Field/Soil Conditions.
It is important to remember:
- Receiver has to go through a warm-up period after starting.
- Vehicle is set up properly (for example: ballasted according to the vehicle operator’s manual).
- Understand how field/soil conditions affect system (loose soil requires more steering than firm soil, but firm soil can cause uneven draft loads).
Status Pie:
IMPORTANT: Although AutoTrac system can be activated when correction signal is confirmed, system accuracy may continue to increase after powering up system.
AutoTrac SF1 activation operates on SF1 signal only.
NOTE: Status pie and steer icon are not displayed if SSU or AutoTrac License is not detected.
AutoTrac icon has four stages as shown in AutoTrac
Status Pie
PC16645—UN—26FEB13

![[PC16645.png]]
**Figure PC16645**

Installed
1. Installed
Steering control unit and all other hardware necessary for use are installed.
- Steering control unit is detected.
- AutoTrac License is detected.
PC16646—UN—26FEB13

![[PC16646.png]]
**Figure PC16646**

Configured
2. Configured
Tracking Mode has been determined, and a valid Track 0 has been established. Correct StarFire signal level for AutoTrac License is selected. The following machine conditions must be met:
- Guidance system turned ON.
- Guidance Track 0 defined.
- StarFire signal is present.
- Steering control unit has no active faults.
- Speed is in range.
- TCM message is available and valid.
- Machine in proper operating gear.
PC16647—UN—26FEB13

![[PC16647.png]]
**Figure PC16647**

Enabled
3. Enabled
AutoTrac on-off button has been pressed. All conditions are met for AutoTrac to operate and system is ready to be activated.
- Select STEER on-off button to turn “Steer On”.
PC16648—UN—26FEB13

![[PC16648.png]]
**Figure PC16648**

Activated
4. Activated
Resume switch has been pressed and AutoTrac is steering the machine.
- Press Resume switch to activate AutoTrac.
Last Exit Code: Indicates why AutoTrac is deactivated or does not activate. Exit codes show up in a new window shade at top of page.
Identify Tire Type
N167383—UN—30APR24

![[N167383.png]]
**Figure N167383** — A: Information and Settings Softkey

1. Select the information and settings softkey (A).
N167385—UN—30APR24

![[N167385.png]]
**Figure N167385** — A: Page Down Softkey; B: AutoTrac Steering Optimization Softkey; C: Row Crop (Narrow); D: Float (Wide); E: OK Softkey

N167384—UN—30APR24

![[N167384.png]]
**Figure N167384** — A: Page Down Softkey; B: AutoTrac Steering Optimization Softkey; C: Row Crop (Narrow); D: Float (Wide); E: OK Softkey

2. Use the page down softkey (A) to scroll down.
3. Select the AutoTrac Steering Optimization softkey (B).
4. Select Row Crop (Narrow) (C) or Float (Wide) (D).
5. Select OK softkey (E).
Steering Sensitivity
Steering sensitivity adjusts aggressiveness of the AutoTrac steering system. A high steering sensitivity setting is more aggressive. This setting allows system to handle tough manual steering conditions, such as integral implements with a heavy draft load. A low steering sensitivity setting is less aggressive, and allows system to handle lighter draft loads and higher speeds.
Enter a number from 50 through 200. Default value is 70. Value may change based on steering control unit:
PC17128—UN—18JUN13

![[PC17128.png]]
**Figure PC17128** — A: 10 Second Interval; B: 1 Second Interval; C: Track Error Pattern

PC17129—UN—18JUN13

![[PC17129.png]]
**Figure PC17129** — A: 10 Second Interval; B: 1 Second Interval; C: Track Error Pattern

- Too Low: If steering sensitivity is too low, a slow wandering track error pattern can be observed on display. This track error pattern (C) takes approximately 10 seconds (A) to go from side to side. If excessive track error is occurring, increase steering sensitivity by small increments until desired accuracy is achieved.
- Too High: Setting steering sensitivity to the highest level does not result in maximum tracking accuracy. If steering sensitivity is too high, excessive front wheel motion is observed which reduces accuracy and causes unnecessary front axle component wear. At extreme high levels, machine motion becomes large enough to cause steering sensitivity to be momentarily changed to default level. Wheel motion determines steering aggressiveness. If aggressiveness is too high, then an interval of approximately 1 second (B) occurs from side to side. If excessive wheel motion is observed, lower steering sensitivity by small increments until desired performance is achieved.
NOTE: It is normal to see a momentary track error when encountering a large rut, furrow, or implement load change. Proper steering sensitivity adjustment helps minimize track error.
Use Help Center Onscreen Help for more information about steering sensitivity.

> Source: OMKK105338 p. 140-1, 140-2, 140-3 · module as09261,1711638024249-19-30APR24
