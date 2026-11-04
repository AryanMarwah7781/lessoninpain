---
type: troubleshooting
title: "AutoTrac Vision troubleshooting"
models: [all]
options: [AutoTrac, RowSense]
engine_tier: null
components: [AutoTrac, vision sensor, camera, steering]
sources:
  - "ouo6092,1737574853595-19-27OCT25"
  - "ouo6092,1737576395987-19-27OCT25"
  - "bn55050,1743093416316-19-27MAR25"
  - "az06166,1748614901810-19-27APR26"
reviewed: true
compiled: 2026-09-23
---

# AutoTrac Vision troubleshooting

**Options: AutoTrac with the Vision sensor (RowSense in vision mode).** These two tables are printed
in the Troubleshooting section: AutoTrac Vision Sensor on 160-29 and 160-30
[[autotrac-vision-sensor--bc8a96|AutoTrac Vision Sensor]], and AutoTrac Vision Performance on 160-31
and 160-32 [[autotrac-vision-performance--a7ed46|AutoTrac Vision Performance]]. If your machine does
not have AutoTrac Vision, this page does not apply. Symptoms and rows are in the manual's printed
order (the tables do not rank causes); the row split was checked against the rendered pages. Where
one problem has several solutions, they are listed in the printed order. Component:
[[components/steering]].

## Warnings for the fixes

> [!warning] CAUTION — printed on [[clean-autotrac-vision-cameras--51a7df|Clean AutoTrac Vision Cameras]] (p. 145-1). Applies to: cleaning the vision cameras
> CAUTION: To avoid serious injury or death, shut OFF the engine, set the parking brake, and remove the key prior to cleaning the vision cameras.

> [!warning] IMPORTANT — printed on [[clean-autotrac-vision-cameras--51a7df|Clean AutoTrac Vision Cameras]] (p. 145-1). Applies to: cleaning the vision cameras
> IMPORTANT: Do not pressure wash the vision cameras. Use normal water pressure less than 3.4 bar (345 kPa) (50 psi). Do not use an abrasive, oily, or dirty cloth to clean the vision cameras.

## Maintenance topic that names a symptom as its trigger

AutoTrac Vision 2.0 calibration may be needed in following conditions: when vision cameras are
replaced, and when undesired guidance performance is experienced while utilizing RowSense in vision
mode [[autotrac-vision-2-0-sensor-calibration--3ad3ca|AutoTrac Vision 2.0 Sensor Calibration]]. Several
performance rows below say "Recalibrate system."; that topic is the calibration procedure.

## AutoTrac Vision Sensor table

### RowSense will not change from disabled to enabled.

| Problem | Solution |
|---|---|
| AutoTrac or RowSense License missing. | Purchase License at ISG price page. |
| Installed on wrong sprayer. | Install on approved sprayer. Contact a John Deere dealer or other service provider. |
| Display software is out of date. | Update to latest software version. |

[[autotrac-vision-sensor--bc8a96|AutoTrac Vision Sensor]]

### No Vision sensor detected.

| Problem | Solution |
|---|---|
| Check that Vision sensor is correctly connected. | Check sensor connection. If problem persists, contact a John Deere dealer or other service provider. |

[[autotrac-vision-sensor--bc8a96|AutoTrac Vision Sensor]]

### System not operating correctly.

| Problem | Solution |
|---|---|
| Diagnostic trouble code generated. | Contact a John Deere dealer or other service provider. |

[[autotrac-vision-sensor--bc8a96|AutoTrac Vision Sensor]]

### No video image on video page.

| Problem | Solution |
|---|---|
| Wrong video channel selected. | Go through all channels. If problem persists, contact a John Deere dealer or other service provider. |
| Vision sensor lenses are not clean or are damaged. | Clean Vision sensor window. — Contact a John Deere dealer or other service provider if Vision sensor is damaged. |
| Diagnostic trouble code generated. | Contact a John Deere dealer or other service provider. |

[[autotrac-vision-sensor--bc8a96|AutoTrac Vision Sensor]] — cleaning:
[[clean-autotrac-vision-cameras--51a7df|Clean AutoTrac Vision Cameras]].

### Vision system cannot be successfully calibrated.

