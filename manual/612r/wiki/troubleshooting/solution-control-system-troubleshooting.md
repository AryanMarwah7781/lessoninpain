---
type: troubleshooting
title: "Solution Control System troubleshooting"
models: [all]
options: []
engine_tier: null
components: [solution pump, flowmeter, pressure sensor, strainer, proportional valve, speed sensor, agitation, quik-fill valve]
sources:
  - "ouo6092,1737486289337-19-26NOV25"
  - "ouo6092,1737119817515-19-19NOV25"
  - "ouo6092,1763039484376-19-27APR26"
  - "ouo6092,1776103274659-19-13APR26"
  - "ouo6092,1776103486502-19-13APR26"
  - "bn55050,1778258663231-19-08MAY26"
  - "bn55050,1778258306993-19-08MAY26"
  - "bn55050,1778258499232-19-08MAY26"
  - "OUO6092,0000EC5-19-11MAY21"
  - "as09261,1712328149088-19-05APR24"
reviewed: true
compiled: 2026-09-23
---

# Solution Control System troubleshooting

The manual's troubleshooting table for the solution (spray) control system, printed on pages 160-10
to 160-19 [[solution-control-system--e1586c|Solution Control System]]. Base machine; no option
condition. Each section below is one symptom, with its heading exactly as printed and its
problem/solution rows in the manual's printed order. The table does not rank causes by cost, so the
printed order is kept. Components: [[components/solution-pump]], [[components/spray-tip]],
[[components/nozzle]], [[components/agitation]], [[components/solution-tank]].

## Maintenance topics that name these symptoms as their trigger

Two maintenance topics say when to do them in the operator's own terms. They are added under the
matching symptoms below.

- **Clean Flowmeter—As Required:** "Clean flowmeter insert (A) as needed with John Deere Brake and
  Parts Cleaner if the following condition exists: Application rates fluctuate."
  [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]] — procedure page
  [[clean-flowmeter-as-required]].
- **Clean Pressure Strainers—Daily:** "Clean the boom supply line strainers if the following conditions
  exist: Pump fails to obtain maximum flow rate. Pump fails to maintain dead head pressure.
  Application rates fluctuate. Difference between solution pump pressure and spray pressure is greater
  than expected for a given application."
  [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]] — procedure page
  [[clean-pressure-strainers-daily]].

> [!inference] Matching the trigger to the table
> The maintenance topics say "Application rates fluctuate"; the troubleshooting table says
> "Application rate varies or is erratic." An application rate that wanders, drifts or will not hold is
> the same observation in the operator's words, so both maintenance fixes are listed under that
> symptom below [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]]
> [[solution-control-system--e1586c|Solution Control System]]. The manual does not cross-reference
> the two itself.

## Warnings for the fixes

> [!warning] CAUTION — printed on [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]] (p. 55-26, 55-27, 115-16). Applies to: cleaning the flowmeter
> CAUTION: Do not close the flowmeter shutoff valve (B) with the solution pump running. This can trap pressure in the plumbing that can be hazardous when removing flowmeters for cleaning.

> [!warning] CAUTION — printed on [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]] (p. 55-26, 55-27, 115-16). Applies to: cleaning the flowmeter
> CAUTION: Spray system can contain hazardous material, which can cause serious injury or death to you or others. Wear protective clothing, eyewear, and gloves. Clean flowmeter in an area where people, animals, vegetation, and water supply, and so on, cannot be contaminated.

> [!warning] CAUTION — printed on [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]] (p. 45-6, 45-7, 45-8, 55-24, 55-25, 55-26, 115-13, 115-14). Applies to: cleaning the pressure strainers
> CAUTION: Do not close flowmeter shutoff valve (A) with the solution pump running. This can trap pressure in the system that can be hazardous when opening strainers for cleaning. Do not drain solution onto the ground. Drain into a container. Drain solution in an area where people, animals, vegetation water supply, and so on, cannot be contaminated.

> [!warning] CAUTION — printed on [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]] (p. 45-6, 45-7, 45-8, 55-24, 55-25, 55-26, 115-13, 115-14). Applies to: cleaning the pressure strainers
> CAUTION: Spray system can contain hazardous material, which can cause serious injury or death to you or others. Wear protective clothing, eyewear, and gloves. Clean filter in an area where people, animals, vegetation, water supply, and so on, cannot be contaminated.

