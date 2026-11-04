---
type: component
title: "Solution Tank"
models: [all]
options: [Dual Product, Target Fill, Load Command]
engine_tier: null
components: [solution tank, sump valve, tank level sensor, agitation, rinse tank, eductor]
sources:
  - "as09261,1712163885782-19-16APR24"
  - "as09261,1710340206090-19-28APR26"
  - "ouo6092,1775656123332-19-08APR26"
  - "ouo6092,1775656278878-19-09APR26"
  - "ouo6092,1775656304972-19-08APR26"
  - "ouo6092,1775656336610-19-08APR26"
  - "ouo6092,1776103583076-19-13APR26"
  - "ouo6092,1777652885033-19-06MAY26"
  - "ouo6092,1763568430102-19-27APR26"
  - "ouo6092,1763136269181-19-27APR26"
  - "bn55050,1778258807890-19-08MAY26"
  - "BN55050,000025A-19-08JUN18"
  - "BN55050,000025D-19-23MAY18"
  - "AOTA2VY,000043B-19-23MAR21"
  - "AOTA2VY,0000439-19-20MAY21"
  - "DX,WW,CHEM02-19-05APR04"
  - "UZEGGEY,1765785596814-19-11MAY26"
reviewed: true
compiled: 2026-09-23
---

# Solution Tank

The solution tank holds the product being applied, feeds the solution pump through the sump valve,
and is agitated, rinsed and drained through valves at its bottom and top. Capacity and construction
depend on the model, and a dual product machine has two reservoirs in one tank.

## Warnings

> [!warning] DANGER
> DANGER
> Tank contents are poisonous. Do not enter tank.
> [[tank-decal--dc661a|Tank Decal]]

> [!warning] CAUTION
> CAUTION: Spray system can contain hazardous material, which can cause serious injury or death to you or others. Wear protective clothing, eyewear, and gloves. Drain solution tank in an area where people, animals, vegetation, water supply, and so on, cannot be contaminated.
> [[drain-solution-tank--463f0b|Drain Solution Tank]]

> [!warning] CAUTION
> CAUTION: Quik-Fill valve (A) can contain hazardous materials that could cause injury or be poisonous. Before removing Quik-Fill cap (B), verify that Quik-Fill valve is closed.
> [[drain-solution-tank--463f0b|Drain Solution Tank]]

> [!warning] CAUTION
> CAUTION: The solution tanks can contain hazardous chemicals that can cause serious injury or death to you or others. Wear protective clothing, eyewear, and gloves. Drain the solution tanks in an area where people, animals, vegetation, water supply, and so on, cannot be contaminated. Do not drain solution onto the ground. Drain solution into a suitable container and dispose of properly.
> [[drain-solution-tanks--b529bf|Drain Solution Tanks]]

There is also a Do Not Stand On Tank decal on the machine
[[do-not-stand-on-tank-decal--5b452a|Do Not Stand On Tank Decal]].

Always follow all label directions for effective, safe, and legal use of agricultural chemicals
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]];
properly dispose of unused chemicals, flushing solution, and empty chemical containers
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].

## What it is

**Standard (single) solution system.** The 408R solution tank is made from polyethylene or stainless
steel (optional) and has a capacity of 3028 L (800 gal)
[[solution-system--544787|Solution System]]. The 410R solution tank is stainless steel and has a
capacity of 3785 L (1000 gal) [[solution-system--544787|Solution System]]. The 412R and 612R
solution tanks are stainless steel and have a capacity of 4542 L (1200 gal)
[[solution-system--544787|Solution System]]. The 616R solution tank is stainless steel and has a
capacity of 6056 L (1600 gal) [[solution-system--544787|Solution System]]. An access/fill cap is at
the top of the tank [[solution-system--544787|Solution System]].

**Dual product solution system.** This sprayer is equipped with a stainless steel dual product
solution tank that is divided into two separate reservoirs: a smaller reservoir (tank 1) intended
for spot spray application and a larger reservoir (tank 2) intended for broadcast spray application
[[solution-system--3fd9a2|Solution System]]. Solution tanks are available with the following fluid
capacities [[solution-system--3fd9a2|Solution System]]:

| Entire Tank | Tank 1 | Tank 2 |
|---|---|---|
| 3785 L (1000 gal) | 1324 L (350 gal) | 2461 L (650 gal) |
| 4542 L (1200 gal) | 1703 L (450 gal) | 2839 L (750 gal) |
| 6057 L (1600 gal) | 2271 L (600 gal) | 3786 L (1000 gal) |

[[solution-system--3fd9a2|Solution System]]

