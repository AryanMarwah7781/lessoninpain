---
module_id: bn55050,1775501315148-19-27APR26
title: ExactApply | Nozzle Body
section: Nozzle System Application
page_labels:
- 25-G-34
- 25-G-35
pdf_pages:
- 195
- 196
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
- N148246D
- N147669
- WZ675762
- N125634C
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | Nozzle Body

N148246D—UN—22AUG25

![[N148246D.png]]
**Figure N148246D**

Nozzle Body Circuits
The Nozzle Body is the component that physically applies the product. The nozzle body has an internal control unit that is powered by 12 V. This allows communication to the domain controller using the Controller Area Network (CAN) protocol for system functionality and proper solenoid timing and control.
The nozzle body has eight external circuits that allow the system to function and communicate to the domain controller using harnessing and connectors:
N147669—UN—02JUN20

![[N147669.png]]
**Figure N147669**

Nozzle Body Circuits
PIN | Function
1 | Sync Out
2 | CAN Hi Out
3 | CAN Lo Out
4 | Ground
5 | Sync In
6 | CAN Hi In
7 | CAN Lo In
8 | Power (12V)
wz675762—UN—22AUG25

![[WZ675762.png]]
**Figure WZ675762**

ExactApply System Components
ExactApply System Components:
- A—Nozzle Body
- B—Domain Controller
- C—Relay
- D—Fuse
- E—CAN Terminator
- Red Wire—Power (12 V)
- Black Wire—Ground
- Blue Wire—Sync Circuit
- Yellow Wire—CAN Hi Circuit
- Green Wire—CAN Lo Circuit
N125634C—UN—24APR26

![[N125634C.png]]
**Figure N125634C**

Nozzle Body Lighting
Each nozzle body is integrated with a light. When set to manual mode, Nozzle Body Lighting can be used to troubleshoot issues. Nozzle body lighting settings can be accessed from the Advanced Settings page of the Boom application.

> Source: OMKK105338 p. 25-G-34, 25-G-35 · module bn55050,1775501315148-19-27APR26
