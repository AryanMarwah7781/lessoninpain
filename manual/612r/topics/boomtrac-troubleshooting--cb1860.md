---
module_id: bn55050,1776442150178-19-20APR26
title: BoomTrac Troubleshooting
section: BoomTrac Performance and Optimization
page_labels:
- 155-8
- 155-9
- 155-10
pdf_pages:
- 846
- 847
- 848
models:
- all
options:
- BoomTrac
engine_tier: null
topic_type: troubleshooting
components:
- boom
- boom height
- boom wing
conditions:
- temperature
signal_words:
- NOTE
figures: []
generic: false
title_inferred: false
parent_module_id: null
---

# BoomTrac Troubleshooting

Symptom | Problem | Solution
Boom bounces or jumps when sprayer is not in motion.
Minor noise or “echo” in the height sensor readings when the machine is stationary.
No action required. This behavior can be considered normal when the sprayer is not moving. The BoomTrac system relies on continuous changes in terrain to stabilize boom height, and stationary testing may lead to slight boom movement from small variations in sensor feedback. This is not indicative of BoomTrac performance during actual field operation.
Always evaluate BoomTrac performance while the machine is
in motion, where sensors receive consistent terrain information and the system is able to respond as designed.
Ground surface directly beneath the sensor may create inconsistent returns (e.g., uneven soil, crop residue, reflective surfaces).
Always evaluate BoomTrac performance while the machine is
in motion, where sensors receive consistent terrain information and the system is able to respond as designed.
General instability or inaccurate operation.
Loose sensors, linkages, or brackets. Verify that all sensors, brackets, and linkages (BHS, IMU, roll, tilts) are tight and secure.
One wing raising or running high while the other operates normally.
IMU issue. | Confirm that all BHS readings are
correct.
Unplug IMU and test machine; if issue resolves, inspect IMU mounting or replace.
NOTE: A DTC will trigger but Boomtrac should still be functional.
Check for DTCs relating to the IMU to confirm harnessing and communication.
Erratic or jumpy height control around the correct height.
Roll lock issue. | Check for roll lock engagement. If
machine “pushes” in the cab when
hunting, roll lock may be active.
Machines with a carbon fiber truss
boom: Confirm roll lock cylinders retract when unfolded. If extended, roll lock is stuck.
Symptom | Problem | Solution
Sway link system issue. | When fully unfolded, hydraulic lines
should not be pressurized. Moving
hydraulic hoses with your hand can be
a quick and easy inidcator if pressure
is present.
Raise the center frame; tilt one side up and the opposite side down to rock the system clockwise/counter-clockwise. Repeat several times. Roll lock cylinders should retract at least 25.4 mm (1 in) after rocking. If still tight, roll lock is stuck.
Machines with a Serial Number of
270001 and above: Push down on one end of the boom. If it freely rolls, system is functioning. If difficult to move 0.3—0.6 m (1—2 ft), damper cylinders may be locked.
Poor or inconsistent control (slow response or erratic movement).
Incorrect or incomplete tilt valve calibration.
Perform tilt valve calibration with warm/hot oil.
Confirm tilt sensors read correctly across full tilt range.
Quickly “bump” tilt functions and ensure that sensors register small movement changes (maintenance mode is fine for this).
Booms are “clocked” (one wing consistently high, the other consistently low).
Roll level calibration or IMU influence. Perform roll level calibration.
Verify that the machine is level; reference Starfire roll angle if needed.
Incorrect IMU influence. | Confirm that the IMU is firmly
mounted.
Unplug the IMU. If the problem disappears, the IMU is influencing control incorrectly.
Center frame moves up/down excessively (more than normal).
Incorrect target type selection. | Change BoomTrac target type
(Ground, Ground+, Canopy) to match
crop conditions.
Accumulator precharge issue. | Check accumulator precharge.
Booms operating at visibly incorrect heights or behaving unpredictably.
Boom Height Sensor (BHS) misreadings.
With booms level at 762 mm (30 in), verify that all BHS readings look correct.
Symptom | Problem | Solution
Tilt one side up to 1.8—2.1 m (6—7 ft) and confirm sensor readings follow expected values. Repeat for opposite side.
Raise/lower booms, stopping every 152—254 mm (6—10 in), and confirm BHS values change smoothly and logically.
Configuration issues. | Inspect for bent brackets, debris on
sensors, incorrect sensor location
assignments, or incorrect target type
selection.

> Source: OMKK105338 p. 155-8, 155-9, 155-10 · module bn55050,1776442150178-19-20APR26
