---
type: troubleshooting
title: "Hydraulic System"
models: [all]
options: []
engine_tier: null
components: [hydraulic system, hydraulic pump, hydraulic oil cooler, orifice, solenoid, load sense check valve, AutoTrac strainer, compensator strainer]
sources:
  - "ouo6092,1737474660828-19-29OCT25"
  - "TB90758,00027F9-19-22MAR21"
  - "ouo6092,1737124093709-19-27OCT25"
  - "ouo6092,1763039484376-19-27APR26"
  - "ouo6092,1737119817515-19-19NOV25"
  - "TB90758,00028A6-19-08APR21"
  - "aota2vy,1686068835846-19-06JUN23"
  - "DX,FLUID-19-16MAR26"
reviewed: true
compiled: 2026-09-23
---
# Hydraulic System — troubleshooting

**System:** hydraulic system, base machine (Troubleshooting section, p. 160-9; no option) [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10). The
manual's table is reproduced symptom → problem → solution in its printed order; the manual gives no
cost or check order, so none is implied. Components: [[engine]], [[steering]], [[boom]],
[[electrical-system]]. Related service: [[replace-hydrostatic-and-hydraulic-filters-1000-hours]],
[[change-hydraulic-oil-1000-hours]].

Before working on hydraulic lines: [[park-machine-safely]]. Escaping fluid under pressure can
penetrate the skin causing serious injury; avoid the hazard by relieving pressure before
disconnecting hydraulic or other lines [[avoid-high-pressure-fluids--3fc79d|Avoid High-Pressure Fluids]] (generic Deere-wide module). Full list:
[[maintenance-safety]].

## Warnings that apply to these fixes

> [!warning] CAUTION
> CAUTION: Reduce compressed air to 210 kPa (2 bar) (30 psi) or less when using for cleaning purposes. Clear area of bystanders, guard against flying debris, and wear personnel protection equipment, including eye protection. A filter-type respirator is also advised to avoid inhalation of harmful particles. [[clean-cooling-package--751bc4|Clean Cooling Package]] (p. 95-11, 95-12)

> [!warning] IMPORTANT
> IMPORTANT: Do not replace the original fuse with a higher rated fuse or machine damage may occur. If the original size fuse does not carry electrical load and continues to blow, have the electrical system checked by a John Deere dealer or other service provider. [[fuse-identification--576581|Fuse Identification]] (p. 85-13)

> [!warning] CAUTION
> CAUTION: Spray system can contain hazardous material, which can cause serious injury or death to you or others. Wear protective clothing, eyewear, and gloves. Clean filter in an area where people, animals, vegetation, water supply, and so on, cannot be contaminated. [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]] (p. 45-6, 45-7, 45-8, 55-24, 55-25, 55-26, 115-13, 115-14)

> [!warning] CAUTION
> CAUTION: Do not close flowmeter shutoff valve (A) with the solution pump running. This can trap pressure in the system that can be hazardous when opening strainers for cleaning.
> Do not drain solution onto the ground. Drain into a container. Drain solution in an area where people, animals, vegetation water supply, and so on, cannot be contaminated.
> [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]] (p. 45-6, 45-7, 45-8, 55-24, 55-25, 55-26, 115-13, 115-14)

> [!warning] CAUTION
> CAUTION: Do not close the flowmeter shutoff valve (B) with the solution pump running. This can trap pressure in the plumbing that can be hazardous when removing flowmeters for cleaning. [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]] (p. 55-26, 55-27, 115-16)

> [!warning] CAUTION
> CAUTION: Spray system can contain hazardous material, which can cause serious injury or death to you or others. Wear protective clothing, eyewear, and gloves. Clean flowmeter in an area where people, animals, vegetation, and water supply, and so on, cannot be contaminated. [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]] (p. 55-26, 55-27, 115-16)

## Symptoms

### All hydraulic system fails to function.

1. **Bad fuse.** — Replace fuse. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[electrical-system]] · [[fuse-identification--576581|Fuse Identification]]
2. **Low oil supply.** — Fill oil to correct fill specification. (See Check Hydraulic Oil Level—Daily in Lubrication and Maintenance section.) [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[check-hydraulic-oil-level-daily--edf17c|Check Hydraulic Oil Level—Daily]]
3. **Engine speed set too low.** — Run engine at high idle. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[engine]]
4. **Clogged suction line.** — Clean line. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)
5. **Damaged pump drive coupling.** — Replace coupling. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)
6. **Pump faulty.** — Replace pump. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)
### System overheating in cold weather.

