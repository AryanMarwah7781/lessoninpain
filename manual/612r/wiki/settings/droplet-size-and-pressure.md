---
type: settings
title: "Droplet size and pressure"
models: [all]
options: []
engine_tier: null
components: [spray tip, nozzle, solution system, ExactApply, Individual Nozzle Control, See & Spray]
conditions: [wind]
sources:
  - "DX,WW,CHEM02-19-05APR04"
  - "CS12167,000073C-19-05JUN26"
  - "CS12167,000022E-19-06FEB13"
  - "BN55050,000005D-19-08JUN18"
  - "BN55050,000005E-19-08JUN18"
  - "ouo6092,1776103274659-19-13APR26"
  - "bn55050,1775500538362-19-27APR26"
  - "ouo6092,1777904098900-19-04MAY26"
  - "bn55050,1775500496563-19-27APR26"
  - "ouo6092,1778517622488-19-11MAY26"
  - "bn55050,1775500517522-19-27APR26"
  - "bn55050,1775500631862-19-27APR26"
  - "ouo6092,1763586442387-19-11MAY26"
  - "UZEGGEY,1765865082901-19-11MAY26"
  - "as09261,1668097103203-19-23MAR26"
  - "ouo6092,1763568256151-19-27APR26"
  - "as09261,1712328149088-19-05APR24"
reviewed: true
compiled: 2026-09-23
---

# Droplet size and pressure

**Short answer.** Lower pressure gives larger droplets and higher pressure gives smaller droplets —
on ExactApply this is the Auto Pulsing Target Pressure: decrease the pressure when larger droplets
are desired, increase it when smaller droplets are desired
[[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]]. To minimize risk of spray
drift, use large nozzle tips operated at lower pressures
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
The pressure you choose must stay within the approved range for the installed tip
[[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]] and never below the
minimum spray pressure entered during machine setup
[[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]]. The manual prints **no**
droplet chart and **no** recommended psi for a droplet size or a wind speed; the tip chart and the
product label decide, and the label governs
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].

This page must agree with [[wind-and-drift]], which uses the same levers for the wind case.

## 1. The condition

The operator wants a particular droplet size — usually larger droplets to reduce drift, or a
droplet size class the product label requires — or wants to keep droplet size constant while speed
or rate changes. The manual addresses both through spray pressure and tip choice
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]],
[[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].

## 2. The manual's hard limits

- Most flat fan spray tips are designed to operate in the 207—414 kPa (2—4 bar) (30—60 psi) range
  [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]].
- Do not operate solution delivery system at pressures exceeding 345kPa (3.5 bar) (50 psi) — generic
  Deere-wide module
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
  **These two disagree; see section 6.**
- Target pressure setting does not override the minimum spray pressure entered during machine setup
  [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].
- Verify that the selected pressure is within the approved range for the selected spray tip size and
  provides the desired droplet size
  [[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]].

## 3. The levers the operator controls

### 3a. Tip type and size (all machines)

- Each spray tip type is designed to produce a specific spray pattern and are offered in different
  sizes to achieve desired application rate [[spray-tip-types--eb73b8|Spray Tip Types]]. Types:
  High Flow Flat Fan for fertilizer application; Ultra Low-Drift Flat Fan for herbicide application;
  Twin-Air Flat Fan, Guardian Flat Fan and Low-Drift Air for insecticide and fungicide application;
  Straight Stream Ceramic for fertilizer application [[spray-tip-types--eb73b8|Spray Tip Types]].
- High Flow spray tips have a multi-stepped, flow-regulating orifice and large atomization orifice
  that produce a consistent pattern with reduced fine droplets, reducing drift potential
  [[flat-fan-high-flow-flood-spray-tip--cc35e0|Flat Fan High Flow (Flood) Spray Tip]].
- Component pages: [[spray-tip]], [[nozzle]].

### 3b. Minimum Pressure (Spray System application — all machines)

- Spray System application → **Minimum Pressure**: maintained when 0 km/h (0 mph) ground speed is
  detected or if target pressure is below minimum set pressure for given application rate and nozzle
  tip size selected; it must be higher than the nozzle check valve pressure to keep all check valves
  open, but not too high to prevent over application during normal speed adjustments in the field
  [[minimum-pressure--5f6b69|Minimum Pressure]].
- Modify when changing carrier solutions, when visual nozzle check valves are changed, or when spray
  tip size or type is changed [[minimum-pressure--5f6b69|Minimum Pressure]]. The procedure sets it by
  raising Manual Target Preset by 6.9 kPa (0.7 bar) (1 psi) increments until all nozzle body check
  valves open and all nozzles spray a full pattern, then entering that recorded pressure
  [[minimum-pressure--5f6b69|Minimum Pressure]].

> [!warning] NOTE
> NOTE: This setting is typically 83—104 kPa (0.83—1.03 bar) (12—15 psi) and should be set below the spray pressure setting. If the setting is set near or equal to the spray pressure there will be fluctuations in rate/ pressure. [[minimum-pressure--5f6b69|Minimum Pressure]]

> [!inference] Is this "the minimum spray pressure entered during machine setup"?
> Auto Pulsing Target Pressure refers to "the minimum spray pressure entered during machine setup"
> [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]]. The Spray System
> application's Minimum Pressure is the only minimum-pressure setting found in the vault
> [[minimum-pressure--5f6b69|Minimum Pressure]], so I take them to be the same setting. The manual
> does not say so explicitly.

### 3c. Pulsing and target pressure — only if your machine has a pulsing nozzle system (ExactApply, or Individual Nozzle Control)

