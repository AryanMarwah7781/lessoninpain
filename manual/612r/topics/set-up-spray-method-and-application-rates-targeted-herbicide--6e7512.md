---
module_id: ouo6092,1763666430899-19-11MAY26
title: Set Up Spray Method and Application Rates (Targeted Herbicide Single Solution)
section: See & Spray (If Equipped)
page_labels:
- 135-8
- 135-9
- 135-10
pdf_pages:
- 774
- 775
- 776
models:
- all
options:
- See & Spray
engine_tier: null
topic_type: procedure
components:
- boom
- nozzle
- nozzle turret
- pwm solenoid
- spray tip
conditions:
- wind
signal_words:
- NOTE
figures:
- N156488
- N155766
generic: false
title_inferred: false
parent_module_id: null
---

# Set Up Spray Method and Application Rates (Targeted Herbicide Single Solution)

See & Spray user settings allow the operator to define the characteristics of how the system operates and behaves. The following describes the pre-requests for system interlocks to enable the system.
The system must have the proper variables input and selected to operate the selected application method from nozzle B, of the live plant (green color) targeted material that is identified by the system.
Available Spray Methods
There are three available spray methods:
- Target apply only from nozzle B
- Traditional broadcast apply using pulse width modulation (PWM) from nozzle A and target spray from nozzle B
- Traditional broadcast apply using non-PWM from nozzle A and target spray from nozzle B
Nozzle B requires the proper input selections and setup for See & Spray Premium to be enabled. Nozzle B will not have full ExactApply functionality (PWM or turn compenstation) when utilizing See & Spray Premium.
To target apply only from nozzle B:
1. Select the proper nozzle tip size for the rate desired and rotate that nozzle tip to rear location on the nozzle turret.
See Determine Nozzle Tip Sizes and Nozzle Turret Orientation in this section for additional information.
2. Go to Menu > Machine Settings > Boom and Nozzles > ExactApply Configuration > Manual Setup.
3. Set Spray Method to See & Spray.
4. Input desired application rate. See Determine Nozzle Tip Sizes and Desired Application rate later in this section.
5. Input all required variables.
6. System is now ready to target apply out of nozzle B.
Nozzle A can be used in conjunction with nozzle B during See & Spray operation. When nozzle A is used in conjunction with nozzle B in See & Spray, nozzle A can be set up with the same functionality that ExactApply (PWM spraying) offers currently for traditional broadcast spraying. When using nozzle A with PWM, a target rate can be input and the system will adjust the PWM signal for nozzle A to meet the expected rate. Additional setup is required to ensure that proper rate can be achieved.
To traditional broadcast apply using PWM from nozzle A and target apply from nozzle B:
1. Select the proper nozzle tip size for the rate desired for traditional broadcast spraying out of nozzle A, and rotate that nozzle tip to the forward position on the nozzle turret.
See Determine Nozzle Tip Sizes and Nozzle Turret Orientation in this section for additional information.
2. Select the proper nozzle tip size for the rate desired for target application out of nozzle B, and move that nozzle to the rear location on the nozzle turret.
See Determine Nozzle Tip Sizes and Nozzle Turret in this section for additional information.
3. Go to Menu > Machine Settings > Boom and Nozzles > ExactApply Configuration > Manual Setup.
4. Select Auto in the Valve Pulsing Mode drop-down menu.
5. Select A+B in the Spray Mode drop-down menu.
6. Select See & Spray in the Spray Method drop-down menu.
7. Select or edit the rate to be broadcast applied from nozzle A. See Determine Nozzle Tip Sizes and Desired Application Rate later in this section.
8. Input the desired rate to be applied from nozzle B. See Determine Nozzle Tip Sizes and Desired Application Rate later in this section.
9. System is now ready to broadcast spray from nozzle A and target spray out of nozzle B.
Nozzle A can also be set up to traditional broadcast (non-PWM). When A+B is selected and nozzle A pulsing is set to OFF, Nozzle A will revert to traditional broadcast at the pressure of the boom plumbing, determined by nozzle B attributes, and the rate is determined by the orifice size (tip) installed for nozzle A. Additional setup for proper nozzle size is required for the desired application rate.
To traditional broadcast apply using non-PWM from nozzle A and target apply from nozzle B:
1. Select the proper nozzle tip size for the rate desired for broadcast application out of nozzle A and rotate that nozzle tip to the forward position on the nozzle turret.
See Determine Nozzle Tip Sizes and Nozzle Turret in this section for additional information.
2. Select the proper nozzle tip size for the rate desired for target application out of nozzle B, and move that nozzle tip to rear location on the nozzle turret.
See Determine Nozzle Tip Sizes and Nozzle Turret Orientation in this section for additional information.
3. Go to Menu > Machine Settings > Boom and Nozzles > ExactApply Configuration > Manual Setup.
4. Select OFF in the Valve Pulsing Mode drop-down menu.
5. Select A+B in the Spray Mode drop-down menu.
6. Select See & Spray in the Spray Method drop-down menu.
7. Input the desired rate to be applied from nozzle B. See Determine Nozzle Tip Sizes and Desired Application Rate later in this section.
8. System will now target apply out of nozzle B and traditional broadcast apply out of nozzle A.
The rate from nozzle A will be calculated using the nozzle tip selected for nozzle A and the boom pressure. Pressure within the boom plumbing system will be determined by nozzle B rate.
Nozzle Turret Orientation
See & Spray will only function from nozzle B.
See & Spray may be combined with a traditional broadcast application from nozzle A (A+B See & Spray mode). To operate in this mode:
- Nozzle A must have turret 1, 2, or 3 properly rotated to the front position.
- Nozzle A can traditional broadcast apply product with the following full ExactApply functionality:
- Pulse width modulation (PWM)
- Curve compensation
- Individual nozzle control
- Nozzle B must have turret 4, 5, or 6 properly rotated to the rear position.
Nozzle B will have the following limited ExactApply functionality:
- No pulse width modulation (PWM)
- No curve compensation
- Individual nozzle control
Nozzle B will target apply product via commands from the See & Spray camera detection system based on live plant (green color) targets identified.
Nozzle B commands will be 100% duty cycle commands for nozzle B fully ON when applying.
Determine Nozzle Tip Sizes
Consider the following when selecting nozzle tip size:
- Nozzle tip size for nozzle A must be sized properly for the rate desired in correlation to the rate desired from nozzle B when nozzles A and B are being used with See & Spray.
- Install all nozzles on nozzle B to point rearward when using the nozzles with an inclined spray pattern.
- If windy conditions may push the spray away from the target, it is recommended to set up See & Spray with setting the buffer width one step wider.
- Always follow the chemical label rates during application. When using See & Spray, use an adequate carrier rate to ensure proper coverage of weeds.
- A contact chemical works best with setting the buffer width one step wider.
- A systemic chemical works best with even coverage nozzle types.
- Setting the buffer width one step wider feature can be utilized in the See & Spray setup.
Use the following formulas to select a proper nozzle tip for nozzle A.
When nozzle A is set to auto pulsing:
N156488—UN—03AUG21

