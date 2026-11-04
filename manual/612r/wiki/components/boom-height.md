---
type: component
title: "Boom height"
models: [all]
options: [BoomTrac]
engine_tier: null
components: [boom height, boom, boom wing, boom tilt, BoomTrac sensor]
sources:
  - "ouo6092,1777984543287-19-05MAY26"
  - "ouo6092,1776448178262-19-28APR26"
  - "ouo6092,1777984352422-19-05MAY26"
  - "ouo6092,1777984448733-19-05MAY26"
  - "ouo6092,1777985086502-19-05MAY26"
  - "ouo6092,1777985111570-19-05MAY26"
  - "bn55050,1778257749093-19-08MAY26"
  - "bn55050,1778257765367-19-08MAY26"
  - "hy01057,1784715061862-19-22JUL26"
  - "OUO6092,0000EE3-19-13MAY21"
  - "BN55050,000005D-19-08JUN18"
reviewed: true
compiled: 2026-09-23
---

# Boom height

Boom height is the distance from the bottom of the spray tips to the target
[[boomtrac--783c2a|BoomTrac]]. It is controlled manually from the multi-function lever, held
automatically by BoomTrac (if equipped), and given a stop point by Return to Height.

## Warnings

> [!warning] CAUTION
> CAUTION: Avoid damage or contamination of your surroundings. Increasing boom height excessively above the target increases the risk of spray drift.
> [[height-mode--b6109a|Height Mode]]

## What it is

The Boom System application is used to configure BoomTrac and return-to-height mode settings;
adjust to maintain the proper boom height above the crop or ground, and adjust when the crop or
terrain conditions change [[boom-system-main-page--9cb34d|Boom System Main Page]].

The BoomTrac system automatically controls boom tilt functions and center frame control relative to
contours of the ground or crop canopy [[boomtrac--783c2a|BoomTrac]]. BoomTrac is an option — the
BoomTrac tab on the Boom System main page is marked "if equipped"
[[boom-system-main-page--9cb34d|Boom System Main Page]].

Target Height on the BoomTrac page displays the distance from the bottom of the spray tips to the
target, and the Input Boxes are selected to change the values [[boomtrac--783c2a|BoomTrac]]. Sensor
Height displays the current height reading for each sensor [[boomtrac--783c2a|BoomTrac]].

## Where it is

![[WZ1408019.png]]

**Figure WZ1408019** — Target Height on the BoomTrac page [[boomtrac--783c2a|BoomTrac]]

![[NX1458247.png]]

**Figure NX1458247** — A: Height Mode Toggle Button, on the Boom System page
[[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings | Height Mode]]

Reach the settings through the Boom System application; its tabs are BoomTrac (if equipped),
Return to Height - Raise, Return to Height - Lower, and Advanced Settings
[[boom-system-main-page--9cb34d|Boom System Main Page]].

## Related settings

### Height Mode

Height Mode allows you to choose the desired mode for BoomTrac operation
[[height-mode--b6109a|Height Mode]]. Press the Height Mode softkey to select between
Locked/Unlocked Height Mode [[height-mode--b6109a|Height Mode]], or press the height mode toggle
button (A) on the Boom System page
[[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings | Height Mode]].

- **Locked Height Mode** maintains the same height above the target for the entire length of the
  boom; use this setting for most applications [[height-mode--b6109a|Height Mode]]. When in Locked
  Height Mode, the center target height is the only value that can be adjusted
  [[height-mode--b6109a|Height Mode]]. It is recommended for most applications where consistent
  spray height across the full boom is critical for optimal coverage and drift control
  [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings | Height Mode]].
- **Unlocked Height Mode** lets you enter a different target height for each sensor; use this
  setting when wing height above the target is different from the center frame target height
  [[height-mode--b6109a|Height Mode]]. An example of when this would be used is in rough terrain,
  where setting the wings higher than the center frame helps keep them from contacting the crop on
  the ground [[height-mode--b6109a|Height Mode]]. Other listed cases are waterways, ditches or
  rolling field transitions, field edges and obstructions, and specialty crops or fields with
  inconsistent canopy height [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings | Height Mode]].

