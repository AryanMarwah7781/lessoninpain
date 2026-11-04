---
type: component
title: "Solution Pump"
models: [all]
options: []
engine_tier: null
components: [solution pump, hydraulic motor, flowmeter, strainer, solution tank, rinse tank]
sources:
  - "UZEGGEY,1765785596814-19-11MAY26"
  - "UZEGGEY,1768888205923-19-20JAN26"
  - "as09261,1712163885782-19-16APR24"
  - "as09261,1710340206090-19-28APR26"
  - "aota2vy,1685563436637-19-31MAY23"
  - "aota2vy,1686069500990-19-06JUN23"
  - "ouo6092,1768942380951-19-20JAN26"
  - "ouo6092,1775656872449-19-08APR26"
  - "bn55050,1778258705100-19-08MAY26"
  - "bn55050,1778258720189-19-08MAY26"
  - "bn55050,1778258742954-19-08MAY26"
reviewed: true
compiled: 2026-09-23
---

# Solution Pump

> The product label and local regulations govern chemical application. The manual tells you to check
> the manufacturer's label of the last used chemical to see if special cleaning procedures are
> necessary before servicing the pump
> [[inspect-and-replenish-high-flow-spray-pump-seal-chamber-flui--5cdd03|Inspect and Replenish High Flow Spray Pump Seal Chamber Fluid—Annually]],
> and to decontaminate by means recommended by the manufacturer of the chemical last used
> [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].

## What it is

The solution pump is a centrifugal pump with a hydraulic drive
[[machine-specification--bfe721|Machine Specification]]. It is driven by a hydraulic motor, and
engagement and disengagement of the pump is controlled by a button on the CommandARM armrest or at
the Fill Station keypad [[solution-system--544787|Solution System]]. To help prevent pump
cavitation, any air trapped in the pump is allowed to escape through the solution pump bleed line
[[solution-system--544787|Solution System]].

On a **dual product** machine there are two pumps: engagement and disengagement of the system 2
pump is controlled by a button on the CommandARM armrest, and the system 1 pump is controlled using
soft keys on the CommandCenter display [[solution-system--3fd9a2|Solution System]].

Performance figures from the Specifications section
[[machine-specification--bfe721|Machine Specification]]:

| Item | Value |
|---|---|
| Boom maximum flow rate at 276 kPa (2.7 bar) (40 psi), standard pump and one flowmeter | 567.8 Lpm (150 gal/min) |
| Boom maximum flow rate at 276 kPa (2.7 bar) (40 psi), high flow pump and two flowmeters | 832.8 Lpm (220 gal/min) |
| Boom maximum pressure (dead head pressure), standard flow pump | 1034.2 kPa (10.3 bar) (150 psi) |
| Boom maximum pressure (dead head pressure), high flow pump | 930.8 kPa (9.3 bar) (135 psi) |

A high flow valve (optional) is used with a high flow solution system for flows above
341 L/min (90 gal/min); for flows less than 341 L/min (90 gal/min) the high flow valve should be
shut off and the high flow (dual flowmeter) option should be shut off in the display
[[solution-system--544787|Solution System]].

When the pump is activated, solution is drawn from the solution tank through the solution tank sump
valve, and the pump pushes the solution through the pressure strainer and flowmeters to the spray
control valves and to the agitation circuit through the agitation valve
[[solution-system--544787|Solution System]]. When the compensator opens, more hydraulic oil is sent
to the hydraulic motor, causing the solution pump to increase its flow; when the compensator closes,
less hydraulic oil is sent, causing the pump to decrease its flow
[[solution-system--544787|Solution System]].

See [[solution-tank]], [[agitation]] and [[fill-valve]] for the
parts of the system either side of the pump.

## Where it is

The solution pump (B) sits below the tank, with its vent line (A) routed upward to the tank top (C)
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].

![[N87475.png]]
**Figure N87475** — A: Vent Line; B: Solution Pump; C: Tank Top
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]]

The solution domain controller (SODC) serial number is located on the solution skid near the
left-hand rear tire [[identification-numbers--b5c28c|Identification Numbers]].

## Related procedures

### Daily

Rinse the pump, flowmeter(s), and boom with clean water daily or anytime chemicals are switched
[[rinse-solution-pump-boom-and-flowmeter-s-daily--124862|Rinse Solution Pump, Boom, and Flowmeter(s) —Daily]].

### Periodic checks on the vent line

