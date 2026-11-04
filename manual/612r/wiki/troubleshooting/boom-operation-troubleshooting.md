---
type: troubleshooting
title: "Boom Operation"
models: [all]
options: []
engine_tier: null
components: [boom, boom fold, boom tilt, boom wing, breakaway, fold cylinder, position sensor, solenoid, orifice]
sources:
  - "ouo6092,1737568523794-19-27OCT25"
  - "az06166,1748615500134-19-27APR26"
  - "az06166,1748615501491-19-27APR26"
  - "az06166,1748615502833-19-27APR26"
  - "az06166,1748615504058-19-27APR26"
  - "bn55050,1778257689748-19-08MAY26"
  - "bn55050,1778257811148-19-08MAY26"
  - "bn55050,1778257918052-19-08MAY26"
  - "bn55050,1778258021856-19-08MAY26"
  - "bn55050,1778258047740-19-08MAY26"
  - "bn55050,1778258131934-19-08MAY26"
  - "bn55050,1763572511240-19-19NOV25"
  - "bn55050,1778257230680-19-08MAY26"
  - "bn55050,1778257251717-19-08MAY26"
  - "OUO6092,0000D53-19-08JUN18"
  - "BN55050,00004F1-19-14MAY21"
  - "BN55050,00004E1-19-03MAY21"
  - "bn55050,1778257673001-19-08MAY26"
  - "bn55050,1778258034466-19-08MAY26"
  - "as09261,1712325678676-19-05APR24"
  - "OUO6092,0000CB7-19-15SEP17"
  - "OUO6092,0000CB8-19-15SEP17"
  - "OUO6092,0000CB9-19-15SEP17"
  - "BN55050,00004E2-19-15APR21"
  - "wp29706,1663098202024-19-01NOV22"
  - "wp29706,1663261579552-19-15SEP22"
  - "BN55050,00004E0-19-15JUN22"
reviewed: true
compiled: 2026-09-23
---
# Boom Operation — troubleshooting

