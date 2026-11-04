---
type: component
title: "Steering"
models: [all]
options: []
engine_tier: null
components: [steering, steering wheel, wheel, axle, suspension, grease points]
sources:
  - "UZEGGEY,1765785596814-19-11MAY26"
  - "UZEGGEY,1768888205923-19-20JAN26"
  - "bn55050,1775664189970-19-01MAY26"
  - "az06166,1747422108306-19-08MAY26"
  - "bn55050,1775664203776-19-08APR26"
  - "az06166,1747425314830-19-27APR26"
  - "N0LMWLO,00003CA-19-30NOV20"
  - "OUO6092,0000C6F-19-06APR17"
  - "OUO6092,0000A39-19-07JUL06"
  - "CS12167,00009CB-19-17APR17"
  - "AM24480,1772511295181-19-08MAR26"
  - "ouo6092,1763581488776-19-04MAY26"
  - "OUO6092,0000BDE-19-09MAY17"
  - "ouo6092,1741882981520-19-13MAR25"
  - "ouo6092,1737474660828-19-29OCT25"
  - "ouo6092,1737555432812-19-27OCT25"
  - "DX,TIRE,INFO-19-19MAY14"
reviewed: true
compiled: 2026-09-23
---

# Steering

## What it is

The steering system is hydrostatic, controlled by a steering control valve, with a relief pressure
of 18 961 kPa (190 bar) (2750 psi)
[[machine-specification--bfe721|Machine Specification]]. Two-wheel steer operation uses two double
acting cylinders and four-wheel steer operation uses four double acting cylinders
[[machine-specification--bfe721|Machine Specification]]. Turning radius is 9.2 m (30.2 ft) in
two-wheel steer and 6.4m (20.9ft) in four-wheel steer
[[machine-specification--bfe721|Machine Specification]].

Three steering modes are available
[[steering-mode--5ec80a|Steering Mode]]:

- **Two-Wheel Steer** — recommended for use during spraying. Reduces yaw in the machine and boom,
  which improves stability and reduces swaying of the boom
  [[steering-mode--5ec80a|Steering Mode]].
- **Four-Wheel Steer** — recommended for use on headlands as it improves maneuverability of the
  machine and reduces crop damage due to the front and rear wheels following similar tracks.
  Four-wheel steer can also be used during road transport to maneuver around tight turns
  [[steering-mode--5ec80a|Steering Mode]].
- **Crab Steer** — useful in certain circumstances such as avoiding soil compaction by offsetting
  the front and rear axle and driving in different tracks. Crab steer can also assist in
  circumstances when the operator needs to avoid an obstacle while maintaining the machine heading
  [[steering-mode--5ec80a|Steering Mode]].

The same three-mode description is printed a second time in the Operate the Machine section
[[steering-mode--4e542c|Steering Mode]].

See [[wheel]] and [[tire]] for what the steering system moves, and
[[commandarm]] for the buttons.

## Where it is

Adjust the steering wheel with the tilt/telescope lever and the memory foot pedal
[[adjusting-steering-wheel--7b011f|Adjusting Steering Wheel]].

![[H127043.png]]
**Figure H127043** — Tilt/Telescope
[[adjusting-steering-wheel--7b011f|Adjusting Steering Wheel]]

Pull the lever away from the steering column to allow adjustments, tilt and telescope the upper
steering column to the desired position, then push the lever toward the steering column to lock the
position [[adjusting-steering-wheel--7b011f|Adjusting Steering Wheel]]. For the memory function,
grasp the steering wheel with both hands and push down on the foot pedal to permit free movement of
the full steering column, then release the foot pedal to lock the column into the current position
[[adjusting-steering-wheel--7b011f|Adjusting Steering Wheel]].

The steering controller (ATX) serial number is on the unit located behind the storage compartment
on the left-hand side of the machine [[identification-numbers--b5c28c|Identification Numbers]].

The steering cylinder ball joints have grease fittings (A)
[[lubricate-steering-cylinder-ball-joints-100-hours--b61afd|Lubricate Steering Cylinder Ball Joints— 100 Hours]].