Verify that the vent line (A) runs on a continuous, upward slope (without horizontal sections or
dips) from pump (B) to the tank top (C); verify a continuous stream of solution discharges from the
vent line into the tank during pump operation; and verify that hoses and fittings are tight and in
good condition
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].
The best time to view the discharge stream is with the tank half full; clean or replace the hose as
needed
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].

### Operating so the pump is not starved

As the tank empties, travel slowly over rough terrain to limit sloshing of solution, which causes
the pump inlet line to gulp air, and shut off the pump before the tank is empty
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].

### Filling with the solution pump

If the solution pump is used for machine filling, make sure that the filling pipe is as short as
possible, and the nurse tank solution level must be above that of the sprayer's pump or the pump
will not prime, leading to seal damage
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].
Use 76.2 mm (3 in) hose and fittings (if possible) on the nurse equipment; if 76.2 mm (3 in) hose is
not available, flood the solution pump with clean water from the rinse tank for several seconds to
make sure the pump is primed
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].

### Storage

Short-term storage — flush the pump with water or neutralizing agent (Spray Tank Cleaner,
Part No. N305631), or by means recommended by the manufacturer of the chemical last used, then
drain the pump
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].
Long-term storage — follow the same procedure, then refill the pump with a mix of SprayMaster
Winterizer Fluid, Part No. N305634; DO NOT store the pump with the chamber dry
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].

### High flow spray pump seal chamber fluid — annually

Flush and decontaminate the system, remove the pump, fill the seal chamber, and reinstall
[[inspect-and-replenish-high-flow-spray-pump-seal-chamber-flui--5cdd03|Inspect and Replenish High Flow Spray Pump Seal Chamber Fluid—Annually]].
Torques given for that job: fill plug 13 N·m (119 lb·in) and high flow pump mounting nuts
315 N·m (232 lb·ft)
[[inspect-and-replenish-high-flow-spray-pump-seal-chamber-flui--5cdd03|Inspect and Replenish High Flow Spray Pump Seal Chamber Fluid—Annually]].
Flush the system with SprayMaster Winterizer Fluid (N305634) if the machine is to be stored in a
climate colder than 0°C (32°F)
[[inspect-and-replenish-high-flow-spray-pump-seal-chamber-flui--5cdd03|Inspect and Replenish High Flow Spray Pump Seal Chamber Fluid—Annually]].

## Related settings and calibration

Pump Control allows you to manually enable or disable a solution system pump; Pump ON/OFF enables
or disables the pump for solution system 1, and the pump for solution system 2 can be enabled or
disabled using the appropriate buttons on the CommandARM
[[pump-control--c7e18b|Pump Control]].

The solution pump must be calibrated in order to achieve the desired application rate and maintain
the desired solution pressure [[spray-calibration-solution-pump--c49854|Spray Calibration | Solution Pump]].
Perform the calibration when the solution pump, hydraulic motor assembly, proportional valve,
hydraulic combo valve or spray rate control unit is replaced, or when pump values A and B are not
within correct ranges [[spray-calibration-solution-pump--c49854|Spray Calibration | Solution Pump]].
The recommended interval is "as needed" and the estimated time required is approximately 5 min
[[spray-calibration-solution-pump--c49854|Spray Calibration | Solution Pump]]. Calibration values
display A and B readings for low and high pump operating speeds and electrical current from the
sensor [[spray-calibration-solution-pump-calibration-values--189d8b|Spray Calibration | Solution Pump | Calibration Values]].

Calibration requirements: engine running at low idle, wheel speed 0 km/h (0 mph), parked and not
applying product, hydraulic fluid at normal operating temperature, solution pump OFF, system
pressure less than 0.34 bar (34.4 kPa) (5 psi), filling operations not active, and enough water to
prevent pump cavitation — minimum volume 567.8 L (150 gal)
[[solution-pump-calibration-procedure--1c72ed|Solution Pump Calibration Procedure]].

In-range calibration readings
[[solution-pump-calibration-procedure--1c72ed|Solution Pump Calibration Procedure]]:

| Pump | Reading | Speed (rpm) | Current (mA) |
|---|---|---|---|
| Standard-Flow | A | 800—1200 | 350—750 |
| Standard-Flow | B | 5500—6000 | 1275—1625 |
| High-Flow | A | 750—1200 | 400—670 |
| High-Flow | B | 4000—4600 | 1450—1750 |

If the calibration fails twice, contact your John Deere dealer or service provider
[[solution-pump-calibration-procedure--1c72ed|Solution Pump Calibration Procedure]].

