---
module_id: bn55050,1775501179731-19-27APR26
title: ExactApply | System Overview
section: Nozzle System Application
page_labels:
- 25-G-31
- 25-G-32
pdf_pages:
- 192
- 193
models:
- all
options:
- ExactApply
engine_tier: null
topic_type: display_ui
components:
- electrical system
- nozzle
conditions: []
signal_words: []
figures:
- WZ675762
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | System Overview

ExactApply | System Overview provides information on the components and functions that make up the ExactApply system.
wz675762—UN—22AUG25

![[WZ675762.png]]
**Figure WZ675762**

ExactApply Components
Each nozzle body (A) has three sets of circuits: power (red) and ground (black), controller area network (CAN) binary unit system (bus) high circuit (yellow) and low circuit (green), and the sync circuit (blue). All of the ExactApply system circuits start at the domain controller (B).
Power and ground circuits are in parallel to each nozzle body. Before reaching the nozzle bodies, power starts at the domain controller and goes to a relay (C) and then through a fuse (D). Each subnet has a separate ground circuit and fuse.
The CAN bus and sync circuits are in series and go from one nozzle body to the next. The CAN bus circuit for each domain controller end with CAN terminators (E).
Select a Component or Function for Additional Information:
ExactApply— is a system consisting of a domain controller communicating with nozzle bodies across four different subnets.
Nozzle Body— is the component that physically applies the product.
Subnets— are a subdivision of the ExactApply communication network.
CAN Communication— is an electronic system that allows the subnets to communicate with the domain controller.
Sync Circuit— is an electronic system that determines the physical location of the nozzle bodies on the boom through addressing mode. The sync circuit also has a second function called the heartbeat function.
Power and Ground—is the electrical circuit that provides 12 V from the domain controllers to the nozzle bodies.

> Source: OMKK105338 p. 25-G-31, 25-G-32 · module bn55050,1775501179731-19-27APR26
