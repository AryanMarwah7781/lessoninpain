---
module_id: ouo6092,1776798312210-19-30APR26
title: AutoTrac Performance and Tuning
section: AutoTrac Tuning, AutoTrac RowSense, and AutoTrac Vision
page_labels:
- 140-14
- 140-15
- 140-16
- 140-17
- 140-18
pdf_pages:
- 825
- 826
- 827
- 828
- 829
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: procedure
components:
- boom
- grease points
- spray tip
- steering
- suspension
- tire
- wheel
conditions:
- road transport
signal_words:
- IMPORTANT
- NOTE
figures:
- NX1458672
- NX1458673
- NX1458674
- NX1458675
- NX1458679
- NX1432684
- NX1458680
- NX1458681
- NX1458682
- NX1458683
- NX1458676
- NX1458677
- NX1458678
generic: false
title_inferred: false
parent_module_id: null
---

# AutoTrac Performance and Tuning

This procedure should be used when Autotrac is not performing as expected. Performance examples include:
- The machine may lag behind the intended guidance path or take longer than expected to establish tracking.
- Steering response may appear overly sensitive or oscillatory while following the guidance path.
- After encountering field disturbances (such as waterways, terraces, or uneven ground), the machine may require additional time to re-establish accurate tracking.
- At higher operating speeds, or in loose, sandy soils and rolling terrain, the machine may exhibit lateral oscillation, S-ing or off track error.
NOTE: After completing each step, it is recommended to check AutoTrac function and performance before continuing to the next step.
1. Restore defaults and verify tire configuration.
NX1458672—UN—24APR26

![[NX1458672.png]]
**Figure NX1458672** — A: Steering Wheel Icon

AutoTrac Steering Optimization a. Navigate to Menu > Applications (left side of screen) > AutoTrac Guidance > Click on the header “AutoTrac Guidance” > Settings.
b. Click steering wheel icon (A) next to AutoTrac Steering Optimization.
NX1458673—UN—24APR26

![[NX1458673.png]]
**Figure NX1458673** — A: Row Crop (Narrow); B: Float (Wide); C: OK Button

Select Tire Type c. Selec Row Crop (A) or Float (B) type of tire on machine.
d. Select OK button (C) to save selection.
NX1458674—UN—24APR26

![[NX1458674.png]]
**Figure NX1458674** — A: Restore Factory Defaults Tab

Steering Optimization e. Navigate to the Steering optimization page and select Restore Factory Defaults tab (A).
NX1458675—UN—24APR26

![[NX1458675.png]]
**Figure NX1458675** — A: Restore Defaults Button

Steering Optimization f. Select Restore Defaults button (A).
g. Check AutoTrac function and performance before continuing to the next step.
2. Lubricate steering and suspension.
IMPORTANT: Use only John Deere SD Polyurea grease for lubricating suspension and steering components. Use of other greases in the suspension system is not recommended. Use of other greases can result in premature wear of the suspension components.
NOTE: Verify spindles and suspension have been properly lubricated. Sticking spindles and suspension can negatively impact AutoTrac performance and result in over-correction.
NX1458679—UN—27APR26

![[NX1458679.png]]
**Figure NX1458679** — A: Grease Fitting (2 used)

Fitting Locations a. Lubricate spindle housing grease fittings (A)
using John Deere SD Polyurea grease.
NX1432684—UN—25NOV25

![[NX1432684.png]]
**Figure NX1432684** — A: Grease Fitting (4 used)

400R, 408R, 410R, and 412R Suspension Grease Bank
NX1458680—UN—24APR26

![[NX1458680.png]]
**Figure NX1458680** — A: Grease Fitting (4 used)

600R, 612R, and 616R Grease Fitting Locations b. Lubricate the front and rear suspension assemblies with ONLY John Deere SD Polyurea grease. Use five pumps of grease at each grease fitting (A).
c. Check AutoTrac function and performance before continuing to the next step.
3. Check boom alignment and gap adjustment.
NX1458681—UN—27APR26

![[NX1458681.png]]
**Figure NX1458681** — A: Suspended Center Frame; B: Wear Pad; C: Gap

Gap Location a. Completely unfold the booms and lower them to provide access for inspecting the center frame.
NOTE: If a gap is observed, excessive boom movement may occur, which can reduce guidance system tracking performance.
b. Verify the suspended center frame (A) contacts the wear pad (B) on the fixed center frame. When properly adjusted, no visible gap (C) should be present at this interface.
NOTE: To adjust this gap, the booms can be adjusted slightly forward by lengthening the inner fold cylinders.
NX1458682—UN—27APR26

![[NX1458682.png]]
**Figure NX1458682** — A: Cap Screw (2 used); B: Cylinder Rod; C: Location

Cylinder c. If gap is present, loosen cap screws (A) on the yokes at the end of the inner fold cylinders.
NOTE: Adjust the left and right cylinder equally. More threads showing at location (C) means you are extending the cylinder.
d. Turn cylinder rod (B) to adjust. Extending the cylinders approximately 3 mm (1/8 in) will help position the booms tips forward and shift the center frame center of gravity forward eliminating the gap.
NX1458683—UN—27APR26

![[NX1458683.png]]
**Figure NX1458683** — A: 1001 Front Steer Calibration

Adjust to Position Boom Tips Forward
e. Check gap and extend fold cylinder evenly on both sides until light contact is maintained with the wear pads.
f. Tighten the cap screws.
g. Check AutoTrac function and performance before continuing to the next step.
4. Perform AutoTrac Valve Calibration.
NOTE: To perform this calibration, you will need a large open area as the sprayer will be driving forward while turning left and right.
NX1458676—UN—24APR26

![[NX1458676.png]]
**Figure NX1458676**

Routines a. Navigate to the calibration following Menu > System > Diagnostics Center > Controllers > AutoTrac Controller (ATX.001) > Routines > 1001 Front Steer Calibration.
b. Select 1001 Front Steer Calibration (A).
NX1458677—UN—24APR26

![[NX1458677.png]]
**Figure NX1458677** — A: 1102 - Rear Steer Calibration

Routines c. If equipped with four-wheel steer, perform the
1102 - Rear Steer Calibration (A) after completing the front steer calibration.
d. Once complete, drive the sprayer as straight as possible for 0.4 km (1/4 mi) to 0.8 km (1/2 mi). This can be done on a straight road or through a field. The purpose of driving the machine straight is that the machine will automatically re-calibrate the wheel angle sensor bias in the background.
e. Check AutoTrac function and performance before continuing to the next step.
5. Update Software.
NX1458678—UN—24APR26

![[NX1458678.png]]
**Figure NX1458678** — A: Hydro Handle Calibration

Calibrations a. Ensure the AutoTrac™controller (ATX), Gen 5
Display, and power train (POD) software are updated to the latest approved versions. Software updates may be performed using Operations Center™Pro Service or by contacting an authorized dealer or independent repair shop to verify and apply updates to the machine.
b. After software is updated, navigate to Menu > Machine Settings > Calibrations & Procedures > Machine and select the Hydro Handle Calibration (A).
c. After completing the calibration, check AutoTrac function and performance.

> Source: OMKK105338 p. 140-14, 140-15, 140-16, 140-17, 140-18 · module ouo6092,1776798312210-19-30APR26
