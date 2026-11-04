---
module_id: bn55050,1775501219712-19-27APR26
title: ExactApply | CAN Communication
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
- electrical system
- nozzle
conditions: []
signal_words: []
figures:
- WZ675764
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | CAN Communication

wz675764—UN—22AUG25

![[WZ675764.png]]
**Figure WZ675764**

CAN Bus Components
The Controller Area Network (CAN) Communication circuit is a two-wire passive series circuit that allows the Nozzle Bodies on the Subnets to communicate with the domain controller. In other words, CAN communication begins at the domain controller and goes from the first nozzle body and continues to the downstream nozzle bodies one after another.
Each nozzle body (A) has three sets of circuits: power (red) and ground (black), controller area network (CAN) binary unit system (bus) hi circuit (yellow) and lo circuit (green), and the sync circuit (blue). All of the ExactApply system circuits start at the domain controller (B).
The CAN bus circuits on each domain controller end with a set of CAN terminators (C). The CAN bus high circuit has one terminator and the CAN bus low circuit has a second terminator.
Select a Component or Function for Additional Information:
- Nozzle Body— provides more information about the harness connector wiring.
- Sync Circuit— a series circuit that synchronizes the nozzle bodies and spraying at the proper time.
- Nozzle Body Pass-Through— CAN information goes from one nozzle body to any nozzle bodies downstream of it that are on the same subnet.
- CAN Communication Failure— because the nozzle bodies are in series, a fault with one nozzle body may cause faults or lose communication with other nozzle bodies on the same subnet that are downstream from the nozzle body with a legitimate fault.
- CAN Bus Disabled— the domain controller may disable an entire subnet if a CAN binary unit system (bus) error is detected.
- Power and Ground— unlike the CAN bus and sync circuits, the power and ground circuits run in parallel and go to each nozzle body. Even if power or ground to the nozzle body is lost, the other nozzle bodies remain in communication with the domain controller.

> Source: OMKK105338 p. 25-G-32 · module bn55050,1775501219712-19-27APR26
