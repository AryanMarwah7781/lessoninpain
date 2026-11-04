---
type: component
title: "Spray Tip"
models: [all]
options: [ExactApply, Individual Nozzle Control, See & Spray]
engine_tier: null
components: [spray tip, nozzle, nozzle turret, strainer]
sources:
  - "CS12167,000022E-19-06FEB13"
  - "BN55050,000005D-19-08JUN18"
  - "BN55050,000005E-19-08JUN18"
  - "BN55050,00000CF-19-08JUN18"
  - "BN55050,0000061-19-30JUL25"
  - "ouo6092,1777914823909-19-04MAY26"
  - "bn55050,1775500650827-19-27APR26"
  - "CS12167,00002D2-19-04JAN13"
  - "as09261,1712948982816-19-12APR24"
  - "UZEGGEY,1765865446363-19-16DEC25"
  - "as09261,1712155978284-19-03APR24"
  - "as09261,1712163885782-19-16APR24"
  - "UZEGGEY,1765865595173-19-16DEC25"
  - "DX,WW,CHEM02-19-05APR04"
reviewed: true
compiled: 2026-09-23
---

# Spray Tip

The spray tip is the orifice at the end of the nozzle turret that meters and atomizes the solution.
Solution flow is metered by the size of the orifice in the nozzle tip, and within limits, solution
flow through a nozzle can be increased or decreased by adjusting system pressure
[[solution-system--544787|Solution System]]. Each spray tip type is designed to produce a specific
spray pattern and are offered in different sizes to achieve desired application rate
[[spray-tip-types--eb73b8|Spray Tip Types]]. The nozzle bodies and turrets that carry the tips are
on [[nozzle|Nozzle]].

## Warnings

> [!warning] CAUTION
> CAUTION: DO NOT clean nozzle tips by placing in mouth and blowing. You could swallow or inhale hazardous chemicals which will poison, causing serious injury or death to you or others.
> [[clean-nozzle-body--a341ce|Clean Nozzle Body]]

> [!warning] IMPORTANT
> IMPORTANT: 50 and 80 mesh strainers are installed in the pressure plumbing of the machine. These strainers must remain installed during all applications to prevent plugging of spray tips and solenoid valves.
> [[exactapply-strainer-requirements--c2ea09|ExactApply Strainer Requirements]]

> [!warning] Chemical sprayer safety — generic Deere-wide module
> Do not place nozzle tips or other components to the mouth to clear obstructions. Keep spare tips on hand for replacement.
> Minimize risk of spray drift.
> Use large nozzle tips operated at lower pressures
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]]

Always follow all label directions for effective, safe, and legal use of agricultural chemicals
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
The product label, not this page, governs which tip and droplet class may be used for a given
product.

## What it is

Basic spray tip types are [[spray-tip-types--eb73b8|Spray Tip Types]]:

- High Flow Flat Fan for fertilizer application [[spray-tip-types--eb73b8|Spray Tip Types]]
- Ultra Low-Drift Flat Fan for herbicide application [[spray-tip-types--eb73b8|Spray Tip Types]]
- Twin-Air Flat Fan for insecticide and fungicide application
  [[spray-tip-types--eb73b8|Spray Tip Types]]
- Guardian Flat Fan for insecticide and fungicide application
  [[spray-tip-types--eb73b8|Spray Tip Types]]
- Low-Drift Air for insecticide and fungicide application
  [[spray-tip-types--eb73b8|Spray Tip Types]]
- Straight Stream Ceramic for fertilizer application [[spray-tip-types--eb73b8|Spray Tip Types]]

**Flat fan (Ultra Low-Drift, Twin-Air, Guardian, Low-Drift Air).** Flat Fan spray tips are an ideal
choice for broadcast spraying when it is desirable to have a uniform amount of chemical applied
across the entire width of the boom, and they apply solution in an elliptical pattern
[[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]]. To achieve uniform application, it is necessary
to overlap these spray tips; usually this is done with spray tips spaced 508 mm (20 in) apart and
positioned 457— 559 mm (18—22 in) above the target surface
[[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]]. Most flat fan spray tips are designed to operate
in the 207—414 kPa (2—4 bar) (30—60 psi) range
[[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]].

