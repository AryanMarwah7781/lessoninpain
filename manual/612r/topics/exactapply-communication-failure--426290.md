---
module_id: bn55050,1775501276850-19-27APR26
title: ExactApply | Communication Failure
section: Nozzle System Application
page_labels:
- 25-G-33
pdf_pages:
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
- N147527D
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | Communication Failure

Communication Failure indicates that at least one Nozzle Body on the Subnet is not communicating to the domain controller by means of the Controller Area Network (CAN). The nozzle bodies communicate on the subnet using the CAN Hi and CAN Lo circuits.
This failure can only occur if the machine powers up and is functioning correctly. Then, the properly addressed and functioning nozzle body on a subnet loses power, ground, or CAN communication.
N147527D—UN—26AUG25

![[N147527D.png]]
**Figure N147527D**

CAN Communication Issue
If the issue is CAN communication, all nozzle bodies outboard from the site of failure on the subnet will also lose communication or show as faulted.
NOTE: See Image Icons for explanations of the icons found within certain images.
If power or ground to the nozzle body is lost, the other nozzle bodies can remain in communication with the domain controller. Refer to Power and Ground for more information.
NOTE: For more information on circuit locations, see ExactApply | Nozzle Body.

> Source: OMKK105338 p. 25-G-33 · module bn55050,1775501276850-19-27APR26