> [!conflict] 1600 gal tank stated as 6056 L, 6057 L and 6065 L
> The manual prints three different metric values for the same 1600 gal tank, and none of the three
> topics is a generic Deere-wide module:
> - The Single Solution Command System topic gives the 616R solution tank capacity as 6056 L
>   (1600 gal) [[solution-system--544787|Solution System]].
> - The Dual System Command System capacity table gives the entire tank as 6057 L (1600 gal)
>   [[solution-system--3fd9a2|Solution System]].
> - The Machine Specification table gives 616R Capacity as 6065 L (1600 gal)
>   [[machine-specification--bfe721|Machine Specification]].
>
> All three print the same US value, 1600 gal, and three different metric values. The first two
> topics describe different tank arrangements, so they may not be the same tank; the specification
> table is machine-level. This page does not pick one. Confirm the capacity for your machine with
> your John Deere dealer.

**Fittings and level indication.** Each solution tank is equipped with a fill neck and lid assembly
[[solution-system--3fd9a2|Solution System]]. On the left-hand side of the machine, there is a clear
tube and graduated scale that indicates the solution level in liters and gallons
[[solution-system--544787|Solution System]]; on a dual product machine there are clear tubes and
graduated scales for each tank system [[solution-system--3fd9a2|Solution System]]. At the bottom of
the tank is the solution tank sump valve [[solution-system--544787|Solution System]], which allows
the solution tank to be drained out the side Quik-Fill valve and supplies the solution pump with
solution fluid [[solution-system--544787|Solution System]].

**Rinse and eductor nozzles.** Tank rinse nozzles in the solution tank are used during a rinse cycle
to clean the inside walls of the tank [[solution-system--544787|Solution System]]. The tank rinse
nozzle/eductor valve either directs solution fluid to the tank rinse nozzles at the top of the
solution tank or directs solution fluid to the eductor venturi
[[solution-system--544787|Solution System]].

**Agitation nozzles.** Agitation nozzles are in four locations on the bottom of the tank
[[solution-system--544787|Solution System]]; see [[agitation|Agitation]].

## Where it is

The single solution system, with the solution tank (1), tank rinse nozzle (2), agitation nozzle (3),
agitation valve (4) and sump valve (5) [[solution-system--544787|Solution System]]:

![[N167216.png]]

**Figure N167216** — 408R and 410R Solution Command System
[[solution-system--544787|Solution System]]

The drain ports are located on the bottom side of the machine underneath the solution tank, and
underframe shields must be lowered to access the drain ports
[[drain-solution-tanks--b529bf|Drain Solution Tanks]]:

![[N161194.png]]

**Figure N161194** — A: Drain Port (tank 1); B: Drain Port (tank 2); C: Menu Button (tank system 1);
D: Menu Button (tank system 2) [[drain-solution-tanks--b529bf|Drain Solution Tanks]]

The Tank System application is reached through the display: Menu, then the Machine Settings tab,
then Tank System; or by pressing the Tank System button on the navigation bar below the display
[[access-tank-system--f3b14b|Access Tank System]].

## Related procedures

- **Fill the tank.** The solution tanks can be filled through the fill necks or through the main
  Quik-Fill valve at the side load station on the left-hand side of the machine or the front load
  station on the front right-hand side of the machine
  [[solution-system--3fd9a2|Solution System]]. Solution can be pushed on using a pump provided with
  the nurse tank or can be pulled on using the onboard POWRSPRAY pump
  [[solution-system--3fd9a2|Solution System]]. The individual filling procedures are separate topics
  per load station and tank configuration, for example
  [[fill-solution-tank-with-nurse-tank-pump-side-fill--445903|Fill Solution Tank with Nurse Tank Pump— Side Fill]]
  and
  [[fill-solution-tank-1-with-nurse-tank-pump-front-fill--d44b44|Fill Solution Tank 1 with Nurse Tank Pump —Front Fill]].
- **Drain a single solution tank.** Verify that the Quik-Fill valve is closed, open the lock levers
  and remove the cap, connect a nurse tank hose or place a suitable container under the Quik-Fill,
  press the menu button on the keypad, press the drain tank button on the micro display, monitor the
  fluid level and press cancel to close the drain valve, then remove the hose, close the Quik-Fill
  valve and replace the cap [[drain-solution-tank--463f0b|Drain Solution Tank]].
- **Drain dual solution tanks.** Open the lock levers and remove the cap from the drain port for the
  tank to be drained, place a suitable container below the drain port or connect a nurse tank hose,
  press the menu button on the keypad for the tank system being drained, press the drain tank button
  on the micro display, monitor the level and press cancel when the desired fluid level is reached,
  then install the cap and close the lock levers
  [[drain-solution-tanks--b529bf|Drain Solution Tanks]].
