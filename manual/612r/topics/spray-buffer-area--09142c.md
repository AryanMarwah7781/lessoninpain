---
module_id: as09261,1668097103203-19-23MAR26
title: Spray Buffer Area
section: See & Spray (If Equipped)
page_labels:
- 135-7
pdf_pages:
- 773
models:
- all
options:
- See & Spray
engine_tier: null
topic_type: procedure
components:
- nozzle
conditions:
- wind
signal_words:
- NOTE
figures:
- NX1451621
- NX1451622
generic: false
title_inferred: false
parent_module_id: null
---

# Spray Buffer Area

NX1451621—UN—20MAR26

![[NX1451621.png]]
**Figure NX1451621** — A: Spray Buffer Area

1. Go to Menu > Machine Settings Tab > See & Spray.
2. Select spray buffer area (A).
NX1451622—UN—20MAR26

![[NX1451622.png]]
**Figure NX1451622**

This setting adjusts the minimum spray length the system applies when a green object is detected.
NOTE: The system uses inputs such as nozzle speed and desired buffer setting to determine when the nozzle starts and stops spraying. This relates to the minimum time in milliseconds that an enabled command is sent to the nozzle. This setting correlates to linear distance.
It is recommended to increase the buffer length when operating at varying speeds, if accelerating and decelerating often, or if operating outside the ideal 30—50 psi spray pressure setting.
If another target is detected during the time an ON command is currently active, the command extends the minimum spray length.
For best results, select Large when operating in windy conditions or at higher boom heights.

> Source: OMKK105338 p. 135-7 · module as09261,1668097103203-19-23MAR26