### Sensor Target

Sensor Target selects what the sensors hold height above
[[boomtrac--783c2a|BoomTrac]]. The choices are Ground (sensor measurement from boom to ground, used
when the field is fallow ground), Ground with Canopy Assist (Ground+) (if equipped; sensor
measurement from boom to ground with reference to the top of the plant, typically used when the
field is partial canopy), and Crop Canopy+ (sensor measurement from the boom to the top of the
plant with reference to the ground, used when the majority of the field is closed canopy)
[[sensor-target--6c6fd9|Sensor Target]].

### Return to Height

Return to Height gives the boom a stop point. Current Set Point is the target raise or lower height
for the system, selected by the operator and displayed as a percentage to the left of the indicator,
with Minimum: 0% (boom fully lowered) and Maximum: 100% (boom fully raised)
[[return-to-height-status--9fe45c|Return to Height | Status]]. Current Boom Height is the current
boom height as detected by each height sensor
[[return-to-height-status--9fe45c|Return to Height | Status]].

Set to Current sets the boom stop point at the current boom height
[[return-to-height-set-to-current--8a9488|Return to Height | Set to Current]]: position the boom
sections to the desired height using the multi-function lever buttons, then select the Set to
Current button [[return-to-height-set-to-current--8a9488|Return to Height | Set to Current]].

## Related procedures

- Operating return to height from the cab, including the Return to Height Mode Operation table for
  Off, Center, Left and Right, and Left, Center, Right modes
  [[operate-boom-return-to-height--e3eb93|Operate Boom Return to Height]].
- **Boom Calibration | Height Assignment** calibrates the location of the BoomTrac sensors and IMU
  sensors on the boom [[boom-calibration-height-assignment--5e951f|Boom Calibration | Height Assignment]].
  Perform it when a BoomTrac or inertial sensor has been replaced
  [[boom-calibration-height-assignment--5e951f|Boom Calibration | Height Assignment]]. The procedure
  requires the engine running, Wheel Speed 0 km/h (0 mph), the machine parked and not applying
  product, the boom unfolded with boom height set to 76.2 cm (30 in), and BoomTrac ready
  [[boom-height-assignment-procedure--8cb704|Boom Height Assignment Procedure]].
- Folding, unfolding and the transport lock: see [[boom]].

## What the manual does not specify here

The Boom System topics give no spray-height value for a crop or a wind condition — they only say to
adjust to maintain the proper boom height above the crop or ground and to adjust when the crop or
terrain conditions change [[boom-system-main-page--9cb34d|Boom System Main Page]]. The only printed
height figures are the tip-geometry values: flat fan spray tips are usually spaced 508 mm (20 in)
apart and positioned 457— 559 mm (18—22 in) above the target surface
[[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]], and 76.2 cm (30 in) is a calibration
precondition, not an operating height
[[boom-height-assignment-procedure--8cb704|Boom Height Assignment Procedure]]. The installed tip's
chart and the product label determine the working height; for chemical application the product
label and local regulations govern.

## Related troubleshooting

- BoomTrac is modified when crop height changes, terrain contour changes, boom lower/raise response
  is too slow or too fast, or when spraying in dusty or muddy conditions
  [[boomtrac--783c2a|BoomTrac]].
- Select the status message next to the BoomTrac status indicator to view BoomTrac | Diagnostics
  [[boomtrac--783c2a|BoomTrac]].
- If the height assignment calibration fails, select Retry and verify that all requirements listed
  on-screen have been met; if calibration fails twice, see your John Deere dealer or service
  provider [[boom-height-assignment-procedure--8cb704|Boom Height Assignment Procedure]].
- Light with Fault-style fault indications for sensors are reached through the Detailed Results and
  Diagnostics Center buttons on the calibration screen
  [[boom-height-assignment-procedure--8cb704|Boom Height Assignment Procedure]].
