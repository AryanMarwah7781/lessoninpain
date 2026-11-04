---
module_id: bn55050,1775500898607-19-27APR26
title: Curve Compensation
section: Nozzle System Application
page_labels:
- 25-G-29
- 25-G-30
- 130-14
- 130-15
pdf_pages:
- 190
- 191
- 748
- 749
models:
- all
options: []
engine_tier: null
topic_type: display_ui
components:
- nozzle
conditions: []
signal_words:
- NOTE
figures:
- WZ1406741
generic: false
title_inferred: false
parent_module_id: null
---

# Curve Compensation

Curve Compensation allows the application rate to be maintained along the boom width during a turn or spraying curved portions of a field. The nozzle controllers adjust the application rate to individual nozzles when making a curve.
Modify When:
- Performing normal spray operations. Enable curve compensation.
- Using a fixed pulse rate. Disable curve compensation.
NOTE: If you switch to fixed pulsing or turn pulsing off, the toggle button will display as OFF and not be selectable
Procedure to Modify:
NOTE: Curve compensation setting is tied to the tank mode setting. If tank mode is changed, curve compensation setting must be updated.
WZ1406741—UN—28MAY25

![[WZ1406741.png]]
**Figure WZ1406741**

Toggle Button
Select the Toggle Button to turn ON/OFF curve compensation.
If Equipped with See & Spray:
NOTE: Curve compensation is disabled on a port when See & Spray is enabled. If a target is detected by See & Spray, the nozzle port is commanded to 100% duty cycle.
NOTE: Curve compensation is only available if automatic nozzle pulsing is selected. The current state of the toggle button is displayed, but it is not selectable when current settings are incompatible with curve compensation.
When turning in a very tight turn radius, nozzle flow may saturate at the top and/or lower end. Use the nozzle flow graph to adjust operation and optimize performance.

> Source: OMKK105338 p. 25-G-29, 25-G-30, 130-14, 130-15 · module bn55050,1775500898607-19-27APR26
