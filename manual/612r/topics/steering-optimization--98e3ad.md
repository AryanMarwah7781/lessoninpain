---
module_id: CS12167,00009CB-19-17APR17
title: Steering Optimization
section: AutoTrac Tuning, AutoTrac RowSense, and AutoTrac Vision
page_labels:
- 140-5
- 140-6
pdf_pages:
- 816
- 817
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: settings
components:
- steering
- wheel
conditions: []
signal_words:
- NOTE
figures:
- PC16972
- PC16969
- PC16971
- PC16970
- PC16976
- PC16977
- PC16974
- PC16973
- PC16980
- PC16979
- PC16983
- PC16982
- PC16986
- PC16985
generic: false
title_inferred: false
parent_module_id: null
---

# Steering Optimization

Monitor Performance
Monitor performance shows heading error and tracking error. It is designed to aid in tuning of Advanced AutoTrac Settings. Heading error indicates relationship of machine direction relative to the current track. Tracking error displays the lateral error or offset relative to the current track.
PC16972—UN—22MAY13

![[PC16972.png]]
**Figure PC16972**

Heading Error Meter
Heading Error indicates relationship of machine direction relative to the current track. Heading Error should be within +/- 1 degree.
Adjust as needed if they are outside of this range.
PC16969—UN—22MAY13

![[PC16969.png]]
**Figure PC16969**

Tracking Error Meter
Tracking Error displays machine lateral error or offset relative to the current track. Arched bar graph value updates minimum and maximum Heading Error changes live during last 10 seconds.
NOTE: Steering Controller values are based on steering controls of machine.
Forward Steering Adjustments
PC16969—UN—22MAY13
Tracking Error
PC16971—UN—22MAY13

![[PC16971.png]]
**Figure PC16971**

Forward High Setting Icon
PC16970—UN—22MAY13

![[PC16970.png]]
**Figure PC16970**

Forward Low Setting Icon
Line Sensitivity Tracking
Determines how aggressively AutoTrac responds to off-track (lateral) error.
- Higher settings: Result in more aggressive response to machine off-track error.
- Lower settings: Result in less aggressive response to machine off-track error.
- Range: 50–200
PC16976—UN—22MAY13

![[PC16976.png]]
**Figure PC16976**

High Heading Lead
PC16977—UN—22MAY13

![[PC16977.png]]
**Figure PC16977**

Low Heading Lead
Heading Lead
Determines impact of yaw rate (machine rate of turn) on tracking performance. Heading lead acts as a look-ahead parameter and can be used to minimize over steering. Large adjustments may result in poor performance.
- Higher settings: Result in more aggressive response to yaw rate.
- Lower settings: Result in less aggressive response to yaw rate.
- Range: 50–130
PC16972—UN—22MAY13
Heading Error
PC16974—UN—22MAY13

![[PC16974.png]]
**Figure PC16974**

High Line Sensitivity Heading
PC16973—UN—22MAY13

![[PC16973.png]]
**Figure PC16973**

Low Line Sensitivity Heading
Line Sensitivity Heading
Determines how aggressively AutoTrac responds to Heading Errors.
- Higher settings: Result in more aggressive response to machine heading error.
- Lower settings: Result in less aggressive response to machine heading error.
- Range: 50–200
PC16980—UN—22MAY13

![[PC16980.png]]
**Figure PC16980**

High Steering Response Rate
PC16979—UN—22MAY13

![[PC16979.png]]
**Figure PC16979**

Low Steering Response Rate
Steering Response Rate
Adjusts rate of machine steering to maintain tracking performance. Increasing steering responsiveness generally results in better tracking performance.
- Higher settings: Result in better tracking performance, but may also cause increased wheel motion or jittery behavior.
- Lower settings: Result in decreased wheel motion, but may also result in worse tracking performance.
- Range: 50–200
PC16983—UN—22MAY13

![[PC16983.png]]
**Figure PC16983**

High Acquire Sensitivity
PC16982—UN—22MAY13

![[PC16982.png]]
**Figure PC16982**

Low Acquire Sensitivity
Acquire Sensitivity
Determines how aggressively machine acquires track. This setting only affects performance while acquiring track.
- Higher settings: Result in an aggressive line acquisition.
- Lower settings: Result in a smoother line acquisition.
- Range: 50–200
PC16986—UN—22MAY13

![[PC16986.png]]
**Figure PC16986**

High Curve Sensitivity
PC16985—UN—22MAY13

![[PC16985.png]]
**Figure PC16985**

Low Curve Sensitivity
Curve Sensitivity
Determines how aggressively AutoTrac responds to a curve in track. This setting affects performance in curve track guidance only.
- Higher settings: Turn machine in a smaller radius (tighter) around curve.
- Lower settings: Turn machine in a larger radius around curve.
- Range: 50–200

> Source: OMKK105338 p. 140-5, 140-6 · module CS12167,00009CB-19-17APR17