> [!warning] CAUTION — printed on [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]] (p. 55-3, 55-4, 55-5). Applies to: solution pump service
> CAUTION: Remove key from the key switch before servicing pump.

> [!warning] CAUTION — printed on [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]] (p. 55-3, 55-4, 55-5). Applies to: solution pump service
> CAUTION: Decontaminate work area before servicing. Flush, decontaminate, and drain pump before servicing. Decontamination should be done in a safe area with water or neutralizing agent, or by means recommended by manufacturer of chemical last used. Spray materials can be extremely dangerous. Treat all spray chemicals, solutions, solution residues, or vapors with great caution. DO NOT take chances. When in doubt, proceed as though contamination is present. Keep spray material from contacting skin. If spray material contacts skin, wash off immediately with clean water and detergent or follow manufacturer's instructions for the chemical last used.

> [!warning] CAUTION — printed on [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]] (p. 55-3, 55-4, 55-5). Applies to: opening solution or hydraulic lines
> CAUTION: Escaping fluid under pressure can penetrate the skin causing serious injury. Avoid the hazard by relieving pressure before disconnecting hydraulic or other lines. Tighten all connections before applying pressure. Search for leaks with a piece of cardboard. Protect hands and body from high-pressure fluids. If an accident occurs, see a doctor immediately. Any fluid injected into the skin must be surgically removed within a few hours or gangrene can result. Doctors unfamiliar with this type of injury should reference a knowledgeable medical source. Such information is available from Deere & Company Medical Department in Moline, Illinois, U.S.A.

Before opening boom plumbing, see [[relieve-spray-pressure]]; all pressure warnings are on
[[pressurized-systems-safety]].

## Fault Code (FC) 110 Check Wiring.

| Problem | Solution |
|---|---|
| Intermittent code 110. | Turn key switch off, then on again. If code goes away, resume operation. If the problem persists, go to the next system check. |
| Intermittent wiring connection. | Check all CAN wiring connectors and reconnect. Inspect connectors for damage and repair. |
| Missing terminator. | Verify that terminators are installed. |
| Bad terminator. | Contact a John Deere dealer or other service provider. |

[[solution-control-system--e1586c|Solution Control System]]

## Fault Code (FC) 110 or (FC) 020. Monitor/Controller disconnected.

| Problem | Solution |
|---|---|
| Blown fuse. | Check fuses to CCU. |

[[solution-control-system--e1586c|Solution Control System]] — fuses: [[components/electrical-system]].

## Zero pressure with the spray system operating.

| Problem | Solution |
|---|---|
| Solution tank empty. | Fill tank with solution. Check tank for leaks or damage. |
| Solution control valves set incorrectly. | Set valves correctly. (See Minimum Pressure in Spray System section.) |
| Solution pump fuse faulty. | Replace fuse. |
| Solution pump bleed line kinked or forms traps. | Unkink bleed line. |
| Solution pump bleed line plugged. | Unplug pump bleed line. |
| Suction line plugged or collapsed. | Clean or replace suction line. |
| Spraying in transport range. | Shift to field range. |
| Plugged solution lines. | Unplug and flush. |
| Boom strainer plugged. | Remove, clean, and install the strainer. |
| Solution pump is not primed. | Prime the solution pump. |
| Solution pump impeller clogged. | Separate pump housing and clean impeller. |
| Low or no hydraulic oil. | Fill hydraulic reservoir to specification. (See Check Hydraulic Oil Level— Daily in Prestarting Checks section.) |
| Dirty or plugged flowmeter. | Remove, clean with brake cleaner, and install the flowmeter. |
| Solution tank valve closed. | Open valve. |
| Proportional valve electrical connection faulty. | Clean, replace, or repair connection. |
| Hydraulic shuttle valve faulty. | Replace or repair shuttle valve. |
| Nut on the solution pump impeller came off. | Install solution pump impeller nut. |
| Pressure sensor inoperative. | Contact a John Deere dealer or other service provider. |
| Shaft between the solution pump and hydraulic motor faulty. | Contact a John Deere dealer or other service provider. |
| Solution pump failure. | Contact a John Deere dealer or other service provider. |
| Proportional valve assembly faulty. | Contact a John Deere dealer or other service provider. |
| Hydraulic pump faulty. | Contact a John Deere dealer or other service provider. |
| Hoses between reservoir, hydraulic pump combo valve, proportional valve assembly, and motor faulty. | Contact a John Deere dealer or other service provider. |
| Check valve stuck open in proportional valve assembly or combo valve assembly. | Contact a John Deere dealer or other service provider. |
| Strainer shutoff valve closed. | Open valve. |
| Flowmeter shutoff valve closed. | Open valve. |

