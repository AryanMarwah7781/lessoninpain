---
type: settings
title: "Slopes and rough ground (BoomTrac response, height mode, center frame, engine speed)"
models: [all]
options: [BoomTrac]
engine_tier: null
components: [BoomTrac sensor, boom, center frame, boom wing, engine, solution tank]
sources:
  - "ouo6092,1776448206631-19-27APR26"
  - "ouo6092,1777984488415-19-05MAY26"
  - "ouo6092,1776448178262-19-28APR26"
  - "ouo6092,1777984543287-19-05MAY26"
  - "ouo6092,1776448104189-19-27APR26"
  - "ouo6092,1777984522438-19-05MAY26"
  - "ouo6092,1777984352422-19-05MAY26"
  - "ouo6092,1777985140776-19-05MAY26"
  - "bn55050,1776442150178-19-20APR26"
  - "ouo6092,1775067618722-19-01APR26"
  - "ouo6092,1775067109003-19-01APR26"
  - "ouo6092,1775656336610-19-08APR26"
  - "ouo6092,1763041058521-19-27APR26"
  - "as09261,1711469474797-19-26MAR24"
  - "DX,WW,CHEM02-19-05APR04"
reviewed: true
compiled: 2026-09-23
---

# Slopes and rough ground

**Option: BoomTrac** for the boom settings on this page. The BoomTrac system automatically controls
boom tilt functions and center frame control relative to contours of the ground or crop canopy
[[boomtrac--783c2a|BoomTrac]]. If your machine does not have BoomTrac, the boom settings below do not
apply; the engine-speed, tank and driving items at the end apply to all machines. Sensor target,
target height and canopy guidance are on [[boom-height-settings]]; the component is on
[[boom-height]] and [[boom]].

## The condition

Spraying across slopes, rolling ground, waterways, ditches and terraces, where the boom must rise and
fall with the terrain. The manual says to modify BoomTrac when terrain contour changes or boom
lower/raise response is too slow or too fast [[boomtrac--783c2a|BoomTrac]].

## The manual's limits

> [!warning] CAUTION
> CAUTION: Avoid damage or contamination of your surroundings. Increasing boom height excessively above the target increases the risk of spray drift.
> [[height-mode--b6109a|Height Mode]]

> [!warning] CAUTION
> CAUTION: When transporting the machine downhill at transport speeds, the machine tries to hold the target speed until the engine starts to overspeed. At this time, the vehicle speed could increase beyond the target speed. Before starting down a hill, select a speed (less than 56.3 km/h [35 mph]) that is appropriate for the load on the machine and the steepness and length of the slope.
> [[drive-the-machine-auto-mode--c2def8|Drive the Machine—Auto Mode]]

The response table below gives slope bands for each response setting; the manual gives no maximum
slope for spraying.

## The levers (display page and setting names as printed)

On the **BoomTrac** page of the **Boom System** application [[boomtrac--783c2a|BoomTrac]]:

| Lever | As printed |
|---|---|
| **Lower/Raise Response** | Response speed of the boom lower/raise function [[boomtrac--783c2a|BoomTrac]]; settings 1–5, changed with + and - [[lower-raise-response--8c31a9|Lower/Raise Response]]. |
| **Height Mode** | Locked Height Mode or Unlocked Height Mode [[boomtrac--783c2a|BoomTrac]]. |
| **Center Frame Control** | Toggle to turn the center frame sensor ON/OFF [[boomtrac--783c2a|BoomTrac]]. |
| **BoomTrac Presets** | Quickly switch between different BoomTrac configurations [[boomtrac--783c2a|BoomTrac]]. |

Elsewhere: **Max Engine Speed** in the Engine application
[[max-engine-speed--e0681e|Max Engine Speed]], and **Low Tank Alarm** in the Tank System application
[[low-tank-alarm--a6bee8|Low Tank Alarm]].

## What the manual says each lever does

### Lower/Raise Response — the terrain table

Lower/Raise Response allows you to set the response speed of the boom raise and lower functions;
select + or - to change it
[[boomtrac-settings-raise-and-lower-response--678d41|BoomTrac Settings — Raise and Lower Response]].

