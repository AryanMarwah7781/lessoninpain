---
type: procedure
title: "Relieve spray system pressure"
models: [all]
options: []
engine_tier: null
components: [boom, nozzle, solution pump, flowmeter, strainer]
requires: []
sources:
  - "ouo6092,1776103331959-19-13APR26"
  - "ouo6092,1776103109013-19-13APR26"
  - "OUO6092,0000DE4-19-13MAR19"
  - "DX,SERV-19-20JAN26"
  - "DX,WW,CHEM02-19-05APR04"
  - "DX,MSDS,NA-19-03MAR93"
  - "aota2vy,1686155085570-19-08JUN23"
  - "UZEGGEY,1765865610192-19-16DEC25"
  - "ouo6092,1737119817515-19-19NOV25"
  - "ouo6092,1763039484376-19-27APR26"
  - "aota2vy,1686068647612-19-06JUN23"
  - "bn55050,1778513253020-19-11MAY26"
  - "UZEGGEY,1765865455065-19-29APR26"
reviewed: true
compiled: 2026-09-23
---

# Relieve spray system pressure

This page gathers what the manual says about relieving pressure in the spray (solution) system. The
manual has one display procedure for it — **Boom Pressure Relief**, in the Spray System application
[[pressure-relief--da45ff|Pressure Relief]] — and it covers pressure trapped **in the boom**. Many
other topics tell you to relieve pressure and point back to it. For the rest of the solution system
(pump, strainers, flowmeter) the manual gives cautions about trapped pressure but no separate
relief procedure; that gap is stated under [What the manual does not say](#what-the-manual-does-not-say).

Applies to all models, base machine (`options: []`) [[pressure-relief--da45ff|Pressure Relief]].

## Why and when the manual calls for it

- The decal on the machine reads: "Spray system is under pressure. Before servicing, conduct boom
  pressure relief function to relieve system pressure."
  [[nozzle-control-system-decal--08af28|Nozzle Control System Decal]]
- The Boom Pressure Relief function allows the pressure trapped in the boom to be bled off after
  spraying is complete, and its main purpose is to minimize the possibility of the sprayer nozzle
  bodies leaking while in transit [[pressure-relief--da45ff|Pressure Relief]].
- Before servicing a nozzle body (ExactApply topic): "Relieve trapped pressure in the spray boom before servicing
  nozzle body," and the first repair step is to perform a pressure relief procedure
  [[repair-nozzle-solenoid--eba495|Repair Nozzle Solenoid]]. The Individual Nozzle Control version
  carries the same sentence [[repair-nozzle-solenoid--fa18a1|Repair Nozzle Solenoid]].
- Before cleaning the fill strainer, aspirators, nozzle bodies and tips, the first step is to
  relieve boom pressure [[clean-fill-strainer-aspirators-nozzle-bodies-and-tips-as-req--c01b81|Clean Fill Strainer, Aspirators, Nozzle Bodies, and Tips—As Required]].
- When preparing to transport: if nozzles are dripping, relieve boom pressure
  [[transport-machine--4216ec|Transport Machine]].
- If a nozzle clogs or the system malfunctions, the generic Deere-wide chemical-safety module says:
  "If nozzle clogs or system malfunctions, stop engine and relieve spray pressure from system."
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]]
- Before any maintenance, the generic Deere-wide maintenance module says: "Disengage all power and
  operate controls to relieve pressure. Lower equipment to the ground. Stop the engine and secure the
  machine." [[practice-safe-maintenance--f22083|Practice Safe Maintenance]]

Two of these sources are generic Deere-wide modules (`generic: true`):
[[practice-safe-maintenance--f22083|Practice Safe Maintenance]] and
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
They say *to* relieve pressure; neither says how on this machine.

## Warnings

> [!warning] CAUTION
> CAUTION: Avoid unintended spray from nozzles. Do not use when non-John Deere aftermarket solution-system equipment is installed. These include, but are not limited to, direct injection and section control systems. See the direct injection system Operator's Manual or details regarding the use of this feature with a direct injection system.
> [[pressure-relief--da45ff|Pressure Relief]]

> [!warning] CAUTION
> CAUTION: Do not close the flowmeter shutoff valve (B) with the solution pump running. This can trap pressure in the plumbing that can be hazardous when removing flowmeters for cleaning.
> [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]]

> [!warning] CAUTION
> CAUTION: Do not close flowmeter shutoff valve (A) with the solution pump running. This can trap pressure in the system that can be hazardous when opening strainers for cleaning.
> [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]]

Check the Material Safety Data Sheet (MSDS) before you start any job using a hazardous chemical
[[handle-chemical-products-safely--05af3d|Handle Chemical Products Safely]] (generic Deere-wide
module). The boom releases fluid through the nozzles during relief
[[spray-system-main-page--0e624d|Spray System Main Page]], so the product being sprayed determines
what protective equipment applies — follow the product label.

