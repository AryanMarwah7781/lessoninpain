---
type: procedure
title: "Park the machine safely"
models: [all]
options: []
engine_tier: null
components: [multi-function lever, park brake, engine, battery disconnect switch]
requires: []
sources:
  - "DX,PARK-19-25NOV25"
  - "as09261,1711471029564-19-26MAR24"
  - "N0LMWLO,00003F0-19-03DEC20"
  - "TB90758,00027DA-19-10MAR21"
reviewed: true
compiled: 2026-09-23
---

# Park the machine safely

This is the prerequisite for any procedure that says to park the machine, stop the engine, or work
on the machine. It combines the machine-specific stopping sequence
[[park-the-machine--a7f533|Park the Machine]] with the general before-you-work-on-it rules
[[park-machine-safely--00d769|Park Machine Safely]]. Applies to all models; one step (battery
disconnect) has an extra condition on Final Tier 4/Stage V engine equipped machines.

## Warnings

> [!warning] IMPORTANT
> IMPORTANT: Prevent engine damage. Before stopping an engine that has been operating at working load, idle the engine for at least 2 minutes to cool the hot engine parts. On the Final Tier 4/Stage V engine equipped machines, do not disconnect the battery until the LED indicator at the battery shutoff is OFF. Selective catalyst reduction system automatically purges lines of diesel exhaust fluid (DEF), immediately after the machine is stopped. If adequate time is not allowed for lines to be purged, any DEF remaining in lines can crystallize and plug the lines. In freezing weather, DEF freezes and possibly bursts lines. [[park-the-machine--a7f533|Park the Machine]]

> [!warning] IMPORTANT
> IMPORTANT: Pressing the park brake switch applies the park brakes at vehicle speeds below 0.8 km/ h (0.5 mph). [[park-brake--e0c23d|Park Brake]]

> [!warning] IMPORTANT
> IMPORTANT: Do not disconnect battery on machines equipped with Final Tier 4/Stage V engines until light emitting diode (LED) (B) has turned off. This indicates that the diesel exhaust fluid (DEF) system purge is complete. [[battery-disconnect-switch--c9c8e5|Battery Disconnect Switch]]

> [!warning] NOTE
> NOTE: Secondary brake switch is not to be engaged when parking the machine. Park brakes are automatically applied when the multi-function lever is in the PARK position. Park brake switch may be engaged to prevent the machine from moving if the multi-function lever is bumped. Park brake switch must be disengaged before moving the machine. [[park-the-machine--a7f533|Park the Machine]]

## Steps — stop and park

![[N166477.png]]

**Figure N166477** — A: Multi-Function Lever; B: Low Idle Switch
[[park-the-machine--a7f533|Park the Machine]]

1. To slow and stop the machine, slowly return the multi-function lever (A) to the PARK position.
   Press down on the brake pedal if a quicker stop is necessary
   [[park-the-machine--a7f533|Park the Machine]].
2. Press low idle switch (B) to reduce engine speed to low idle
   [[park-the-machine--a7f533|Park the Machine]].
3. Turn off all lights and accessories [[park-the-machine--a7f533|Park the Machine]].
4. If the engine has been operating at working load, idle it for at least 2 minutes before
   stopping it, to cool the hot engine parts [[park-the-machine--a7f533|Park the Machine]].
5. Turn the key switch to the OFF position and remove the key
   [[park-the-machine--a7f533|Park the Machine]].
6. Lower the ladder [[park-the-machine--a7f533|Park the Machine]].

Park brakes are automatically applied when multi-function lever is in park position, so the park
brake switch does not need to be engaged when parking the machine [[park-brake--e0c23d|Park Brake]].
If the park brake switch is engaged, it must be manually disengaged before moving the machine; park
brakes will not automatically release when the park brake switch has been engaged
[[park-brake--e0c23d|Park Brake]].

## Steps — before working on the machine

Before working on the machine [[park-machine-safely--00d769|Park Machine Safely]]:

7. Lower all equipment to the ground [[park-machine-safely--00d769|Park Machine Safely]].
8. Stop the engine and secure the machine; if equipped, remove the key before leaving the machine
   unattended [[park-machine-safely--00d769|Park Machine Safely]].
9. Disconnect the battery ground strap [[park-machine-safely--00d769|Park Machine Safely]].
   **Final Tier 4/Stage V engine equipped machines:** first wait until the LED at the battery
   shutoff is OFF (see the conflict below) [[park-the-machine--a7f533|Park the Machine]].
   The battery disconnect switch (A) is rotated counterclockwise to turn the machine electrical
   system off [[battery-disconnect-switch--c9c8e5|Battery Disconnect Switch]].
10. Hang a "DO NOT OPERATE" tag in operator station
    [[park-machine-safely--00d769|Park Machine Safely]].

![[N153287.png]]

**Figure N153287** — A: Switch; B: Light Emitting Diode (LED)
[[battery-disconnect-switch--c9c8e5|Battery Disconnect Switch]]

> [!conflict] When to disconnect the battery
> The generic Deere-wide module (`generic: true`) lists "Disconnect the battery ground strap" as a
> plain step before working on the machine, with no waiting condition
> [[park-machine-safely--00d769|Park Machine Safely]]. The machine-specific topics say that on Final
> Tier 4/Stage V engine equipped machines the battery must not be disconnected until the LED at the
> battery shutoff is OFF, because the DEF lines are purged after the machine is stopped
> [[park-the-machine--a7f533|Park the Machine]],
> [[battery-disconnect-switch--c9c8e5|Battery Disconnect Switch]]. This page does not merge them: on
> those machines, the machine-specific condition is printed and the generic step is silent on it.

> [!conflict] Which brake switch not to engage when parking
> The Park Brake topic says the **park brake switch** does not need to be engaged when parking
> machine [[park-brake--e0c23d|Park Brake]]. The Park the Machine topic says the **secondary brake
> switch** is not to be engaged when parking the machine, and that the park brake switch *may* be
> engaged to prevent the machine from moving if the multi-function lever is bumped
> [[park-the-machine--a7f533|Park the Machine]]. Both are machine-specific. The manual does not say
> whether "secondary brake switch" and "park brake switch" are the same control; ask your dealer if
> the switch in your cab is labelled differently.

## What the manual does not specify here

- The "Before working on the machine" list comes from a generic Deere-wide module and does not
  mention relieving hydraulic or spray pressure; tasks that need that link to
  [[relieve-spray-pressure]] separately.
- None of these topics states how long the DEF purge takes; the only printed signal is the LED
  turning off [[battery-disconnect-switch--c9c8e5|Battery Disconnect Switch]].