**System:** boom fold, lift and roll, base machine (Troubleshooting section, p. 160-26; no option)
[[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29). The manual's table is reproduced in its printed order; the manual gives no cost or check
order, so none is implied. Two symptoms are marked "carbon fiber booms only" by the manual itself.
Components: [[boom]], [[boom-height]]. Boom maintenance mode (manual control of individual boom
sections) is listed for diagnosing boom folding problems [[boom-maintenance-mode--f3caf2|Boom Maintenance Mode]].

## Warnings that apply to these fixes

> [!warning] CAUTION
> CAUTION: Spray booms move quickly. Keep everyone out of the folding and unfolding area of the spray booms. Failure to stay out of the folding and unfolding area can result in injury or death. [[boom-fold-unfold-procedures--6a73ff|Boom Fold/Unfold Procedures]] (p. 30-34, 30-35)
> Also printed in: [[auto-boom-fold-unfold--db954d|Auto Boom Fold/Unfold]] (p. 30-35) · [[sequential-boom-fold-unfold--260a45|Sequential Boom Fold/Unfold]] (p. 30-35, 30-36) · [[one-side-fold-unfold--0afab8|One Side Fold/Unfold]] (p. 30-36, 30-37, 30-38)

> [!warning] IMPORTANT
> IMPORTANT: Avoid damage; only unfold the booms where there is enough space. [[boom-fold-unfold-procedures--6a73ff|Boom Fold/Unfold Procedures]] (p. 30-34, 30-35)
> Also printed in: [[auto-boom-fold-unfold--db954d|Auto Boom Fold/Unfold]] (p. 30-35) · [[sequential-boom-fold-unfold--260a45|Sequential Boom Fold/Unfold]] (p. 30-35, 30-36)

> [!warning] CAUTION (also printed in option sections: See & Spray)
> CAUTION: Spray booms move quickly. Keep everyone out of the folding and unfolding area of the spray booms. Failure to stay out of the area can result in injury or death. [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] (p. 25-B-35)
> Also printed in: [[center-frame-position-calibration-procedure--af16c1|Center Frame Position Calibration Procedure]] (p. 25-B-39) · [[boom-level-position-calibration-procedure--328056|Boom Level Position Calibration Procedure]] (p. 25-B-42, 25-B-43) · [[boom-calibration-see-and-spray-camera-calibration-procedure--0a9775|Boom Calibration — See & Spray Camera Calibration — Procedure]] (p. 25-B-46) · [[tilt-sensor-calibration-procedure--e44603|Tilt Sensor Calibration Procedure]] (p. 25-B-47, 25-B-48) · [[tilt-valve-calibration-procedure--17c550|Tilt Valve Calibration Procedure]] (p. 25-B-49, 25-B-50) · [[boom-unfold-fold-27-4-30-5-36-6-and-40-2-m-90-100-120-and-13--31675a|Boom Unfold/Fold—27.4, 30.5, 36.6, and 40.2 m (90, 100, 120, and 132 ft) Booms]] (p. 80-1, 80-2, 80-3, 80-4, 80-5)

> [!warning] IMPORTANT (also printed in option sections: See & Spray)
> IMPORTANT: Booms can contact and may damage the exhaust stack and/or walkway handrail when using manual mode to fold and unfold booms. Do not allow booms to go higher than the top of the cradle support when operating boom in manual mode. [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] (p. 25-B-35)
> Also printed in: [[center-frame-position-calibration-procedure--af16c1|Center Frame Position Calibration Procedure]] (p. 25-B-39) · [[boom-level-position-calibration-procedure--328056|Boom Level Position Calibration Procedure]] (p. 25-B-42, 25-B-43) · [[boom-calibration-see-and-spray-camera-calibration-procedure--0a9775|Boom Calibration — See & Spray Camera Calibration — Procedure]] (p. 25-B-46) · [[tilt-valve-calibration-procedure--17c550|Tilt Valve Calibration Procedure]] (p. 25-B-49, 25-B-50)

> [!warning] IMPORTANT (also printed in option sections: See & Spray)
> IMPORTANT: This procedure requires fully unfolding the boom. Ensure that adequate space is available. [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] (p. 25-B-35)
> Also printed in: [[center-frame-position-calibration-procedure--af16c1|Center Frame Position Calibration Procedure]] (p. 25-B-39) · [[boom-level-position-calibration-procedure--328056|Boom Level Position Calibration Procedure]] (p. 25-B-42, 25-B-43) · [[boom-calibration-see-and-spray-camera-calibration-procedure--0a9775|Boom Calibration — See & Spray Camera Calibration — Procedure]] (p. 25-B-46)

> [!warning] CAUTION
> CAUTION: Folding spray booms while in maintenance mode is not the same as folding in normal operation. Maintain awareness of surroundings and keep bystanders out of folding and unfolding area. [[boom-maintenance-mode--f3caf2|Boom Maintenance Mode]] (p. 25-B-10, 25-B-11)
> Also printed in: [[boom-maintenance-mode-procedure--ec37ef|Boom Maintenance Mode Procedure]] (p. 25-B-11, 25-B-12)

> [!warning] IMPORTANT
> IMPORTANT: Booms can contact and may damage the exhaust stack and/or walkway handrail when using maintenance mode to fold and unfold booms. Do not allow booms to go higher than the top of the cradle support when operating boom in maintenance mode. [[boom-maintenance-mode--f3caf2|Boom Maintenance Mode]] (p. 25-B-10, 25-B-11)
> Also printed in: [[boom-maintenance-mode-procedure--ec37ef|Boom Maintenance Mode Procedure]] (p. 25-B-11, 25-B-12)

> [!warning] IMPORTANT
> IMPORTANT: This procedure enables fully folding/ unfolding the boom and raising tilts to highest positions. Ensure that adequate space is available. [[boom-maintenance-mode--f3caf2|Boom Maintenance Mode]] (p. 25-B-10, 25-B-11)
> Also printed in: [[boom-maintenance-mode-procedure--ec37ef|Boom Maintenance Mode Procedure]] (p. 25-B-11, 25-B-12)

> [!warning] CAUTION
> CAUTION: Serious injury or death to you or others can occur from standing in front of boom when it is returning to its original position. Full boom breakaway system is under hydraulic pressure. If the boom must be lifted or aided over an object or an obstruction, stand behind the boom to avoid injury. [[full-boom-breakaway--f070b7|Full Boom Breakaway]] (p. 80-6)

> [!warning] IMPORTANT
> IMPORTANT: Verify that the fold stops are properly aligned before tightening. Unevenly aligned bumpers can lead to uneven load distribution, resulting in failure of the fold stop hardware. Trimming the shims for each fold stop individually may be necessary to achieve optimal performance. [[inspect-and-adjust-as-required-t3-link-shims-and-t6-t7-rope--0631f2|Inspect and Adjust (As Required) T3 Link, Shims, and T6/T7 Rope]] (p. 80-13, 80-14, 80-15, 80-16)
> Also printed in: [[adjust-breakaway-alignment-36-6-m-120-ft-as-required--12e3e8|Adjust Breakaway Alignment—36.6 m (120 ft) (As Required)]] (p. 80-22, 80-23, 80-24, 115-21, 115-22, 115-23)

## Symptoms

### Inner boom section does not fold out.

1. **Faulty switch.** — Replace switch. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
2. **Load sense jamming valve not working.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
3. **Damaged or corroded electrical connections.** — Repair, replace, or clean electrical connection. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[electrical-system]]
4. **Failed solenoid coil or relay.** — Replace coil or relay. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
5. **Sticking hydraulic spool cartridge.** — Remove hydraulic spool cartridge and clean. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
6. **Plugged orifice or hydraulic line.** — Remove and clean the orifice or hydraulic line. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
7. **Faulty inner boom fold cylinder.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
8. **Faulty inner boom position sensor.** — Replace and calibrate the sensor. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
9. **Boom fold/unfold sensors out of calibration.** — Calibrate fold/unfold sensors. (See Auto Boom Fold/Unfold Calibration Procedure in Calibrations section.) [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] · [[boom-calibration-auto-boom-fold-unfold--ae3084|Boom Calibration — Auto Boom Fold/Unfold]]