## Steps — Boom Pressure Relief

The Pressure Relief item on the Spray System main page relieves pressure in booms by releasing fluid
through the nozzles until boom pressure matches the atmospheric pressure or the check valve
pressures, depending on machine configuration
[[spray-system-main-page--0e624d|Spray System Main Page]].

1. Enable boom Pressure Relief [[pressure-relief--da45ff|Pressure Relief]].

   ![[N118160.png]]

   **Figure N118160** — ON/OFF [[pressure-relief--da45ff|Pressure Relief]]

2. Press the Solution Pump switch to turn OFF the solution pump
   [[pressure-relief--da45ff|Pressure Relief]].

   ![[N120497.png]]

   **Figure N120497** — Solution Pump [[pressure-relief--da45ff|Pressure Relief]]

3. Press the Boom Raise/Lower switch on the multi-function lever to raise the boom center frame to
   the highest position [[pressure-relief--da45ff|Pressure Relief]].

   ![[N152641.png]]

   **Figure N152641** — Boom Raise/Lower [[pressure-relief--da45ff|Pressure Relief]]

4. Verify that the solution system pressure is 27 kPa (0.27 bar) (4 psi)
   [[pressure-relief--da45ff|Pressure Relief]].
5. Enable all boom sections. See the Boom Sections tab of the Nozzle System application
   [[pressure-relief--da45ff|Pressure Relief]].
6. Press the Spray System Master switch. Section valves open for 6 seconds to relieve pressure.
   Section valves automatically close after 6 seconds [[pressure-relief--da45ff|Pressure Relief]].

   ![[N120251.png]]

   **Figure N120251** — Spray System Master [[pressure-relief--da45ff|Pressure Relief]]

7. Before working on the machine, park it as described on [[park-machine-safely]]; the generic
   maintenance module says to lower equipment to the ground, stop the engine and secure the machine
   [[practice-safe-maintenance--f22083|Practice Safe Maintenance]].

> [!inference] Order of steps 1–6 and step 7
> Steps 1–6 are the manual's own sequence and need the machine's electrical system and solution
> controls active. Step 7 is placed last because the generic maintenance module lists "operate
> controls to relieve pressure" before "Stop the engine and secure the machine"
> [[practice-safe-maintenance--f22083|Practice Safe Maintenance]]. The Pressure Relief topic itself
> does not say whether the engine must be running.

## Pressure trapped on the chassis side (strainers, flowmeter)

The manual does not give a relief procedure for the chassis plumbing; it gives an order of
operations that avoids trapping pressure there:

- Clean flowmeter: first shut off the solution pump, then close the flowmeter shutoff valve
  [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]].
- Clean pressure strainers: close the flowmeter shutoff valve (with the pump not running — see the
  caution above), remove the plug and open the strainer drain valves to drain solution into a
  suitable container through the drain hoses
  [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]].

## If your machine has Individual Nozzle Control (INC) Pro with Direct Injection

For high flow usage with DI, the high-pressure relief kit should be installed to prevent trapped
pressure; the system can trap pressure above the 1034 kPa (10.34 bar) (150 psi) working range of
the nozzles, and in this condition the nozzle solenoids may not open
[[operate-system-with-direct-injection-installed--d099f8|Operate System with Direct Injection Installed]].
System pressure can be relieved using the strainer drain valves on the boom or by opening a fence row
nozzle momentarily (if equipped)
[[operate-system-with-direct-injection-installed--d099f8|Operate System with Direct Injection Installed]].
Note that the Boom Pressure Relief caution above says not to use that function when non-John Deere
aftermarket direct injection is installed [[pressure-relief--da45ff|Pressure Relief]].

## What the manual does not say

- No topic gives a procedure for relieving pressure in the solution pump, pressure strainers or
  flowmeter housings as such. The strainer and flowmeter topics rely on shutting the pump off before
  closing the shutoff valve, and on draining through the strainer drain valves
  [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]]
  [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]].
- The generic modules say to "relieve spray pressure from system" and "operate controls to relieve
  pressure" without naming a control
  [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]]
  [[practice-safe-maintenance--f22083|Practice Safe Maintenance]]. On this machine the named control
  is Boom Pressure Relief [[nozzle-control-system-decal--08af28|Nozzle Control System Decal]].
- No topic states a residual pressure that is safe to open a fitting at, other than the 27 kPa
  (0.27 bar) (4 psi) check in step 4 of Boom Pressure Relief [[pressure-relief--da45ff|Pressure Relief]].
  If you are unsure the plumbing is depressurised, ask your John Deere dealer.