> [!warning] NOTE
> NOTE: Do not perform this procedure for erratic solution pump rate or pressure if the A and B
> numbers are within range. If A and B numbers are within range, see Operator’s Manual.
> [[solution-pump-calibration-procedure--1c72ed|Solution Pump Calibration Procedure]]

## Related warnings

> [!warning] CAUTION — decontaminate before servicing
> CAUTION: Decontaminate work area before servicing. Flush, decontaminate, and drain pump before
> servicing. Decontamination should be done in a safe area with water or neutralizing agent, or by
> means recommended by manufacturer of chemical last used.
> [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]]

> [!warning] CAUTION — high-pressure fluids
> CAUTION: Escaping fluid under pressure can penetrate the skin causing serious injury.
> [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]]

> [!warning] CAUTION — flammable or explosive fluids
> CAUTION: DO NOT pump flammable or explosive fluids such as gasoline, fuel oil, and kerosene. ONLY
> pump solutions compatible with pump components.
> [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]]

> [!warning] CAUTION — prepare machine
> CAUTION: Remove key from the key switch before servicing pump.
> [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]]

> [!warning] CAUTION — hazardous material in the spray system
> CAUTION: Spray system can contain hazardous material which can cause serious injury or death to
> you or others. Wear protective clothing, eyewear, and gloves. Drain solution and clean strainer in
> an area where people, animals, vegetation and water supply etc., cannot be contaminated.
> [[rinse-solution-pump-boom-and-flowmeter-s-daily--124862|Rinse Solution Pump, Boom, and Flowmeter(s) —Daily]]

> [!warning] CAUTION — weight of the pump and motor assembly
> CAUTION: Approximate weight of the solution pump and motor assembly is 40 kg (88 lb). Use two
> people to remove pump and motor assembly.
> [[inspect-and-replenish-high-flow-spray-pump-seal-chamber-flui--5cdd03|Inspect and Replenish High Flow Spray Pump Seal Chamber Fluid—Annually]]

> [!warning] IMPORTANT — vent line
> IMPORTANT: To prevent pump damage from a dry run, vent line MUST be routed correctly and be free
> of obstructions so trapped air is bled from the pump chamber.
> [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]]

> [!warning] IMPORTANT — chemical left in the pump
> IMPORTANT: Chemicals and chemical residue left in the solution pump for an extended period can be
> damaging to pump components. Rinse pump interior with clean rinse water daily and do not let
> chemical solution remain in the pump overnight.
> [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]]

## Related troubleshooting

The pump topic carries its own symptom table
[[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]],
ordered here cheapest-to-check-first:

- **Low discharge** — pump not primed: inspect vent line. Air leaks in the inlet line: check and
  reseal inlet fittings. Blocked or clogged line filter: inspect strainer and clear debris from
  screen. Impeller clogged or blocked: inspect impeller and clear obstruction
  [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].
- **Low discharge, impeller damage** — impeller eye rubbing on volute (front casing) due to
  chemical induced swelling: inspect impeller, refer to the machine repair technical manual. Due to
  the pump running dry: inspect impeller for black or melted appearance, reuse or replace impeller
  depending on severity
  [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].
- **Mechanical seal leak** — pump ran dry: replace seal. Mechanical interruption of seal faces due
  to chemical solids getting in between seal faces (leak is usually temporary): replace seal if leak
  persists. Seal bellows torn due to chemical causing seal faces to stick together: replace seal,
  flush pump correctly in future
  [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].
- **Hydraulic motor leak** — motor housing socket head screws are loose: tighten screws to
  20 N·m (15 lb·ft). Oil seal failure: replace oil seal, inspect shaft, bearings, and oil "slinger"
  for damage and replace as needed
  [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].

If the current voltage value is red, then the current reading is outside the calibrated range
[[solution-pump-calibration-procedure--1c72ed|Solution Pump Calibration Procedure]].

## Applicability

The pump descriptions above are written for the single solution command system
[[solution-system--544787|Solution System]]. On a dual product machine the layout and controls
differ — there are two pumps, two strainers and two flowmeters, and the system 1 pump is operated
from the CommandCenter display rather than the CommandARM
[[solution-system--3fd9a2|Solution System]]. Standard-flow and high-flow pumps have different flow,
pressure and calibration figures; use the row that matches the pump fitted to your machine
[[machine-specification--bfe721|Machine Specification]].
