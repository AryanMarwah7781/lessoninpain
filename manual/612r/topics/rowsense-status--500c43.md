---
module_id: aota2vy,1685108824941-19-26MAY23
title: RowSense Status
section: AutoTrac Vision and RowSense
page_labels:
- 25-O-2
- 25-O-3
pdf_pages:
- 276
- 277
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: display_ui
components:
- camera
- steering
conditions: []
signal_words:
- NOTE
figures:
- N128640
- N128637
- N128638
- N128639
- N128472
generic: false
title_inferred: false
parent_module_id: null
---

# RowSense Status

Sensor Offsets
An offset can be added to row guidance to change alignment wheels in the crop row.
- Entering offset values less than 0 causes machine to drive slightly left.
- Entering offset values greater than 0 causes machine to drive slightly right.
- Default value is 0, with a range of -10 to 10.
RowSense Status Icons
N128640—UN—09FEB17

![[N128640.png]]
**Figure N128640**

Standby
System on standby.
N128637—UN—09FEB17

![[N128637.png]]
**Figure N128637**

Active
System active, operating with both row sensor and GPS.
N128638—UN—09FEB17

![[N128638.png]]
**Figure N128638**

No GPS Signal
No GPS signal. Operating with row sensor data only.
N128639—UN—09FEB17

![[N128639.png]]
**Figure N128639**

No Row Sensor Signal
No row sensor signal. Operating with GPS only.
Diagnostics
Guidance Track Selected—Tracking mode selected and guidance line established.
GPS Signal Adequate—Differential correction signal is available.
AutoTrac Active— AutoTrac is active and engaged.
Vision Sensor Calibrated—Sensor is calibrated.
Vision Sensor Confidence OK—Camera accuracy of its ability to detect crop.
Vision Sensor
Displays camera view.
NOTE: Camera view may include additional status icons.
Confidence value has a range of 0 to 10. Value must be between 8 to 10 for RowSense to use Vision sensor.
N128472—UN—09FEB17

![[N128472.png]]
**Figure N128472**

Calibration
Select Calibration button to view Vision Sensor calibration.

> Source: OMKK105338 p. 25-O-2, 25-O-3 · module aota2vy,1685108824941-19-26MAY23