**Flat fan high flow (flood).** High Flow spray tips are used when high flow (2 to 6 gal/ min) is
required, and these application rates are typically required when applying liquid fertilizers
[[flat-fan-high-flow-flood-spray-tip--cc35e0|Flat Fan High Flow (Flood) Spray Tip]]. They provide a
wide angled spray pattern (140°) to enable wider spaced machine setups while assuring excellent
distribution [[flat-fan-high-flow-flood-spray-tip--cc35e0|Flat Fan High Flow (Flood) Spray Tip]].
The multi-stepped, flow-regulating orifice and large atomization orifice produce a consistent
pattern with reduced fine droplets, reducing drift potential
[[flat-fan-high-flow-flood-spray-tip--cc35e0|Flat Fan High Flow (Flood) Spray Tip]].

**Straight stream ceramic.** The straight stream ceramic tip is ideal for applying fertilizer into
solid seeded crops; it creates six individual streams that distribute the fertilizer on the soil
while getting less on the crop
[[straight-stream-ceramic-spray-tip--fdd7c0|Straight Stream Ceramic Spray Tip]]. The ceramic
metering orifice and unique low pressure distribution chamber keep the streams stable to reduce
atomization and prevent leaf burn and scorching
[[straight-stream-ceramic-spray-tip--fdd7c0|Straight Stream Ceramic Spray Tip]]. Spacing and spray
height is similar to 110° broadcast tips
[[straight-stream-ceramic-spray-tip--fdd7c0|Straight Stream Ceramic Spray Tip]].

> [!conflict] Maximum solution pressure
> The generic Deere-wide chemical-safety module (`generic: true`) says: do not operate solution
> delivery system at pressures exceeding 345kPa (3.5 bar) (50 psi)
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
> The machine-specific Wet System topic says most flat fan spray tips are designed to operate in the
> 207—414 kPa (2—4 bar) (30—60 psi) range
> [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]]. The two overlap only up to the lower figure, and
> this page does not choose between them. Confirm the limit for your machine and your installed tip
> with your John Deere dealer, and follow the product label.

## Where it is

The tip sits in the nozzle turret, and its position on the turret determines whether it is fed by
one solenoid or two [[nozzle-body-indicators--7301c8|Nozzle Body Indicators]]. Nozzle positions are
stamped on the nozzle body turret aiding in correct spray tip placement and control unit
configuration [[nozzle-body-indicators--7301c8|Nozzle Body Indicators]].

Tip patterns and how they are aimed
[[install-and-position-nozzle-tips-and-strainers--c6590a|Install and Position Nozzle Tips and Strainers]]:

![[N33978.png]]

**Figure N33978** — A: Flat Spray (weed Control, broadcast, pre-emerge); B: Cone Spray (insect
control); C: Flood Spray (broadcast); D: Even Spray (banding)
[[install-and-position-nozzle-tips-and-strainers--c6590a|Install and Position Nozzle Tips and Strainers]]

The coverage and distribution profile of a flat fan tip
[[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]]:

![[N135228.png]]

**Figure N135228** — A: Coverage Percent; B: Distribution Profile
[[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]]

## Related procedures

**Install and position the tips**
[[install-and-position-nozzle-tips-and-strainers--c6590a|Install and Position Nozzle Tips and Strainers]]:

1. Use the nozzle tip calculator to determine size of tips
   [[install-and-position-nozzle-tips-and-strainers--c6590a|Install and Position Nozzle Tips and Strainers]].
2. Install nozzle tips
   [[install-and-position-nozzle-tips-and-strainers--c6590a|Install and Position Nozzle Tips and Strainers]].
3. Position nozzles for the desired spray pattern; set flat or even nozzles so the slot in the
   bottom is at right angles to the row
   [[install-and-position-nozzle-tips-and-strainers--c6590a|Install and Position Nozzle Tips and Strainers]].
4. Boom nozzle section brackets are slotted for adjustment — loosen hardware to raise or lower the
   nozzle section
   [[install-and-position-nozzle-tips-and-strainers--c6590a|Install and Position Nozzle Tips and Strainers]].
5. Install strainers if desired; several different-sized mesh strainers are available (see a John
   Deere dealer or other service provider)
   [[install-and-position-nozzle-tips-and-strainers--c6590a|Install and Position Nozzle Tips and Strainers]].
6. Position nozzles for either broadcast spraying or banding
   [[install-and-position-nozzle-tips-and-strainers--c6590a|Install and Position Nozzle Tips and Strainers]].

