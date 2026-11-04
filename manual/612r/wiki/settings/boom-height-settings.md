---
type: settings
title: "Boom height settings (BoomTrac sensor target, height mode, target height, center frame)"
models: [all]
options: [BoomTrac]
engine_tier: null
components: [boom height, BoomTrac sensor, boom, center frame, boom wing]
sources:
  - "ouo6092,1776448050606-19-28APR26"
  - "ouo6092,1776448178262-19-28APR26"
  - "ouo6092,1776448104189-19-27APR26"
  - "ouo6092,1776448206631-19-27APR26"
  - "ouo6092,1776448146768-19-28APR26"
  - "ouo6092,1777984352422-19-05MAY26"
  - "ouo6092,1777984448733-19-05MAY26"
  - "ouo6092,1777984468622-19-05MAY26"
  - "ouo6092,1777984543287-19-05MAY26"
  - "ouo6092,1777984566356-19-05MAY26"
  - "ouo6092,1777984522438-19-05MAY26"
  - "ouo6092,1777985061812-19-05MAY26"
  - "ouo6092,1777985140776-19-05MAY26"
  - "hy01057,1784715061862-19-22JUL26"
  - "bn55050,1776442150178-19-20APR26"
  - "BN55050,000005D-19-08JUN18"
  - "CS12167,000022E-19-06FEB13"
  - "DX,WW,CHEM02-19-05APR04"
  - "ouo6092,1777290384202-19-06MAY26"
  - "ouo6092,1767966071356-19-17JUL26"
  - "bn55050,1778257647148-19-08MAY26"
  - "az06166,1748611183764-19-27APR26"
reviewed: false
compiled: 2026-09-23
---

# Boom height settings

**Short answer: the manual gives no target boom height for a crop, a canopy density, a product or a
wind speed.** The heights it does print are tip geometry, See & Spray camera confidence bands, and
diagnostic/procedure check heights — listed in "Heights the manual prints" below, with what each one
is and is not. The only height rule tied to drift is a direction: increasing boom height excessively
above the target increases the risk of spray drift [[height-mode--b6109a|Height Mode]] (p. 25-A-6).

**Option: BoomTrac.** Everything on this page is a BoomTrac setting. The BoomTrac system
automatically controls boom tilt functions and center frame control relative to contours of the
ground or crop canopy [[boomtrac--783c2a|BoomTrac]]. If your machine does not have BoomTrac, these
settings do not apply. The component itself (sensors, calibration, return to height) is on
[[boom-height]]; the boom structure is on [[boom]]. Terrain response (slopes, waterways) is on
[[slopes-and-rough-ground]].

## The condition

Setting how BoomTrac holds the boom above the crop or the ground: what the sensors aim at, whether the
wings follow the center frame, how high the tips run, and whether the center frame sensor controls
height. The manual says to modify BoomTrac when crop height changes, terrain contour changes, boom
lower/raise response is too slow or too fast, or when spraying in dusty or muddy conditions
[[boomtrac--783c2a|BoomTrac]].

## The manual's limits

> [!warning] CAUTION
> CAUTION: Avoid damage or contamination of your surroundings. Increasing boom height excessively above the target increases the risk of spray drift.
> [[height-mode--b6109a|Height Mode]]

- Target Heights are the distance from the bottom of the nozzle tips to the crop canopy or ground
  [[target-height--c66795|Target Height]] (p. 25-A-6).
- For chemical application, always follow all label directions; do not spray when winds exceed
  16 km/h (10 mph) [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]]
  (p. 55-1; the same module is also printed at 50-1 and 165-1).

## Heights the manual prints

None of these is a target height for a crop, canopy density, product or wind speed.

**Operating heights (what the boom runs at):**

- **Flat fan tip geometry — all machines.** Flat Fan spray tips apply solution in an elliptical
  pattern; to achieve uniform application the tips are overlapped. Usually this is done with spray tips
  spaced 508 mm (20 in) apart and positioned 457— 559 mm (18—22 in) above the target surface
  [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]] (p. 55-6). (The space in "457— 559" is as
  printed.) This is tip geometry for an even pattern, not a BoomTrac setting.