**When to increase or decrease**, as printed
[[boomtrac-settings-raise-and-lower-response--678d41|BoomTrac Settings — Raise and Lower Response]]:

- Increase the response when the spray boom does not rise fast enough to avoid contact with the
  ground/ crop or the boom does not lower fast enough to avoid spray drift or skips in coverage.
- Decrease the raise response when the spray boom motion is not smooth or continuously adjusting
  height when minimal terrain height difference is present.

**Recommended Response Rates Based on Terrain**, as printed (hyphenation and slope bands exactly as in
the manual; cell layout checked against the rendered page — "Slopes" belongs to the <15% cell)
[[boomtrac-settings-raise-and-lower-response--678d41|BoomTrac Settings — Raise and Lower Response]]:

| Raise/ Lower Re-sponse | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Terrain Type | Flat | Mild | Mild/ Moderate | Moder-ate/ Aggres-sive | Aggres-sive |
| Max Slopes | 0—5% | 2—7% | <15% Slopes | >12% | >18% |
| Terrain Features | No Water-ways or crossings | Mild water-ways | Water-way crossings | Terraces, aggres-sive waterway crossing | Terraces, aggres-sive waterway crossing |

![[NX1458317.png]]

**Figure NX1458317** — Lower/Raise Response
[[boomtrac-settings-raise-and-lower-response--678d41|BoomTrac Settings — Raise and Lower Response]]

**What each setting is for**, as printed in the Boom System Application section
[[lower-raise-response--8c31a9|Lower/Raise Response]]:

- Setting 1 (least aggressive)— for use on flat ground where boom motion should be minimized.
- Setting 2 (less aggressive)— provides a less active boom track for flat to gentle rolling terrain
  and mild water ways while maintaining good performance.
- Setting 3 (nominal position)— provides the best stability for booms when cornering or performing
  S-curve operations. This setting can be used for most operating conditions, including flat to
  moderately rolling terrain and waterway crossings.
- Setting 4 (more aggressive)— provides improved ability to protect booms when encountering moderate
  terraces, aggressive water ways, or ditches. Booms appear more active during all operations.
- Setting 5 (most aggressive)— provides improved boom height performance on significant terraces,
  aggressive water ways, or other terrain features. Booms appear active across all terrains and
  become less stable during hard cornering or performing S-curve operations.

The same topic's Modify When: spray boom response speed is not fast enough — increase the lower/raise
response; spray boom motion is not smooth or continuously adjusts height when minimal terrain height
difference is present — decrease the lower/raise response
[[lower-raise-response--8c31a9|Lower/Raise Response]].

> [!inference] Reading the table for a slope of about six percent with mild waterways
> A six-percent slope falls inside the 2—7% band of setting 2, whose terrain features are "Mild water-ways"
> [[boomtrac-settings-raise-and-lower-response--678d41|BoomTrac Settings — Raise and Lower Response]],
> and setting 2 is described for "flat to gentle rolling terrain and mild water ways"
> [[lower-raise-response--8c31a9|Lower/Raise Response]]. So setting 2 is the starting point the
> manual's table points to. Six percent is also under the <15% band of setting 3, which is described as usable
> for most operating conditions, including waterway crossings
> [[lower-raise-response--8c31a9|Lower/Raise Response]]. If the boom does not rise fast enough to
> avoid the ground or crop, or does not lower fast enough to avoid drift or skips, increase the
> response; if it keeps hunting where the ground is nearly flat, decrease it
> [[boomtrac-settings-raise-and-lower-response--678d41|BoomTrac Settings — Raise and Lower Response]].
> The choice between 2 and 3 is yours; the manual does not rank overlapping bands.

### Height Mode on rough ground

Unlocked Height Mode is for situations where the wings must operate at heights different from the
center frame to avoid obstacles or terrain-related interference
[[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]]. The typical scenarios it
lists include [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]]:

- Rough or highly uneven terrain. Raising the wings above the center frame can help prevent the tips
  from dipping into the crop, striking the ground, or hitting sharp terraces or ridges.
- Operating in waterways, ditches, or rolling field transitions. The center frame may need to stay
  low for target spray height while the wings must run higher for safe clearance.

