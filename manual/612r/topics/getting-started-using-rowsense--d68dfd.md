---
module_id: aota2vy,1685108825113-19-26MAY23
title: Getting Started Using RowSense
section: AutoTrac Vision and RowSense
page_labels:
- 25-O-1
- 25-O-2
pdf_pages:
- 275
- 276
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: display_ui
components:
- steering
conditions: []
signal_words: []
figures:
- N128475
- N128632
- N128633
- N128474
generic: false
title_inferred: false
parent_module_id: null
---

# Getting Started Using RowSense

RowSense Overview—AutoTrac RowSense is an enhancement to integrated AutoTrac when used to harvest corn or apply product. RowSense uses existing guidance tracks and global positioning system (GPS) data combined with sensor data for optimal accuracy.
RowSense Settings—Turn RowSense on / off and select row entry mode.
RowSense Status—Set sensor offsets, view sensor voltages, calibrate sensors, and view RowSense diagnostics.
Creating Tracks—There are several guidance track creation methods. Select the best method for your application.
N128475—UN—09FEB17

![[N128475.png]]
**Figure N128475**

Straight Track
Straight Track uses straight-line parallel passes.
N128632—UN—09FEB17

![[N128632.png]]
**Figure N128632**

Adaptive Curve Track
Adaptive Curve Track uses a manually driven initial pass to generate passes that are based on the previous pass.
N128633—UN—09FEB17

![[N128633.png]]
**Figure N128633**

AB Curve Track
AB Curve Track uses a manually driven curved path with two end points (beginning and end) to generate parallel passes.
N128474—UN—09FEB17

![[N128474.png]]
**Figure N128474**

Circle Track
Circle Track creates concentric circle guidance lines for use in fields with a center pivot.
Row Dropout
Row dropout occurs when row sensor data is lost.
AutoTrac operates using GPS until row data is reacquired. This can occur when entering waterways.
When using straight track or AB curve track, and the row drops out, the guidance track is recentered. The provides a greater chance RowSense reacquires correct track on other side of waterway.

> Source: OMKK105338 p. 25-O-1, 25-O-2 · module aota2vy,1685108825113-19-26MAY23
