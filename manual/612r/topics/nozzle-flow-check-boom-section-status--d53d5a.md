---
module_id: bn55050,1778257414936-19-08MAY26
title: Nozzle Flow Check | Boom Section Status
section: Calibrations Application
page_labels:
- 25-B-22
pdf_pages:
- 82
models:
- all
options: []
engine_tier: null
topic_type: display_ui
components:
- boom
- nozzle
conditions: []
signal_words:
- NOTE
figures:
- N119616
- N119617
- N122954
- N125628
- N122953
- N122955
generic: false
title_inferred: false
parent_module_id: null
---

# Nozzle Flow Check | Boom Section Status

Boom Section Status is shown for each section on the spray boom.
Available Statuses:
N119616—UN—14NOV16

![[N119616.png]]
**Figure N119616**

Section Ready
Section Ready—spray section is enabled and will begin spraying when spray system master switch is pressed.
N119617—UN—14NOV16

![[N119617.png]]
**Figure N119617**

Section Applying
Section Applying—spray section is currently applying product.
N122954—UN—14NOV16

![[N122954.png]]
**Figure N122954**

Section Applying Fault
Section Applying Fault—spray section fault is detected. Product is not being applied.
N125628—UN—14NOV16

![[N125628.png]]
**Figure N125628**

Section Control Auto OFF
Section Control Auto OFF—spray section is commanded off by Section Control system and is not applying product.
N122953—UN—14NOV16

![[N122953.png]]
**Figure N122953**

Section Indexed OFF
Section Indexed OFF—spray section is commanded off by Indexed Boom Section (IBS) switches on the multi-function lever and is not applying product.
N122955—UN—14NOV16

![[N122955.png]]
**Figure N122955**

Section Disabled
Section Disabled—spray section is disabled using the Boom and Nozzles application. Spray section will not apply product when spray system master switch is pressed.
NOTE: Spray section can also be disabled using the appropriate encoders on the CommandARM.

> Source: OMKK105338 p. 25-B-22 · module bn55050,1778257414936-19-08MAY26
