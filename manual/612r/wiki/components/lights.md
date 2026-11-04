---
type: component
title: "Lights"
models: [all]
options: [ExactApply]
engine_tier: null
components: [lights, road lights, worklights, beacon lights, egress lights, nozzle lights]
sources:
  - "N0LMWLO,00003F6-19-04DEC20"
  - "ouo6092,1775594262280-19-07APR26"
  - "ouo6092,1775594382707-19-07APR26"
  - "ouo6092,1775594856521-19-07APR26"
  - "CS12167,00001EA-19-04JAN13"
  - "as09261,1712251907359-19-04APR24"
  - "AG,OUO1011,756-19-20OCT25"
  - "DX,FLASH-19-07JUL99"
reviewed: true
compiled: 2026-09-23
---

# Lights

The machine's lighting splits into road and warning lighting (regulated, not configurable),
worklights and beacons (switched and configurable from the display), egress lights, and — with
ExactApply — nozzle body lights that double as a fault indicator.

## Warnings

> [!warning] CAUTION
> CAUTION: When transporting the machine on a road or highway at night or during the day, use lights and devices for adequate warning to operators of other vehicles. Check local governmental regulations. Various safety devices are available and can be obtained via regular spare part channels. Contact a John Deere dealer or other service provider. Keep safety items in good condition. Replace missing or damaged items.
> [[operate-warning-lights--b8e48e|Operate Warning Lights]]

Use headlights, flashing warning lights, and turn signals day and night
[[use-safety-lights-and-devices--fe3bed|Use Safety Lights and Devices]]. Follow local regulations
for equipment lighting and marking; keep lighting and marking visible, clean, and in good working
order, and replace or repair lighting and marking that has been damaged or lost
[[use-safety-lights-and-devices--fe3bed|Use Safety Lights and Devices]].

> [!inference] Generic module
> [[use-safety-lights-and-devices--fe3bed|Use Safety Lights and Devices]] is flagged
> `generic: true` in its frontmatter, and its text addresses slow moving tractors with attachments
> or towed equipment and self-propelled machines on public roads. I therefore treat it as
> Deere-wide boilerplate rather than sprayer-specific instruction, and report it alongside the
> machine-specific [[operate-warning-lights--b8e48e|Operate Warning Lights]] instead of merging the
> two.

## What it is

Switched lights at the operator's station
[[lights--ab0cd4|Lights]]:

- **Beacon Lights (If Equipped)** — press to turn beacon lights ON/OFF [[lights--ab0cd4|Lights]].
- **Hazard Light** — press to turn hazard lights ON/OFF [[lights--ab0cd4|Lights]].
- **Parking Lights** — press to turn on parking lights, press again to turn off; indicator light is
  on when active [[lights--ab0cd4|Lights]].
- **Road Lights** — press button to turn road lights on, press button again to turn off; indicator
  light is on when active [[lights--ab0cd4|Lights]].
- **Worklights** — press to turn on worklights, press again to turn off; indicator light is on when
  active [[lights--ab0cd4|Lights]].
- **High-Beam/Low-Beam Lever** — to switch between preset 1 and 2, toggle the high-beam/low-beam
  lever located on the left-hand side of the front console; preset 1 is active when the lever is in
  the aft position and preset 2 is active when the lever is in the forward position
  [[lights--ab0cd4|Lights]].

Work lights are configurable; road lights are not configurable
[[lights-overview--abe77e|Lights Overview]].

With ExactApply, the nozzle bodies carry lights. Nozzle lights turn off when the nozzles are not
spraying [[operate-nozzle-lights--382bd0|Operate Nozzle Lights]].

## Where it is

![[N36564.png]]

**Figure N36564** — A: Lights; B: Slow Moving Vehicle Emblem; C: Reflector Tape; D: Reflectors
[[operate-warning-lights--b8e48e|Operate Warning Lights]]

![[H117884.png]]

**Figure H117884** — Beacon Lights switch [[lights--ab0cd4|Lights]]

The Lights application is reached from the display through Menu → Machine Settings tab → Lights, or
by pressing the Lights button on the navigation bar below the display
[[access-lights--5c9ef5|Access Lights]]. On the CommandARM, Lights is selected to access light
presets that you can configure
[[commandarm-console-and-display--f3fc44|CommandARM Console and Display]]; see [[commandarm]].

