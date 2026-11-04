---
type: procedure
title: "Prepare Machine for Cold-Weather Storage – Winterizing"
models: [all]
options: []
engine_tier: null
components: [solution system, rinse tank, solution tank, eductor, boom, nozzle, def system, fuel system]
requires: []
sources:
  - "aota2vy,1686231146950-19-08JUN23"
  - "aota2vy,1686230606303-19-08JUN23"
  - "aota2vy,1686231797294-19-08JUN23"
  - "ouo6092,1763568256151-19-27APR26"
  - "bn55050,1778257397921-19-08MAY26"
  - "DX,DEF,STORE-19-28AUG25"
  - "ouo6092,1737129759073-19-27OCT25"
  - "aota2vy,1686149453536-19-07JUN23"
  - "ouo6092,1763565405881-19-27APR26"
reviewed: true
compiled: 2026-09-23
---

# Prepare Machine for Cold-Weather Storage – Winterizing

This page is written for the base machine first. The printed procedure mixes base steps with steps
for options (Front Fill, Load Command, ExactApply, Manual Load System, high flow pump, fence row
nozzles, boom air purge)
[[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]].
The step numbers below are the printed numbers, so you can follow the manual side by side. Where an
option step falls in the sequence, the base list says so; the option steps themselves are in the
conditional sections further down. Do them **at that point in the sequence**, not at the end.

For machines stored in cold temperatures, the general storage procedure sends you here
[[prepare-machine-for-storage--fd6f6c|Prepare Machine for Storage]].

## Prerequisite — the solution system must already be clean

> [!warning] NOTE — starting condition (p. 165-3)
> NOTE: The following procedure is for winterizing a machine that has already been through the chemical cleaning process and only contains water in its solution system. [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]]

Do [[clean-solution-system--d8c29a|Clean Solution System]] first (p. 165-2 to 165-3). It ends with
"Flush system with SprayMaster Winterizer Fluid (N305634) if machine is to be stored in a climate
colder than 0°C (32°F)" [[clean-solution-system--d8c29a|Clean Solution System]].

> [!warning] CAUTION — decontaminate before storage (p. 165-2)
> CAUTION: Chemicals and pesticides are hazardous and can poison, causing serious injury or death. All spraying equipment should be decontaminated before being overhauled or placed in storage. Decontamination should be done in a safe area by washing with water, neutralization, or by means recommended by the chemical manufacturer. [[clean-solution-system--d8c29a|Clean Solution System]]

Spray rinse and winterizer solution only in a safe location where contamination cannot occur
[[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]].

## Warnings

> [!warning] IMPORTANT — DEF storage (p. 165-4)
> IMPORTANT: Long-term storage in the vehicle (over six months) is not recommended. If long-term storage is necessary, periodic testing of diesel exhaust fluid (DEF) is recommended to ensure that urea concentration does not fall out of specification. [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]]

> [!warning] IMPORTANT — which antifreeze (p. 165-4)
> IMPORTANT: Use of John Deere sprayer winterizer fluid is recommended for field use to protect the sprayer plumbing during storage. If an RV antifreeze is used, it must be a propylene glycol type rated for at least 8°C (15°F) below the lowest expected ambient temperature that the machine is subjected to during storage. To prevent damage to the seals and hoses, do not use other cheaper methanol, ethanol, or isopropanol type fluids. [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]]

> [!conflict] How long DEF may stay in the tank
> The winterizing procedure says long-term storage in the vehicle over six months is not recommended,
> and that DEF "could be stored in the vehicle for as long as six months depending upon storage
> conditions"
> [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]].
> The Storing Diesel Exhaust Fluid (DEF) topic says "Long-term storage in the DEF tank (over 12
> months) is not recommended" and that DEF is expected to remain useable for a minimum of 18 months
> under ideal conditions [[storing-diesel-exhaust-fluid-def--18be20|Storing Diesel Exhaust Fluid (DEF)]].
> The 12-month text comes from a generic Deere-wide module (`generic: true`); the six-month text is
> machine-specific. Neither is chosen here — if the machine will sit longer than six months, drain
> the DEF tank or test DEF before operating, and confirm with your dealer.

