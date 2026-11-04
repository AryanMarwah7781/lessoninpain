---
type: settings
title: "Wind and drift"
models: [all]
options: []
engine_tier: null
components: [spray tip, nozzle, boom height, BoomTrac, ExactApply, See & Spray]
conditions: [wind]
sources:
  - "DX,WW,CHEM02-19-05APR04"
  - "CS12167,000073C-19-05JUN26"
  - "CS12167,000022E-19-06FEB13"
  - "BN55050,000005D-19-08JUN18"
  - "BN55050,000005E-19-08JUN18"
  - "ouo6092,1777984543287-19-05MAY26"
  - "ouo6092,1776448178262-19-28APR26"
  - "ouo6092,1776448206631-19-27APR26"
  - "bn55050,1775500538362-19-27APR26"
  - "ouo6092,1777904098900-19-04MAY26"
  - "bn55050,1775500631862-19-27APR26"
  - "ouo6092,1777379103872-19-28APR26"
  - "ouo6092,1777652977908-19-01MAY26"
  - "as09261,1668097103203-19-23MAR26"
  - "ouo6092,1774282874383-19-25MAR26"
  - "ouo6092,1763666430899-19-11MAY26"
  - "ouo6092,1767966071356-19-17JUL26"
  - "ouo6092,1763568256151-19-27APR26"
  - "as09261,1712328149088-19-05APR24"
  - "bn55050,1742234626870-19-27OCT25"
  - "ouo6092,1763040518428-19-27APR26"
  - "CS12167,0000A33-19-01MAY17"
  - "UZEGGEY,1765865595173-19-16DEC25"
  - "bn55050,1743093416316-19-27MAR25"
  - "aota2vy,1686070140879-19-06JUN23"
reviewed: false
compiled: 2026-09-23
---

# Wind and drift

Page references: "p." gives the printed page label where the statement appears. The chemical-safety
module *Service and Operate Chemical Sprayers Safely* is printed three times, word for word, at 50-1
(Operate the Machine), 55-1 (Wet System) and 165-1 (Storage)
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]];
this page cites the **55-1 Wet System copy**.

## Checklist answer

For "what setting should I have in wind?" the manual supports four points:

1. **Do not spray when winds exceed 16 km/h (10 mph)**, and do not spray when wind is blowing towards
   a nearby sensitive crop, garden, or populated area
   [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1).
2. **The product label governs.** Always follow all label directions for effective, safe, and legal
   use of agricultural chemicals
   [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1).
3. **Use large nozzle tips operated at lower pressures**
   [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1),
   **and keep the boom at target height** — increasing boom height excessively above the target
   increases the risk of spray drift [[height-mode--b6109a|Height Mode]] (p. 25-A-6).
4. **If equipped:** with ExactApply, decrease Auto Pulsing Target Pressure when larger droplets are
   desired [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]] (p. 25-G-14; also
   printed at 130-15); with See & Spray, select a Large Spray Buffer Area when operating in windy
   conditions [[spray-buffer-area--09142c|Spray Buffer Area]] (p. 135-7).

The manual **never** maps a wind speed to a pressure, a height or a tip (section 4). The rest of this
page is the reference detail behind the checklist.

> [!inference] At 10 mph you are at the printed limit
> Not a manual statement. The printed rule is "Do not spray when winds exceed 16 km/h (10 mph)"
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1),
> so a steady 10 mph is not itself prohibited by the manual. It is, however, the maximum: any rise or
> gust above it puts you over the limit, and the manual gives no gust or averaging rule. Wind toward a
> sensitive crop, garden, or populated area is a "don't spray now" regardless of speed (same source),
> and the product label may set a lower limit.

## 1. The condition

The operator question is usually "how windy is too windy?" and "what do I change when it is
windy?". The manual files its wind rules under minimizing the risk of spray drift
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1).

## 2. The manual's hard limits

