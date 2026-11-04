---
module_id: ouo6092,1763586442387-19-11MAY26
title: Nozzle Control System Overview (Single Solution)
section: ExactApply Nozzle Control System (If Equipped)
page_labels:
- 125-1
- 125-2
pdf_pages:
- 695
- 696
models:
- all
options:
- ExactApply
engine_tier: null
topic_type: description
components:
- boom
- display
- nozzle
- spray tip
conditions: []
signal_words:
- NOTE
figures:
- N125630
- N125615
- N127957
generic: false
title_inferred: false
parent_module_id: null
---

# Nozzle Control System Overview (Single Solution)

The nozzle control system allows individual nozzle bodies to be turned on and off based on Section Control. The nozzle bodies each contain two valves that can be pulsed or turned on continuously for spraying. There are five active nozzle settings available for the system; A only, B only, A + B, combined A + B, and automatic. Nozzle control provides the operator a larger speed range and varied application rates without changing pressure or spray tips. Operating a combination of nozzle pulsing and active nozzle settings allows the system to maintain a constant pressure and droplet size while changing speeds. These features also allow the system to change the rate and the spray width, compensating for speed differences at boom ends when turning. Prescription or map-based applications are also possible using nozzle pulsing. When section control is used nozzle bodies are turned ON or OFF individually minimizing the amount of overlap.
Active Nozzle Selection allows operator to select the desired nozzle or combination of nozzles to use during the application.
NOTE: Nozzles 1, 2, or 3 must be in the forward position for all modes except Combined A + B.
N125630—UN—16DEC16

![[N125630.png]]
**Figure N125630**

- A Only (Example Shown) — only solenoid A is activated or pulsed during application. The A nozzle is the forward most spray tip on the nozzle body. Solenoid B and all other spray tips remain OFF in this mode.
- B Only — only solenoid B is activated or pulsed during application. The B nozzle is the rearward most spray tip on the nozzle body. Solenoid A and all other spray tips will OFF in this mode.
- A + B Nozzle — nozzle 1, 2, or 3 is in the forward position. Both solenoids A and B are activated in this mode. Solution is sprayed from both nozzles.
- Automatic — nozzle control unit determines which solenoid or combination of solenoids to activate based on selected nozzle tip configuration to achieve the desired application rate. Solenoid can be pulsing or non-pulsing in this mode based on user setup.
- Combined A + B — nozzle 4, 5, or 6 is in the forward position. Both solenoids A and B are activated or pulsed in this mode. The full volume of solution is sprayed through the front nozzle.
N125615—UN—16DEC16

![[N125615.png]]
**Figure N125615**

Two target pressure settings are available. Both settings are available in the A only, B only, A + B, and Combined A + B active nozzle selections. Nozzle pulsing must be enabled in automatic pulsing setting in order to use target pressures. Target pressures are maintained throughout the spray application. Changes to the target pressure made on the run page overwrite the value entered on setup page.
The Curve Compensation feature allows the duty cycle (solenoid ON time) of each nozzle body to vary along the spray boom.
The flow through the inside nozzles during a turn is reduced. Reducing the duty cycle (solenoid ON time) causes less solution to be sprayed controlling over application on the slower moving boom sections.
The flow through the outside nozzles during a turn is increased. Increasing the duty cycle (solenoid ON time) causes more solution to be sprayed, controlling under application on the faster moving boom sections.
N127957—UN—05JAN17

![[N127957.png]]
**Figure N127957**

Section Flow
Section Flow %
The section flow is an available run page module. It displays the average flow percentage for each virtual section in graph form. The average flow percentage is the percent of maximum flow possible being used for the current active spray tip. In the example shown, the machine would be making a right-hand turn. The graph decreases gradually as it progresses from the left-hand side to the right-hand side of the spray boom. The Section Flow % graph is generated from vehicle heading and always active and updating when in Auto pulsing mode. Optimization: If nozzles are sized correctly the average flow percentage should read approximately 75% at maximum speed to account for turns when curve compensation is being used. If average flow percentage is greater than approximately 75% when operating at maximum speed it indicates nozzles are too small.
- The Section Flow % bars will display 100% when the valve pulsing mode is set to “off” in the manual setup page for the nozzle turrets.
- The Section Flow % bars will display the nozzle flow percentage set by operator when valve pulsing mode is set to “fixed” in the manual setup page for the nozzle turrets.
- The Section Flow % bars will change percentage when the valve pulsing mode is set to “Auto” in the manual setup page for the nozzle turrets.
The Section Flow % widget also provides the operator with a visual representation of the minimum flow % or duty cycle for the current setup to maintain desired application pressure. The horizontal gray line is the "floor" of the percent flow, percent flow by virtual section is then indicated by the vertical blue bars. Within the advanced settings of the Booms and Nozzles page there is a check box under nozzle flow that says “Limit Minimum Flow %”. If this box is checked the floor will be approximately 25%. Upon key on, the system begins calculating values based on the nozzle size you choose and what the software has populated for flow relative to specific tips. The line tends to adjust with real time nozzle size calculations done by the system as there are increases in speed which would ultimately increase system flow. For optimal application performance, it is recommended to remain at or above this indication, when traveling in a straight line at minimum desired application speed to maintain desired application pressure. If the machine speed is reduced and the % flow bar indicates operation below this line, rate will continue to be maintained by the ExactApply system, however, the operator will notice application system pressure lower than desired or input. The system will continue to adjust and maintain rate until the minimum spray pressure setting value is reached and will maintain that minimum pressure value setting until either speed is increased, machine is stopped or Master Spray is disabled.
Variable rate prescription applications are also possible when using the Nozzle Control system.
NOTE: Prescriptions must be created externally and then loaded to the machine before prescription application can be performed.

> Source: OMKK105338 p. 125-1, 125-2 · module ouo6092,1763586442387-19-11MAY26
