---
module_id: ouo6092,1777290384202-19-06MAY26
title: Operating Conditions
section: See & Spray (If Equipped)
page_labels:
- 135-5
- 135-6
pdf_pages:
- 771
- 772
models:
- all
options:
- See & Spray
engine_tier: null
topic_type: description
components:
- boom
- boom height
- camera
- lights
- nozzle
- pwm solenoid
- spray tip
conditions:
- slope
signal_words:
- IMPORTANT
- NOTE
figures: []
generic: false
title_inferred: false
parent_module_id: null
---

# Operating Conditions

The system constantly monitors the following inputs across the boom to calculate an operating condition factor of fully met, partially met, or not met.
Operating conditions being monitored by the system are:
Optimal Boom Height: Targeted Herbicide
- Optimal boom height
- Machine speed measured at each nozzle
- Camera image quality (includes ambient light and image quality inputs)
Follow the guidelines below to maintain the operating conditions of each input at fully met or partially met to obtain the optimal performance of the system.
A message on the display will appear when a confidence level is not met, and the system will activate the operator-selected fallback mode. For example, if broadcast is the selected fallback mode, and one or more of the input operating conditions are not met, the system will then revert to traditional broadcast spray out of the affected nozzles.
The system will return to normal operation once operating conditions return to a fully met or partially met state.
Approximate Boom Height Above Target | Confidence Level
>1397 mm (>55 in) and Above | Not Met
1397 mm (55 in) | Partially Met
>1200 mm (>47 in) | Partially Met
Optimal Upper Height Above Target | 1200 mm (47 in) | Fully Met
Optimal Lower Height Above Target | 500 mm (20 in) | Fully Met
<500 mm (<20 in) | Partially Met
305 mm (12 in) | Partially Met
<305 mm (<12 in) or Less | Not Met
Designed optimal boom height above the target or ground is 500—1200 mm (20—47 in). Operating within this range obtains a confidence level of fully met.
Operating with the boom 305—508 mm (12—20 in) above the target or ground obtains a confidence level of partially met.
Operating with the boom 1194—1397 mm (47—55 in)
above the target or ground obtains a confidence level of partially met.
Operating with the boom less than 305 mm (12 in) or greater than 1397 mm (55 in) above the target or ground obtains a confidence level of not met and activates the fallback mode for the affected nozzles.
Approximate Boom Height Above Target | Confidence Level
Optimal Upper Height Above Target | 1676 mm (66 in) | Fully Met
Optimal Lower Height Above Target | 500 mm (20 in) | Fully Met
Optimal Boom Height: Variable Rate
Optimal Nozzle Speed
NOTE: The system uses GPS inputs to determine the speed of the ExactApply nozzle over the ground. Outer nozzles in a turn travel faster than inner nozzles, so the outer nozzles can travel above optimal speeds in a turn and activate the fallback mode for the affected nozzles.
Optimal nozzle speed is 0.8—26 km/h (0.5—16 mph).
Operating nozzles within this range obtains a confidence level of fully met.
Nozzles operating above or below this speed range obtains a confidence level of not met and will activate the fallback mode for the affected nozzles.
NOTE: If nozzle speed is less than 0.8 km/h (0.5 mph), the system will activate the OFF fallback mode instead of the broadcast fallback mode, even if broadcast is selected.
See & Spray Gen 2
Nozzle Alignment | Nozzle Tip | Max Speed
Straight Down | ER80, TP65, TP80, DG80, AIXR110 | 19 kmh (12 mph)
Rear Incline | ULD, LDM | 24 kmh (15 mph)
TSL60/80, ER80, 3D, TP65, DGX65, TP80,
26 kmh (16 mph) DG80, AI80, AIXR110, SF40
NOTE: Only nozzle tips approved for Pulse Width Modulation (PWM) operation are permitted. Using non-PWM approved nozzle tips may result in improper spray performance.
Camera Image Quality
Ambient Light—The cameras measure the light to determine the ambient light value. Ambient lighting is dependent upon several varying factors, including but not limited to:
- Time of year
- Ambient conditions
- Time of day
- Overcast
- Shading
When minimum ambient lighting requirements are not met, the system reverts to a confidence level of not met and will activate the fallback mode for the affected nozzles.
Debris/Obstructions—The system interprets the image and determines if a lens has any debris or obstructions. The system notifies the operator if it determines that the lens has damage or fixed debris obstructing the camera’s vision. Debris behind the tires is the most common image quality issue, resulting in fallback mode activation. Lenses should be cleaned daily and as required in certain conditions.
IMPORTANT: Avoid damage to camera lenses. Use only water in a spray bottle, a damp cloth with minimal pressure, or low-pressure air to clean lenses.
If the system determines that there are no obstructions or occlusions, a confidence level of fully met is obtained.
If the system determines that there are minor obstructions or occlusions, a confidence level of partially met is obtained.
If the system determines that there are major obstructions or occlusions, a confidence level of not met is obtained and will activate the fallback mode for the affected nozzles.
This is determined across several zones within an image. Hence, a partially obstructed lense may still provide a confidence level of met in the image areas that are not obstructed.

> Source: OMKK105338 p. 135-5, 135-6 · module ouo6092,1777290384202-19-06MAY26
