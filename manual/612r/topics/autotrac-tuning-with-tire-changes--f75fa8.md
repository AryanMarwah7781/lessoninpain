---
module_id: AM24480,1772511295181-19-08MAR26
title: AutoTrac Tuning with Tire Changes
section: AutoTrac Tuning, AutoTrac RowSense, and AutoTrac Vision
page_labels:
- 140-13
pdf_pages:
- 824
models:
- all
options:
- AutoTrac
- RowSense
engine_tier: null
topic_type: procedure
components:
- steering
- tire
conditions: []
signal_words:
- NOTE
figures:
- NX698072
- NX698073
- NX698074
generic: false
title_inferred: false
parent_module_id: null
---

# AutoTrac Tuning with Tire Changes

NOTE: Ensure that the software is updated with the latest version before performing this procedure.
This procedure only applies to wet systems with a liquid skid and not to dry systems.
Use this setting when switching between Float tire and Row Crop tire to ensure optimal AutoTrac performance.
NX698072—UN—02MAR26

![[NX698072.png]]
**Figure NX698072**

AutoTrac Guidance
1. Open the AutoTrac Guidance application page and select the Information and Settings link.
NX698073—UN—02MAR26

![[NX698073.png]]
**Figure NX698073**

AutoTrac Steering Optimization Settings
2. Select the AutoTrac Steering Optimization settings. This will open up the Tire Type selection window.
NX698074—UN—02MAR26

![[NX698074.png]]
**Figure NX698074**

Tire Type Selection Window
3. Select the appropriate Tire Type (Row Crop or Float) fitted to the machine and select OK.
4. Machines with the largest tire size width of 800 mm require additional steering optimization settings.
a. Steering Sensitivity: 75
b. Heading Lead: 75
c. Steering Response Rate: 75
5. Ensure that the settings have been applied, and verify that performance meets the needs. Advanced tuning may still be required based on field conditions.

> Source: OMKK105338 p. 140-13 · module AM24480,1772511295181-19-08MAR26