[[solution-control-system--e1586c|Solution Control System]]

Fix pages: [[minimum-pressure--5f6b69|Minimum Pressure]] · [[check-hydraulic-oil-level-daily--99fd63|Check Hydraulic Oil Level—Daily]] ·
[[clean-flowmeter-as-required]] · [[clean-pressure-strainers-daily]] · priming:
[[procedure-auto-prime--6f80d1|Procedure — Auto Prime]].

## Low pressure reading.

| Problem | Solution |
|---|---|
| Low engine speed. | Operate engine at high idle. |
| Nozzle tips worn. | Replace nozzle tips with new tips properly calibrated for current application. |
| Solution pump impeller clogged. | Separate pump housing. Remove and clean the impeller. |
| Suction line partially blocked or collapsed. | Clean, repair, or replace suction line as necessary. |
| Air leak in the suction line. | Repair or replace suction line. |
| Spray system not programmed properly. | See Spray System section. |
| Pressure line leaking. | Repair or replace pressure line as necessary. |
| Low or no hydraulic oil. | Fill hydraulic reservoir to center of the sight tube. |
| Pressure sensor faulty. | Contact a John Deere dealer or other service provider. |
| Shaft between the solution pump and hydraulic motor faulty. | Contact a John Deere dealer or other service provider. |
| Solution pump shaft seal(s) leaking. | Contact a John Deere dealer or other service provider. |
| Proportional valve faulty. | Contact a John Deere dealer or other service provider. |
| Hydraulic pump faulty. | Contact a John Deere dealer or other service provider. |
| Hydraulic shuttle valve faulty. | Contact a John Deere dealer or other service provider. |
| Hoses between reservoir, hydraulic pump priority valve, proportional valve assembly, and motor faulty. | Contact a John Deere dealer or other service provider. |
| Missing bleed valve orifice. | Contact a John Deere dealer or other service provider. |
| Check valve stuck open in the hydraulic load sense line. | Contact a John Deere dealer or other service provider. |

[[solution-control-system--e1586c|Solution Control System]] — worn tips: [[check-and-replace-worn-nozzles--baa644|Check and Replace Worn Nozzles]].

## High pressure reading during spraying operation.

| Problem | Solution |
|---|---|
| Boom in-line strainers (if equipped) partially or completely plugged. | Clean strainers. |
| Spray nozzles plugged. | Clean and inspect nozzles. Check orifices and calibration of nozzles. Replace nozzles as necessary. |
| Boom supply hoses partially or completely plugged. | Clean out hoses. |
| Spray system not programmed properly. | See Spray System section. |
| High/low flow valve in wrong position. | Turn high/low valve to correct position. (See Applying Low Application Rates in Wet System section.) |
| Minimum pressure set too high. | Lower minimum pressure setting. |
| Dirty or faulty flowmeter. | Clean with brake cleaner daily. |
| Boom shutoff valves faulty. | Contact a John Deere dealer or other service provider. |
| Pressure sensor faulty. | Contact a John Deere dealer or other service provider. |
| Faulty proportional valve assembly. | Contact a John Deere dealer or other service provider. |

[[solution-control-system--e1586c|Solution Control System]] — [[minimum-pressure--5f6b69|Minimum Pressure]] · [[clean-flowmeter-as-required]].

## Pressure reading varies or is erratic.

| Problem | Solution |
|---|---|
| Minimum spray pressure setting entered too high. | Determine minimum pressure required and enter correct value. (See Minimum Pressure in Spray System section.) |
| Inadequate solution supply in tank. | Fill solution tank. |
| High/low flow valve in wrong position. | Turn high/low valve to correct position. (See Applying Low Application Rates in Wet System section.) |
| Solution contains heavy solids (poor mixture). | Check engine and pump speed. Check agitation line and valves. Be sure that agitation jets are not clogged. |
| Spray nozzles plugged. | Clean and inspect nozzles. Check orifices and calibration of nozzles. Replace nozzles as needed. |
| Flowmeter dirty or stuck. | Clean flowmeter with brake cleaner. |
| Incorrect Sprayer Response min/max value in the control unit adjust. | Enter correct min/max setting. (See Spray System Response in Spray System section.) |
| Boom charge not on when it should be. | Set boom charge correctly. |
| Boom supply hoses to booms partially plugged or collapsed. | Remove and inspect solution hoses to booms. Clean or replace hoses as necessary. |
| Boom section shutoff valve(s) faulty. | Contact a John Deere dealer or other service provider. |
| Pressure sensor faulty. | Contact a John Deere dealer or other service provider. |
| Faulty proportional valve assembly. | Contact a John Deere dealer or other service provider. |
| Nurse tank valve at tank instead of end of line putting air in system. | Put nurse tank valve at end of line. |