- **See & Spray optimal boom height — See & Spray machines only.** For Targeted Herbicide, designed
  optimal boom height above the target or ground is 500—1200 mm (20—47 in); operating within this
  range obtains a confidence level of fully met [[operating-conditions--8fd625|Operating Conditions]]
  (p. 135-5). As printed on the same page
  [[operating-conditions--8fd625|Operating Conditions]] (p. 135-5):
  - Operating with the boom 305—508 mm (12—20 in) above the target or ground obtains a confidence
    level of partially met.
  - Operating with the boom 1194—1397 mm (47—55 in) above the target or ground obtains a confidence
    level of partially met.
  - Operating with the boom less than 305 mm (12 in) or greater than 1397 mm (55 in) above the target
    or ground obtains a confidence level of not met and activates the fallback mode for the affected
    nozzles.
  - Optimal Boom Height: Variable Rate — Optimal Upper Height Above Target 1676 mm (66 in), Optimal
    Lower Height Above Target 500 mm (20 in), both Fully Met.

  The printed band edges do not line up exactly with the table on the same page (the table gives
  <500 mm (<20 in) and >1200 mm (>47 in) as Partially Met, the text gives 305—508 mm (12—20 in) and
  1194—1397 mm (47—55 in)) [[operating-conditions--8fd625|Operating Conditions]] (p. 135-5). They are
  copied here as printed.

**Check heights (NOT operating settings):**

- **762 mm (30 in)** — a troubleshooting check: for Boom Height Sensor (BHS) misreadings, "With booms
  level at 762 mm (30 in), verify that all BHS readings look correct"
  [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]] (p. 155-9).
- **approximately 500 mm (20 in)** — See & Spray camera calibration setup: unfold, level, and lower
  the booms to approximately 500 mm (20 in) above the ground
  [[see-and-spray-calibration-procedure--80b067|See & Spray Calibration Procedure]] (p. 25-B-29).
- **Minimum 500 mm (19-11/16 in)** — See & Spray Detection Procedure requirement (machine parked on
  gravel or bare ground) [[see-and-spray-detection-procedure--dcaefb|See & Spray Detection Procedure]]
  (p. 25-B-28), printed again at 135-44
  [[see-and-spray-detection-procedure--699337|See & Spray Detection Procedure]].
- **± 203 mm (8 in)** is not a height at all: it is how close to the crop rows to position the
  BoomTrac sensors sideways
  [[boomtrac-settings-sensor-placement-setup--c8149c|BoomTrac Settings — Sensor Placement Setup]] (p. 155-7).

> [!conflict] Flat fan tip height vs See & Spray optimal height (not reconciled by the manual)
> The Flat Fan Spray Tip topic says tips are usually positioned 457— 559 mm (18—22 in) above the
> target surface [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]] (p. 55-6). The See & Spray
> Operating Conditions topic says the designed optimal boom height above the target or ground is
> 500—1200 mm (20—47 in), with 305—508 mm (12—20 in) only partially met
> [[operating-conditions--8fd625|Operating Conditions]] (p. 135-5). On a See & Spray machine the two
> ranges only partly overlap: the lower part of the flat fan range sits in See & Spray's "partially
> met" band, and most of the See & Spray optimum is above the flat fan range. The manual does not say
> which to follow or how to reconcile them. This page does not choose; ask your dealer, and check
> the product label and the installed tip's chart. In any case, increasing boom height excessively
> above the target increases the risk of spray drift [[height-mode--b6109a|Height Mode]] (p. 25-A-6).

## The levers (display page and setting names as printed)

All are on the **BoomTrac** page of the **Boom System** application
[[boomtrac--783c2a|BoomTrac]]:

| Lever | What it is, as printed |
|---|---|
| **Sensor Target** | Select the target for the sensors to maintain the height above [[boomtrac--783c2a|BoomTrac]]. Choices: Ground, Ground with Canopy Assist, Canopy [[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]]. |
| **Height Mode** | Select Locked Height Mode to use the same target height setting for all boom sections; choose Unlocked Height Mode to set separate target height settings for each boom section [[boomtrac--783c2a|BoomTrac]]. |
| **Target Height** | Displays the distance from the bottom of the spray tips to the target; select the Input Boxes to change the values [[boomtrac--783c2a|BoomTrac]]. |
| **Center Frame Control** | Use the toggle button to turn the center frame sensor ON/OFF [[boomtrac--783c2a|BoomTrac]]. |
| **Lower/Raise Response** | Response speed of the boom lower/raise function [[boomtrac--783c2a|BoomTrac]] — see [[slopes-and-rough-ground]]. |
| **BoomTrac Presets** | Allows you to quickly switch between different BoomTrac configurations [[boomtrac--783c2a|BoomTrac]]. |

## What the manual says each lever does

### Sensor Target — Ground, Ground with Canopy Assist, Canopy

How the sensors work: the boom height sensors are ultrasonic sensors that emit a sound pulse, then
listen for the return echo; the first reflection received is used as the canopy signal, and the last
reflection received is referred to as the ground signal
[[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]].

The manual's guidance, as printed
[[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]]:

**Ground** — When to use: Operating in fallow ground or fields with less than 30% canopy coverage.
Description of Mode: Ground mode prioritizes sensing the soil surface, which provides the most
accurate boom height control when crop canopy is minimal. If excessive crop canopy is present where
the height sensor cannot always get a ground reading, it can cause the boom height control to jump
back and forth from a canopy to ground reading and cause erratic performance
[[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]].

**Ground with Canopy Assist** — When to use: Working in fields with 30–60% canopy coverage. This
setting is also recommended when excessive crop debris such as corn stubble remains in the field.
Description of Mode: This mode blends ground and canopy sensing, helping maintain consistent boom
height as crop canopy begins to interfere with ground sensors
[[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]].

**Canopy** — When to use: Operating in fields with 60% or more of canopy coverage. Description of
Mode: This mode relies primarily on canopy sensing, which is critical when dense crop cover prevents
accurate ground detection. Using the Canopy setting, the boom height control software filters out
the further of the two readings (distance to ground) and relies on the closer of the two readings
(distance crop) to set the boom height
[[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]].

![[NX1458211.png]]

**Figure NX1458211** — A: Ground; B: Ground with Canopy Assist; C: Canopy
[[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]]

The Boom System Application section describes the same three targets more briefly: Ground — used
when the field is fallow ground; Ground with Canopy Assist (Ground+) (if equipped) — typically used
when the field is partial canopy; Crop Canopy+ — used when the majority of the field is closed canopy
[[sensor-target--6c6fd9|Sensor Target]]. Note that Ground with Canopy Assist is marked "(if equipped)"
there [[sensor-target--6c6fd9|Sensor Target]].

To change it: select the Sensor Target box on the Boom System page, then select Ground, Ground with
Canopy Assist, or Canopy [[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]].

### Height Mode — Locked or Unlocked

Press height mode toggle button on the Boom System page to select between Unlocked Height Mode and
Locked Height Mode [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]].

![[NX1458247.png]]

**Figure NX1458247** — A: Height Mode Toggle Button
[[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]]

**Locked Height Mode** keeps the entire boom operating at the same height above the target (ground or
canopy) by matching the wing heights to the established center frame height; only the center target
height can be adjusted, and wing target heights are locked to match the center frame target height
[[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]]. When to Use Locked Height
Mode [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]]:

- Recommended for most applications where consistent spray height across the full boom is critical
  for optimal coverage and drift control.
- Ideal when operating in fields with moderate to dense canopy, where maintaining a stable, uniform
  spray height prevents wings from reacting independently to noisy canopy variations.