> [!note] Also check before anything else in this table: speed and Transport Lock
> To unfold or fold the booms, the machine must be traveling less than 8 km/h (5 mph) and the
> Transport Lock must be disengaged [[boom-fold-unfold-procedures--6a73ff|Boom Fold/Unfold Procedures]]. The Transport Lock switch prevents hydraulic boom
> movements (boom folding/unfolding, center frame raise/lower, tilt raise/lower) [[transport-lock-switch--1c890e|Transport Lock Switch]]. This is a
> condition printed with the fold procedures, not a row of the troubleshooting table.
>
> The calibration topics state their own triggers: perform the Auto Boom Fold/Unfold calibration
> when the boom is not folding or unfolding properly [[boom-calibration-auto-boom-fold-unfold--ae3084|Boom Calibration — Auto Boom Fold/Unfold]]; perform the tilt sensor calibration when
> automatic boom fold/unfold is not operating correctly [[boom-calibration-tilt-sensors--0b4418|Boom Calibration — Tilt Sensors]].
### Outer boom section does not fold out.

1. **Faulty switch.** — Replace switch. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
2. **Load sense jamming valve not working.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
3. **Damaged or corroded electrical connections.** — Repair, replace, or clean electrical connection. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[electrical-system]]
4. **Failed solenoid coil or relay.** — Replace coil or relay. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
5. **Sticking hydraulic spool.** — Remove hydraulic spool and clean. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
6. **Check valve stuck shut in the load sense line.** — Remove and clean check valve. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
7. **Plugged orifice or hydraulic line.** — Remove and clean the orifice or hydraulic line. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
8. **Faulty inner boom cylinder switch.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
9. **Faulty outer boom fold cylinder.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
10. **Faulty outer boom position sensor.** — Replace and calibrate the sensor. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
11. **Boom fold/unfold sensors out of calibration.** — Calibrate fold/unfold sensors. (See Auto Boom Fold/Unfold Calibration Procedure in Calibrations section.) [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] · [[boom-calibration-auto-boom-fold-unfold--ae3084|Boom Calibration — Auto Boom Fold/Unfold]]
### Outer boom section folds out part way and stops.