[[solution-control-system--e1586c|Solution Control System]] — [[spray-system-response--b1e261|Spray System Response]] · [[clean-flowmeter-as-required]].

## Application rate varies or is erratic.

| Problem | Solution |
|---|---|
| Minimum spray pressure setting entered too high. | Determine minimum pressure required and enter correct value. (See Minimum Pressure in Spray System section.) |
| Inadequate solution supply in tank. | Fill solution tank. |
| High/low flow valve in wrong position. | Turn high/low valve to correct position. (See Applying Low Application Rates in Wet System section.) |
| Solution contains heavy solids (poor mixture). | Check engine and pump speed. Check agitation line and valves. Be sure that agitation jets are not clogged. |
| Spray nozzles plugged. | Clean and inspect nozzles. Check orifices and calibration of nozzles. Replace nozzles as needed. |
| Flowmeter dirty or stuck. | Clean flowmeter with brake cleaner. |
| Incorrect sprayer response min/max valve in the control unit adjust. | Enter correct min/max setting. (See Sprayer System Response in Spray System section.) |
| Boom charge not on when it should be. | Set boom charge correctly. |
| Solution hoses to booms partially plugged or collapsed. | Remove and inspect solution hoses to booms. Clean or replace hoses as necessary. |
| Boom section shutoff valve(s) faulty. | Repair or replace boom section shutoff valve(s). |
| Air trapped in the solution system. | Verify that air is bled out of high spots. |
| Pressure sensor faulty. | Contact a John Deere dealer or other service provider. |
| Faulty proportional valve assembly. | Repair or replace. |
| Nurse tank valve at tank instead of end of line putting air in system. | Put nurse tank valve at end of line. |
| Boom supply line bleed line plugged or check valve faulty. | Clean or replace line or check valve. |

[[solution-control-system--e1586c|Solution Control System]]

**Also triggered by this symptom (maintenance topics):**

- Clean the flowmeter insert — its stated trigger is "Application rates fluctuate."
  [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]] → [[clean-flowmeter-as-required]].
- Clean the boom supply line (pressure) strainers — one of its stated triggers is "Application rates
  fluctuate." [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]] →
  [[clean-pressure-strainers-daily]].
- Air trapped in the solution system: the air-elimination recommendations and boom air bleed are on
  [[recommendations-for-eliminating-air-from-solution-system]].

> [!inference] Where to start
> The table itself does not rank causes. Three causes in this section are also the subject of
> operator maintenance topics with this exact trigger or fix (flowmeter, pressure strainers, trapped
> air), and all three are operator tasks rather than dealer tasks
> [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]]
> [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]]
> [[solution-control-system--e1586c|Solution Control System]]. That is the only basis for looking at
> them early; the manual does not say to.

## Pressure reading at the pressure sensor when there should not be a reading."

(The heading is printed with the stray closing quotation mark shown.)

| Problem | Solution |
|---|---|
| Pressure sensor not calibrated correctly. | "Zero-out" the pressure sensor. (See Pressure Sensor Calibration Procedure in the Calibrations section.) |
| Faulty proportional valve assembly. | Contact a John Deere dealer or other service provider. |

[[solution-control-system--e1586c|Solution Control System]] — [[pressure-sensor-calibration-procedure--fb814c|Pressure Sensor Calibration Procedure]].

## Pressure sensor leaks solution.

| Problem | Solution |
|---|---|
| Solution leaking from pressure sensor connection. | Tighten connection and/or apply a sealant. |

[[solution-control-system--e1586c|Solution Control System]]

## Will not maintain 827—1103 kPa (8.2—11 bar) (120—150 psi) “dead head” pressure.

