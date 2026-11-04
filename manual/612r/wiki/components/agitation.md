---
type: component
title: "Agitation"
models: [all]
options: [Dual Product, Load Command]
engine_tier: null
components: [agitation, agitation valve, agitation nozzle, solution tank, solution pump]
sources:
  - "ouo6092,1775656637108-19-08APR26"
  - "ouo6092,1775656663701-19-08APR26"
  - "ouo6092,1763567551641-19-27APR26"
  - "bn55050,1769006118343-19-21JAN26"
  - "ouo6092,1775656278878-19-09APR26"
  - "ouo6092,1775656336610-19-08APR26"
  - "ouo6092,1775656123332-19-08APR26"
  - "as09261,1712163885782-19-16APR24"
  - "as09261,1710340206090-19-28APR26"
  - "aota2vy,1686142179306-19-07JUN23"
reviewed: true
compiled: 2026-09-23
---

# Agitation

Agitation circulates solution in the tank to aid in keeping chemicals in suspension, and is also
used to mix chemical solution in the tank when required [[agitation--995e05|Agitation]]. It is
hydraulic: the solution pump feeds the agitation circuit through the agitation valve, so the pump
runs whenever agitation runs [[solution-system--544787|Solution System]].

## Warnings

The agitation topics carry no DANGER, WARNING or CAUTION blocks of their own. The notes below are
the manual's own NOTE blocks, verbatim.

> [!warning] NOTE
> NOTE: Agitation Level and Agitation Boost Level will be set to 100% if Power Agitation is turned ON.
> [[agitation--995e05|Agitation]]

> [!warning] NOTE
> NOTE: For automatic agitation to operate correctly, solution tank volume must be reset when tank is filled or solution is added. See Tank Fill Volume.
> [[agitation--995e05|Agitation]]

> [!warning] NOTE
> NOTE: It is recommended to turn off agitation when tank volume is below 378.5 L (100 gal) to reduce foaming.
> [[agitation--995e05|Agitation]]

> [!warning] NOTE
> NOTE: To minimize foaming, operate agitation at a lower rate. Turn off agitation when tank volume drops below 378.5 L (100 gal) to prevent foaming and air in system.
> [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]]

Anything mixed in the tank is governed by the product label
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].

## What it is

Agitation nozzles are in four locations on the bottom of the tank; the nozzles create a vigorous
fan-type agitation throughout the tank to keep chemicals, such as wettable powders, in suspension
[[solution-system--544787|Solution System]]. The agitation valve controls the agitation flow and
has three settings (1 —3), which can be selected by the operator through the display located in the
operator's station cab [[solution-system--544787|Solution System]]. The agitation valve can be
opened by a button on the Fill Station keypad and by a button on the CommandARM armrest in the
operator's station cab [[solution-system--544787|Solution System]].

On a dual product machine, agitation nozzles are mounted in four locations in the bottom of each
tank, and each tank has its own agitation valve
[[solution-system--3fd9a2|Solution System]]. When a tank is inactive in a single-independent-tank
configuration, agitation is still available for it
[[sprayer-setup-tank-configuration-icons--a2d851|Sprayer Setup — Tank Configuration Icons]].

Pump speed and agitation valve setting determine the amount of agitation
[[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]]. The
solution pump is also turned ON when agitation is turned ON
[[agitation--995e05|Agitation]].

## Where it is

Agitation is operated from the load station keypad and from the cab. On the load station keypad the
buttons are the solution pump on/off and the agitation on/off
[[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]], with a
second pair of buttons on the intensity keypad
[[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]]:

![[NX1440413.png]]

**Figure NX1440413** — A: Intensity Increase Button; B: Intensity Decrease Button; C: Auto Intensity
On/Off Button; D: Power Agitation On/Off Button
[[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]]

In the cab, the Agitation page is part of the Tank System application, reached through Menu, the
Machine Settings tab, then Tank System [[access-tank-system--f3b14b|Access Tank System]]. Agitation
level, boost level, auto intensity, auto stop and power agitation status are also shown on the Tank
System main page [[tank-system-main-page--42f006|Tank System Main Page]].

![[WZ1406712.png]]

**Figure WZ1406712** — Agitation Level [[agitation--995e05|Agitation]]

## Related procedures

**Mix solution in the tank (single solution system)**
[[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]]:

1. Push solution pump on-off to engage solution pump
   [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]].
2. Press agitation on/off to begin agitation
   [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]].
3. Adjust the agitation intensity using the intensity increase or intensity decrease button
   [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]].
4. Enable auto intensity using the auto intensity on/off button
   [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]].
5. Enable power agitation using the power agitation on/off button
   [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]].
6. Mix solution thoroughly before operating in the field
   [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]].
