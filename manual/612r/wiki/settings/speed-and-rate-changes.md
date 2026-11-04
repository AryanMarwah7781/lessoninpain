---
type: settings
title: "Speed and rate changes"
models: [all]
options: []
engine_tier: null
components: [solution pump, nozzle, spray tip, flowmeter, display]
sources:
  - "as09261,1712163885782-19-16APR24"
  - "ouo6092,1776103109013-19-13APR26"
  - "ouo6092,1776103254051-19-13APR26"
  - "ouo6092,1776103274659-19-13APR26"
  - "ouo6092,1776103486502-19-13APR26"
  - "ouo6092,1776103360596-19-07MAY26"
  - "ouo6092,1776103382330-19-13APR26"
  - "ouo6092,1776103466856-19-13APR26"
  - "UZEGGEY,1765785596814-19-11MAY26"
  - "ouo6092,1777904065201-19-07MAY26"
  - "ouo6092,1777904098900-19-04MAY26"
  - "bn55050,1775500496563-19-27APR26"
  - "bn55050,1775500517522-19-27APR26"
  - "bn55050,1775500538362-19-27APR26"
  - "ouo6092,1777914851141-19-04MAY26"
  - "ouo6092,1778690708032-19-13MAY26"
  - "bn55050,1775500631862-19-27APR26"
  - "ouo6092,1763587157303-19-27APR26"
  - "BN55050,000005D-19-08JUN18"
  - "DX,WW,CHEM02-19-05APR04"
  - "ouo6092,1777921717923-19-13MAY26"
reviewed: true
compiled: 2026-09-23
---

# Speed and rate changes

## The condition

You change ground speed during application (rolling ground, headlands, slowing for obstacles) or
change the target application rate. The base machine's rate controller holds the rate by changing
pump flow and therefore pressure; a machine with **ExactApply** can instead pulse the nozzles to hold
pressure — and with it droplet size — constant. Base-machine guidance comes first; ExactApply is a
conditional section below.

> [!note] Quick answer — ExactApply on rolling ground with frequent speed changes
> Set Broadcast Pulsing Mode to **automatic**: the manual's "Modify When" list says "Varying
> application speeds are used. Select automatic."
> [[broadcast-pulsing-mode--ae9c2a|Broadcast Pulsing Mode]]. Pulsing "allows a reduced rate to be
> applied while maintaining system pressure for constant droplet size"
> [[broadcast-pulsing-mode--ae9c2a|Broadcast Pulsing Mode]], and Auto Pulsing Target Pressure
> "maintains droplet size when changing speeds or application rates" — decrease the pressure for
> larger droplets, increase it for smaller, and revisit it whenever the spray tip size is changed
> [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]]. The manual gives no speed-to-
> pressure number: the pressure you enter comes from your tip's approved range, the droplet size you
> need, and the product label.

## The manual's limits

- Field speed range: Speed Range (Field) w/Wet System 0—40 km/h (0—25 mph)
  [[machine-specification--bfe721|Machine Specification]].
- Boom maximum pressure (dead head pressure): standard flow pump 1034.2 kPa (10.3 bar) (150 psi);
  high flow pump 930.8 kPa (9.3 bar) (135 psi)
  [[machine-specification--bfe721|Machine Specification]].
- Most flat fan spray tips are designed to operate in the 207—414 kPa (2—4 bar) (30—60 psi) range
  [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]].
- Minimum Pressure "is typically 83—104 kPa (0.83—1.03 bar) (12—15 psi) and should be set below the
  spray pressure setting"
  [[minimum-pressure--5f6b69|Minimum Pressure]].
- ExactApply Auto Pulsing Target Pressure entry limits: Minimum 34 kPa (0.34 bar) (5 psi), Maximum
  1034 kPa (10.34 bar) (150 psi)
  [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].

> [!conflict] Maximum solution pressure
> The generic chemical-safety module says: "Do not operate solution delivery system at pressures
> exceeding 345kPa (3.5 bar) (50 psi)"
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
> Machine-specific text allows more: most flat fan tips are designed for 207—414 kPa (2—4 bar)
> (30—60 psi) [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]], and the Auto Pulsing Target
> Pressure entry accepts up to 1034 kPa (10.34 bar) (150 psi)
> [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]]. The 50 psi line comes from a
> generic Deere-wide module (`generic: true`). The manual does not reconcile them — confirm the
> limit for your machine with your dealer.

## Base machine — the levers

All of these are in the **Spray System** application
[[spray-system-main-page--0e624d|Spray System Main Page]].