- **Mix the solution.** See [[agitation|Agitation]] and
  [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]].
- **Check the tank straps (poly tank only).** At both intervals below, fill the solution tank and
  check the solution tank straps for tightness; if loose, loosen the lock
  nuts, tighten until straps are snug and then turn nuts an additional two turns, and tighten the
  lock nuts
  [[check-solution-tank-straps-after-first-ten-hours-poly-tank-o--9bb6e5|Check Solution Tank Straps—After First Ten Hours (Poly Tank Only)]]
  [[check-solution-tank-straps-250-hours-poly-tank-only--31db94|Check Solution Tank Straps—250 Hours (Poly Tank Only)]].
- **Calibrate the tank level sensor.** The procedure requires the engine OFF with the key in the Run
  position, the machine parked, the rinse tank empty, and the solution pump off with plumbing open;
  on standard solution systems the solution tank must also be empty
  [[solution-tank-level-sensor-procedure--1225f2|Solution Tank Level Sensor Procedure]]. If
  calibration fails, select Retry and verify that all requirements listed on-screen have been met;
  if calibration fails twice, contact your John Deere dealer or other service provider
  [[solution-tank-level-sensor-procedure--1225f2|Solution Tank Level Sensor Procedure]].

## Related settings

All on the Tank System application [[access-tank-system--f3b14b|Access Tank System]]:

- **Tank Fill Volume** allows you to enter the current solution tank level using one of two presets,
  and must be used after adding solution to the tank to display the current tank volume accurately
  [[tank-fill-volume--7949c3|Tank Fill Volume]]. It must be used to allow the low tank alarm to
  function properly and to allow you to verify that proper application rates are being achieved
  [[tank-fill-volume--7949c3|Tank Fill Volume]].
- **Low Tank Alarm** audibly alerts you when the tank volume is below the preset level, and
  indicates when to turn off agitation to reduce foaming, refill the tank, or when the solution
  level is not sufficient for operating on hills [[low-tank-alarm--a6bee8|Low Tank Alarm]]. Modify
  it when changing the alarm threshold is desired, or when terrain requires a certain level of
  solution to maintain constant application [[low-tank-alarm--a6bee8|Low Tank Alarm]].
- **Current Tank Volume** displays the anticipated tank volume based on your input and the
  calculated solution usage or target fill sensor (if equipped)
  [[tank-system-main-page--42f006|Tank System Main Page]].
- **Specific Gravity** displays the current specific gravity setting for the product being used
  [[tank-system-main-page--42f006|Tank System Main Page]].
- **Target Fill** (if equipped) automatically fills the tank to a desired level
  [[tank-system-main-page--42f006|Tank System Main Page]].
- **Tank configuration.** On a machine with a standard solution system the icon is Single Tank —
  only one solution tank is available on this machine
  [[sprayer-setup-tank-configuration-icons--a2d851|Sprayer Setup — Tank Configuration Icons]]. On a
  dual product machine the configurations are Dual Independent Tanks, Single Independent Tank 1,
  Single Independent Tank 2 and Combined Tanks
  [[sprayer-setup-tank-configuration-icons--a2d851|Sprayer Setup — Tank Configuration Icons]]. With
  Single Independent Tank 1 or 2 the other tank is inactive, but agitation is available
  [[sprayer-setup-tank-configuration-icons--a2d851|Sprayer Setup — Tank Configuration Icons]]. Which
  spray modes each configuration supports is listed on the Tank Configuration screen, and pumps must
  be turned off before changing tank configuration
  [[tank-configuration--1faae2|Tank Configuration]].

## Related warnings

The callouts under [Warnings](#warnings) above are carried by the tank topics and decals. The rule
that governs everything put into the tank is the product label
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].

## Related troubleshooting

- A tank volume that does not match reality is usually an input problem, not a sensor problem: tank
  fill volume must be used after adding solution for the displayed volume, the low tank alarm and
  the rate check to be right [[tank-fill-volume--7949c3|Tank Fill Volume]]. For automatic agitation
  to operate correctly, solution tank volume must be reset when tank is filled or solution is added
  [[agitation--995e05|Agitation]].
- Foaming at low tank level is addressed by agitation level, not by the tank — see
  [[agitation|Agitation]].
- If the level sensor calibration fails twice, contact your John Deere dealer or other service
  provider [[solution-tank-level-sensor-procedure--1225f2|Solution Tank Level Sensor Procedure]].

> [!inference] Scope of this page
> The manual describes the tank inside the Solution System overviews (one for the single solution
> machine, one for the dual product machine), in the Tank System display application, in the fill
> and drain procedures, and on the decals. This page gathers those and adds no facts of its own.
> Model-specific capacities are quoted from the topic that states them, per model.
