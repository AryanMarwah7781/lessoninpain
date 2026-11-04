---
type: troubleshooting
title: "Eductor troubleshooting"
models: [all]
options: []
engine_tier: null
components: [eductor, solution pump, solution tank, fill valve]
sources:
  - "OUO6092,0000A67-19-16FEB16"
  - "ouo6092,1763565405881-19-27APR26"
  - "aota2vy,1685563436637-19-31MAY23"
  - "ouo6092,1763567486862-19-27APR26"
  - "as09261,1710352148383-19-21JAN26"
reviewed: true
compiled: 2026-09-23
---

# Eductor troubleshooting

This page follows the manual's Eductor troubleshooting table (p. 160-19 to 160-20) [[eductor--31f8b9|Eductor]]. Each symptom
heading is the symptom as printed, and the causes are in the printed order. The manual does not rank
causes by cost. The table applies to the base machine; for how to use the eductor, see
[[use-eductor-to-load-chemicals-with-full-solution-tank]]. The eductor valves are described in
[[wet-system-valves--2f14aa|Wet System Valves]]: the eductor sump valve allows chemical to be drawn from
the bottom of the eductor hopper to the top of the solution tank. Both the sump valve and the rinse valve
are only operational when the eductor flow rate valve is open.

> [!inference] Rows continued across pages
> The rows at the top of p. 160-20 ("No liquid in solution tank", "Engine speed too low") have an empty
> Symptom column. They are listed under *Eductor rinse nozzle does not rinse.*, the last symptom on
> p. 160-19 [[eductor--31f8b9|Eductor]].

## Eductor fills with chemical after using.
*p. 160-19* [[eductor--31f8b9|Eductor]]

- **Eductor rinse valve left on when eductor not in use.** → Close eductor flow rate whenever eductor not
  being used. Close eductor valve after use.
- **Valves not closed in proper sequence** → After using eductor, close eductor flow rate valve first then
  close eductor sump valve.

## Solution spills out of eductor when hopper is raised.
*p. 160-19* [[eductor--31f8b9|Eductor]]

- **Hopper is not completely empty.** → Empty hopper before raising eductor.

## Eductor rinse nozzle does not rinse.
*p. 160-19, continued on p. 160-20* [[eductor--31f8b9|Eductor]]

- **Nozzle not being depressed.** → When inserting jug over rinse nozzle, depress nozzle to activate flow.
- **Eductor rinse valve not turned ON.** → Turn valve on.
- **Valve or line plugged.** → Clear obstruction from line or valve.
- **Solution pump not primed.** → Prime solution pump. See [[solution-pump]] and
  [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]].
- *(p. 160-20)* **No liquid in solution tank.** → Add liquid to solution tank.
- **Engine speed too low.** → Increase engine speed to 1800 rpm minimum. (Manual controls only.)

## Eductor hopper rinse does not rinse.
*p. 160-20* [[eductor--31f8b9|Eductor]]

- **Eductor rinse valve not turned ON.** → Turn valve on.
- **Valve or line plugged.** → Clear obstruction from line or valve.
- **Solution pump not primed.** → Prime solution pump.
- **No liquid in solution tank.** → Add liquid to solution tank.
- **Engine speed too low.** → Increase engine speed to 1800 rpm minimum. (Manual controls only.)

## Eductor will not extract chemicals from hopper.
*p. 160-20* [[eductor--31f8b9|Eductor]]

- **Eductor rinse valve is OFF.** → Turn valve to ON position.
- **Eductor sump valve is closed.** → Open valve.
- **Solution pump not primed.** → Prime solution pump.
- **No liquid in solution tank.** → Add liquid to solution tank.
- **Eductor/Tank rinse valve in wrong position.** → Select proper tank with selector valve.
- **Engine speed too low.** → Increase engine speed to 1800 rpm minimum. (Manual controls only.)
- **Venturi is plugged.** → Clean venturi of obstructions.
- **Venturi is assembled wrong.** → Verify correct assembly of venturi.
- **Eductor discharge hose is plugged.** → Remove obstruction from discharge hose.
- **Dry chemical bridged.** → Turn on eductor rinse valve.
- **Diminished eductor performance with solution tank full.** → Use eductor before solution tank gets
  completely full.
- **Eductor hose in hopper is plugged or missing.** → Remove obstruction. Replace hose (if missing).

The eductor procedure makes the same point: eductor performance can be diminished somewhat with a full
tank [[use-eductor-to-load-chemicals-with-full-solution-tank--e0f0ee|Use Eductor to Load Chemicals with Full Solution Tank]].

## If your machine has Dual Product

The table above is the only eductor table in the manual. On dual product machines the eductor pressure
can also be set to settings (1—3) on the CommandCenter display, and the manual says "Do not start the
eductor before the solution tank is half full to prevent foaming when the chemical is added."
[[add-chemicals-to-full-tank-using-eductor--d5a96a|Add Chemicals to Full Tank Using Eductor]].

## Warnings for the fixes

Clearing the hopper, venturi or hoses means handling chemical. The product label governs chemical
handling. These warnings from the eductor procedure apply:

> [!warning] CAUTION — reading the label before loading chemicals · [[use-eductor-to-load-chemicals-with-full-solution-tank--e0f0ee|Use Eductor to Load Chemicals with Full Solution Tank]]
> CAUTION: Read the directions printed on the chemical manufacturer's labels carefully before handling chemicals to prevent exposure to hazardous materials that could cause injury or be poisonous.
>
> *Printed on:* p. 60-20 [[use-eductor-to-load-chemicals-with-full-solution-tank--e0f0ee|Use Eductor to Load Chemicals with Full Solution Tank]]
> *Applies to:* all models (single solution procedure)

> [!warning] IMPORTANT — when to add chemical · [[use-eductor-to-load-chemicals-with-full-solution-tank--e0f0ee|Use Eductor to Load Chemicals with Full Solution Tank]]
> IMPORTANT: Do not add chemical to the solution tank until just before field use. Follow the chemical manufacturer's instructions for mixing the spray solution to obtain the desired application rate and effect.
>
> *Printed on:* p. 60-21 [[use-eductor-to-load-chemicals-with-full-solution-tank--e0f0ee|Use Eductor to Load Chemicals with Full Solution Tank]]
> *Applies to:* all models

> [!warning] CAUTION — Quik-Fill valve · [[use-eductor-to-load-chemicals-with-full-solution-tank--e0f0ee|Use Eductor to Load Chemicals with Full Solution Tank]]
> CAUTION: Quik-Fill valve (A) can contain hazardous materials that could cause injury or be poisonous.
>
> *Printed on:* p. 60-21 [[use-eductor-to-load-chemicals-with-full-solution-tank--e0f0ee|Use Eductor to Load Chemicals with Full Solution Tank]]
> *Applies to:* all models

## What the manual does not specify

- How to check the venturi's "correct assembly"; no figure or procedure for the venturi is referenced in
  the table [[eductor--31f8b9|Eductor]].
- A separate engine speed for automatic controls. The 1800 rpm minimum is marked "(Manual controls only.)"
  [[eductor--31f8b9|Eductor]].
