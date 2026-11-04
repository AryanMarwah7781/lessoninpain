---
module_id: bn55050,1775501295428-19-27APR26
title: ExactApply | Nozzle Addressing Failure
section: Nozzle System Application
page_labels:
- 25-G-33
- 25-G-34
pdf_pages:
- 194
- 195
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
- N147993D
- WZ675766
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | Nozzle Addressing Failure

Nozzle Addressing Failure indicates that one or more Nozzle Bodies did not complete the Addressing Process when the ignition key was turned on.
When the ignition key is turned on initially, the system must determine the physical location of each nozzle body on the boom using the following sequence:
N147993D—UN—26AUG25

![[N147993D.png]]
**Figure N147993D**

Nozzle Addressing Sequence
1.The addressing process begins by sending a frequency signal (A) from the domain controller (B) to the first nozzle body (C) on the Subnet by means of the Sync Line Circuit.
2.The nozzle body then reports its location back to the domain controller by means of the Controller Area Network (CAN).
3.Once the first nozzle body establishes its proper location on that respective subnet of the boom, it sends a different frequency (D) to the next nozzle body (E). This allows the second nozzle body on the subnet to establish its location and report back to the domain controller using the CAN.
4.This process repeats until all nozzle bodies on the subnet have established their location.
If a nozzle body does not have power, ground, CAN, or Sync, it and the remaining nozzle bodies on that subnet cannot establish their location. A fault will trigger if too many or too few nozzle bodies report on a subnet. The domain controller knows how many nozzles must report back a claimed location on the subnet.
wz675766—UN—22AUG25

![[WZ675766.png]]
**Figure WZ675766**

Nozzle Body Lighting
1.To determine if an issue is related to the sync circuit or the power, ground, or CAN circuits, set the Nozzle Body Lighting mode to manual. Faulted nozzle bodies that remain illuminated indicate an issue with the Sync Circuit. Faulted nozzle bodies that are not illuminated indicate an issue with the CAN Bus, Power, or Ground circuits.
NOTE: For more information on circuit locations, see ExactApply | Nozzle Body.

> Source: OMKK105338 p. 25-G-33, 25-G-34 · module bn55050,1775501295428-19-27APR26
