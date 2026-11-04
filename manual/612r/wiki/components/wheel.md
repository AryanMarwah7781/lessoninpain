---
type: component
title: "Wheel"
models: [all]
options: []
engine_tier: null
components: [wheel, wheel motor, wheel mounting nut, final drive]
sources:
  - "OUO6092,0000ECC-19-25MAR21"
  - "TB90758,00028B3-19-08APR21"
  - "TB90758,00028A1-19-08APR21"
  - "OUO6092,0000EE1-19-03MAY21"
  - "bn55050,1778258392798-19-08MAY26"
  - "bn55050,1778258405478-19-08MAY26"
  - "bn55050,1775664203776-19-08APR26"
  - "ouo6092,1777578346785-19-30APR26"
  - "N0LMWLO,00003CA-19-30NOV20"
reviewed: true
compiled: 2026-09-23
---

# Wheel

This page is about the road wheels, their mounting hardware and the wheel motors. The *steering*
wheel in the cab is a different part — see [Steering wheel](#steering-wheel-in-the-cab) at the
bottom. Tires are covered on [[tire]].

## Warnings

> [!warning] IMPORTANT
> IMPORTANT: Damage to the planetary hub and wheel can occur when the correct mounting nut torque is not maintained. Tighten nuts in a crisscross pattern to specification. Tighten the wheel mounting nuts after the first 1 hour of use and every 10 hours thereafter until the correct torque is maintained. Check the torque on the wheel nuts after every 100 hours of use.
> [[tighten-wheel-hardware--d61ec1|Tighten Wheel Hardware]]

> [!warning] IMPORTANT
> IMPORTANT: Damage to the planetary hub and wheel can occur when the correct wheel hardware torque is not maintained. Tighten wheel hardware in a crisscross pattern to specification. Tighten wheel hardware after the first 10 hours of use and every 100 hours thereafter until the correct torque is maintained. Check wheel hardware torque after every 100 hours of use.
> [[tighten-wheel-hardware-100-hours--db6073|Tighten Wheel Hardware—100 Hours]]

## What it is

Each wheel is retained by wheel mounting nuts — twelve are called out in the wheel illustrations
[[tighten-wheel-hardware--d61ec1|Tighten Wheel Hardware]]. The wheel motors drive the wheels and
are calibrated from the display [[machine-calibration-wheel-motor--b49cd4|Machine Calibration | Wheel Motor]].

Wheel slip control system is designed to provide additional tractive effort when needed
[[wheel-slip-control--ff23e8|Wheel Slip Control]]. The system is always active and provides
additional tractive effort to the non-spinning wheels when one or more wheels spin out
[[wheel-slip-control--ff23e8|Wheel Slip Control]]. The wheel slip control system helps the machine
avoid becoming mired; it does not keep wheels from "spinning out" when mired
[[wheel-slip-control--ff23e8|Wheel Slip Control]].

## Where it is

![[N153564.png]]

**Figure N153564** — A: Wheel Mounting Nut (12 used) — 400R, 408R, 410R, and 412R
[[tighten-wheel-hardware--d61ec1|Tighten Wheel Hardware]]

![[N155091.png]]

**Figure N155091** — A: Wheel Mounting Nut (12 used) — 600R, 612R, and 616R
[[tighten-wheel-hardware--d61ec1|Tighten Wheel Hardware]]

![[N154907.png]]

**Figure N154907** — A: Wheel Mounting Nut (12 used), as shown in the maintenance topics; clamp
rings are shaded grey for visual appearance
[[tighten-wheel-hardware-100-hours--db6073|Tighten Wheel Hardware—100 Hours]]

## Related procedures

### Tighten wheel hardware

Check torque on the wheel hardware and tighten wheel mounting nuts (A) in a crisscross pattern to
specification [[tighten-wheel-hardware--d61ec1|Tighten Wheel Hardware]].

Specification — Wheel Mounting Nuts—Torque (dry): 531 N·m (392 lb·ft)
[[tighten-wheel-hardware--d61ec1|Tighten Wheel Hardware]]. The same value is printed in the
maintenance topics [[tighten-wheel-hardware-100-hours--db6073|Tighten Wheel Hardware—100 Hours]]
and [[tighten-wheel-hardware-after-first-10-hours--5797ef|Tighten Wheel Hardware—After First 10 Hours]].

The manual schedules the same check in two places, and the intervals printed there do not agree.

> [!conflict] Wheel hardware retightening interval
> The Wheels and Tires section says to tighten the wheel mounting nuts "after the first 1 hour of
> use and every 10 hours thereafter until the correct torque is maintained"
> [[tighten-wheel-hardware--d61ec1|Tighten Wheel Hardware]], while the Lubrication and Maintenance
> section says to tighten wheel hardware "after the first 10 hours of use and every 100 hours
> thereafter until the correct torque is maintained"
> [[tighten-wheel-hardware-100-hours--db6073|Tighten Wheel Hardware—100 Hours]] — the same wording
> appears in the after-first-10-hours topic
> [[tighten-wheel-hardware-after-first-10-hours--5797ef|Tighten Wheel Hardware—After First 10 Hours]].
> Both are machine-specific topics (neither is a generic Deere-wide module) and both give the same
> torque and the same "check after every 100 hours of use" rule; only the run-in interval differs.
> This page does not choose between them. Confirm the interval for your machine with your John Deere
> dealer, and if in doubt the shorter interval is the more frequent check.

### Wheel motor calibration

Machine Calibration | Wheel Motor calibrates the wheel motors
[[machine-calibration-wheel-motor--b49cd4|Machine Calibration | Wheel Motor]]. The recommended
interval is "As needed" and the estimated time required is "Less than 1 min"
[[machine-calibration-wheel-motor--b49cd4|Machine Calibration | Wheel Motor]].

Procedure requirements: engine running, Wheel Speed 0 km/h (0 mph), and the operating state in
Park, not applying product
[[wheel-motor-calibration-procedure--23b7fb|Wheel Motor Calibration Procedure]]. Select Calibrate
to begin, follow the messages on-screen, and confirm the calibration by selecting Save
[[wheel-motor-calibration-procedure--23b7fb|Wheel Motor Calibration Procedure]].

## Related settings

- **Steering mode** selects how the wheels can be steered: Two-Wheel Steer (recommended for use
  during spraying), Four-Wheel Steer (recommended for use on headlands) and Crab Steer
  [[steering-mode--5ec80a|Steering Mode]]. See [[steering]].
- **Speed source.** Select Wheel Speed when the GPS signal is degraded, GPS is not installed, or
  wheel slip is not likely to occur; select GPS when wheel slip is likely to occur
  [[rate-control-display-speed--8b68eb|Rate Control/Display Speed]]. See [[display]].

## Related troubleshooting

- The wheel motor calibration page shows current (in milliamps), frequency (in hertz) and variance
  readings for the left-front/left-rear and right-front/right-rear wheel motors, which is where a
  side-to-side difference would show up
  [[machine-calibration-wheel-motor--b49cd4|Machine Calibration | Wheel Motor]].
- If the wheel motor calibration fails, select Retry and verify that all requirements listed
  on-screen have been met; if the calibration fails twice, see your John Deere dealer or service
  provider [[wheel-motor-calibration-procedure--23b7fb|Wheel Motor Calibration Procedure]].
- Uneven wear, replacement sizes and tire inspection are on [[tire]], not here.

## Steering wheel in the cab

Do not confuse the road wheels with the steering wheel. Tilt/Telescope — pull the lever away from
the steering column to allow adjustments, tilt and telescope the upper steering column to the
desired position, then push the lever toward the steering column to lock the position
[[adjusting-steering-wheel--7b011f|Adjusting Steering Wheel]]. Memory — grasp the steering wheel
with both hands and push down on the foot pedal to permit free movement of the full steering
column, then release the foot pedal to lock the column into the current position
[[adjusting-steering-wheel--7b011f|Adjusting Steering Wheel]].