## Base steps

1. Verify that the fuel tank is filled with winter grade diesel fuel, or treat the tank with diesel
   winterizer according to product label instructions
   [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-3).
2. Diesel exhaust fluid (DEF) has a limited shelf life, but could be stored in the vehicle for as long
   as six months depending upon storage conditions. Drain the DEF tank if necessary
   [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4)
   — see [[drain-and-flush-diesel-exhaust-fluid-def-tank--7579fe|Drain and Flush Diesel Exhaust Fluid (DEF) Tank]].
3. Drain the eye wash tank
   [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4).
4. *(Front Fill, if equipped — see step 4 below.)*
5. *(Load Command, if equipped — see step 5 below.)*
6. Drain the rinse tank using the rinse tank fill valve
   [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4).
   The rinse tank fill valve is shown in [[fill-valve]]
   [[wet-system-valves--2f14aa|Wet System Valves]].
7. Operate the eductor function and transfer any eductor hopper water to the solution tank
   [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4).
8. Empty the solution tank water by opening the solution tank fill valve to let the water escape
   [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4).
9. Empty the rinse tank water by using the boom rinse function and spraying the rinse tank water out
   until spray pressure is lost at the boom
   [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4).
10. Fill the rinse tank with 190 L (50 gal) of winterizer fluid. R/V antifreeze or JD Winterizer Fluid
    is available in 9.46 L (2.5 gal) jugs (N305634) or 208 L (55 gal) drums (TY26555)
    [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4).
11. Perform foam marker storage procedure
    [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4).
    The manual refers to "Prepare Foam Marker System for Cold-Weather Storage in this section", but
    no topic with that title is printed in this manual — ask your dealer.
12. Machines Equipped with Solution Command System
    [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4):
    1. Perform a system rinse (see [[operate-rinse-system--738e0d|Operate Rinse System]]). The
       following systems are rinsed: Eductor, Agitation, Bypass, Solution Tank, Boom, Pressure
       Recirculation/Product Reclaim (if equipped). When rinsing the eductor, the operator must
       manually open the eductor rinse and sump valves when the display shows that portion of the
       rinse cycle. Boom is rinsed when the rinse solution is sprayed off at the end of the procedure
       [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]].
    2. For machines not equipped with pressure recirculation, after the rinse procedure is complete,
       unfold the booms and spray the rinse solution in a safe location where contamination cannot
       occur. For machines equipped with pressure recirculation, after the rinse procedure is
       complete, unfold the booms, enable pressure recirculation and turn on the solution pump; allow
       pressure recirculation to fill the solution system plumbing with winterization fluid
       (approximately 30 seconds), then spray the rinse solution in a safe location where
       contamination cannot occur
       [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]].
13. *(Manual Load System instead of Solution Command — see step 13 below.)*
14. *(ExactApply, if equipped — see step 14 below.)*
15. *(Front Fill, if equipped — see step 15 below.)*
16. *(Load Command, if equipped — see step 16 below.)*
17. *(High flow solution pump — see step 17 below.)*
18. Close all nozzle turrets other than the ones on each end of every spray pipe
    [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-5).
19. Spray the winterizer fluid in the solution tank out of the open turrets using the Nozzle Flow
    Check procedure until you see winterizer fluid coming out of every open spray pipe turret
    location
    [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-5)
    — see [[nozzle-flow-check-procedure--e0f861|Nozzle Flow Check Procedure]].
20. *(Fence row nozzles, if equipped — see step 20 below.)*
21. Spray winterizer fluid using the boom only rinse function until a pump dry warning is displayed
    [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-5).
22. *(Boom air purge, if equipped — see step 22 below.)*

## If your machine has Front Fill