![[N98883.png]]
**Figure N98883** — A: Grease Fitting
[[lubricate-steering-cylinder-ball-joints-100-hours--b61afd|Lubricate Steering Cylinder Ball Joints— 100 Hours]]

## Related settings

![[WZ1405080.png]]
**Figure WZ1405080** — Steering Mode [[steering--14dc8e|Steering]]

The Steering page allows you to change four-wheel steering modes; modify it when you need to change
between two-wheel steering and four-wheel steering [[steering--14dc8e|Steering]]. Steering Mode
displays the active steering mode and current angle of the wheels
[[steering--14dc8e|Steering]]. Four-Wheel Steering Max Speed displays the maximum travel speed at
which four-wheel steering is still engaged; speeds above the maximum set speed cause the machine to
revert to two-wheel steering mode [[steering--14dc8e|Steering]]. Select the plus (+) symbol to
increase the maximum speed, the minus (-) symbol to decrease it, or the current maximum speed value
to open a keypad and enter the desired maximum speed [[steering--14dc8e|Steering]].

The manual prints the same Steering page description twice — once in the Chassis System Application
section [[steering--14dc8e|Steering]] and once in Operate the Machine
[[steering--9906de|Steering]]. The text is identical; the manual does not give a numeric default or
limit for the four-wheel steering maximum speed in either place.

Select four-wheel steer mode by pressing the button on the CommandARM or pressing the four-wheel
steer foot switch; press the CommandARM button or foot switch again to return to two-wheel steer
mode [[steering-mode--5ec80a|Steering Mode]]. Select crab steer mode by pressing the button on the
CommandARM; press the CommandARM button again to return to two-wheel steer mode
[[steering-mode--5ec80a|Steering Mode]].

### AutoTrac steering optimization (if equipped with AutoTrac)

Monitor Performance shows heading error and tracking error and is designed to aid in tuning of
Advanced AutoTrac Settings [[steering-optimization--98e3ad|Steering Optimization]]. Heading Error
should be within +/- 1 degree; adjust as needed if outside of this range
[[steering-optimization--98e3ad|Steering Optimization]]. The adjustable settings and their ranges
[[steering-optimization--98e3ad|Steering Optimization]]:

| Setting | What it does | Range |
|---|---|---|
| Line Sensitivity Tracking | Determines how aggressively AutoTrac responds to off-track (lateral) error | 50–200 |
| Heading Lead | Determines impact of yaw rate (machine rate of turn) on tracking performance | 50–130 |
| Line Sensitivity Heading | Determines how aggressively AutoTrac responds to Heading Errors | 50–200 |
| Steering Response Rate | Adjusts rate of machine steering to maintain tracking performance | 50–200 |
| Acquire Sensitivity | Determines how aggressively machine acquires track | 50–200 |
| Curve Sensitivity | Determines how aggressively AutoTrac responds to a curve in track | 50–200 |

Higher settings give a more aggressive response and lower settings a less aggressive response for
Line Sensitivity Tracking, Heading Lead and Line Sensitivity Heading; for Heading Lead, large
adjustments may result in poor performance
[[steering-optimization--98e3ad|Steering Optimization]].

When switching between Float tire and Row Crop tire, select the appropriate Tire Type in the
AutoTrac Steering Optimization settings to ensure optimal AutoTrac performance
[[autotrac-tuning-with-tire-changes--f75fa8|AutoTrac Tuning with Tire Changes]]. Machines with the
largest tire size width of 800 mm require additional steering optimization settings — Steering
Sensitivity: 75, Heading Lead: 75, Steering Response Rate: 75
[[autotrac-tuning-with-tire-changes--f75fa8|AutoTrac Tuning with Tire Changes]]. That procedure only
applies to wet systems with a liquid skid and not to dry systems
[[autotrac-tuning-with-tire-changes--f75fa8|AutoTrac Tuning with Tire Changes]].

## Related procedures

### Rephasing the steering system

