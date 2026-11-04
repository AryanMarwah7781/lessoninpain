---
module_id: bn55050,1775501244896-19-27APR26
title: ExactApply | Addressing
section: Nozzle System Application
page_labels:
- 25-G-32
pdf_pages:
- 193
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
signal_words: []
figures:
- N147715D
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | Addressing

Addressing establishes the location of each Nozzle Body when the ignition key is turned on. The system goes into sync after addressing is complete. Sync keeps the entire boom on the same “time clock” or in sync.
N147715D—UN—26AUG25

![[N147715D.png]]
**Figure N147715D**

Addressing
The addressing process happens on each Subnet. The signal sent on this circuit originates from the domain controller and passes to the first nozzle body on the subnet which is closest to center of the machine. It then passes from nozzle body to nozzle body outboard to the end of the subnet.

> Source: OMKK105338 p. 25-G-32 · module bn55050,1775501244896-19-27APR26