| Problem | Solution |
|---|---|
| Worn impeller in the solution pump. | Replace impeller. See regular spare part channels to order. |
| Faulty solution pump. | Repair or replace solution pump. |
| Hydraulic standby pressure set too low. | Contact a John Deere dealer or other service provider. |
| Faulty proportional valve. | Replace proportional valve. |
| Faulty priority valve. | Contact a John Deere dealer or other service provider. |
| Faulty hydraulic pump. | Contact a John Deere dealer or other service provider. |

[[solution-control-system--e1586c|Solution Control System]]

**Also triggered by this symptom:** clean the boom supply line strainers — one of its stated
triggers is "Pump fails to maintain dead head pressure."
[[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]] → [[clean-pressure-strainers-daily]].

## Speed indicates 0.

| Problem | Solution |
|---|---|
| Wiring to speed sensor or radar disconnected. | Connect wiring. |
| Wheel speed calibration or radar calibration incorrectly set. | Calibrate wheel speed sensor. (See Speed Sensors Calibration Procedure in Calibration section.) |
| Bad ground. | Check ground. |
| Speed sensor connector pins corroded. | Clean connector. |
| Speed sensor misadjusted. | Contact a John Deere dealer or other service provider. |

[[solution-control-system--e1586c|Solution Control System]] — [[speed-sensors-calibration-procedure--00b315|Speed Sensors Calibration Procedure]].

## Speed incorrect.

| Problem | Solution |
|---|---|
| No radar signal because of a tall crop. | Disconnect radar and use wheel speed sensor. |
| Jumper wire (dust cap) not installed on chassis harness when radar connector is disconnected. | Install jumper wire (dust cap). |
| Wheel speed calibration or radar calibration incorrectly set. | Calibrate wheel speed sensor. (See Speed Sensors Calibration Procedure in Calibrations section.) |
| Bad ground. | Check ground. |
| Radar or wheel speed sensor faulty. | Contact a John Deere dealer or other service provider. |
| Wheel speed sensor misadjusted. | Contact a John Deere dealer or other service provider. |

[[solution-control-system--e1586c|Solution Control System]] — [[speed-sensors-calibration-procedure--00b315|Speed Sensors Calibration Procedure]].

## Tank volume does not count down.

| Problem | Solution |
|---|---|
| Flowmeter calibration value incorrectly entered in display. | Enter correct calibration information in display. (See Flowmeter Calibration Procedure in Calibrations section.) |
| Flowmeter wiring harness disconnected. | Connect flowmeter wiring harness connector. |
| Flowmeter plugged or dirty. | Clean flowmeter. |
| Flowmeter connector pins corroded. | Clean connector. |
| Flowmeter wiring harness damaged. | Repair or replace wiring harness. |
| Flowmeter installed backwards. | Remove and install the flowmeter correctly. (Arrow located on flowmeter body indicates direction of flow.) |
| Speed sensor faulty. | See "Speed indicates 0" symptom in this section. |
| Spray not discharging from nozzles. | See "No discharge from nozzles" symptom in this group. |
| Flowmeter faulty. | Contact a John Deere dealer or other service provider. |
| Boom calibration numbers incorrect. | Enter correct nozzle numbers, sections, and spacings. (See Section Setup in Boom section.) |

[[solution-control-system--e1586c|Solution Control System]] — [[flowmeter-calibration-procedure--44ce32|Flowmeter Calibration Procedure]] · [[clean-flowmeter-as-required]].

> [!inference] Cross-reference with no target
> This row and one below refer to a "No discharge from nozzles" symptom, but no symptom with that
> heading appears in this table [[solution-control-system--e1586c|Solution Control System]].

## Tank volume countdown is incorrect.

| Problem | Solution |
|---|---|
| Flowmeter calibration value incorrectly entered in display. | Enter correct calibration information in display. (See Flowmeter Calibration Procedure in Calibrations section.) |
| Flowmeter partially plugged or dirty. | Disassemble, clean, and assemble the flowmeter. |
| Flowmeter connector pins corroded. | Clean connector. |
| Flowmeter wiring harness damaged. | Repair or replace wiring harness. |
| Solution contains heavy solids (chemicals not properly mixed with the water). | See "Solution contains heavy solids" symptom in this group. |
| Air leak in the suction side of pump. | Repair air leak. |
| Flowmeter sensor not screwed in all the way. | Screw flowmeter completely into passage. |
| Flowmeter faulty. | Contact a John Deere dealer or other service provider. |
| Speed sensor faulty. | See "Speed indicates 0" symptom in this section. |
| Display set to high flow, but the valve to second flowmeter is closed. | Open valve to second flowmeter. |
| Display set to low flow, but the valve to second flowmeter is open. | Close valve to second flowmeter. |