1. **Hydraulic cylinder magnetic switch releases.** — Fold boom and retry unfolding procedure. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[boom]]
2. **Boom fold/unfold sensors out of calibration.** — Calibrate fold/unfold sensors. (See Auto Boom Fold/Unfold Calibration Procedure in Calibrations section.) [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] · [[boom-calibration-auto-boom-fold-unfold--ae3084|Boom Calibration — Auto Boom Fold/Unfold]]
### Inner boom section does not fold in.

1. **Faulty switch.** — Replace switch. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
2. **Load sense jamming valve not working.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
3. **Damaged or corroded electrical connections.** — Repair, replace, or clean electrical connection. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[electrical-system]]
4. **Failed solenoid coil or relay.** — Replace coil or relay. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
5. **Sticking hydraulic spool.** — Remove hydraulic spool and clean. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
6. **Check valve stuck shut in the load sense line.** — Remove and clean check valve. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
7. **Plugged orifice or hydraulic line.** — Remove and clean the orifice or hydraulic line. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
8. **Faulty outer boom cylinder switch.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
9. **Faulty inner boom fold cylinder.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
10. **Faulty inner boom position sensor.** — Replace and calibrate the sensor. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
11. **Boom fold/unfold sensors out of calibration.** — Calibrate fold/unfold sensors. (See Auto Boom Fold/Unfold Calibration Procedure in Calibrations section.) [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] · [[boom-calibration-auto-boom-fold-unfold--ae3084|Boom Calibration — Auto Boom Fold/Unfold]]
### Inner boom section folds in part way and stops.

1. **Hydraulic cylinder magnetic switch releases.** — Unfold boom and retry folding procedure. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[boom]]
2. **Boom fold/unfold sensors out of calibration.** — Calibrate fold/unfold sensors. (See Auto Boom Fold/Unfold Calibration Procedure in Calibrations section.) [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] · [[boom-calibration-auto-boom-fold-unfold--ae3084|Boom Calibration — Auto Boom Fold/Unfold]]
### Outer boom section does not fold in or inner boom folds in before outer boom folds in.

1. **Faulty switch.** — Replace switch. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
2. **Load sense jamming valve not working.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
3. **Damaged or corroded electrical connections.** — Repair, replace, or clean electrical connections. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[electrical-system]]
4. **Failed solenoid coil or relay.** — Replace coil or relay. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
5. **Sticking hydraulic spool.** — Remove hydraulic spool and clean. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
6. **Check valve stuck shut in the load sense line.** — Remove and clean check valve. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
7. **Plugged orifice or hydraulic line.** — Remove and clean the orifice or hydraulic line. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
8. **Faulty outer boom fold cylinder.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
9. **Faulty outer boom position sensor.** — Replace and calibrate the sensor. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
10. **Boom fold/unfold sensors out of calibration.** — Calibrate fold/unfold sensors. (See Auto Boom Fold/Unfold Calibration Procedure in Calibrations section.) [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[auto-boom-fold-unfold-calibration-procedure--567ee2|Auto Boom Fold/Unfold Calibration Procedure]] · [[boom-calibration-auto-boom-fold-unfold--ae3084|Boom Calibration — Auto Boom Fold/Unfold]]
### Boom will not return to level after rolling in either direction or boom does not roll freely.

1. **Suspended center frame binds at wear plates or center mounting bearings too far forward on shaft.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
### Boom does not raise or lower.

1. **Faulty switch.** — Replace switch. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
2. **Load sense jamming valve not working.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
3. **Damaged or corroded electrical connections.** — Repair, replace, or clean electrical connection. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[electrical-system]]
4. **Failed solenoid coil or relay.** — Replace coil or relay. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
5. **Sticking hydraulic spool.** — Remove hydraulic spool and clean. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
6. **Check valve stuck shut in the load sense line.** — Remove and clean check valve. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
7. **Faulty lift cylinders.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
8. **Hydraulic compensator pressure not to specification.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
### Boom lift raises too fast.