Rephasing is required before road transport
[[check-front-axle-toe-in-annually-or-as-needed--b4cc6e|Check Front Axle Toe-In—(Annually or as Needed)]],
and the same note is repeated in the 100-hour tire wear check
[[inspect-tires-for-uneven-wear-100-hours--6bad5a|Inspect Tires For Uneven Wear—100 Hours]].
To rephase: turn the wheels full left, then turn the steering wheel three additional revolutions
while slowly moving forward at around 0.8 km/h (0.5 mph); turn the wheels full right and repeat;
then repeat these steps 1—3 more times
[[check-front-axle-toe-in-annually-or-as-needed--b4cc6e|Check Front Axle Toe-In—(Annually or as Needed)]].

Front wheel toe-in specification is 0—10 mm (0—0.375 in), measured at the wheel rim
[[check-front-axle-toe-in-annually-or-as-needed--b4cc6e|Check Front Axle Toe-In—(Annually or as Needed)]].

### Lubrication

Lubricate steering cylinder ball joints (A) using John Deere SD Polyurea Grease every 100 hours
[[lubricate-steering-cylinder-ball-joints-100-hours--b61afd|Lubricate Steering Cylinder Ball Joints— 100 Hours]].
Use ONLY SD POLYUREA GREASE, Part Number TY6341
[[suspension-and-steering-grease--f4a9c8|Suspension and Steering Grease]].

### Warm-up

As the engine and hydraulic fluid warm up, cycle the steering wheel back and forth to circulate warm
hydraulic fluid; continue until steering turns freely
[[warm-the-engine--a6676a|Warm the Engine]].

## Related warnings

> [!warning] IMPORTANT — rephase before setting toe-in
> IMPORTANT: Failure to rephase steering system before setting toe-in can result in insufficient
> ball joint thread engagement on cylinder barrel.
> [[check-front-axle-toe-in-annually-or-as-needed--b4cc6e|Check Front Axle Toe-In—(Annually or as Needed)]]

> [!warning] IMPORTANT — grease type
> IMPORTANT: Use only John Deere SD Polyurea Grease for lubricating suspension and steering
> components. Use of other greases in the suspension system is not recommended. Use of other greases
> can result in premature wear of the suspension components.
> [[lubricate-steering-cylinder-ball-joints-100-hours--b61afd|Lubricate Steering Cylinder Ball Joints— 100 Hours]]

> [!warning] IMPORTANT — tires affect steering
> IMPORTANT: Installing tires that do not meet original equipment tire specifications may cause
> machine malfunction. Consult a John Deere dealer, other service provider, or tire supplier. Use of
> substandard tires or larger than recommended tires voids the warranty and decreases stability,
> affects steering, results in premature tire failure, or causes other durability or safety issues.
> [[machine-specification--bfe721|Machine Specification]]

Use of other than prescribed tires may decrease stability, affect steering, result in premature tire
failure, or cause other durability or safety issues — this comes from a generic Deere-wide safety
module [[follow-tire-recommendations--fe9e2b|Follow Tire Recommendations]]. See
[[tire]].

## Related troubleshooting

- **Erratic steering** — hydraulic oil overheated: fill tank to the proper level, clean oil cooler
  and screens. Pump faulty: replace pump
  [[hydraulic-system--47f651|Hydraulic System]].
- **AutoTrac slow to acquire line or sluggish response** — clean AutoTrac strainer
  [[hydraulic-system--47f651|Hydraulic System]].
- **Excessive play in suspension or steering components** — main suspension spindles or bushings
  are worn: contact a John Deere dealer or other service provider
  [[suspension-system--105ebe|Suspension System]].
- **Uneven tire wear** — inspect tires for uneven wear; if uneven wear is found, rotate the tires
  and check for component wear that may be causing the wear
  [[inspect-tires-for-uneven-wear-100-hours--6bad5a|Inspect Tires For Uneven Wear—100 Hours]].

## What the manual does not specify

- No numeric value or default is given for the Four-Wheel Steering Max Speed setting
  [[steering--14dc8e|Steering]].
- The Steering Optimization ranges are given, but the manual does not give a recommended starting
  value for each setting except for the 800 mm tire case
  [[steering-optimization--98e3ad|Steering Optimization]]
  [[autotrac-tuning-with-tire-changes--f75fa8|AutoTrac Tuning with Tire Changes]].
