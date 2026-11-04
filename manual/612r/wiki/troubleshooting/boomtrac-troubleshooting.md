---
type: troubleshooting
title: "BoomTrac"
models: [all]
options: [BoomTrac]
engine_tier: null
components: [BoomTrac, boom height sensor, IMU, roll lock, sway link, tilt valve, center frame, accumulator]
sources:
  - "bn55050,1776442150178-19-20APR26"
  - "ouo6092,1777984543287-19-05MAY26"
  - "bn55050,1778257689748-19-08MAY26"
  - "bn55050,1778257811148-19-08MAY26"
  - "bn55050,1778257918052-19-08MAY26"
  - "bn55050,1778258021856-19-08MAY26"
  - "bn55050,1778258047740-19-08MAY26"
  - "bn55050,1778258131934-19-08MAY26"
  - "bn55050,1763572511240-19-19NOV25"
  - "bn55050,1778257849578-19-08MAY26"
  - "bn55050,1778257958941-19-08MAY26"
  - "bn55050,1778258186350-19-08MAY26"
  - "bn55050,1778257230680-19-08MAY26"
  - "bn55050,1778257251717-19-08MAY26"
  - "ouo6092,1745442560362-19-27APR26"
  - "bn55050,1778258117064-19-08MAY26"
  - "bn55050,1778257903543-19-08MAY26"
  - "bn55050,1778257834998-19-08MAY26"
  - "bn55050,1778257943196-19-08MAY26"
  - "bn55050,1778257749093-19-08MAY26"
  - "ouo6092,1776448146768-19-28APR26"
  - "ouo6092,1777984448733-19-05MAY26"
  - "DX,WW,ACCLA-19-15APR03"
reviewed: true
compiled: 2026-09-23
---
# BoomTrac — troubleshooting

