---
module_id: bn55050,1775500327022-19-27APR26
title: Nozzle Controller | Status
section: Nozzle System Application
page_labels:
- 25-G-5
- 25-G-6
pdf_pages:
- 166
- 167
models:
- all
options: []
engine_tier: null
topic_type: display_ui
components:
- nozzle
conditions: []
signal_words:
- NOTE
figures:
- N118420
- N118022
- N118025
- N118026
- A99030
generic: false
title_inferred: false
parent_module_id: null
---

# Nozzle Controller | Status

The Nozzle Controller | Status page displays the status of the selected nozzle controller and provides additional information when a fault is detected.
NOTE: For more information on how to locate a faulted nozzle on the boom, see Determining Nozzle Location.
Available Nozzle Statuses:
NOTE: For further information on how to diagnose ExactApply issues, see ExactApply | Troubleshooting.
N118420—UN—02NOV16

![[N118420.png]]
**Figure N118420**

OK
OK— indicates that there are no faults or flow errors within the nozzle controllers.
N118022—UN—13JAN17

![[N118022.png]]
**Figure N118022**

Faults Detected
Faults Detected— indicates an electrical fault or a flow error within a nozzle controller.
N118025—UN—09MAR16

![[N118025.png]]
**Figure N118025**

Checkmark
Checkmark— indicates a normal state for the nozzle controller.
N118026—UN—30NOV16

![[N118026.png]]
**Figure N118026**

Exclamation Point
Exclamation Point— indicates a fault condition within the nozzle controller.
Fault Conditions:
- Low voltage detected.
- Sync fault detected.
- Missing controller detected.
- Solenoid high current detected.
- Solenoid low current detected.
- Solenoid sticking detected.
Items Accessible on Nozzle Controller | Status Page:
A99030—UN—20MAR18

![[A99030.png]]
**Figure A99030**

Diagnostic Readings
Diagnostic Readings— select to access more information about the nozzle controller being viewed.

> Source: OMKK105338 p. 25-G-5, 25-G-6 · module bn55050,1775500327022-19-27APR26
