---
module_id: bn55050,1775500939377-19-27APR26
title: Nozzle Body Lighting
section: Nozzle System Application
page_labels:
- 25-G-30
- 25-G-31
pdf_pages:
- 191
- 192
models:
- all
options: []
engine_tier: null
topic_type: display_ui
components:
- boom
- lights
- nozzle
conditions:
- road transport
signal_words:
- CAUTION
- NOTE
figures:
- WZ675766
- N125634C
- N125623C
generic: false
title_inferred: false
parent_module_id: null
---

# Nozzle Body Lighting

Nozzle Body Lighting allows you to select the operation mode and brightness of the nozzle lights. The nozzle body lights turn on by way of a Controller Area Network (CAN) message sent by the domain controller to the nozzle body using the Controller Area Network (CAN). The nozzle body lights are only able to illuminate if the power and ground circuits are functioning properly.
wz675766—UN—22AUG25

![[WZ675766.png]]
**Figure WZ675766**

Nozzle Body Lighting
Modify When:
- Troubleshooting nozzle faults.
- Viewing nozzle spray patterns and pulsing.
- A change in brightness is desired.
Nozzle Body Lighting Modes:
OFF— nozzle body lights are not illuminated when spraying.
ON— nozzle body lights illuminate on actively spraying nozzles when the spray system master switch is pressed. The ON mode allows you to clearly view the entire width of the boom in low light conditions.
Strobe— nozzle body lights flash at a fixed rate on actively spraying nozzles when the spray system master switch is pressed. Strobe mode allows you to better view the spray pattern and pulsing from the nozzle body.
Manual— nozzle body lights are illuminated regardless of boom position or the spray system master switch status. Manual mode assists in diagnosing wiring issues and spray tip cleaning in low light situations. When using manual mode to diagnose issues:
- Faulted nozzle or nozzles that are illuminated indicate a Sync Circuit issue.
- Faulted nozzle or nozzles that do not illuminate indicate an issue with Controller Area Network (CAN) Communication, the Power circuit, or the Ground circuit.
NOTE: For further information on how to diagnose ExactApply issues, see ExactApply | Troubleshooting.
Procedure to Modify:
CAUTION: Do not transport the machine when the nozzle lights are in manual mode. Your vision and the vision of others will be impaired.
N125634C—UN—24APR26

![[N125634C.png]]
**Figure N125634C**

Nozzle Body Lighting Mode
1.Select the desired nozzle body lighting mode.
NOTE: The vertical placement of spray pipes and nozzle bodies affects overall lighting effectiveness.
N125623C—UN—24APR26

![[N125623C.png]]
**Figure N125623C**

Nozzle Body Lighting Brightness
2.Select the desired nozzle body lighting brightness.

> Source: OMKK105338 p. 25-G-30, 25-G-31 · module bn55050,1775500939377-19-27APR26