- **Do not spray when winds exceed 16 km/h (10 mph).**
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1)
- **Do not spray when wind is blowing towards a nearby sensitive crop, garden, or populated area.**
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1)
- Always follow all label directions for effective, safe, and legal use of agricultural chemicals
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1).

The wind limit comes from a **generic** Deere-wide module (`generic: true`)
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
No machine-specific topic gives a different general spraying limit. The only machine-specific wind
statements are for See & Spray: avoid operating See & Spray when wind speeds are above 16 km/h
(10 mph) [[operate-machine--ed621a|Operate Machine]] (p. 135-18), and do not perform the See & Spray
camera calibration during rain or winds over 16 km/h (10 mph)
[[see-and-spray-calibration-procedure--80b067|See & Spray Calibration Procedure]] (p. 25-B-31) — that
second one is about calibrating, not spraying.

## 3. The levers the operator controls

These are the drift-reducing levers the manual supports, in the order to consider them. The first
applies to every machine; the rest are conditional on options.

### 3a. Tip type and size (all machines)

- To minimize risk of spray drift, use large nozzle tips operated at lower pressures
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1).
- The basic spray tip types are High Flow Flat Fan for fertilizer application, Ultra Low-Drift Flat
  Fan for herbicide application, Twin-Air Flat Fan, Guardian Flat Fan and Low-Drift Air for
  insecticide and fungicide application, and Straight Stream Ceramic for fertilizer application
  [[spray-tip-types--eb73b8|Spray Tip Types]] (p. 55-5).
- Each spray tip type is designed to produce a specific spray pattern and are offered in different
  sizes to achieve desired application rate [[spray-tip-types--eb73b8|Spray Tip Types]] (p. 55-5).
- Most flat fan spray tips are designed to operate in the 207—414 kPa (2—4 bar) (30—60 psi) range
  [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]] (p. 55-6) — see the conflict in section 6.
- For liquid fertilizer, High Flow spray tips have a multi-stepped, flow-regulating orifice and large
  atomization orifice that produce a consistent pattern with reduced fine droplets, reducing drift
  potential [[flat-fan-high-flow-flood-spray-tip--cc35e0|Flat Fan High Flow (Flood) Spray Tip]] (p. 55-6).

Component background: [[spray-tip]], [[nozzle]]. Pressure and droplet size in detail:
[[droplet-size-and-pressure]].

### 3b. Boom height (all machines; automatic with BoomTrac)

> [!warning] CAUTION
> CAUTION: Avoid damage or contamination of your surroundings. Increasing boom height excessively above the target increases the risk of spray drift. [[height-mode--b6109a|Height Mode]] (p. 25-A-6)

- Keep the boom at its target height: increasing boom height excessively above the target
  increases the risk of spray drift [[height-mode--b6109a|Height Mode]] (p. 25-A-6). For flat fan tips
  the manual prints the usual geometry: spray tips spaced 508 mm (20 in) apart and positioned
  457— 559 mm (18—22 in) above the target surface [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]] (p. 55-6).
  That is tip geometry for an even pattern, not a wind setting.
- Component page: [[boom-height]]. Settings page for boom height: [[boom-height-settings]].

> [!note] If your machine has BoomTrac
> - Boom System application → BoomTrac → **Height Mode**. Locked Height Mode is recommended for most
>   applications where consistent spray height across the full boom is critical for optimal
>   coverage and drift control
>   [[boomtrac-settings-height-mode--2e3a37|BoomTrac Settings | Height Mode]] (p. 155-6).
> - **Raise and Lower Response**: increase the response when the boom does not lower fast enough to
>   avoid spray drift or skips in coverage
>   [[boomtrac-settings-raise-and-lower-response--678d41|BoomTrac Settings | Raise and Lower Response]] (p. 155-5).

### 3c. Larger droplets through lower target pressure — only if your machine has ExactApply