## Related settings

- **Worklight presets.** The Lights application allows you to access light preset configurations,
  and selecting one of the tab presets allows you to make adjustments
  [[lights-overview--abe77e|Lights Overview]]. The tabs are Worklights Preset 1, Worklights
  Preset 2, a Highlighted Tab that indicates which light preset is selected, Worklights Controls,
  and Advanced Settings [[lights-overview--abe77e|Lights Overview]].
- **Linked or unlinked pairs.** Select Link on the toggle button to link paired left-hand and
  right-hand lights for simultaneous ON and OFF operation on all tabs
  [[egress-lights--da80e6|Egress Lights]].
- **Egress lights.** Egress Lights allows you to select the duration and lights which will remain
  illuminated after the key switch is turned to OFF position
  [[egress-lights--da80e6|Egress Lights]]. Egress lights turn on if road or work lights were used
  in the last 5 minutes [[egress-lights--da80e6|Egress Lights]]. Select the Egress Light tab, select
  the Light or Light Pair buttons for the lights you want illuminated, open the Egress Timeout
  screen, select the desired egress timeout setting, and select OK to save
  [[egress-lights--da80e6|Egress Lights]].
- **Nozzle lights** are set up under Nozzle Body Lighting in the Boom and Nozzles Application
  section, then activated by pressing the spray system On/Off switch (A) to begin application
  [[operate-nozzle-lights--382bd0|Operate Nozzle Lights]]. See [[nozzle]].

> [!inference] Egress timeout values
> The manual's Egress Lights topic tells you to "select the desired egress timeout setting" but does
> not print the list of available durations
> [[egress-lights--da80e6|Egress Lights]]. The available durations are therefore whatever the
> display offers on your machine — this page does not state a number, because none is printed.

## Related procedures

- **Aim Head Lights.** Park the sprayer on a level surface with low beam road lights (A) 7.5 meters
  (25 ft) (C) from a vertical wall and turn on the low beam road lights
  [[aim-head-lights--3c7ae3|Aim Head Lights]]. The distance between the low beam road lights' beam
  centers and the center line should be 914 mm (36 in.) ((F))
  [[aim-head-lights--3c7ae3|Aim Head Lights]]; adjust high beam road lights so the edge of the
  bright area (H) is at least one tenth of distance (B) above the center of the low beam road lights
  spot (E) [[aim-head-lights--3c7ae3|Aim Head Lights]]; the distance between the high beam road
  lights' beam center and center line should be 787 mm (31 in.) ((I)), and between the high beam
  road light beam center (K) and inner hood light center line should be 635 mm (25 in.) ((J))
  [[aim-head-lights--3c7ae3|Aim Head Lights]].
- **Operate Nozzle Lights.** Set up the nozzle lights, then press the spray system On/Off switch
  (A) to begin application; nozzle lights activate in the previously selected mode
  [[operate-nozzle-lights--382bd0|Operate Nozzle Lights]].

## Related troubleshooting

- **Light with Fault** — an exclamation point in the Lights application indicates that a light is in
  error, for example a burnt out light bulb [[lights-overview--abe77e|Lights Overview]].
- **Nozzle light faults (ExactApply).** Nozzle lights are also used to indicate nozzle bodies with
  faults present; fault indication occurs when the spray system On/Off switch is ON or the operator
  selects the fault display button on the display
  [[operate-nozzle-lights--382bd0|Operate Nozzle Lights]]. Nozzle lights flash at a slower rate than
  the strobe setting to indicate a hardware fault, and software faults are not indicated
  [[operate-nozzle-lights--382bd0|Operate Nozzle Lights]]. Nozzle lights indicate the fault until
  disabled by the operator or until 2 minutes have elapsed since the fault occurred
  [[operate-nozzle-lights--382bd0|Operate Nozzle Lights]]. Fault indication is enabled for all
  nozzles at all times regardless of section control, IBS, or CommandARM section switch status
  [[operate-nozzle-lights--382bd0|Operate Nozzle Lights]].
- **Nozzle light burned out.** Nozzle light and lens are not replaceable; the complete nozzle body
  must be replaced if the light burns out
  [[operate-nozzle-lights--382bd0|Operate Nozzle Lights]].