![[N156488.png]]
**Figure N156488** — A: Desired Traditional Broadcast Rate (nozzle A); B: Desired Target Rate (nozzle B); C: Target Spray Nozzle Tip Size (nozzle B); D: Desired Duty Cycle Percentage Expressed as a Decimal (e.g. 65% = 0.65); E: Traditional Broadcast Nozzle Tip Size (nozzle A)

Nozzle A Is Set to Auto Pulsing
NOTE: Desired duty cycle percentage for optimum curve compensation is 65—70% for pulse width modulating (PWM) spraying.
When nozzle A is set to non-PWM:
A
B | C =D
N155766—UN—17MAY21

![[N155766.png]]
**Figure N155766** — A: Desired Traditional Broadcast Rate (nozzle A); B: Desired Target Rate (nozzle B); C: Target Spray Nozzle Tip Size (nozzle B); D: Traditional Broadcast Spray Nozzle Tip Size (nozzle A)

Nozzle A Is Set to non-PWM
Example of nozzle B tip size calculation = GPA x MPH x W / 5940:
- Desired target spray application rate from nozzle B = 15 gpa.
- Desired traditional broadcast spray application rate from nozzle B = 10 gpa.
- Desired travel speed = 10 mph.
- Machine setup is 15 in nozzle spacing on a 120 ft boom.
15 x 10 x 15 / 5940 = 0.38 nozzle tip flow rate = 04 red nozzle tip.
Example of nozzle A tip size calculation = A GPA / B GPA x target spray nozzle tip size = non-PWM nozzle A tip size:
10 / 15 x 4 = 2.67 or 025 nozzle tip at 50 psi, or 03 nozzle tip at 40 psi.
2.67 / 0.6 or 04 red tip for PWM nozzle A spraying.
Desired Application Rate
There are two areas in which application rate input is required to be input when spraying in A+B with See & Spray, where nozzle B uses See & Spray and nozzle A is set to auto pulsing.
NOTE: When non-PWM application is in A+B mode with See & Spray enabled for nozzle B, nozzle A application rate is calculated based on nozzle tip A input and boom pressure. This rate is not adjustable and proper nozzle tip selection is required.
- Traditional broadcast target rate within the Spray System application: When See & Spray is enabled, the input or selected target rate defines the traditional broadcast application rate out of nozzle A when spray method A +B is selected from the Nozzle Turret Setup.
- See & Spray target application rate within the Spray System application: When See & Spray is enabled, this input defines the targeted application rate out of nozzle B. This rate input determines the boom plumbing system pressure when spray method A+B or B Only is selected from the Nozzle Turret Setup.
NOTE: This rate will determine the system spray pressure within the boom plumbing. Nozzle tip sizing and selection is required to ensure that proper application rate and pressure are achieved for the desired machine speed during application from both nozzle A and nozzle B.
NOTE: Recommended minimum application rate is 10 gal/ac.
- Total will be filled in, showing the combined amount to be targeted when both nozzles A and B are actively applying.

> Source: OMKK105338 p. 135-8, 135-9, 135-10 · module ouo6092,1763666430899-19-11MAY26