1. **When operating machine in low ambient temperatures below -7°C (20° F), the hydraulic oil may overheat due to a restriction at the hydraulic oil cooler.** — Install winter screens to hydraulic coolers to maintain correct temperature. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[cold-weather-and-storage]]
### Oil escapes at breather in the reservoir cap.

1. **Reservoir over-filled.** — Reduce oil to correct fill specification. (See Check Hydraulic Oil Level—Daily in Lubrication and Maintenance section.) [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[check-hydraulic-oil-level-daily--edf17c|Check Hydraulic Oil Level—Daily]]
2. **Excessive speed on rough terrain.** — Select slower target speed. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[slopes-and-rough-ground]]
3. **Driving on steep slopes.** — Stay off slopes to steep for operation. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[slopes-and-rough-ground]]
### Booms level or fold too fast.

1. **Incorrect orifice, or none in the work port.** — Use correct orifices, properly installed. Contact a John Deere dealer or other service provider. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[boom]]
### Lift arms drop too fast.

1. **Incorrect orifice, or none in the boom valve.** — Use correct orifices, properly installed. Contact a John Deere dealer or other service provider. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[boom]]
### Booms fold too slow.

1. **Plugged orifice.** — Remove orifice, clean, and reinstall. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[boom]]
2. **Incorrect orifice.** — Install correct orifice. Contact a John Deere dealer or other service provider. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)
### Some functions work erratically or not at all.

1. **Low oil.** — Fill tank to the proper level. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[check-hydraulic-oil-level-daily--edf17c|Check Hydraulic Oil Level—Daily]]
2. **Loose or disconnected wires at switch or solenoid.** — Check and repair connections. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[electrical-system]]
3. **Failed solenoid coil.** — Replace coil. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)
### Erratic steering.

1. **Hydraulic oil overheated.** — Fill tank to the proper level. Clean oil cooler and screens. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[check-hydraulic-oil-level-daily--edf17c|Check Hydraulic Oil Level—Daily]] · [[clean-cooling-package--751bc4|Clean Cooling Package]]
2. **Pump faulty.** — Replace pump. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[steering]]
### AutoTrac slow to acquire line or sluggish response.

1. Clean AutoTrac strainer. (See Clean AutoTrac Strainer—As Required in Lubrication and Maintenance section.) [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[clean-autotrac-strainer-as-required--75a191|Clean AutoTrac Strainer—As Required]]

> [!note] The fix topic states the same trigger (AutoTrac)
> Clean the AutoTrac strainer as needed if at least one of the following conditions exists: slow steering response; poor or slow guidance line acquisition when the resume button is selected [[clean-autotrac-strainer-as-required--75a191|Clean AutoTrac Strainer—As Required]].
### All hydraulic functions but one do not work or are slow.

1. **Check valve stuck open in the load sense line of function that works properly.** — Clean or replace check valve. Contact a John Deere dealer or other service provider. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)
### Sluggish or slow rate control, cannot meet speed or pressure requirements, must drive at too low of speed.

1. **Plugged hydraulic compensator strainer.** — Remove, inspect, and clean strainer. Contact a John Deere dealer or other service provider. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)

> [!inference] Spray-side causes with similar wording (from the fix topics' own trigger lists)
> The table's cause is the **hydraulic** compensator strainer [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10). Two spray-system maintenance
> topics state their own triggers in similar operator words, so check them too — the match of
> wording is mine, not the manual's:
> - Clean the boom supply line strainers if: pump fails to obtain maximum flow rate; pump fails to
>   maintain dead head pressure; application rates fluctuate; difference between solution pump
>   pressure and spray pressure is greater than expected for a given application [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]] —
>   [[clean-pressure-strainers-daily]].
> - Clean flowmeter insert as needed if application rates fluctuate [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]] — [[clean-flowmeter-as-required]].
### One hydraulic function fails to work properly.

1. **Bad fuse.** — Replace. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)  
   Fix / related: [[electrical-system]]
2. **Bad switch.** — Repair or replace. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)
3. **Check valve sticks shut in the load sense line of the hydraulic valve.** — Clean or replace check valve. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)
4. **Solenoid or hydraulic function faulty.** — Repair or replace. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)
5. **Hydraulic spool not shifting properly.** — Clean or replace hydraulic spool. Contact a John Deere dealer or other service provider. [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10)

## What the manual does not specify here

- Orifice sizes, compensator pressures and check-valve locations — the table sends these to the
  dealer [[hydraulic-system--47f651|Hydraulic System]] (p. 160-9, 160-10).
