---
module_id: ouo6092,1776103538605-19-16APR26
title: Boom Charge
section: Spray System Application
page_labels:
- 25-I-10
- 25-I-11
pdf_pages:
- 220
- 221
models:
- all
options: []
engine_tier: null
topic_type: display_ui
components:
- boom
- nozzle
conditions: []
signal_words: []
figures:
- NX1453160
- NX1453161
- NX1453162
generic: false
title_inferred: false
parent_module_id: null
---

# Boom Charge

Boom Charge pressurizes the boom plumbing to a preset value for 3 seconds after the Spray System Master switch is pressed ON. This compresses any air in the boom to ensure that the nozzles are spraying at the desired rate as soon as possible.
Modify When:
- Spraying under normal operating conditions. Change the Boom Charge setting to AUTO.
- Using section control. Change the Boom Charge setting to AUTO.
- Troubleshooting irregular application rates, such as when rates and speeds vary drastically at headlands. Change the Boom Charge setting to MANUAL.
- Lower rates are desired when leaving headlands or crossing interior boundaries. Change the Boom Charge setting to OFF.
Items Accessible on Boom Charge Page:
NX1453160—UN—13APR26

![[NX1453160.png]]
**Figure NX1453160**

Auto
Auto—allows the system to charge the boom at an automatically predetermined pressure and flow. This is calculated by the control unit based on the previous speed, boom section width, and flow rate output with the Spray System Master switch OFF.
It also allows the system to operate on a pressure-based application rate control versus a flow-based rate below 56.8 L/min (15 gal/min). This allows the spray rate control system to reach the target application rate faster when smaller flow rate nozzles are used.
NX1453161—UN—13APR26

![[NX1453161.png]]
**Figure NX1453161**

Manual
Manual—allows the system to charge the boom for 3 seconds after the Spray System Master switch is pressed ON. After 3 seconds, the automatic rate control system will take over. When manual boom charge is enabled, the manual target pressure setting is used. Manual target pressure can adjusted on the Target Rate/Rx page.
Using manual boom charge may cause over or under application if the manual target pressure is not equal to spray speed after headland turns.
NX1453162—UN—13APR26

![[NX1453162.png]]
**Figure NX1453162**

OFF
OFF—boom charge feature is disabled. The system will return to the target rate or target pressure when the Spray System Master switch is ON. You may experience a longer delay reaching your target rate when boom charge is OFF.

> Source: OMKK105338 p. 25-I-10, 25-I-11 · module ouo6092,1776103538605-19-16APR26