**Option: BoomTrac (if equipped).** Table from BoomTrac Performance and Optimization (p. 155-8)
[[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10), reproduced in its printed order; the manual gives no cost or check order, so none is implied.
I checked the row layout of p. 155-9 against the rendered page (the sway-link row carries three
remedies). Spellings "inidcator" and "Boomtrac" are as printed. Components: [[boom-height]],
[[boom]]. Settings: [[boom-height-settings]].

Accumulators: relieve pressure from the hydraulic system before removing accumulator; never attempt
to relieve hydraulic system or accumulator pressure by loosening a fitting [[service-accumulator-systems-safely--6bd0ed|Service Accumulator Systems Safely]] (generic
Deere-wide module) — accumulator precharge work is a dealer job.

## Warnings that apply to these fixes

> [!warning] CAUTION
> CAUTION: Avoid damage or contamination of your surroundings. Increasing boom height excessively above the target increases the risk of spray drift. [[height-mode--b6109a|Height Mode]] (p. 25-A-6)

> [!warning] CAUTION (also printed in option sections: See & Spray)
> CAUTION: Spray booms move quickly. Keep everyone out of the folding and unfolding area of the spray booms. Failure to stay out of the area can result in injury or death. [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] (p. 25-B-35)
> Also printed in: [[center-frame-position-calibration-procedure--af16c1|Center Frame Position Calibration Procedure]] (p. 25-B-39) · [[boom-level-position-calibration-procedure--328056|Boom Level Position Calibration Procedure]] (p. 25-B-42, 25-B-43) · [[boom-calibration-see-and-spray-camera-calibration-procedure--0a9775|Boom Calibration — See & Spray Camera Calibration — Procedure]] (p. 25-B-46) · [[tilt-sensor-calibration-procedure--e44603|Tilt Sensor Calibration Procedure]] (p. 25-B-47, 25-B-48) · [[tilt-valve-calibration-procedure--17c550|Tilt Valve Calibration Procedure]] (p. 25-B-49, 25-B-50) · [[boom-unfold-fold-27-4-30-5-36-6-and-40-2-m-90-100-120-and-13--31675a|Boom Unfold/Fold—27.4, 30.5, 36.6, and 40.2 m (90, 100, 120, and 132 ft) Booms]] (p. 80-1, 80-2, 80-3, 80-4, 80-5)

> [!warning] IMPORTANT (also printed in option sections: See & Spray)
> IMPORTANT: Booms can contact and may damage the exhaust stack and/or walkway handrail when using manual mode to fold and unfold booms. Do not allow booms to go higher than the top of the cradle support when operating boom in manual mode. [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] (p. 25-B-35)
> Also printed in: [[center-frame-position-calibration-procedure--af16c1|Center Frame Position Calibration Procedure]] (p. 25-B-39) · [[boom-level-position-calibration-procedure--328056|Boom Level Position Calibration Procedure]] (p. 25-B-42, 25-B-43) · [[boom-calibration-see-and-spray-camera-calibration-procedure--0a9775|Boom Calibration — See & Spray Camera Calibration — Procedure]] (p. 25-B-46) · [[tilt-valve-calibration-procedure--17c550|Tilt Valve Calibration Procedure]] (p. 25-B-49, 25-B-50)

> [!warning] IMPORTANT
> IMPORTANT: This procedure requires unfolding the inner boom and will automatically control tilt valves. Ensure adequate space is available. [[tilt-valve-calibration-procedure--17c550|Tilt Valve Calibration Procedure]] (p. 25-B-49, 25-B-50)

> [!warning] IMPORTANT (also printed in option sections: See & Spray)
> IMPORTANT: This procedure requires fully unfolding the boom. Ensure that adequate space is available. [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] (p. 25-B-35)
> Also printed in: [[center-frame-position-calibration-procedure--af16c1|Center Frame Position Calibration Procedure]] (p. 25-B-39) · [[boom-level-position-calibration-procedure--328056|Boom Level Position Calibration Procedure]] (p. 25-B-42, 25-B-43) · [[boom-calibration-see-and-spray-camera-calibration-procedure--0a9775|Boom Calibration — See & Spray Camera Calibration — Procedure]] (p. 25-B-46)

> [!warning] IMPORTANT
> IMPORTANT: This procedure requires unfolding the inner boom and will automatically roll damper valves. Ensure that adequate space is available. [[boom-calibration-center-frame-valve-calibration--680c7a|Boom Calibration — Center Frame Valve Calibration]] (p. 25-B-40, 25-B-41)
> Also printed in: [[roll-damper-valve-calibration--fe07db|Roll Damper Valve Calibration]] (p. 25-B-44) · [[yaw-valve-calibration-procedure--dbd912|Yaw Valve Calibration Procedure]] (p. 25-B-51, 25-B-52)

> [!warning] CAUTION
> CAUTION: Folding spray booms while in maintenance mode is not the same as folding in normal operation. Maintain awareness of surroundings and keep bystanders out of folding and unfolding area. [[boom-maintenance-mode--f3caf2|Boom Maintenance Mode]] (p. 25-B-10, 25-B-11)
> Also printed in: [[boom-maintenance-mode-procedure--ec37ef|Boom Maintenance Mode Procedure]] (p. 25-B-11, 25-B-12)

> [!warning] IMPORTANT
> IMPORTANT: Booms can contact and may damage the exhaust stack and/or walkway handrail when using maintenance mode to fold and unfold booms. Do not allow booms to go higher than the top of the cradle support when operating boom in maintenance mode. [[boom-maintenance-mode--f3caf2|Boom Maintenance Mode]] (p. 25-B-10, 25-B-11)
> Also printed in: [[boom-maintenance-mode-procedure--ec37ef|Boom Maintenance Mode Procedure]] (p. 25-B-11, 25-B-12)

> [!warning] IMPORTANT
> IMPORTANT: This procedure enables fully folding/ unfolding the boom and raising tilts to highest positions. Ensure that adequate space is available. [[boom-maintenance-mode--f3caf2|Boom Maintenance Mode]] (p. 25-B-10, 25-B-11)
> Also printed in: [[boom-maintenance-mode-procedure--ec37ef|Boom Maintenance Mode Procedure]] (p. 25-B-11, 25-B-12)

> [!warning] IMPORTANT
> IMPORTANT: There are more accumulator decals with different factory precharge pressures in different locations that are not illustrated in this manual. Follow the same caution message on those decals, but consider the precharge pressure indicated on each decal. For more information, contact a John Deere Dealer or other service provider. [[accumulator-decals--25a6f0|Accumulator Decals]] (p. 10-7)

## Symptoms

### Boom bounces or jumps when sprayer is not in motion.

1. **Minor noise or “echo” in the height sensor readings when the machine is stationary.** — No action required. This behavior can be considered normal when the sprayer is not moving. The BoomTrac system relies on continuous changes in terrain to stabilize boom height, and stationary testing may lead to slight boom movement from small variations in sensor feedback. This is not indicative of BoomTrac performance during actual field operation. Always evaluate BoomTrac performance while the machine is in motion, where sensors receive consistent terrain information and the system is able to respond as designed. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)
2. **Ground surface directly beneath the sensor may create inconsistent returns (e.g., uneven soil, crop residue, reflective surfaces).** — Always evaluate BoomTrac performance while the machine is in motion, where sensors receive consistent terrain information and the system is able to respond as designed. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)
### General instability or inaccurate operation.

1. **Loose sensors, linkages, or brackets.** — Verify that all sensors, brackets, and linkages (BHS, IMU, roll, tilts) are tight and secure. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)

> [!note] Calibrations that name this symptom as their own trigger
> Boom Level Position: perform when BoomTrac is not working properly [[boom-calibration-boom-level-position--45e59a|Boom Calibration — Boom Level Position]]. Tilt Valves, Roll Damper Valve and Center Frame Valve: perform when BoomTrac is not performing as expected [[boom-calibration-tilt-valves--0cf993|Boom Calibration — Tilt Valves]], [[boom-calibration-roll-damper-valve--3a09b1|Boom Calibration — Roll Damper Valve]], [[boom-calibration-center-frame-valve--5fa01e|Boom Calibration — Center Frame Valve]].
### One wing raising or running high while the other operates normally.