> [!note] If your machine has ExactApply
> - Nozzle System application → **ExactApply** tab → **Auto Pulsing Target Pressure** (enabled with
>   Auto Pulsing Target Pressure Enable) [[exactapply--8eb5fa|ExactApply]] (p. 25-G-3).
> - Auto Pulsing Target Pressure is the pressure maintained by the solution system during
>   application; using target spray pressures maintains droplet size when changing speeds or
>   application rates [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]] (p. 25-G-14).
> - Modify when larger droplets are desired: **decrease the pressure**. Smaller droplets: increase
>   the pressure. Also modify when the spray tip size is changed
>   [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]] (p. 25-G-14).
> - Target spray pressures are only available when using automatic pulsing mode, and the target
>   pressure setting does not override the minimum spray pressure entered during machine setup
>   [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]] (p. 25-G-14).
> - Stay inside the tip's approved range: verify that the selected pressure is within the approved
>   range for the selected spray tip size and provides the desired droplet size
>   [[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]] (p. 25-G-18).
>
> The display accepts target pressures from Minimum: 34 kPa (0.34 bar) (5 psi) to Maximum: 1034 kPa
> (10.34 bar) (150 psi) [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]] (p. 25-G-14)
> — that is the input range of the box, **not** a recommended value.

The Auto Pulsing Target Pressure topic is printed twice, at 25-G-14 (Nozzle System Application) and
130-15 [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]].

### 3d. Spray buffer — only if your machine has See & Spray

> [!note] If your machine has See & Spray
> - Avoid operating See & Spray when wind speeds are above 16 km/h (10 mph)
>   [[operate-machine--ed621a|Operate Machine]] (p. 135-18).
> - Menu > Machine Settings Tab > See & Spray → **Spray Buffer Area**: for best results, select
>   Large when operating in windy conditions or at higher boom heights
>   [[spray-buffer-area--09142c|Spray Buffer Area]] (p. 135-7); the same sentence is printed again in
>   [[machine-and-display-application-setup--1d5c23|Machine and Display Application Setup]] (p. 135-17).
> - Spray Buffer → **Length**: the spray length may require adjustment if the machine speed or wind
>   speed change [[spray-buffer--77d0c0|Spray Buffer]] (p. 25-J-7).
> - If windy conditions may push the spray away from the target, it is recommended to set up
>   See & Spray with setting the buffer width one step wider
>   [[set-up-spray-method-and-application-rates-targeted-herbicide--6e7512|Set Up Spray Method and Application Rates (Targeted Herbicide Single Solution)]] (p. 135-9).

## 4. What the manual does NOT specify

- **No wind-to-setting mapping.** No topic maps a wind speed to a spray pressure, a target pressure,
  a boom height, a tip size or a droplet size class. The manual gives the direction of each lever
  (lower pressure → larger droplets; do not raise the boom above target; larger buffer on See &
  Spray), never a number for a given wind.
- **No recommended psi.** A specific psi is not "the setting" for wind. The only pressures printed
  near this topic are the flat fan design range, a generic safety cap, an input-box range and
  rinse/air-bleed values (section 6) — none of them is a wind setting.
- **No gust rule.** The manual gives one number, "exceed 16 km/h (10 mph)"; it says nothing about
  gusts or averaging
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1).
- **No droplet size classes.** The manual does not print a droplet-size chart for any tip; that
  comes from the tip manufacturer's chart.
- **No temperature or inversion guidance** on drift in these topics.
- **The 15 mph figure is NOT a spraying wind limit.** The AutoTrac Vision requirements list includes
  "Wind speeds of up to 24 km/h (15 mph)"
  [[autotrac-vision-theory-of-operation--96fd90|AutoTrac Vision Theory of Operation]] (p. 140-8; the
  list begins on 140-7). It sits with camera and row requirements for the vision steering system, and
  the list ends "NOTE: Operating outside of these requirements may result in diminished performance."
  [[autotrac-vision-theory-of-operation--96fd90|AutoTrac Vision Theory of Operation]] (p. 140-8). It is
  a guidance (steering camera) condition. It does **not** raise the spraying limit: the spraying rule
  stays "Do not spray when winds exceed 16 km/h (10 mph)"
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1).
  Never answer "15 mph is OK" for spraying.

