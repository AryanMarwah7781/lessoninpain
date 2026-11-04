---
module_id: ouo6092,1776448050606-19-28APR26
title: BoomTrac Settings | Sensor Target Mode
section: BoomTrac Performance and Optimization
page_labels:
- 155-2
- 155-3
pdf_pages:
- 840
- 841
models:
- all
options:
- BoomTrac
engine_tier: null
topic_type: procedure
components:
- boom
- boom height
conditions: []
signal_words: []
figures:
- NX1458210
- NX1458211
- NX1458215
- NX1458219
- NX1458225
- NX1458228
- NX1458231
- NX1458234
- NX1458236
generic: false
title_inferred: false
parent_module_id: null
---

# BoomTrac Settings | Sensor Target Mode

The BoomTrac system automatically controls boom tilt functions and center frame control relative to contours of the ground or crop canopy.
Boom Sensors—How they work:
The boom height sensors are ultrasonic sensors that emit a sound pulse, then listen for the return echo as the pulse reflects off surfaces below the boom. The first reflection received is used as the canopy signal, as the canopy is expected to be the closest object to the boom. The last reflection received is referred to as the ground signal. In situations where there is no canopy, the ground and canopy signals are likely to be the same.
NX1458210—UN—21APR26

![[NX1458210.png]]
**Figure NX1458210** — A: Sensor Target box

Boom System
1. To change sensor target select the Sensor Target box (A).
NX1458211—UN—21APR26

![[NX1458211.png]]
**Figure NX1458211** — A: Ground; B: Ground with Canopy Assist; C: Canopy

Sensor Target
2. Select from Ground (A), Ground with Canopy Assist (B), or Canopy (C).
Ground
NX1458215—UN—21APR26

![[NX1458215.png]]
**Figure NX1458215**

NX1458219—UN—21APR26

![[NX1458219.png]]
**Figure NX1458219**

Ground Setting Examples
When to use:
- Operating in fallow ground or fields with less than 30% canopy coverage.
Description of Mode:
- Ground mode prioritizes sensing the soil surface, which provides the most accurate boom height control when crop canopy is minimal.
If excessive crop canopy is present where the height sensor cannot always get a ground reading, it can cause the boom height control to jump back and forth from a canopy to ground reading and cause erratic performance.
Ground with Canopy Assist
NX1458225—UN—21APR26

![[NX1458225.png]]
**Figure NX1458225**

NX1458228—UN—21APR26

![[NX1458228.png]]
**Figure NX1458228**

NX1458231—UN—21APR26

![[NX1458231.png]]
**Figure NX1458231**

Ground with Canopy Assist Setting Example
When to use:
- Working in fields with 30–60% canopy coverage. This setting is also recommended when excessive crop debris such as corn stubble remains in the field (see above images).
Description of Mode:
- This mode blends ground and canopy sensing, helping maintain consistent boom height as crop canopy begins to interfere with ground sensors.
Canopy
NX1458234—UN—21APR26

![[NX1458234.png]]
**Figure NX1458234**

NX1458236—UN—21APR26

![[NX1458236.png]]
**Figure NX1458236**

Canopy Examples
When to use:
- Operating in fields with 60% or more of canopy coverage.
Description of Mode:
- This mode relies primarily on canopy sensing, which is critical when dense crop cover prevents accurate ground detection. When operating in crops, a boom heigh sensor will typically detect both the distance to the ground and to the crop. Using the Canopy setting, the boom height control software filters out the further of the two readings (distance to ground) and relies on the closer of the two readings (distance crop) to set the boom height.

> Source: OMKK105338 p. 155-2, 155-3 · module ouo6092,1776448050606-19-28APR26
