---
module_id: ouo6092,1776448146768-19-28APR26
title: BoomTrac Settings | Sensor Placement Setup
section: BoomTrac Performance and Optimization
page_labels:
- 155-6
- 155-7
pdf_pages:
- 844
- 845
models:
- all
options:
- BoomTrac
engine_tier: null
topic_type: procedure
components:
- boom
- boom height
- boom wing
- display
conditions: []
signal_words:
- NOTE
figures:
- NX1458203
- NX1458205
- NX1458206
generic: false
title_inferred: false
parent_module_id: null
---

# BoomTrac Settings | Sensor Placement Setup

Edit Sensor
NX1458203—UN—20APR26

![[NX1458203.png]]
**Figure NX1458203** — A: Setup Button, L2 Sensor; B: Setup Button, L1 Sensor; C: Setup Button, C Sensor; D: Setup Button, R1 Sensor; E: Setup Button, R2 Sensor

NOTE: The 5-sensor setup is shown. The display can have a different amount of setup buttons depending on the machine configuration.
Sensor setup buttons can also have a Disabled Sensor icon, which indicates that the setup is incomplete or the sensor is turned off.
By pressing setup buttons (A—E) on the Boom System page, the operator can access the Edit Sensor function.
NX1458205—UN—20APR26

![[NX1458205.png]]
**Figure NX1458205** — A: Toggle Button; B: Location, Software Version; C: Edit Sensor Placement Button

The Edit Sensor function allows the operator to:
- Turn an individual sensor ON or OFF using toggle button (A).
- View the sensor’s software version in location (B).
- Edit the sensor’s physical placement on the boom using Edit Sensor Placement button (C).
When to Modify Sensor Settings
Use the Edit Sensor function when any of the following conditions occur:
1. A sensor has been replaced.
- A new sensor must be configured before BoomTrac can operate correctly.
2. A sensor’s mounting location has changed.
- Any repositioning requires updating its distance and offset.
3. A sensor needs to be disabled.
- Useful when diagnosing issues or when a sensor is temporarily unusable.
4. Software version verification is needed.
Edit Sensor Placement
NX1458206—UN—20APR26

![[NX1458206.png]]
**Figure NX1458206** — A: Input Box; B: Input Box; C: Sensor Toggle Bar

The Edit Sensor Placement screen enables entry of two key measurements:
- Sensor Distance—the horizontal distance from the machine’s centerline to the center of the boom height sensor. Edit the distance using input box (A).
- Sensor Offset—the vertical distance from the spray tip to the bottom of the sensor. Edit the distance using input box (B).
NOTE: The 5-sensor setup is shown. The display can have a different toggle bar depending on the machine configuration.
Select which sensors to edit using sensor toggle bar (C).
These measurements ensure that BoomTrac interprets sensor readings accurately relative to the boom and target.
Important Placement Requirements
Mirrored sensor rule—except for the center sensor, whenever a sensor is moved on one wing of the boom, the corresponding sensor on the opposite wing must be moved to the mirrored position.
Both sensors must have:
- The same distance from the centerline.
- The same vertical offset.
When to Modify Sensor Placement
Update sensor placement in these scenarios:
1. Initial system installation.
All sensor locations must be measured and entered during setup.
- A new sensor must be configured before BoomTrac can operate correctly.
2. Sensor relocation due to interference.
Sensors may need to be repositioned if:
- They interfere with other components.
- They cannot read the target properly.
- Machine configuration changes require adjustment.
Sensor Alignment Recommendations
For optimal BoomTrac performance:
- Sensors should be aligned so they are centered directly over the crop rows whenever possible.
- Since machines may operate in fields with varying row spacing, aim to position the sensors within ± 203 mm (8 in) of the crop rows.
Proper alignment reduces sensor “noise,” improves consistency of height readings, and provides more stable boom control.

> Source: OMKK105338 p. 155-6, 155-7 · module ouo6092,1776448146768-19-28APR26
