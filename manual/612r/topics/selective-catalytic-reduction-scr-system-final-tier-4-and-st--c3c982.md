---
module_id: ouo6092,1741962082679-19-27OCT25
title: Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)
section: Operate the Machine
page_labels:
- 50-13
- 50-14
pdf_pages:
- 348
- 349
models:
- all
options: []
engine_tier: Interim Tier 4
topic_type: safety
components:
- aftertreatment
- def system
- engine
conditions:
- temperature
signal_words:
- IMPORTANT
- NOTE
figures:
- NX1396835
generic: false
title_inferred: false
parent_module_id: null
---

# Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)

IMPORTANT: It is unlawful to tamper with or remove any component of the aftertreatment system. It is also unlawful to use diesel exhaust fluid (DEF) that does not meet the specifications provided or to operate the vehicle with no DEF.
Using incorrect or unapproved aftertreatment components can damage the vehicle’s aftertreatment system and reduce ability of the aftertreatment system to function correctly. Never interchange aftertreatment components between Interim Tier 4/Stage III B and Final Tier 4/Stage V equipped vehicles.
NOTE: SCR system monitors quality of DEF flowing through it. If a fluid other than DEF at correct urea concentration is detected, system displays a diagnostic trouble code and engine derates to 50% power.
SCR system supplies DEF to the engine aftertreatment system. DEF works in conjunction with machine aftertreatment components to reduce emissions. See Fuel, Lubricants, and Coolants section in this manual for specifications and information about DEF.
NX1396835—UN—18MAR25

![[NX1396835.png]]
**Figure NX1396835** — A: DEF Level Gauge; B: DEF Icon

Machine electronic systems monitor DEF level to assure proper performance. DEF level gauge (A) on the corner post display shows current DEF level. Refilling DEF tank every time machine is refueled is recommended. See Fill Diesel Exhaust Fluid (DEF) Tank (Final Tier 4/Stage V) in Prestarting Checks section of this manual.
DEF level and operation changes:
Normal Operation—When DEF level is within normal operation range , DEF icon (B) is on and the machine operates normally. Always maintain fill within this range for uninterrupted performance.
Low DEF Level 1—When the level reaches 10%, the level indicator flashes, alarm sounds, and the low fluid message appears.
Low DEF Level 2—When the level reaches 0%, level indicator illuminates and stops flashing, alarm sounds, and empty fluid message and engine power limited message appears.
DEF Tank Empty—When loss of prime is reached, level indicator illuminates and stops flashing. Alarm sounds and empty fluid message, engine power limited message, and speed limited mesage appears. Stop engine warning indicator (Red) illuminates, engine is derated and machine functions are restricted.
DEF freezes at -11°C (12°F) and will not flow to the SCR system. Machine systems sense low temperature and allow engine to start, even with no DEF flow. Engine coolant is used to thaw fluid in the DEF tank when engine is running. If system senses that DEF has thawed and SCR system is operating normally within 60 to 90 minutes, machine operates normally. If DEF flow is not sensed within 60 to 90 minutes, FAIL TO THAW DTC is displayed. Machine is allowed to operate normally for 4 hours after DTC is displayed. If DEF flow is not sufficient after 4 hours, engine power will be reduced to 50% until DEF flow is achieved. Freezing and thawing of DEF does not degrade it.
If desired, locking DEF tank cap and strainer/screen kits are available via regular spare part channels.

> Source: OMKK105338 p. 50-13, 50-14 · module ouo6092,1741962082679-19-27OCT25
