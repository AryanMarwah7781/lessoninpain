---
module_id: as09261,1711638675997-19-28MAR24
title: Operate AutoTrac
section: AutoTrac Tuning, AutoTrac RowSense, and AutoTrac Vision
page_labels:
- 140-3
- 140-4
pdf_pages:
- 814
- 815
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: procedure
components:
- display
- multi-function lever
- steering
- wheel
conditions:
- road transport
signal_words:
- CAUTION
- NOTE
figures:
- N155449
- N128433
- N128434
generic: false
title_inferred: false
parent_module_id: null
---

# Operate AutoTrac

CAUTION: While AutoTrac is active, the operator is responsible for steering at the end of the path and collision avoidance.
The system automatically steers the machine. To avoid injury, verify that no bystanders are in the vicinity before calibration.
Always turn off (disable) AutoTrac system before entering a roadway. Do not attempt to turn on (activate) AutoTrac system while transporting on a roadway.
1. Press the steer on-off button on the display to toggle between enable/disable AutoTrac. To enable the system, the following conditions must be met:
- AutoTrac control unit has been detected.
- Tracking has been set up.
- Tracking is ON.
- Control unit is in normal operating mode.
N155449—UN—27APR21

![[N155449.png]]
**Figure N155449** — A: AutoTrac Resume Button

2. Press the AutoTrac resume button (A) on the multi-function lever. To activate the system, the following conditions must be met:
- Machine heading within 80° of the desired track if speed is less than 17.7 km/h (11 mph)
- Machine heading within 45° of the desired track if speed is higher than 17.7 km/h (11 mph)
- Off track error within 40% of the track spacing
- Boom unfolded if operating above 24 km/h (15 mph)
- Operator in seat
N128433—UN—09FEB17

![[N128433.png]]
**Figure N128433** — A: AutoTrac Installed Indicator; B: AutoTrac Configured Indicator; C: AutoTrac Enabled Indicator; D: AutoTrac Activated Indicator

3. Check the AutoTrac status indicator. Status indicator shows the stage that AutoTrac is in:
- Stage 1—Installed (A)—AutoTrac control unit and all other hardware necessary for use are installed.
- Stage 2—Configured (B)—Valid AutoTrac License, Tracking Mode has been determined and a valid Track 0 has been established. Correct GPS signal level for AutoTrac License is selected. Vehicle conditions are met.
- Stage 3—Enabled (C)—Auto on-off button has been pressed and “Steer On” is displayed.
- Stage 4—Activated (D)—Resume button on the multi-function lever has been pressed and AutoTrac is steering the machine.
N128434—UN—09FEB17

![[N128434.png]]
**Figure N128434** — A: System Installed Icon; B: System Active Icon; C: Lost GPS Icon; D: Lost Row Sensor Signal Icon

When operating RowSense, an icon appears to indicate that the row sensor is available. Each icon indicates what is happening on the machine at that moment.
The guidance status icon changes from white to colored (green) animated form when row sensor is controlling machine, as follows:
- System Installed (A) (gray background)
- System Active (B), operating with both row sensor and GPS (green background)
- Lost GPS (C), operating with the row sensor data only (yellow background)
- Lost Row Sensor Signal (D), operating with GPS only (orange background)
NOTE: Guidance accuracy is diminished when operating with icon status C or D.
The row sensor guides the machine whenever it can determine a row position. The operator knows that the row sensor is guiding machine by the AutoTrac icon changing to green and showing motion.
Field Operation
The following describes the basic operating process when operating in a field:
1. Align the machine parallel with well-defined crop rows.
2. Perform a calibration check.
- If the calibration is successful, proceed with procedure.
- If the calibration is not successful, verify that rows are well-defined and perform the calibration procedure.
3. Begin spray application.
4. Create an accurate guidance line using AutoTrac. (See Getting Started Using Rowsense in the AutoTrac Vision and Rowsense section.) This line is utilized if the sensor signal is lost.
5. Complete a turn at headlands. DO NOT engage AutoTrac Vision or AutoTrac RowSense until the machine has left the headland.
6. Continue spray operation. Proceed as follows if the following conditions occur:
- When entering new pass: a. Engage AutoTrac RowSense once both front wheels are fully parallel with the crop row and both paddles are engaging crop. b. Engage AutoTrac Vision once the machine and camera are pointing parallel to the crop row after leaving headlands.
- If the row is not detected by sensors: a. GPS guidance resumes control. b. GPS guidance may result in crop damage if the guidance line does not follow rows. c. Sensors resume control when the row is detected again.
- If system performance is not satisfactory:
a. See the Troubleshooting section for solutions to symptoms.
Deactivate AutoTrac
CAUTION: Always turn off (disable) AutoTrac system before entering a roadway. To disable AutoTrac from the display, press the steer on-off button until STEER OFF is displayed.
AutoTrac system can be made INACTIVE by the following methods:
- Press the steer on-off button to select between ON-OFF.
- Turn the steering wheel more than 30°.
- Engage the transport lock.
- Decrease ground speed to less than 0.5 km/h (0.3 mph) for longer than 30 seconds.
- Operator is not seated for more than 7 seconds.
- Track number is changed.

> Source: OMKK105338 p. 140-3, 140-4 · module as09261,1711638675997-19-28MAR24