## 5. What overrides it

- **The product label.** It may set a lower wind limit or require a droplet size class, and it
  governs. The manual itself says to always follow all label directions
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1),
  and to read and follow the manufacturer's label for each chemical applied and state or regional
  guidelines [[avoid-exposure-to-chemicals--54538c|Avoid Exposure To Chemicals]] (p. 55-2).
- **The installed tip's rated pressure range and droplet chart** decide how low you can take the
  pressure for larger droplets; the machine check is that the selected pressure is within the
  approved range for the selected spray tip size
  [[auto-switching-pressure-settings--9ad35a|Auto Switching | Pressure Settings]] (p. 25-G-18).
- **The minimum spray pressure entered at machine setup** is a floor the target pressure does not
  override [[auto-pulsing-target-pressure--9d18fd|Auto Pulsing Target Pressure]] (p. 25-G-14).
- **Your John Deere dealer** for the machine's pressure limits (see the conflict below).

> [!inference] What to have ready before deciding
> Not a manual statement — it follows from the overrides above. Have: the product being applied
> (its label wind limit and any droplet requirement), the installed tip type and size with its
> chart, and the target rate and travel speed. Treat gusts above the printed limit as being above
> the limit, since the manual gives no averaging rule.

## 6. Conflicts

> [!conflict] Maximum solution pressure — generic safety cap vs tip design range
> The generic Deere-wide chemical-safety module (`generic: true`) says do not operate solution
> delivery system at pressures exceeding 345kPa (3.5 bar) (50 psi)
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1).
> The machine-specific Flat Fan Spray Tip topic says most flat fan spray tips are designed to operate
> in the 207—414 kPa (2—4 bar) (30—60 psi) range [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]] (p. 55-6).
> The upper part of the tip range is above the generic cap. This page does not choose; confirm the
> limit for your machine with your dealer. For wind, the low-pressure / large-droplet direction stays
> below both.

> [!conflict] Machine procedures that run above the generic 50 psi cap
> The rinse procedure says to set spray pressure at 620—690 kPa (6.2—6.9 bar) (90—100 psi) when
> spraying rinse water [[operate-rinse-system--738e0d|Operate Rinse System]] (p. 60-25), and the boom air
> bleed says to run the sprayer in manual spray mode at 620.6 kPa (90 psi)
> [[recommendations-for-eliminating-air-from-solution-system--c98980|Recommendations for Eliminating Air from Solution System]] (p. 55-19).
> Both are machine-specific and both exceed the generic 345kPa (3.5 bar) (50 psi) cap
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]] (p. 55-1).
> These are cleaning/bleeding operations, not application settings, but the manual does not say the
> cap excludes them. Reported, not resolved.

**Not a conflict, and not more evidence for the 50 psi cap:** the manual's "use normal water pressure
less than … (50 psi)" notes are pressure-washing limits for cleaning components, not solution
pressure — decal note at 50-4
[[machine-informational-decals--8583ad|Machine Informational Decals]], nozzle bodies at 125-20
[[clean-nozzle-body--f5b5d2|Clean Nozzle Body]] and 130-21 [[clean-nozzle-body--a341ce|Clean Nozzle Body]],
and AutoTrac Vision cameras at 145-1
[[clean-autotrac-vision-cameras--51a7df|Clean AutoTrac Vision Cameras]]. Likewise the
207—345 kPa (2.07—3.45 bar) (30—50 psi) printed at 115-48 is the Charge Pump Pressure specification in the filter-replacement
start-up procedure
[[replace-hydrostatic-and-hydraulic-filters-1000-hours--98578b|Replace Hydrostatic and Hydraulic Filters —1000 Hours]],
not a spray pressure.

## Related pages

[[droplet-size-and-pressure]] · [[spray-tip]] · [[nozzle]] · [[boom-height]] ·
[[boom-height-settings]] · [[operate-rinse-system]]