> [!note] If your machine has ExactApply (or INC Pro)
> - Nozzle System application → **ExactApply** tab → **Auto Pulsing Target Pressure Enable** and the
>   target spray pressure; modify when adjusting the target pressure to achieve the desired droplet
>   size [[exactapply--8eb5fa|ExactApply]].
> - **Auto Pulsing Target Pressure** is the pressure maintained by the solution system during
>   application. Target spray pressures are only available when using automatic pulsing mode. Using
>   target spray pressures maintains droplet size when changing speeds or application rates
>   [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].
> - Modify when: larger droplets are desired — decrease the pressure; smaller droplets are desired —
>   increase the pressure; the spray tip size is changed
>   [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].
> - The input box accepts Minimum: 34 kPa (0.34 bar) (5 psi) to Maximum: 1034 kPa (10.34 bar)
>   (150 psi) [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]] — an input range,
>   **not** a recommendation. If equipped with dual product solution system, the target spray
>   pressures for each solution system are adjusted separately
>   [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].
> - **Broadcast Pulsing Mode**: pulsing allows a reduced rate to be applied while maintaining system
>   pressure for constant droplet size; select automatic when varying application speeds are used or
>   curve compensation is being used; select OFF when continuous spray from the tip is desired
>   [[broadcast-pulsing-mode--ae9c2a|Broadcast Pulsing Mode]]. The same text is printed for INC
>   machines [[broadcast-pulsing-mode--84fbbf|Broadcast Pulsing Mode (INC)]].
> - Operating a combination of nozzle pulsing and active nozzle settings allows the system to
>   maintain a constant pressure and droplet size while changing speeds
>   [[nozzle-control-system-overview-single-solution--072796|Nozzle Control System Overview (Single Solution)]].
>   On INC Pro, nozzle pulsing must be enabled in automatic pulsing setting in order to use target
>   pressures [[individual-nozzle-control-inc-system-overview--50f97f|Individual Nozzle Control (INC) System Overview]].
> - **Broadcast Pulsing Nozzle Flow** (fixed pulsing): input the desired percentage of flow from the
>   active tip; for example a 08 spray tip operated at a fixed 50% flow now operates as a 04 spray tip
>   [[broadcast-pulsing-nozzle-flow--b8f7dc|Broadcast Pulsing Nozzle Flow]].
> - **Auto Switching | Pressure Settings** (automatic nozzle selection): set the minimum and maximum
>   pressures for the enabled tips, and verify that the selected pressure is within the approved range
>   for the selected spray tip size and provides the desired droplet size
>   [[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]].

### 3d. See & Spray pressure note — only if your machine has See & Spray

> [!note] If your machine has See & Spray
> It is recommended to increase the buffer length when operating at varying speeds, if accelerating
> and decelerating often, or if operating outside the ideal 30—50 psi spray pressure setting
> [[spray-buffer-area--09142c|Spray Buffer Area]]. That "ideal" range is printed for See & Spray
> buffer behaviour; it is not a droplet-size recommendation.

## 4. What the manual does NOT specify

- **No droplet-size chart.** No topic gives the droplet size (or size class) a tip produces at a
  given pressure. That is on the tip manufacturer's chart for the installed tip.
- **No pressure for a condition.** No topic maps a wind speed, a product or a droplet class to a
  pressure. Do not present a specific psi as "the setting" unless it comes from the installed tip's
  chart or the product label.
- **No base-machine target pressure.** On a machine without a pulsing nozzle system, the manual gives
  no separate droplet-size setting; the levers are the tip and the minimum pressure
  [[minimum-pressure--5f6b69|Minimum Pressure]].
- **How far below the tip range is too low** — the manual only says to stay within the approved
  range for the tip size [[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]].

## 5. What overrides it

- **The product label** — it may require a droplet size class or set application limits, and it
  governs: always follow all label directions for effective, safe, and legal use of agricultural
  chemicals
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]],
  and read and follow the manufacturer's label for each chemical applied
  [[avoid-exposure-to-chemicals--54538c|Avoid Exposure To Chemicals]].
- **The installed tip's rated pressure range and droplet chart**
  [[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]].
- **The minimum spray pressure entered at machine setup** — a floor the target pressure does not go
  below [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].
- **Your John Deere dealer** for the machine's maximum pressure (section 6).

## 6. Conflicts

> [!conflict] Maximum solution pressure — generic safety cap vs tip design range
> The generic Deere-wide chemical-safety module (`generic: true`) says do not operate solution
> delivery system at pressures exceeding 345kPa (3.5 bar) (50 psi)
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
> The machine-specific Flat Fan Spray Tip topic says most flat fan spray tips are designed to operate
> in the 207—414 kPa (2—4 bar) (30—60 psi) range [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]].
> This page does not choose; confirm the machine's limit with your dealer. Low-pressure,
> large-droplet settings for drift stay below both.

> [!conflict] Machine procedures that run above the generic 50 psi cap
> The rinse procedure says to set spray pressure at 620—690 kPa (6.2—6.9 bar) (90—100 psi) when
> spraying rinse water [[operate-rinse-system--738e0d|Operate Rinse System]], and the boom air
> bleed says to run the sprayer in manual spray mode at 620.6 kPa (90 psi)
> [[recommendations-for-eliminating-air-from-solution-system--c98980|Recommendations for Eliminating Air from Solution System]].
> Both are machine-specific and both exceed the generic 345kPa (3.5 bar) (50 psi) cap
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
> They are cleaning/bleeding operations, not application settings, but the manual does not say the
> cap excludes them. Reported, not resolved.

## Related pages

[[wind-and-drift]] · [[spray-tip]] · [[nozzle]] · [[boom-height-settings]] ·
[[operate-rinse-system]]
