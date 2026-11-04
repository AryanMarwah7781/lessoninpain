---
module_id: bn55050,1775501548883-19-27APR26
title: ExactApply | Sync Signal Missing
section: Nozzle System Application
page_labels:
- 25-G-36
- 25-G-37
pdf_pages:
- 197
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
- N147988C
- N147986C
- N147987C
generic: false
title_inferred: false
parent_module_id: null
---

# ExactApply | Sync Signal Missing

Sync Signal Missing indicates that the faulted Nozzle Body is not receiving the 15-Hz heartbeat signal from the adjacent nozzle body inboard.
NOTE: NOTE: For more information on the function and operation of the sync circuit, refer to ExactApply | Sync Circuit.
Missing sync signal is typically caused by faulty nozzle body or an issue with the wiring harness. Sync circuit faults are usually indicated by a nozzle body either not receiving a sync signal (input) or not sending a sync signal (output).
Missing Sync Signal Scenarios:
N147988C—UN—26JUN25

![[N147988C.png]]
**Figure N147988C**

Failed Input
- The nozzle body reporting the error has a failed input internally.
N147986C—UN—26JUN25

![[N147986C.png]]
**Figure N147986C**

Failed Output
- The nozzle body directly inboard from the nozzle body reporting the error has a failed output internally.
N147987C—UN—26JUN25

![[N147987C.png]]
**Figure N147987C**

Failed Circuit
- There is a failed circuit or circuit component between the nozzle body reporting the error and the nozzle body directly inboard.
NOTE: See Image Icons for explanations of the icons found within certain images.
Missing sync signal usually triggers diagnostic trouble code (DTC) 1668.11, 1669.11, 1670.11, or 1671.11. The DTC that gets triggered depends on which Subnet the fault is located on.
When this failure occurs, and no other failures are active, the machine will continue to function and spray. Once the machine is turned off and restarted, the issue may change to a Nozzle Addressing Failure with the additional nozzles on the Subnet reporting as faulted. This requires troubleshooting of the Sync Circuit to regain proper function of the system.
Determine the location of the fault using the Nozzle Turret | Status screen in the Nozzle System display application. Start by troubleshooting the sync circuit at the fault location that is closest to the center of the machine.
NOTE: For more information on circuit locations, See ExactApply | Nozzle Body.

> Source: OMKK105338 p. 25-G-36, 25-G-37 · module bn55050,1775501548883-19-27APR26