1. **Orifice in the boom valve is missing.** — Install correct size orifice. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
2. **Auxiliary pump high compensator pressure set too high.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
### One individual boom function does not stop when switch is released or is slow to release.

1. **Sticking or faulty switch.** — Repair or replace switch. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
2. **Sticking hydraulic spool assembly.** — Clean spool assembly. Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
3. **Faulty solenoid valve.** — Repair or replace solenoid valve. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
4. **Load sense jamming valve not working.** — Contact a John Deere dealer or other service provider. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)
### Poor boom stability, carbon fiber booms only.

1. **T3 link is not properly adjusted.** — Verify that the T3 link adjustment is within specification, adjust as needed. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[inspect-and-adjust-as-required-t3-link-shims-and-t6-t7-rope--0631f2|Inspect and Adjust (As Required) T3 Link, Shims, and T6/T7 Rope]] · [[inspect-and-adjust-as-required-t3-link-shims-and-t6-t7-rope--a210ba|Inspect and Adjust (As Required) T3 Link, Shims, and T6/T7 Rope—After First 50 Hours]] · [[inspect-and-adjust-as-required-t3-link-shims-and-t6-t7-rope--c4bf58|Inspect and Adjust (As Required) T3 Link, Shims, and T6/T7 Rope—After First 100 Hours]] · [[inspect-and-adjust-as-required-t3-link-shims-and-t6-t7-rope--fcea7f|Inspect and Adjust (As Required) T3 Link, Shims, and T6/T7 Rope—250 Hours]]
2. **T6/T7 rope not properly adjusted.** — Verify that the T6/T7 rope adjustment is within specification, adjust as needed. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[inspect-and-adjust-as-required-t3-link-shims-and-t6-t7-rope--0631f2|Inspect and Adjust (As Required) T3 Link, Shims, and T6/T7 Rope]] · [[inspect-and-adjust-as-required-t3-link-shims-and-t6-t7-rope--a210ba|Inspect and Adjust (As Required) T3 Link, Shims, and T6/T7 Rope—After First 50 Hours]] · [[inspect-and-adjust-as-required-t3-link-shims-and-t6-t7-rope--c4bf58|Inspect and Adjust (As Required) T3 Link, Shims, and T6/T7 Rope—After First 100 Hours]] · [[inspect-and-adjust-as-required-t3-link-shims-and-t6-t7-rope--fcea7f|Inspect and Adjust (As Required) T3 Link, Shims, and T6/T7 Rope—250 Hours]]
### Breakaway section does not stay in desired position, carbon fiber boom only.

1. **Breakaway alignment is not properly adjusted.** — Adjust breakaway alignment. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[adjust-breakaway-alignment-36-6-m-120-ft-as-required--12e3e8|Adjust Breakaway Alignment—36.6 m (120 ft) (As Required)]] · [[adjust-breakaway-alignment-40-2-m-132-ft-as-required--fe7c3b|Adjust Breakaway Alignment—40.2 m (132 ft) (As Required)]]
2. **Breakaway tension is not properly adjusted.** — See Adjust Breakaway Tension-Carbon Fiber Booms. Adjust breakaway tension chain. [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29)  
   Fix / related: [[adjust-breakaway-tension-as-required-carbon-fiber-booms--008880|Adjust Breakaway Tension (As Required)-- Carbon Fiber Booms]] · [[adjust-breakaway-tension-as-required-carbon-fiber-booms--dfc10f|Adjust Breakaway Tension (As Required)-- Carbon Fiber Booms]] · [[adjust-breakaway-tension-chain-as-required--12f600|Adjust Breakaway Tension Chain (As Required)]]

> [!inference] Cheapest-first
> The manual lists causes in the same order for each "does not fold" symptom, starting with a faulty
> switch and ending with sensor calibration [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29). It does not say this is a check order. The only
> printed pre-check is the speed / Transport Lock condition in the note under the first symptom.

## What the manual does not specify here

- Where the load sense jamming valve, check valves and orifices are, or their specifications — the
  table sends these to the dealer [[boom-operation--dd7f82|Boom Operation]] (p. 160-26, 160-27, 160-28, 160-29).
