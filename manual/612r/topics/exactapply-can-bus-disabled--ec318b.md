---
module_id: bn55050,1775501259968-19-27APR26
title: ExactApply | CAN Bus Disabled
section: Nozzle System Application
page_labels:
- 25-G-32
- 25-G-33
pdf_pages:
- 193
- 194
models:
- all
options:
- ExactApply
engine_tier: null
topic_type: display_ui
components:
- nozzle
conditions: []
signal_words:
- NOTE
figures:
- N148181D
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | CAN Bus Disabled

CAN Bus Disabled indicates that a Controller Area Network (CAN) bus error was detected by the domain controller and has disabled the Subnet.
N148181D—UN—26AUG25

![[N148181D.png]]
**Figure N148181D**

CAN Bus Disabled
This fault will show the entire subnet as faulted. The subnet has a failure that does not allow CAN communication. The controller identifies this and disables the subnet. This can be caused by one or more of the following:
- Failed terminator
- Internal Nozzle Body failure
- CAN circuit short
NOTE: For more information on circuit locations, see ExactApply | Nozzle Body.

> Source: OMKK105338 p. 25-G-32, 25-G-33 · module bn55050,1775501259968-19-27APR26