- **Step 4:** Open the front fill isolation valve and use the front fill purge valve to push any water
  in the front fill hose into the solution tank
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4).
- **Step 15** (p. 165-5)
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]]:
  1. Remove the front fill cap.
  2. Open the front fill isolation valve using the electrical switch, then open the manual front fill
     valve to let the winterizer fluid drain into the front fill hose.
  3. Once winterizer fluid is seen coming out of the end of the front fill, close the manual valve.
  4. Use the air purge valve to push the winterizer fluid back into the solution tank.

## If your machine has Load Command

- **Step 5:** Open the Load Command poppet using the poppet maintenance menu on the display and drain
  the water out of the Load Command coupler
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4).
- **Step 16:** Rinse the Load Command system (see Preparing Machine for Storage in the Load Command
  section) [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-5).
  That procedure: evacuate chemicals from the Load Command system, rinse it with clean rinse water,
  fill the rinse tank with 189 L (50 gal) with SprayMaster Winterizer Fluid N305634, repeat the rinse
  procedure, and lubricate the Load Command pump and nurse arm
  [[preparing-machine-for-storage--7d877b|Preparing Machine for Storage]] (p. 120-17).

> [!warning] IMPORTANT — Load Command storage temperature (p. 120-17)
> IMPORTANT: Load Command components must be stored at temperature below 50°C (122°F). [[preparing-machine-for-storage--7d877b|Preparing Machine for Storage]]

> [!conflict] Winterizer fluid volume for the rinse tank
> The winterizing procedure says to fill the rinse tank with 190 L (50 gal) of winterizer fluid
> [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]],
> while the Load Command storage procedure says to fill the rinse tank with 189 L (50 gal)
> [[preparing-machine-for-storage--7d877b|Preparing Machine for Storage]]. Both give 50 gal; the
> metric figure differs by 1 L. Neither is a generic module. The manual does not say whether the Load
> Command fill is in addition to the step 10 fill or replaces it.

## If your machine has the Manual Load System (instead of Solution Command)

- **Step 13:** With the solution pump running, manually actuate the following functions
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-4):
  - Eductor — during the "eductor" portion of the system rinse, use the manual rinse valve at the
    eductor to rinse the eductor bowl with winterizer fluid, then use the eductor manual valve to suck
    the hopper empty of winterizer fluid and put it into the solution tank.
  - Agitation — activate for minimum of 10 seconds.
  - Bypass — activate for minimum of 10 seconds.
  - Solution Tank Rinse — activate for minimum of 10 seconds.

The manual does not say which of the two load systems (Solution Command or Manual Load) is standard
on a given model
[[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]].

## If your machine has ExactApply

- **Step 14** (p. 165-4 to 165-5)
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]]:
  1. Select A + B spray mode (see the ExactApply Operator's Manual).
  2. Verify that the nozzle turret is positioned with nozzle one, two, or three in the forward
     position.
  3. Spray the winterizer fluid in the solution tank out of the solenoids using the Nozzle Flow Check
     procedure until the winterizer fluid is coming out of every solenoid (see
     [[nozzle-flow-check-procedure--e0f861|Nozzle Flow Check Procedure]]).
  4. Allow the winterizer fluid to spray until the solution tank is empty.

## If your machine has the high flow solution pump

- **Step 17:** Verify that the flowmeter valve is in the OPEN position
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-5).

## If your machine has fence row nozzles

- **Step 20:** Spray through one or both fence row nozzles until winterizer fluid is coming out of the
  fence row nozzle location
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-5).

## If your machine has boom air purge

- **Step 22:** Use this function to remove excess winterizer fluid from the boom plumbing
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]] (p. 165-5).

## What the manual does not specify

- The foam marker storage procedure it references (step 11) is not printed in this manual.
- No temperature threshold at which winterizing becomes necessary is given in this procedure; the
  cleaning procedure's winterizer flush applies "if machine is to be stored in a climate colder than
  0°C (32°F)" [[clean-solution-system--d8c29a|Clean Solution System]].
- The high flow pump seal chamber has its own storage instruction; see
  [[inspect-and-replenish-high-flow-spray-pump-seal-chamber-flui]].

## Related

- [[solution-pump]] · [[fill-valve]] · [[aftertreatment]]
