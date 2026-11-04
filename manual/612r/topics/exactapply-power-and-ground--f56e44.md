---
module_id: bn55050,1775501565680-19-27APR26
title: ExactApply | Power and Ground
section: Nozzle System Application
page_labels:
- 25-G-37
pdf_pages:
- 198
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
signal_words:
- NOTE
figures:
- WZ675767
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | Power and Ground

Power and Ground circuit provides 12 V to the domain controllers and nozzle bodies. The power and ground circuit is a parallel circuit and runs to each nozzle body.
wz675767—UN—22AUG25

![[WZ675767.png]]
**Figure WZ675767**

Power and Ground Circuits
Starting at the battery (A), power goes to the domain controller (B). The domain controller sends 12 V to a relay (C) which then feeds the each nozzle body (D). Each power circuit is protected by a fuse (E).
Depending on the location on the wiring harness, a power (red) or ground (black) issue can result in a single faulted nozzle body or a bank of faulted nozzle bodies. Check for fuse failure. (See Fuse Locations in the Maintenance section of the Operator's Manual.)
NOTE: For more information on circuit locations, see ExactApply | Nozzle Body.

> Source: OMKK105338 p. 25-G-37 · module bn55050,1775501565680-19-27APR26
