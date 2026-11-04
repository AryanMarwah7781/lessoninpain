---
module_id: bn55050,1775501532586-19-27APR26
title: ExactApply | Sync Circuit
section: Nozzle System Application
page_labels:
- 25-G-35
- 25-G-36
pdf_pages:
- 196
- 197
models:
- all
options:
- ExactApply
engine_tier: null
topic_type: display_ui
components:
- boom
- nozzle
conditions: []
signal_words:
- NOTE
figures:
- WZ675765
- N148180D
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | Sync Circuit

The sync circuit, also known as the heartbeat function, keeps all of the nozzle bodies on the entire boom synchronized and spraying at the proper time. The sync circuit is a series circuit that establishes the Nozzle Bodies' physical locations on the boom. The system goes into sync after Addressing is complete. Unlike the Controller Area Network (CAN) circuit, this sync circuit is not a pass-through circuit.
wz675765—UN—22AUG25

![[WZ675765.png]]
**Figure WZ675765**

Sync Circuit
This 15-Hz sync signal (A) originates from the domain controller (B) and is sent to the first nozzle body (C) on each Subnet. It is then passed in-series to each nozzle body outboard on that subnet. A different frequency is used for each nozzle body.
NOTE: For more information about how nozzle bodies address along the boom, refer to Nozzle Addressing Failure.
The sync circuit has two functions:
- Addressing Function— allows the nozzle bodies to report their physical position across the boom. This occurs when the ignition key is turned on.
- Heartbeat Function— keeps the nozzle bodies spraying at the proper time across the boom.
Initial Key-On Example:
N148180D—UN—26AUG25

![[N148180D.png]]
**Figure N148180D**

Effect of Failed Sync Circuit
A nozzle body has a sync circuit failure. When the machine is powered on, the sync circuit is now broken at that nozzle body. This acts the same as if the Sync Out circuit wire was not plugged into that nozzle body. This will result in the remainder of the nozzle bodies on the subnet to be faulted outboard from the location of the issue.
NOTE: See Image Icons for explanations of the icons found within certain images.

> Source: OMKK105338 p. 25-G-35, 25-G-36 · module bn55050,1775501532586-19-27APR26