- Useful in relatively smooth terrain, where the center frame height provides a reliable reference
  point for the rest of the boom.

**Unlocked Height Mode** allows the operator to set different boom height targets for the left wing,
right wing, and center frame sections of the boom, and is intended for situations where the wings
must operate at heights different from the center frame to avoid obstacles or terrain-related
interference [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]]. Typical
scenarios [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]]:

- Rough or highly uneven terrain. Raising the wings above the center frame can help prevent the tips
  from dipping into the crop, striking the ground, or hitting sharp terraces or ridges.
- Operating in waterways, ditches, or rolling field transitions. The center frame may need to stay
  low for target spray height while the wings must run higher for safe clearance.
- Field edges, obstructions, or boundaries. Keeping a wing elevated can prevent contact with fences,
  posts, trees, washouts, or raised headlands.
- Specialty crops or fields with inconsistent canopy height. When crop height varies across the boom
  width, the operator may choose to run one or both wings higher than the center to avoid leaf or
  tassel contact.

The Boom System Application section says Locked Height Mode maintains the same height above the
target for the entire length of the boom — "Use this setting for most applications"
[[height-mode--b6109a|Height Mode]].

### Target Height

Target Heights are the distance from the bottom of the nozzle tips to the crop canopy or ground; each
boom section can be adjusted separately unless Height Mode is set to Locked, in which case only the
center boom section input box allows changes [[target-height--c66795|Target Height]]. To modify:
select the Target Height input box, enter the desired spray tip height using the keypad, and select
OK [[target-height--c66795|Target Height]].

> [!warning] NOTE
> NOTE: Only the Center section input box allows changes if the Match Center Height mode has been selected in Advanced Settings. [[target-height--c66795|Target Height]]

### Center Frame Control — ON or OFF

Select Center Frame Control toggle to change from ON to OFF
[[boomtrac-settings-center-frame--8fa924|BoomTrac Settings — Center Frame]]. As printed
[[boomtrac-settings-center-frame--8fa924|BoomTrac Settings — Center Frame]]:

**Center Frame OFF** — What happens: the center frame boom height sensor is used initially to
establish the initial center frame height; after that, the center frame control is disabled, and
only the wings adjust automatically. When to turn Center Frame Control to Off:

- If the center frame height sensor is not well aligned with the crop row spacing (sensor should be
  positioned in the middle of the row for best performance).
- If tire size or spacing causes the machine to run down the canopy rows, interfering with sensor
  accuracy.
- If the canopy under the center frame is too noisy (e.g., uneven crop or tire tracks), leading to
  incorrect readings.
- Excessive dust conditions – where dust from the tires may impact the Center Frame sensor readings.

**Center Frame ON** — What happens: the Center Frame Height Sensor continuously takes measurements to
actively adjust and maintain proper Center Frame height while the sprayer traverses through the
field. When to use:

- When operating in dense canopy conditions to prevent wings from running uphill or downhill due to
  an incorrect center frame height.
- When center frame boom height sensor is positioned correctly between rows to provide consistent
  height measurements to the ground/canopy.
- Operating in fallow ground.

The Boom System Application section adds: heavy dust or mud discharged by rear tires can cause poor
sensor signal and erratic boom movement, and you may choose to turn off the center sensor in these
conditions [[center-frame-control--9c2f13|Center Frame Control]].

### BoomTrac Presets

BoomTrac Presets allows you to quickly switch between two different BoomTrac configurations to react
to changing conditions — for example, one preset for normal spraying conditions and the other for
crossing waterways [[boomtrac-presets--f8f865|BoomTrac Presets]]. Select the desired preset, then
adjust settings such as height mode, target height, and sensor height; changes are automatically
saved to the selected preset [[boomtrac-presets--f8f865|BoomTrac Presets]].

### Sensor alignment (affects every setting above)

