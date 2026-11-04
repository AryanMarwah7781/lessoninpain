---
module_id: ch177nn,1737962575461-19-24NOV25
title: Sprayer AutoTrac Turn Automation
section: AutoTrac Tuning, AutoTrac RowSense, and AutoTrac Vision
page_labels:
- 140-9
- 140-10
- 140-11
pdf_pages:
- 820
- 821
- 822
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: settings
components:
- axle
- display
- steering
conditions: []
signal_words:
- IMPORTANT
- NOTE
figures:
- PC661530
- PC662153
- PC661535
- PC659264
- PC661529
- PC662154
generic: false
title_inferred: false
parent_module_id: null
---

# Sprayer AutoTrac Turn Automation

Requirements for Operation
Sprayer AutoTrac Turn Automation is available on following display types with Automation 4.0 or G5 Advanced License:
- 4640 Universal Display
- 4600 CommandCenter Display
- G5/ G5Plus Universal Display
- G5/G5Plus CommandCenter Display
Following track types are supported with Sprayer AutoTrac Turn Automation:
- Straight track
- AutoPath (rows)
- AutoPath (boundaries)
NOTE: During headland entry and field exit, the system shall set the Out of Crop flag to true at the headland intersection with the center of the front axle of the machine.
During headland exit and field entry, the system shall set the Out of Crop flag to false at the headland intersection with the center of the front axle of the machine.
Following functionalities are not available in Sprayer AutoTrac Turn Automation:
- Speed Control
- Sequence Setup
- Speed settings for in-field and turn speed
- AB Curves, Adaptive Curves, and Circles
Sprayer AutoTrac Turn Automation Settings
NOTE: When enabled, Sprayer AutoTrac Turn Automation moves to Ready state without speed control settings or sequence setup.
Turn Settings—Straight Track
PC661530—UN—29JAN25

![[PC661530.png]]
**Figure PC661530**

Turn Settings—Straight Track
Turn Size (A): Adjust the shape of the turn path. A smaller number will result in a smaller turn, and vice versa.
Start Turn (B): Adjust the turn path to begin before or after crossing the headland boundary.
Follow The Headland
PC662153—UN—17FEB25

![[PC662153.png]]
**Figure PC662153**

Follow The Headland
Follow the Headland is an advanced setting only available when using the Straight Track guidance mode.
PC661535—UN—02FEB25

![[PC661535.png]]
**Figure PC661535** — A: Follow The Headland ON; B: Follow The Headland OFF

Follow The Headland
When enabled, the machine follows the curvature of the headland where curves are present. When disabled, the machine follows the shortest (straight) path across the headland and does not follow the curvature if present. Follow the Headland is ON by default. The toggle selection is maintained across key cycles.
NOTE: Follow the Headland is only available when using the Straight Track guidance mode.
Turn Settings—AutoPath (Rows)
PC659264—UN—29JAN25

![[PC659264.png]]
**Figure PC659264**

Shift Row
When using AutoPath (rows), the Shift Row setting moves the specified row(s) from current AutoPath headland pass. Shift Row allows to choose the direction of shift (in or out) and the number of rows to move.
Turn Settings—AutoPath (Boundaries)
PC661529—UN—29JAN25

![[PC661529.png]]
**Figure PC661529**

Start Turn Offset
Start Turn Offset is the location where the machine begins its automated turn in relation to the AutoPath boundary track.
PC662154—UN—20FEB25

![[PC662154.png]]
**Figure PC662154** — A: AutoPath Boundary Track; B: Positive Offset; C: Negative Offset

Start Turn Offset
A positive offset (B) means the machine makes the turn after the AutoPath boundary track (A). A negative offset (C) means the turn is made before the AutoPath boundary track (A).
Start Turn Offset value range is +100 to -100 and is adjusted in increments of 0.3 m (1 ft).
Sprayer/Floater AutoTrac Turn Automation
Compatibility:
IMPORTANT: Reference Ag Sales manual for more information on compatibility: salesmanual.deere.com
Turn Patterns
Sprayer AutoTrac Turn Automation supports U-turns only.

> Source: OMKK105338 p. 140-9, 140-10, 140-11 · module ch177nn,1737962575461-19-24NOV25
