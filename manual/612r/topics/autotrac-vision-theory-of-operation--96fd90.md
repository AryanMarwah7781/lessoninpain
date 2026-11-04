---
module_id: bn55050,1742234626870-19-27OCT25
title: AutoTrac Vision Theory of Operation
section: AutoTrac Tuning, AutoTrac RowSense, and AutoTrac Vision
page_labels:
- 140-6
- 140-7
- 140-8
pdf_pages:
- 817
- 818
- 819
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: description
components:
- camera
- display
- steering
conditions:
- wind
- slope
- night
signal_words:
- IMPORTANT
- NOTE
figures:
- PC666478
- PC659258
- PC631733
generic: false
title_inferred: false
parent_module_id: null
---

# AutoTrac Vision Theory of Operation

IMPORTANT: Avoid potential damage to crops. AutoTrac Vision 2.0 does not support night operation. Do not operate machine with AutoTrac Vision 2.0 turned ON during night time.
AutoTrac Vision 2.0 overlay view is displayed when the machine is in well-defined crop rows and the vision camera LED status is shown as green. Other variations are possible depending on conditions.
PC666478—UN—19MAR25

![[PC666478.png]]
**Figure PC666478**

AutoTrac Vision 2.0 Overlay
AutoTrac Vision 2.0 Requirements:
- AutoTrac 2.0 activation
- AutoTrac RowSense 2.0 activation
PC659258—UN—14JAN25

![[PC659258.png]]
**Figure PC659258** — A: AutoTrac Vision Camera (front view); B: AutoTrac Vision Camera (rear view)

PC631733—UN—30OCT24

![[PC631733.png]]
**Figure PC631733** — A: AutoTrac Vision Camera (front view); B: AutoTrac Vision Camera (rear view)

AutoTrac Vision Camera
- AutoTrac Vision cameras (A and B)
- ATX control unit (depending on machine make and model), updated to the latest firmware
NOTE: For more information, reference Value Selling Navigator or contact a John Deere dealer or other service provider.
- Digital wheel angle sensor
- G5 Display or newer with following:
- 24-2 software version or newer
- AutoTrac Guidance activation
- AutoTrac RowSense activation
- StarFire 7500 or newer receiver with following:
- 2.21P DTAC software or newer
- New terrain control module (TCM) calibration and TCM correction enabled
- SF-RTK or RTK activation
- Differential mode setting to SF-RTK or RTK
- StarFire differential source accuracy to reach SF-RTK or RTK accuracy.
- JDLink Modem
AutoTrac Vision is an enhancement to integrated AutoTrac. The vision camera system mounted to the machine looks for color differences between the crop and the ground to determine the location of the crop rows. Signals provided by the vision camera are integrated with existing AutoTrac signals to help keep the machine on rows. When there is no signal coming from the vision camera (for example, driving through a waterway), normal global positioning system (GPS) guidance applies if the operator has set up a guidance line.
Most other characteristics of AutoTrac remain unchanged. The vision camera is simply another position input for steering the machine. All tracking modes are set up the same way as they are with GPS-based AutoTrac.
NOTE: Refer to the G5 Display Operator’s Manual for more information.
Row Spacing Requirements:
- AutoTrac Vision supports row spacing of 51—102 cm (20—40 in).
- The maximum tire width in row crops is 38 cm (15 in) when operating in 76 cm (30 in) rows.
- Minimum crops height is 10 cm (4 in).
- Maximum canopy level is 90%.
- Curves are supported up to 50 m (164 ft) radius.
- The maximum speed on straight row crops must not exceed 35 km/h (22 mph).
- The maximum speed on slightly curved row crops must not exceed 19 km/h (12 mph).
- The maximum speed on strong curved row crops must not exceed 13 km/h (8 mph).
- Side slope must not exceed 6 degrees.
- Number of rows must be even.
- The camera should be free of water droplets.
- Wind speeds of up to 24 km/h (15 mph).
- Visibility of 50 m (165 ft) of row crops.
NOTE: Operating outside of these requirements may result in diminished performance.

> Source: OMKK105338 p. 140-6, 140-7, 140-8 · module bn55050,1742234626870-19-27OCT25