Sensors should be aligned so they are centered directly over the crop rows whenever possible; aim to
position the sensors within ± 203 mm (8 in) of the crop rows
[[boomtrac-settings-sensor-placement-setup--c8149c|BoomTrac Settings — Sensor Placement Setup]].
Proper alignment reduces sensor "noise," improves consistency of height readings, and provides more
stable boom control
[[boomtrac-settings-sensor-placement-setup--c8149c|BoomTrac Settings — Sensor Placement Setup]].

### Not the same thing: Return to Height "Height Mode"

Return to Height has its own Height Mode (OFF, Center, Left and Right, Left, Center, Right), which
chooses which boom sections stop at set points when raising/lowering
[[return-to-height-height-mode--a5b864|Return to Height — Height Mode]]. It is a different setting
from BoomTrac's Locked/Unlocked Height Mode. Using the correct return-to-height mode helps to prevent
you from lowering the boom too low and damaging the crop or the boom structure
[[return-to-height--5f2ad4|Return to Height]].

## Reading the guidance for a dense, uneven canopy

For example, fungicide into a thick, uneven soybean canopy covering well over half the ground:

- **Sensor Target:** 60% or more canopy coverage → Canopy
  [[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]].
- **Height Mode:** Locked Height Mode is ideal in moderate to dense canopy, where a uniform spray
  height prevents wings from reacting independently to noisy canopy variations
  [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]]. Unlocked is described for
  fields where crop height varies across the boom width
  [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]].
- **Center Frame Control:** ON in dense canopy conditions, to prevent the wings running uphill or
  downhill from an incorrect center frame height — **but** turn it OFF if the canopy under the center
  frame is too noisy (uneven crop or tire tracks), if the sensor is not aligned with the row spacing,
  or if the machine runs down the canopy rows
  [[boomtrac-settings-center-frame--8fa924|BoomTrac Settings — Center Frame]].

> [!inference] How the two center-frame rules combine
> "Dense canopy → ON" and "noisy canopy under the center frame → OFF" can both apply to a thick,
> uneven crop. The manual does not rank them. Start with ON, which the topic names for dense canopy,
> and switch to OFF if the center frame reading is erratic — the OFF condition is written as "leading
> to incorrect readings" [[boomtrac-settings-center-frame--8fa924|BoomTrac Settings — Center Frame]].
> The "Center frame moves up/down excessively" troubleshooting entry also points at the target type
> matching crop conditions [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]].

## What the manual does NOT specify

- **No target height value** for a crop, a canopy density, a product or a wind speed. The printed
  operating heights are the flat fan tip geometry [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]]
  (p. 55-6) and, on See & Spray machines, the camera confidence bands
  [[operating-conditions--8fd625|Operating Conditions]] (p. 135-5); neither is tied to a crop,
  product or wind. The 762 mm and 500 mm figures in "Heights the manual prints" are check heights for
  diagnostics and calibration, not operating settings. See also [[boom-height]].
- **No wind-to-height mapping.** The manual gives only the direction: raising the boom excessively
  above target increases drift risk [[height-mode--b6109a|Height Mode]] (p. 25-A-6).
- **Canopy percentage boundaries meet at 60%.** Ground with Canopy Assist is printed as 30–60% and
  Canopy as 60% or more
  [[boomtrac-settings-sensor-target-mode--909fda|BoomTrac Settings — Sensor Target Mode]]; the manual
  does not say which applies at exactly 60%, or how to measure coverage.
- **No priority between conflicting Center Frame conditions** (see the inference above).

## What overrides it

- **The product label** — for chemical application it governs, and the label may require a spray
  height, droplet class or wind limit; always follow all label directions
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
  For fungicide, the manual's tip types are Twin-Air Flat Fan, Guardian Flat Fan and Low-Drift Air
  [[spray-tip-types--eb73b8|Spray Tip Types]] — see [[spray-tip]].
- **The installed tip's chart** — the rated height and spacing for your tip.
- **Your John Deere dealer** — if BoomTrac does not hold height after the settings above, the
  troubleshooting table points to sensor readings, brackets, calibration and target type
  [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]].