1. **IMU issue.** — Confirm that all BHS readings are correct. Unplug IMU and test machine; if issue resolves, inspect IMU mounting or replace. NOTE: A DTC will trigger but Boomtrac should still be functional. Check for DTCs relating to the IMU to confirm harnessing and communication. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)  
   Fix / related: [[boom-calibration-height-assignment--5e951f|Boom Calibration — Height Assignment]]
### Erratic or jumpy height control around the correct height.

1. **Roll lock issue.** — Check for roll lock engagement. If machine “pushes” in the cab when hunting, roll lock may be active. Machines with a carbon fiber truss boom: Confirm roll lock cylinders retract when unfolded. If extended, roll lock is stuck. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)
2. **Sway link system issue.** — When fully unfolded, hydraulic lines should not be pressurized. Moving hydraulic hoses with your hand can be a quick and easy inidcator if pressure is present. Raise the center frame; tilt one side up and the opposite side down to rock the system clockwise/counter-clockwise. Repeat several times. Roll lock cylinders should retract at least 25.4 mm (1 in) after rocking. If still tight, roll lock is stuck. Machines with a Serial Number of 270001 and above: Push down on one end of the boom. If it freely rolls, system is functioning. If difficult to move 0.3—0.6 m (1—2 ft), damper cylinders may be locked. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)
### Poor or inconsistent control (slow response or erratic movement).

1. **Incorrect or incomplete tilt valve calibration.** — Perform tilt valve calibration with warm/hot oil. Confirm tilt sensors read correctly across full tilt range. Quickly “bump” tilt functions and ensure that sensors register small movement changes (maintenance mode is fine for this). [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)  
   Fix / related: [[tilt-valve-calibration-procedure--17c550|Tilt Valve Calibration Procedure]] · [[boom-calibration-tilt-valves--0cf993|Boom Calibration — Tilt Valves]] · [[boom-maintenance-mode--f3caf2|Boom Maintenance Mode]]

> [!note] Tilt Valves calibration's own triggers
> Perform when boom tilt response is too slow or fast, a valve cartridge has been replaced, BoomTrac is not performing as expected, or boom tilt cylinders are replaced [[boom-calibration-tilt-valves--0cf993|Boom Calibration — Tilt Valves]].
### Booms are “clocked” (one wing consistently high, the other consistently low).

1. **Roll level calibration or IMU influence.** — Perform roll level calibration. Verify that the machine is level; reference Starfire roll angle if needed. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)  
   Fix / related: [[boom-level-position-calibration-procedure--328056|Boom Level Position Calibration Procedure]] · [[boom-calibration-boom-level-position--45e59a|Boom Calibration — Boom Level Position]]
2. **Incorrect IMU influence.** — Confirm that the IMU is firmly mounted. Unplug the IMU. If the problem disappears, the IMU is influencing control incorrectly. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)
### Center frame moves up/down excessively (more than normal).

1. **Incorrect target type selection.** — Change BoomTrac target type (Ground, Ground+, Canopy) to match crop conditions. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)  
   Fix / related: [[sensor-target--6c6fd9|Sensor Target]] · [[boom-height]]
2. **Accumulator precharge issue.** — Check accumulator precharge. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)  
   Fix / related: [[service-accumulator-systems-safely--6bd0ed|Service Accumulator Systems Safely]]

> [!note] Center Frame Valve calibration's own trigger
> Perform when center frame response is too slow or too fast [[boom-calibration-center-frame-valve--5fa01e|Boom Calibration — Center Frame Valve]].
### Booms operating at visibly incorrect heights or behaving unpredictably.

1. **Boom Height Sensor (BHS) misreadings.** — With booms level at 762 mm (30 in), verify that all BHS readings look correct. Tilt one side up to 1.8—2.1 m (6—7 ft) and confirm sensor readings follow expected values. Repeat for opposite side. Raise/lower booms, stopping every 152—254 mm (6—10 in), and confirm BHS values change smoothly and logically. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)
2. **Configuration issues.** — Inspect for bent brackets, debris on sensors, incorrect sensor location assignments, or incorrect target type selection. [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10)  
   Fix / related: [[boomtrac-settings-sensor-placement-setup--c8149c|BoomTrac Settings — Sensor Placement Setup]] · [[boom-calibration-height-assignment--5e951f|Boom Calibration — Height Assignment]] · [[sensor-target--6c6fd9|Sensor Target]]

> [!note] Sensor setup topics' own triggers
> Use the Edit Sensor function when a sensor has been replaced or a sensor's mounting location has changed [[boomtrac-settings-sensor-placement-setup--c8149c|BoomTrac Settings — Sensor Placement Setup]]. Boom Calibration | Height Assignment: perform when a BoomTrac or inertial sensor has been replaced [[boom-calibration-height-assignment--5e951f|Boom Calibration — Height Assignment]].

## What the manual does not specify here

- Expected BHS readings at the check heights — the table says readings should "look correct" and
  "follow expected values" [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-8, 155-9, 155-10).
- Accumulator precharge values, beyond those printed on each accumulator decal.