7. To stop agitation, press the solution pump button to stop the pump and press the agitation on/off
   button to close the agitation valve
   [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]].

On a dual product machine the same sequence is used, but the pump and agitation buttons are per tank
system: press the solution pump on/off button for the desired tank, then the agitation on/off button
for that tank [[mix-solution-in-tank-using-agitation--2ed382|Mix Solution in Tank (Using Agitation)]].

Open solution tank lid to verify sufficient mixing visually
[[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]].

## Related settings

Modify agitation when solution contents require more or less agitation, when manual control of
agitation is desired (turn off automatic agitation), or when reduced risk of foaming at low solution
levels is desired (turn on automatic agitation) [[agitation--995e05|Agitation]].

- **Agitation Level** displays the current agitation level setting; select the Input Box to change
  it [[agitation--995e05|Agitation]]. Use a lower agitation level for easily mixed products to
  minimize foaming; use a mid-range agitation level for products not likely to foam; use a higher
  agitation level for dry-flowable and heavy or thick liquids to keep them in suspension
  [[agitation--995e05|Agitation]].
- **Agitation Boost Level** uses separate boost nozzles to increase agitation at the set level
  [[agitation--995e05|Agitation]].
- **Mechanical Agitation Level** (if equipped) displays the current agitation mechanical level
  setting [[agitation--995e05|Agitation]].
- **Auto Intensity** automatically regulates the level of agitation based on factors such as tank
  level and the type of chemicals being used, which helps maintain a consistent mixture throughout
  the operation; maximum intensity is used when the tank is full and minimum intensity is used when
  the tank is close to empty [[agitation--995e05|Agitation]]. The minimum and maximum levels of
  intensity can be adjusted by the operator [[agitation--995e05|Agitation]].
- **Power Agitation** quickly turns on maximum agitation [[agitation--995e05|Agitation]].
- **Auto Agitation Stop** stops tank agitation when a preset amount of product is left in the tank;
  the input box sets the amount of product remaining in the tank at which auto agitation stops
  [[agitation--995e05|Agitation]]. On a dual product machine in combined tank mode, the auto off
  threshold is the combined tank level from tank 1 and tank 2, and the input level is split between
  tank 1 and tank 2 depending on each tank volume proportional to the combined tank volume
  [[agitation-solution-system-1-and-2--14d3d1|Agitation — Solution System 1 and 2]]. Agitation for
  each individual tank will automatically turn off when the volume for that tank has reached the
  proportional threshold
  [[agitation-solution-system-1-and-2--14d3d1|Agitation — Solution System 1 and 2]].
- The **Low Tank Alarm** is the related tank setting: it indicates when to turn off agitation to
  reduce foaming, refill the tank, or when the solution level is not sufficient for operating on
  hills [[low-tank-alarm--a6bee8|Low Tank Alarm]].
- Tank volume itself is set on [[solution-tank|Solution Tank]].

> [!inference] What the manual does not give
> The agitation topics give no numeric agitation level for a named product or chemical class. They
> give a direction only — lower for easily mixed products, mid-range for products not likely to
> foam, higher for dry-flowable and heavy or thick liquids [[agitation--995e05|Agitation]] — and one
> volume threshold, 378.5 L (100 gal), below which agitation should be turned off
> [[agitation--995e05|Agitation]]. Any specific percentage beyond that comes from the product label
> or the chemical supplier, not from this manual.

## Related warnings

The NOTE callouts under [Warnings](#warnings) are the only signal-word blocks in the agitation
topics. Draining and entering the tank carry their own DANGER and CAUTION text — see
[[solution-tank|Solution Tank]].

## Related troubleshooting

- **Foaming.** Operate agitation at a lower rate to minimize foaming, and turn off agitation when
  tank volume drops below 378.5 L (100 gal) to prevent foaming and air in system
  [[mix-solution-in-tank-using-agitation--3a7ef4|Mix Solution in Tank (Using Agitation)]]. Turning
  on automatic agitation is the listed way to reduce the risk of foaming at low solution levels
  [[agitation--995e05|Agitation]].
- **Foaming while filling with Load Command** is a different fault with its own table: the symptom
  "Tank foams too much" is listed against a reduction in pump speed not being triggered during the
  first 265 L (70 gal) of filling (check 265 L (70 gal) tank level sensor function), a 76 mm (3 in)
  drop line directing the flow incorrectly into the tank, a chemical susceptible to foaming (use
  anti-foaming agent), and air in the system (check for vacuum leaks in plumbing upstream of pump)
  [[troubleshooting-load-command-system--1bc786|Troubleshooting Load Command System]].
- **Automatic agitation behaving oddly after a fill** points at tank volume, not at agitation: for
  automatic agitation to operate correctly, solution tank volume must be reset when tank is filled
  or solution is added [[agitation--995e05|Agitation]].
