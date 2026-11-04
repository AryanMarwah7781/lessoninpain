---
module_id: ouo6092,1774282874383-19-25MAR26
title: Machine and Display Application Setup
section: See & Spray (If Equipped)
page_labels:
- 135-13
- 135-14
- 135-15
- 135-16
- 135-17
pdf_pages:
- 779
- 780
- 781
- 782
- 783
models:
- all
options:
- See & Spray
engine_tier: null
topic_type: procedure
components:
- boom
- boom height
- camera
- display
- lights
- nozzle
conditions:
- wind
signal_words:
- IMPORTANT
- NOTE
figures:
- N156487
- NX1451617
- NX1451618
- NX1451620
- NX1451996
- NX1451621
- NX1451622
generic: false
title_inferred: false
parent_module_id: null
---

# Machine and Display Application Setup

1. Perform all daily maintenance items. (See machine Operator’s Manual for details.)
IMPORTANT: Avoid damage to the camera lenses. Do not use chemical cleaners, high-pressure water, or highly pressurized air when cleaning lenses.
2. Clean camera lenses. Remove as much debris as possible using a spray bottle with water, a damp cloth with light pressure, or low-pressure air. A soft cloth with a mild detergent and water may be used to remove grease from the lens.
3. Clean the See & Spray boom lights.
4. Access the Spray System application by selecting Menu > Machine Settings > Spray System, or select Rate on the boom widget. Enter the desired See & Spray target rate.
N156487—UN—02AUG21

![[N156487.png]]
**Figure N156487** — A: Nozzle Turret Setup

5. Select the See & Spray target rate.
6. Enter the desired target rate and select OK.
7. Select nozzles that are appropriate for the application requirements.
8. Rotate the turrets so that nozzles 1, 2, and 3 are in the forward A position and nozzles 4, 5, and 6 are in the rearward position.
NX1451617—UN—20MAR26

![[NX1451617.png]]
**Figure NX1451617** — A: Nozzle Turret Setup

9. Select Nozzle Turret Setup (A) from the See & Spray Premium main page.
NX1451618—UN—20MAR26

![[NX1451618.png]]
**Figure NX1451618** — A: Spray Mode; B: Spray Method; C: OK Button

10. Select Spray Mode (A) on the Spray Mode & Method page.
11. Enter the desired spray method (B) for the B nozzles.
12. Select OK button (C) to save settings and activate the system.
NOTE: This system requires sensor input from the BoomTrac Pro system, but BoomTrac Pro is not required to be ON during operation.
13. Verify that all software updates have been made and no fault codes exist.
14. Go to Menu > Machine Settings Tab > See & Spray. Set up the following configurable settings:
NX1451620—UN—20MAR26

![[NX1451620.png]]
**Figure NX1451620** — A: Fallback Mode

NX1451996—UN—20MAR26

![[NX1451996.png]]
**Figure NX1451996**

a. Select Fallback Mode (A) and set to Broadcast (default) or OFF. Select OK to save the setting.
- When Broadcast is selected, if the confidence level of the system is not fully or partially met, nozzle B reverts to Broadcast. Nozzle B will then broadcast apply product from the affected nozzles until confidence levels are back within optimal levels.
- When OFF is selected, if the confidence level is inadequate, Nozzle B reverts to OFF. Nozzle B will not apply any product from the affected nozzles until confidence levels are back within optimal levels.
NX1451621—UN—20MAR26

![[NX1451621.png]]
**Figure NX1451621** — A: Spray Buffer Area

NX1451622—UN—20MAR26

![[NX1451622.png]]
**Figure NX1451622**

Spray Buffer Area
b. Select Spray Buffer Area (A).
This setting adjusts the minimum spray length the system applies when a green object is detected.
NOTE: The system uses inputs such as nozzle speed and desired buffer setting to determine when the nozzle starts and stops spraying. This relates to the minimum time in milliseconds that an enabled command is sent to the nozzle. This setting correlates to linear distance.
It is recommended to increase the buffer length when operating at varying speeds, if accelerating and decelerating often, or if operating outside the ideal 30—50 psi spray pressure setting.
If another target is detected during the time an ON command is currently active, the command extends the minimum spray length.
For best results, select Large when operating in windy conditions or at higher boom heights.

> Source: OMKK105338 p. 135-13, 135-14, 135-15, 135-16, 135-17 · module ouo6092,1774282874383-19-25MAR26
