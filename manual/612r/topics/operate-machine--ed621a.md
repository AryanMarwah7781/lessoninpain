---
module_id: ouo6092,1777379103872-19-28APR26
title: Operate Machine
section: See & Spray (If Equipped)
page_labels:
- 135-18
- 135-19
pdf_pages:
- 784
- 785
models:
- all
options:
- See & Spray
engine_tier: null
topic_type: procedure
components:
- boom
- boom height
- boom wing
- camera
- display
- lights
- nozzle
conditions:
- wind
- dust
signal_words:
- NOTE
figures:
- N118420
generic: false
title_inferred: false
parent_module_id: null
---

# Operate Machine

NOTE: When operating in dusty conditions, slow machine speed and increase spray sensitivity to improve system performance.
1. Change the flow rate mode to standard flow on the display.
a. Go to Menu > Machine Settings > Spray System.
b. Touch the screen area under Flow Rate Mode.
c. Select Standard Flow from the Flow Rate Mode screen.
d. Press the OK button.
2. Avoid operating See & Spray when wind speeds are above 16 km/h (10 mph). Monitor all field conditions and status indicator to adjust operating method as needed to get the most out of the system.
N118420—UN—02NOV16

![[N118420.png]]
**Figure N118420**

3. Operate machine and monitor the See & Spray status using the status indicator on the home page.
- Indicator gray—System is not fully set up.
- Indicator green—System is active.
- Indicator orange—System is in partial or full fallback mode.
- Indicator red—System has recognized a full or partial system fault.
4. Watch for window shades on the display for alerts that confidence levels of the inputs are out of range, causing the system to revert to fallback mode settings for the affected nozzles.
During operation, the system must remain within a working range with all criteria met for proper system performance and functionality.
The following table is a list of possible fallback conditions.
Sub-System | Logic
Informational Text (Within See & Spray Diagnostic Center)
Informational Text
(Window Shade Alert) | Impact to System
Ambient Light | Outside of Working Range
Ambient light inadequate. Spray system reverted to fallback. Inspect sensor for mount orientation or obstructions, wait for lighting to improve, or turn off system to operate in traditional broadcast mode.
Clean sensor or await proper lighting. Ambient light inadequate for image processing.
Full System Fallback
NOTE: The center frame has a different ambient light threshold than the wings and will stay in fallback longer at sunrise. This only applies in crop applications where lights cannot be used.
Camera Lens | Obstruction Detected Past
Threshold
Camera lens obstructed. Associated nozzles reverted to fallback. Inspect camera for mount orientation and lens obstructions.
Camera inspection required. One or more camera lens obstructed.
Partial System Fallback
Nozzle Speed | Outside of Working Range
Nozzle speed outside working range. Associated nozzles reverted to fallback. Nozzle speed is outside of 0.8—26 km/h (0.5—16 mph) working range. Turning decreases speed on inside nozzles while increasing speed on outside nozzles. Adjust machine speed or turning radius.
Adjust speed or turn radius. Nozzle speed outside range of 0.8—26 km/h (0.5 —16 mph).
Partial System Fallback
Center Frame Height
Center Frame Outside Working Range By > 300 mm (11-13/16 in)
Center frame height outside normal range. Associated nozzles reverted to fallback. Adjust boom height settings or speed over changing terrain. Center frame height
Adjust boom height or travel speed. Boom height outside working range.
Partial System Fallback
Sub-System | Logic
Informational Text (Within See & Spray Diagnostic Center)
Informational Text
(Window Shade Alert) | Impact to System
Center Frame Outside Working Range By > 200 mm (7-13/16 in)
is 300 mm (11-13/16 in) below or above the calibrated height. Additional troubleshooting may be required.
Center frame height outside normal range. Associated nozzles reverted to fallback. Adjust boom height settings or speed over changing terrain. Center frame height is 300 mm (11-13/16 in) below or above the calibrated height. Additional troubleshooting may be required.
Adjust boom height or travel speed. Boom height outside working range.
Boom Wing Height
Wing Outside Working Range By > 300 mm (11- 13/16 in)
Wing Height Outside Working Range By > 200 mm (7-13/16 in)
Boom wing height outside working range. Associated nozzles reverted to fallback. Adjust boom height settings or speed over changing terrain. Center frame height is 300 mm (11-13/16 in) below or above the calibrated height. Additional troubleshooting may be required.
Boom wing height outside normal range. Associated nozzles reverted to fallback. Adjust boom wing height settings or speed over changing terrain. Center frame height is 200 mm (7-13/16 in) below or above the calibrated height. Additional troubleshooting may be required.
Adjust boom height or travel speed. Boom height outside working range.
Adjust boom height or travel speed. Boom height outside working range.
Partial System Fallback
Updating Camera | Camera Firmware Being
Updated
Updating camera firmware. This may take a few minutes. Maintain power until process is complete. One or more cameras are updating firmware. Associated nozzles reverted to fallback. If power is removed, the firmware install will restart on the next key cycle. This firmware update includes enhancements and resolves items within cameras. See Operator’s Manual for more details.
Updating camera firmware. This may take a few minutes. Maintain power until process is complete.
Partial System Fallback
Diagnostic Trouble Codes (DTCs)
Go to See & Spray Diagnostics/Diagnostic History in the See & Spray Application section of this manual for information on DTCs that may be causing the fault.
Full or Partial System Fallback

> Source: OMKK105338 p. 135-18, 135-19 · module ouo6092,1777379103872-19-28APR26
