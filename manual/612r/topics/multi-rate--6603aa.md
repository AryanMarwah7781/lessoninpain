---
module_id: ouo6092,1777915351683-19-11MAY26
title: Multi-Rate
section: Nozzle System Application
page_labels:
- 25-G-38
- 25-G-39
pdf_pages:
- 199
- 200
models:
- all
options: []
engine_tier: null
topic_type: settings
components:
- nozzle
- spray tip
conditions: []
signal_words: []
figures:
- N157743
generic: false
title_inferred: false
parent_module_id: null
---

# Multi-Rate

Multi-Rate allows you to control multiple application rates from multiple meters on the boom. When using multi-rate, sprayers can achieve a more precise application rate and product cost-savings by reducing waste.
Multi-rate is always enabled by default, but is functional when using pulse-width modulation (PWM), prescription rates (Rx), and See & Spray variable rate.
N157743—UN—02DEC24

![[N157743.png]]
**Figure N157743**

Multi-Rate Run Page Module
The multi-rate run page page module shows the difference in percentage between the average as-applied rate and the average target rate for each meter.
Run Page Module Guidelines:
- Update rate is every 1 second.
- Values are shown in 0.5% increments.
- If the error is within 1%, no bar is shown.
- If the error is within 1—5%, a black bar to scale is shown.
- If the error is within 5—10%, a yellow bar is shown.
- If the error is above 10%, a red bar is shown.
- Maximum value is +/-15%.
Scenarios Where Increased Error Rates Are Expected:
Scenario 1:
The prescription map has a rate higher than what is achievable from the selected nozzle tips or spray mode. Sections impacted show as a negative value on the run page module.
Actions to take:
- Decrease speed.
- Adjust the spray mode to Combined A+B, if not already being used.
- Change the nozzle tip sizes.
Scenario 2:
The prescription map has a rate lower than what is achievable from the selected nozzle tips or spray mode. Sections impacted show as a positive value on the run page module.
Actions to take:
- Increase speed.
- Adjust the spray mode, if applicable.
- Change the nozzle tip sizes.
Scenario 3:
Curve compensation causes the rate to go above or below achievable range.
Actions to take:
- Adjust the turning speed.
- Adjust the spray mode, if applicable.
- Change the nozzle tip sizes.
Scenarios That Require Troubleshooting:
Scenario 1:
The desired prescription rates are within the acceptable range of the selected nozzle tips and spray modes while traveling straight (no curve compensation), but high error rates are shown similar to the example image of the run page module.
Actions to take:
- Check the troubleshooting procedures in the Operator's Manual for erratic flow rates.
- Turn down the ratio if you are saturated high and low:
- Maximum and minimum flow rates.
- Run auto A/B with auto pulsing to get the turn down ratio.
Scenario 2:
One section is consistently high or low.
Action to take:
Check the troubleshooting procedures in the Operator's Manual for erratic flow rates.

> Source: OMKK105338 p. 25-G-38, 25-G-39 · module ouo6092,1777915351683-19-11MAY26