**Check and replace worn tips.** A major cause of improper spray application is nozzle wear
[[check-and-replace-worn-nozzles--baa644|Check and Replace Worn Nozzles]]. New spray tips produce a
uniform distribution when properly overlapped; worn spray tips have a higher output with more spray
concentrated under each tip; damaged spray tips have a very erratic output — overlapping and under
applying [[check-and-replace-worn-nozzles--baa644|Check and Replace Worn Nozzles]]. Over-application
can cause crop damage, chemical carry-over affecting future crops, and ground water contamination;
under-application may require additional field passes and cause inadequate weed, pest or disease
control [[check-and-replace-worn-nozzles--baa644|Check and Replace Worn Nozzles]].

![[N69199.png]]

**Figure N69199** — A: NEW SPRAY TIPS produce a uniform distribution when properly overlapped;
B: WORN SPRAY TIPS have a higher output with more spray concentrated under each tip; C: DAMAGED
SPRAY TIPS have a very erratic output—overlapping and under applying
[[check-and-replace-worn-nozzles--baa644|Check and Replace Worn Nozzles]]

**Strainer requirements.** A minimum 20 mesh strainer is required in the machine fill lines when
equipped with ExactApply, and machines come equipped with a 20 mesh strainer in the fill line from
the side Fill Station [[exactapply-strainer-requirements--c2ea09|ExactApply Strainer Requirements]].
If the machine is equipped with front fill then a 20 mesh strainer must be used when filling to
remove any large contaminates in the solution
[[exactapply-strainer-requirements--c2ea09|ExactApply Strainer Requirements]].

Rinsing the tips and nozzle bodies is on [[nozzle|Nozzle]].

## Related settings

- **Select Tip** allows you to set the spray tip size installed on the turret for the selected
  location, and provides a searchable library of available tips
  [[select-tip--1ed46e|Select Tip]]. The list can be filtered to Recent or All, sorted, and
  searched by keyword; an indicator shows that a tip can be used with See and Spray
  [[select-tip--1ed46e|Select Tip]].
- **Enabled Spray Tip** checkboxes allow you to select from three combinations available in the
  automatic mode: Small Tip to Large Tip, Large Tip to Combination of Tips, and Small Tip to Large
  Tip to Combination of Tips [[enabled-spray-tip--35e522|Enabled Spray Tip]]. The selection of spray
  tip combinations can be used to overcome gaps in spray speeds if other methods cannot be used
  [[enabled-spray-tip--35e522|Enabled Spray Tip]]. Modify it when the size between small and large
  tips is too large, or when the size difference between large tip and combination of tips is too
  large [[enabled-spray-tip--35e522|Enabled Spray Tip]].
- The solution pressure required for a given application rate is determined by speed and nozzle tip
  size [[solution-system--544787|Solution System]]. Before beginning an application, refer to a
  nozzle tip calculator or nozzle tip selection chart, and make sure that the spray boom is equipped
  with spray tip nozzles that provide desired application rates at desired pressures and speeds
  [[solution-system--544787|Solution System]].

> [!inference] What the manual does not give
> None of the topics above map a wind speed, a droplet class or a product to a pressure setting for
> a given tip. The manual points at the nozzle tip calculator and the tip selection chart for that
> [[solution-system--544787|Solution System]], and at the product label for what is permitted
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
> Treat any specific psi not taken from your tip's chart as unsourced.

## Related warnings

The callouts under [Warnings](#warnings) above are the signal-word blocks and safety-topic text the
spray-tip topics carry. The pressure disagreement is in the conflict callout under
[What it is](#what-it-is).

## Related troubleshooting

- Some spray tips create an angled spray pattern; do not alternate the direction of the angle when
  using these tip types when using A only, B only, and A + B modes, because skips can occur when
  operating in these modes and the angle directions are alternated
  [[spray-tip-selection--327eb6|Spray Tip Selection]]. The INC version of the same topic states that
  skips can occur when operating in automatic or fixed pulsing modes and the angle directions are
  alternated [[spray-tip-selection--c44725|Spray Tip Selection]].
- The nozzle calculator is only accurate if one spray tip is being used without nozzle pulsing
  [[spray-tip-selection--327eb6|Spray Tip Selection]]; the INC topic states it is only accurate with
  the same spray tip type and size on the entire boom width without nozzle pulsing
  [[spray-tip-selection--c44725|Spray Tip Selection]].
- "Incorrect spray tip installed" is listed as a problem under the symptom "System cannot maintain
  constant pressure", with the solution "Install correctly sized spray tips"
  [[nozzle-body--325070|Nozzle Body]]. "Debris in nozzle tip" is listed under "Boosted nozzles won't
  spray", with the solution "Clean around nozzle and nozzle tips"
  [[nozzle-body--325070|Nozzle Body]].
