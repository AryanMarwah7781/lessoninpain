---
module_id: UZEGGEY,1765865082901-19-11MAY26
title: Individual Nozzle Control (INC) System Overview
section: Individual Nozzle Control (INC) System (If Equipped)
page_labels:
- 130-1
- 130-2
pdf_pages:
- 735
- 736
models:
- all
options:
- Individual Nozzle Control
engine_tier: null
topic_type: description
components:
- boom
- nozzle
conditions: []
signal_words:
- NOTE
figures:
- WZ290104002
- N125615
generic: false
title_inferred: false
parent_module_id: null
---

# Individual Nozzle Control (INC) System Overview

Individual Nozzle Control (INC) Pro allows the nozzle bodies to be turned on and off using section control. Section control uses GPS and controls each nozzle body as a section. Each nozzle body contains a valve that can switch the nozzle body ON and OFF. Prescription or map-based applications are also possible using active nozzle settings. If manual section control is used, virtual sections are turned ON or OFF minimizing the amount of overlap. Controller based section control shuts off individual nozzles based on the GPS signal.
NOTE: Prescriptions must be created externally and then loaded to the machine before prescription application can be performed.
WZ290104002—UN—25AUG20

![[WZ290104002.png]]
**Figure WZ290104002** — A: Display; C: Spray Rate Control Unit (SRC); D: Nozzle Domain Controller (NODC); E: Individual Nozzle Control (INC) Unit; F: Individual Nozzle Bodies

B—StarFire™Receiver
The display (A), Starfire™receiver (B), Spray Rate Controller (SRC) (C), and Nozzle Domain Controller (NODC) (D) are connected to the machine ISOBUS. The Individual Nozzle Control (INC) unit (E) are connected to the NODC with two separate CAN buses. The number of INC units and individual nozzles depends on the boom length and configuration. The individual nozzle bodies are connected to the INC unit with electrical wires. Maximum of five individual nozzle bodies can be connected to one INC unit.
NOTE: The group of nozzles connected to an INC unit does not represent a virtual section. Virtual sections are created using software.
N125615—UN—16DEC16

![[N125615.png]]
**Figure N125615**

Two target pressure settings are available. Nozzle pulsing must be enabled in automatic pulsing setting in order to use target pressures. Target pressures are maintained throughout the spray application. Changes to the target pressure made on the run page overwrite the value entered on the setup page.
The Curve Compensation feature allows the duty cycle (solenoid ON time) of each nozzle body to vary along the spray boom.
The flow through the inside nozzles during a turn is reduced. Reducing the duty cycle (solenoid ON time) causes less solution to be sprayed controlling over application on the slower moving boom sections.
StarFire is a trademark of Deere & Company
The flow through the outside nozzles during a turn is increased. Increasing the duty cycle (solenoid ON time) causes more solution to be sprayed, controlling under application on the faster moving boom sections.

> Source: OMKK105338 p. 130-1, 130-2 · module UZEGGEY,1765865082901-19-11MAY26