| Problem | Solution |
|---|---|
| Vision sensor cannot detect row due to crop conditions. | Reattempt calibration in an area that is straight without weeds and clearly defined crop rows. |
| The image from the Vision sensor is not available on the display. | Go to Vision sensor diagnostics. |
| The image from the Vision sensor is not focused. | Clean Vision sensor window and inspect camera for damage. If problem persists, contact a John Deere dealer or other service provider. |
| Vision sensor cannot detect row spacing. | Recommended for 762 mm (30 in) row spacing. If problem persists, contact a John Deere dealer or other service provider. — Verify that camera is installed at correct height. If problem persists, contact a John Deere dealer or other service provider. |
| System cannot detect row. | Align sprayer parallel to crop row. |

[[autotrac-vision-sensor--bc8a96|AutoTrac Vision Sensor]] — calibration:
[[autotrac-vision-2-0-sensor-calibration--3ad3ca|AutoTrac Vision 2.0 Sensor Calibration]].

## AutoTrac Vision Performance table

### AutoTrac Status Indicator jumps from Activated status (4-pie) to Enabled status (3-pie).

| Problem | Solution |
|---|---|
| The current sensor being used may have become unplugged. | Check diagnostics to determine sensor health. |
| Vision sensor cannot detect crop rows (low confidence). | Recalibrate system. — Clean Vision sensor window. — Set up A--B line to revert to GPS in challenging conditions. — Operate in crop rows that are not canopied. — Operate in crop rows that have fewer weeds/crop residue. |

[[autotrac-vision-performance--a7ed46|AutoTrac Vision Performance]]

### Sprayer immediately steers and runs over crop.

| Problem | Solution |
|---|---|
| Sensor offset is too large. | Reset sensor offset to zero (default). Readjust as necessary. |
| "GPS--Row" Row Entry Mode is selected with A--B line which does not match crop rows. | Setup A--B line which matches crop rows. |

[[autotrac-vision-performance--a7ed46|AutoTrac Vision Performance]]

### Sprayer gradually runs over crop.

| Problem | Solution |
|---|---|
| Sprayer consistently drives to one side of the center of the crop row gap. | Clean the Vision sensor window. — Operate in fields with less side slope — Change the sensor offset. |
| Operating tires in guess rows. | Avoid driving in or straddling guess rows. |
| System not recalibrated in changing crop conditions, such as crop height or lighting conditions. | Recalibrate system. |
| Operating too fast for system limits. | Lower speed. If problem persists, contact a John Deere dealer or other service provider. |
| System does not switch to GPS. | Reset A—B line. |
| Lights may be inadequate when operating system in short crop conditions. | Install premium lighting package. |
| Not enough space to steer in a row. | Change to smaller tire size. |
| Cresting hills which are too steep. | Reduce speed. — Record an Adaptive Curve. |
| Vision sensor cannot detect crop rows (low confidence). | Operate in areas with fewer weeds, taller plants, and/or better lighting. |
| Vision system may not perform as well in areas with high crop residue (i.e. corn on corn) and on side hills. | Operate at slower speeds or drive manually through these areas until confidence is improved and re-engage Vision. |
| System switches to GPS too often. | Disable system and operate manually or use AutoTrac. |

[[autotrac-vision-performance--a7ed46|AutoTrac Vision Performance]]

### Sprayer "S-ing".

| Problem | Solution |
|---|---|
| Vision sensor is not detecting consistent crop. | Recalibrate system. |
| AutoTrac is not tuned to operate in these conditions. | Reset Steering Sensitivity to 100 (default) and reset Advanced Settings to 100 (default). — Adjust Advanced Settings to make steering more aggressive or less aggressive. If problem persists, contact a John Deere dealer or other service provider. — Slow down, use different tires, change soil conditions. |

[[autotrac-vision-performance--a7ed46|AutoTrac Vision Performance]]

### Sprayer runs over crop in curved rows.

| Problem | Solution |
|---|---|
| Row curvature is excessive. | Improve performance by recording an Adaptive Curve. — Lower speed. |

[[autotrac-vision-performance--a7ed46|AutoTrac Vision Performance]]

### Sprayer runs over crop during night operation

| Problem | Solution |
|---|---|
| Check that all lights are clean and working well. | Clean and repair or replace lights. — Clean the Vision sensor window. — Install premium lighting package. |

[[autotrac-vision-performance--a7ed46|AutoTrac Vision Performance]] — [[components/lights]].