| Lever (as printed) | Where | What the manual says it does |
|---|---|---|
| **Target Rate/Rx** | Spray System main page | Target application rate can be edited for presets 1, 2, and 3; the manual pressure setting can also be modified; a prescription can be selected [[target-rate-rx--d50882|Target Rate/Rx]]. |
| **Minimum Pressure** | Spray System main page | Maintained when 0 km/h (0 mph) ground speed is detected or if target pressure is below minimum set pressure; must be higher than the nozzle check valve pressure but not so high it causes over application during normal speed adjustments [[minimum-pressure--5f6b69|Minimum Pressure]]. |
| **Spray System Response** | Spray System → Advanced Settings [[advanced-settings--5e4b27|Advanced Settings]] | The time it takes for the actual application rate to reach the target rate. Increase when the target rate is never reached or takes longer than 4 seconds; decrease when the application rate is erratic; "In most cases, the spray system response should be set to three." [[spray-system-response--b1e261|Spray System Response]] |
| **Flow Rate Mode** | Spray System main page (if equipped) | High, standard, intermediate or low flow; modify when changing application rates or when application speed changes significantly [[flow-rate-mode--7a4961|Flow Rate Mode]]. |
| **Flow Recommendations** | From Flow Rate Mode → Recommendations | Enter Working Speed and Target Rate; the display calculates the correct flow rate mode and valve positions [[flow-recommendations--26ca8c|Flow Recommendations]]. |
| **Rate Control/Display Speed** | Spray System → Advanced Settings [[advanced-settings--5e4b27|Advanced Settings]] | Speed source for the rate controller — GPS, Wheel or Radar — chosen by wheel slip, GPS signal and crop conditions [[rate-control-display-speed--1f29f0|Rate Control/Display Speed]]. |

### What the rate controller does when speed changes (base machine)

- The spray rate control unit (SRC) maintains application within a tolerance range of application
  rates while changing speeds; some differences can be observed if the operator makes rapid speed
  changes or operates at the extremes of the solution system's capacity
  [[solution-system--544787|Solution System]].
- The SRC is a volume-regulating system, so pressures displayed may vary at a given ground speed;
  the solution pressure required for a given application rate is determined by speed and nozzle tip
  size [[solution-system--544787|Solution System]].
- If the machine is moving slowly or is not moving, the pump maintains the minimum solution pressure,
  which may result in an application rate higher than the target; if the machine is moving too fast,
  the pump maintains the maximum solution pressure, which may result in a rate lower than the target
  [[solution-system--544787|Solution System]].
- Before using the SRC, refer to a nozzle tip calculator or nozzle tip selection charts and make
  sure the boom has tips that provide the desired rates at the desired pressures and speeds
  [[solution-system--544787|Solution System]].

> [!inference] What this means for a base machine on rolling ground
> On a machine without pulsing, holding the rate across a speed change means the pressure changes
> with speed [[solution-system--544787|Solution System]], and pressure affects atomization
> ("Line pressures that are too high or too low affect the atomization of the solution")
> [[solution-system--544787|Solution System]]. So on the base machine droplet size will vary with
> speed; the levers above keep the *rate* on target, not the droplet size. The manual does not say
> this in one sentence — it follows from the two statements linked.

## If your machine has ExactApply

ExactApply settings are on the **ExactApply** tab of the **Nozzle System** application: status,
spray mode, nozzle boost, active spray tips, and auto pulsing target pressure
[[nozzle-system-main-page--e7fa7e|Nozzle System Main Page]] [[exactapply--8eb5fa|ExactApply]].
Modify these when adjusting the target pressure to achieve the desired droplet size, when the specific
gravity of the solution changes, or when changing the spray mode or the auto pulsing target pressure
[[exactapply--8eb5fa|ExactApply]].

### Lever 1 — Broadcast Pulsing Mode (valve pulsing mode)

"Pulsing allows a reduced rate to be applied while maintaining system pressure for constant droplet
size. Pulsing also enables the machine to apply an even rate when curve compensation is active."
[[broadcast-pulsing-mode--ae9c2a|Broadcast Pulsing Mode]]

Modify When, as printed [[broadcast-pulsing-mode--ae9c2a|Broadcast Pulsing Mode]]:

- Continuous spray from the tip is desired. Select OFF.
- Curve compensation is being used. Select automatic.
- **Varying application speeds are used. Select automatic.**
- Band spraying. Select fixed or OFF.

Available valve pulsing modes [[broadcast-pulsing-mode--ae9c2a|Broadcast Pulsing Mode]]:

- **No Pulsing** — nozzles that are broadcast spraying are continuously open when the spray system
  master switch is pressed ON.
- **Auto Pulsing** — the control unit controls nozzle flow by pulsing the solenoid valve to achieve
  the desired application rate and maintain the desired spray pressure.
- **Fixed Pulsing** — you enter the desired nozzle flow percentage; no adjustments to the nozzle flow
  are made automatically.

> [!warning] NOTE — band spraying (p. 25-G-13)
> NOTE: Band spraying is not supported by automatic mode but is available in fixed or OFF modes. [[broadcast-pulsing-mode--ae9c2a|Broadcast Pulsing Mode]]

To change it: select the Input Box under valve pulsing mode (on a dual product machine, the one for
the solution system you want to modify), then select the mode from the list
[[broadcast-pulsing-mode--ae9c2a|Broadcast Pulsing Mode]].

For Fixed Pulsing, **Broadcast Pulsing Nozzle Flow** sets the percentage of the tip's maximum flow,
Minimum: 1%, Maximum: 100%; this amount is constantly maintained during application — for example, a
08 spray tip operated at a fixed 50% flow operates as a 04 spray tip
[[broadcast-pulsing-nozzle-flow--b8f7dc|Broadcast Pulsing Nozzle Flow]]. Because the flow is fixed,
this mode does not follow speed changes automatically
[[broadcast-pulsing-mode--ae9c2a|Broadcast Pulsing Mode]].