Locked Height Mode is useful in relatively smooth terrain, where the center frame height provides a
reliable reference point for the rest of the boom
[[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings — Height Mode]]. Raising the wings is still
subject to the drift CAUTION above [[height-mode--b6109a|Height Mode]]. Full Locked/Unlocked guidance
is on [[boom-height-settings]].

### Center Frame Control on slopes

Center Frame ON is to be used when operating in dense canopy conditions to prevent wings from running
uphill or downhill due to an incorrect center frame height
[[boomtrac-settings-center-frame--8fa924|BoomTrac Settings — Center Frame]]. Turn it OFF if the canopy
under the center frame is too noisy, if the sensor is not aligned with the row spacing, if the
machine runs down the canopy rows, or in excessive dust from the tires
[[boomtrac-settings-center-frame--8fa924|BoomTrac Settings — Center Frame]] — full list on
[[boom-height-settings]].

### BoomTrac Presets for waterways

One preset can be used for normal spraying conditions and the other preset for crossing waterways
[[boomtrac-presets--f8f865|BoomTrac Presets]]. Settings such as height mode, target height, and sensor
height are saved to the selected preset [[boomtrac-presets--f8f865|BoomTrac Presets]].

### Return to Height on rolling ground

Return to Height | Height Mode is modified when field terrain changes or crop height changes, and
chooses which boom sections stop at set points (OFF, Center, Left and Right, Left, Center, Right)
[[return-to-height-height-mode--a5b864|Return to Height — Height Mode]].

### Engine speed, tank level and moving on slopes (all machines)

- Max Engine Speed — Modify When: applying on hilly terrain, increase engine speed; applying on flat
  terrain, lower engine speed [[max-engine-speed--e0681e|Max Engine Speed]]. The setting range is
  Maximum: 2150 rpm Minimum: 1200 rpm [[max-engine-speed--e0681e|Max Engine Speed]].
- Hilly terrain increases power consumption [[engine-power--4234ca|Engine Power]].
- Low Tank Alarm indicates when the solution level is not sufficient for operating on hills; modify
  it when terrain requires a certain level of solution to maintain constant application
  [[low-tank-alarm--a6bee8|Low Tank Alarm]].
- Trailer loading mode allows the operator to move a machine that is parked on an incline or slope
  forward without the machine rolling back, in the field or for loading onto a trailer
  [[trailer-loading-mode--76716f|Trailer Loading Mode]].

## What the manual does NOT specify

- **No low-tank alarm value for a given slope** — the manual says the alarm helps on hills but gives
  no volume [[low-tank-alarm--a6bee8|Low Tank Alarm]].
- **No engine speed value for a given slope** — only "increase" on hilly terrain, within the printed
  range [[max-engine-speed--e0681e|Max Engine Speed]].
- **Overlapping slope bands.** The response table's bands overlap (0—5%, 2—7%, <15%, >12%, >18%) and
  the manual does not say which setting wins where two bands apply
  [[boomtrac-settings-raise-and-lower-response--678d41|BoomTrac Settings — Raise and Lower Response]].
  The "Max Slopes" row is also headed "Max" while two cells read ">12%" and ">18%".
- **How to measure slope or classify a waterway** as "mild" versus "aggressive" is not given.
- **No maximum spraying slope** or side-slope stability limit in these topics.

## What overrides it

- **The product label** for chemical application; always follow all label directions, and do not
  spray when winds exceed 16 km/h (10 mph)
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
- **What the boom actually does in motion.** Always evaluate BoomTrac performance while the machine is
  in motion, where sensors receive consistent terrain information and the system is able to respond
  as designed [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]]. The increase/decrease
  rules above take precedence over the table's starting point
  [[boomtrac-settings-raise-and-lower-response--678d41|BoomTrac Settings — Raise and Lower Response]].
- **Your John Deere dealer** — for poor or inconsistent control (slow response or erratic movement),
  the troubleshooting table lists incorrect or incomplete tilt valve calibration, and says to perform
  tilt valve calibration with warm/hot oil [[boomtrac-troubleshooting--cb1860|BoomTrac Troubleshooting]].
