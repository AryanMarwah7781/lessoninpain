---
module_id: bn55050,1775501494465-19-27APR26
title: ExactApply | Nozzle Body Pass-Through
section: Nozzle System Application
page_labels:
- 25-G-35
pdf_pages:
- 196
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
- N147768D
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | Nozzle Body Pass-Through

If a nozzle body loses power, controller area network (CAN) information from the other nozzle bodies remain in communication with the domain controller. This is referred to as nozzle body pass-through.
n147768d—UN—25AUG25

![[N147768D.png]]
**Figure N147768D**

Nozzle Body Pass-Through
NOTE: See Image Icons for explanations of the icons found within certain images.
Example of Nozzle Body Pass-Through:
1.Nozzle body number 1 functions properly.
2.Nozzle body number 2 loses power. CAN communication still passes through.
3.Nozzle body number 3 functions properly because CAN communication continues through faulted nozzle body number 2.
NOTE: Nozzle 3 will have an active error message (Sync Signal Missing) but will still function properly.
If a nozzle body is disconnected, it will not be able to pass CAN communication messages to downstream nozzle bodies.

> Source: OMKK105338 p. 25-G-35 · module bn55050,1775501494465-19-27APR26