### Lever 2 — Auto Pulsing Target Pressure

As printed [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]]:

- "Auto Pulsing Target Pressure is the pressure maintained by the solution system during
  application."
- "Target spray pressures are only available when using automatic pulsing mode."
- "Using target spray pressures maintains droplet size when changing speeds or application rates."
- "Target pressure setting does not override the minimum spray pressure entered during machine
  setup."
- Modify When: larger droplets are desired — decrease the pressure; smaller droplets are desired —
  increase the pressure; the spray tip size is changed.
- Entry range: Minimum 34 kPa (0.34 bar) (5 psi), Maximum 1034 kPa (10.34 bar) (150 psi). On a dual
  product machine the target pressures for each solution system are adjusted separately.

Enable it with **Auto Pulsing Target Pressure Enable** on the ExactApply tab, then select the input
box to change the value [[exactapply--8eb5fa|ExactApply]].

> [!inference] "Minimum spray pressure entered during machine setup"
> The Auto Pulsing Target Pressure topic does not name the screen where that minimum is entered
> [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]]. The Spray System
> application has a **Minimum Pressure** setting maintained while spraying
> [[minimum-pressure--5f6b69|Minimum Pressure]]; it is probably the same setting, but the manual does
> not say so explicitly.

### Lever 3 — Spray Mode (turret position and solenoids)

Spray Mode is modified when application rates change or application speeds change
[[spray-mode--ade6a0|Spray Mode]]. With nozzle 1, 2, or 3 in front
[[spray-mode--ade6a0|Spray Mode]]:

- **A Only** / **B Only** — "Use for maximum speed ranges, better curve compensation performance, and
  15 or smaller tip sizes."
- **A + B** — both solenoids active; use with size 15 or smaller spray tips.
- **Automatic** — the nozzle control unit determines which solenoid or combination to operate;
  "Solenoids are not pulsed in this mode."

With nozzle 4, 5, or 6 in front: **Combined A + B** — when pulsing is selected, the nozzle is pulsed at
twice the pulse rate of a single nozzle; for size 30 and smaller spray tips
[[spray-mode--ade6a0|Spray Mode]].

The ExactApply Mode Comparison table rates Speed Range as follows: Combined A + B—Pulsing OFF
"Base"; Combined A + B—Automatic Pulsing "Better"; A Only or B Only—Automatic Pulsing "Best";
A + B—Automatic Pulsing "Best"; Automatic—Pulsing OFF "Good"; Automatic—Pulsing ON "Best"
[[exactapply-mode-comparison--54cd41|ExactApply Mode Comparison]]. Its Pressure Selection row is
"Target" for the pulsing modes and "Target Range" for Automatic—Pulsing OFF
[[exactapply-mode-comparison--54cd41|ExactApply Mode Comparison]].

For the non-pulsed Automatic spray mode, **Auto Switching | Pressure Settings** sets a minimum and
maximum pressure for each enabled tip; "Verify that the selected pressure is within the approved
range for the selected spray tip size and provides the desired droplet size", and keep the larger
tip no more than double the size of the smaller tip
[[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]]. Auto mode requires
valve pulsing set to OFF, the turret in a separate flow position (1, 2, or 3 in front), tips set up
for both front and rear positions, and rate-based application selected
[[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]].

### Field operation note

> [!warning] NOTE — manual pressure mode (p. 125-11)
> NOTE: Rate selected is highlighted on the display. [[field-operation--87b1c4|Field Operation]]
>
> Only use manual pressure mode with fixed pulsing or pulsing turned off.

## What the manual does NOT specify

- **No mapping from ground speed to a pressure number**, and no recommended Auto Pulsing Target
  Pressure value — only the entry range
  [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].
- No droplet-size chart: the manual says lower pressure gives larger droplets, not what size you get
  at a given pressure with a given tip
  [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].
- No speed at which to switch between pulsing modes, and no maximum rate of speed change the
  controller can follow; it only warns that rapid speed changes can cause rate differences
  [[solution-system--544787|Solution System]].
- No numeric default for Spray System Response beyond "In most cases … three"
  [[spray-system-response--b1e261|Spray System Response]].

## What overrides it

- **The product label.** "Always follow all label directions for effective, safe, and legal use of
  agricultural chemicals."
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
  A label droplet-size or pressure requirement governs the target pressure you choose.
- **The tip chart.** The pressure must be within the approved range for the selected spray tip size
  [[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]]; use a nozzle tip
  calculator or selection charts [[solution-system--544787|Solution System]].
- **The machine's minimum spray pressure** — target pressure does not override it
  [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].

## What to tell the assistant (needs from the operator)

Installed tip type and size, target rate, expected speed range, the product being applied (label
droplet/pressure requirements), and whether the machine has ExactApply.

## Related

- [[nozzle]] · [[spray-tip]] · [[solution-pump]]