[[solution-control-system--e1586c|Solution Control System]] — [[flowmeter-calibration-procedure--44ce32|Flowmeter Calibration Procedure]] · [[clean-flowmeter-as-required]].

## Application rates and the acre counter are incorrect in job summaries.

| Problem | Solution |
|---|---|
| Excessive spray overlap. | Adjust spraying to keep spray overlap to a minimum. |
| Large gap between sprayer passes. | Adjust spraying to minimize gaps. |
| Wheel speed and radar calibration information incorrectly entered in display. | Calibrate wheel speed sensor. (See Speed Sensors Calibration Procedure in Calibrations section.) |
| Improper data entered in the boom setup. | Enter proper data for the boom setup. (See Section Setup in Boom section.) |
| Minimum pressure too high, causing overapplication. | Decrease minimum pressure setting. (See Minimum Pressure in Spray System section.) Choose different nozzles for the higher pressure setting at same speed. |
| Radar picking up signal for tall crops. | Switch to the wheel speed sensor in tall crops. |
| Left front wheel spinning causing wheel speed sensor to give improper speed. | Recalibrate wheel speed sensor or switch to radar in muddy or hilly conditions. |
| Check if spray discharges from nozzles. | Refer to "No discharge from nozzles" symptom in this group. |
| Display set to high flow but the valve to second flowmeter is closed. | Open valve to second flowmeter. |
| Display set to low flow but the valve to second flowmeter is open. | Close valve to second flowmeter. |

[[solution-control-system--e1586c|Solution Control System]]

## Solution contains heavy solids (inadequate mixing of chemicals).

| Problem | Solution |
|---|---|
| Improper mixing method when solution tank is filled. | Mix chemicals properly. (See the chemical label.) |
| Agitation valves are closed or do not open adequately. | Open agitation valve as necessary. |
| Sprayoff pressure not set high enough for proper agitation. | Increase the sprayoff pressure setting. |
| Incorrect engine speed. | Operate engine at high idle. |
| Pump not running at specified speed. | Check hydraulic flow to hydraulic motor on pump. |
| Agitation nozzles plugged. | Unplug agitation nozzles. |
| Agitation nozzles installed backwards. | Install agitation nozzles correctly. |
| Faulty agitation nozzles. | Replace agitation nozzles. |

[[solution-control-system--e1586c|Solution Control System]] — see [[components/agitation]]. The
chemical label governs how the product is mixed.

## Sprayer will not load through the Quik-Fill valve.

| Problem | Solution |
|---|---|
| Fill strainer plugged. | Clean the fill strainer. Use clean water source for optimal performance. Contaminated water may cause strainer to plug. |

[[solution-control-system--e1586c|Solution Control System]] — [[clean-fill-strainer-aspirators-nozzle-bodies-and-tips-as-req]].

## Pump not primed.

| Problem | Solution |
|---|---|
| Solution control valves improperly set. | Set valves correctly. |
| Air in pump. | Allow solution to fill pump and push air out before running pump. |
| Fill strainer plugged. | Clean fill strainer. Use clean water source for optimal performance. Contaminated water may cause strainer to plug. |
| Pump priming procedure incorrect. | Prime the solution pump correctly. |
| Pump bleed line kinked or forms a trap. | Route bleed line so it goes directly upward from pump to the solution tank. |
| Pump bleed line partially or entirely plugged. | Clean or blow out pump bleed line. |
| Nurse tank hose does not have shutoff valve or has valve on the nurse tank end of hose. | Install shutoff valve on end of the nurse tank hose. |

[[solution-control-system--e1586c|Solution Control System]] — [[procedure-auto-prime--6f80d1|Procedure — Auto Prime]] · [[recommendations-for-eliminating-air-from-solution-system]].

## Triggers with no matching symptom heading

Clean Pressure Strainers—Daily also names "Pump fails to obtain maximum flow rate." and "Difference
between solution pump pressure and spray pressure is greater than expected for a given application."
as reasons to clean the boom supply line strainers
[[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]]. The table has no symptom
worded that way; the nearest printed symptoms are the pressure-reading symptoms above.
