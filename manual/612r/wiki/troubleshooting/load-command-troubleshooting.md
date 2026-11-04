---
type: troubleshooting
title: "Load Command troubleshooting"
models: [all]
options: [Load Command]
engine_tier: null
components: [load command pump, sprayer coupler, nurse arm, tank level sensor, solution tank]
sources:
  - "aota2vy,1686142179306-19-07JUN23"
  - "OUO6092,0000A8E-19-26FEB16"
  - "BN55050,0000262-19-23JAN26"
  - "ouo6092,1763585035606-19-27APR26"
  - "ouo6092,1737395939957-19-27OCT25"
  - "bjn2cs6,1768321198858-19-15JAN26"
  - "aota2vy,1686075851431-19-08JUN23"
  - "bn55050,1778258526757-19-08MAY26"
  - "aota2vy,1686075980838-19-06JUN23"
  - "aota2vy,1686148101904-19-07JUN23"
  - "aota2vy,1686147285889-19-07JUN23"
  - "BN55050,0000264-19-08JUN18"
  - "CS12167,000049C-19-24OCT13"
  - "bn55050,1778257283886-19-08MAY26"
  - "aota2vy,1686075917695-19-06JUN23"
reviewed: true
compiled: 2026-09-23
---

# Load Command troubleshooting

**This page applies only to machines with the Load Command option** [[troubleshooting-load-command-system--1bc786|Troubleshooting Load Command System]]. The manual prints Load Command
troubleshooting as separate tables. This page carries the Load Command System table (p. 120-10 to 120-11)
and the Load Command Pump table (p. 120-11 to 120-12), each under its own heading, with symptoms as
printed and causes in the printed order. The Nurse Arm and Sprayer Coupler tables are separate
([[troubleshooting-nurse-arm--064225|Troubleshooting Nurse Arm]],
[[troubleshooting-sprayer-coupler--8f85af|Troubleshooting Sprayer Coupler]]).

The tank level values in these tables are printed only for the 612R and 616R. The 612R Load Command
system slows pumping down at 4353 L (1150 gal) and shuts off at 4542 L (1200 gal). The 616R system slows
pumping down at 5867 L (1550 gal) and shuts off at 6056 L (1600 gal) [[operating-load-command--d37e14|Operating Load Command]].

> [!inference] Rows continued across pages
> On p. 120-12 the row "Improper Load Command pump calibration." has an empty Symptom column. It is listed
> under *Pump does not achieve full rate.*, the last pump symptom on p. 120-11 [[troubleshooting-load-command-pump--4d3750|Troubleshooting Load Command Pump]].

## Load Command System table

### Tank foams too much.
*p. 120-10* [[troubleshooting-load-command-system--1bc786|Troubleshooting Load Command System]]

- **During first 265 L (70 gal) of filling, reduction in pump speed is not triggered.** → Check 265 L
  (70 gal) tank level sensor function.
- **The 76 mm (3 in) drop line inside tank is directing the flow incorrectly into the tank.** → Properly
  position 76 mm (3 in) drop line on rod guide so that the outlet of hose is submersed before the 265 L
  (70 gal) mark.
- **Chemical used is susceptible to foaming.** → Use anti-foaming agent.
- **Air in system.** → Check for vacuum leaks in plumbing upstream of pump.
- **Foam generated during auto evacuation cycle.** → Evacuate only when required.

### Pump running at full speed with slow fill time.
*p. 120-10* [[troubleshooting-load-command-system--1bc786|Troubleshooting Load Command System]]

- **Air entering suction line.** → Check for air leaks in plumbing on the nurse vehicle and sprayer.

### Load Command system does not start.
*p. 120-11* [[troubleshooting-load-command-system--1bc786|Troubleshooting Load Command System]]

- **Machine not started or not in park.** → Verify that machine is on and in park.
- **Load Command system believes that the tank is already full.** → Check 4542 L (1200 gal) for the 612R
  tank level sensor function, and check 6056 L (1200 gal) for the 616R tank level sensor function.
- **Nurse coupler not properly connected to sprayer coupler.** → Verify that coupler is fully seated.
- **Arming switch has not been activated.** → Activate arming switch on the front coupler.
- **Proximity sensors covered with dirt/ debris or failed.** → Clean sensors with mild detergent and damp
  cloth. See [[clean-sprayer-coupler--977ce7|Clean Sprayer Coupler]].

> [!conflict] 616R tank level sensor volume
> The troubleshooting table says to "check 6056 L (1200 gal) for the 616R tank level sensor function" [[troubleshooting-load-command-system--1bc786|Troubleshooting Load Command System]],
> but the Load Command operating topic says the 616R system "shuts off at 6056 L (1600 gal)" [[operating-load-command--d37e14|Operating Load Command]]. The
> metric figure agrees; the gallon figure does not. Neither is a generic module. The manual does not say
> which is correct. The 616R solution tank capacity is itself printed three different ways elsewhere in
> the manual; see the conflicts register.

### Cannot evacuate chemicals out of system.
*p. 120-11* [[troubleshooting-load-command-system--1bc786|Troubleshooting Load Command System]]

- **Evacuation incorrectly selected on display.** → Verify that evacuation is correctly selected on display.
- **Fewer than 284 L (75 gal) in the solution tank.** → Verify that at least 284 L (75 gal) are in the
  solution tank.
- **Eductor valve not opening, venturi blocked.** → Verify that eductor valve opens and closes properly.
  Verify that venturi at the top of tank is free of obstruction. See [[eductor-troubleshooting]].
- **Eductor hopper valves are open.** → Verify that eductor hopper valves are closed.

### System does not shut off after 4542 L (1200 gal).
*p. 120-11* [[troubleshooting-load-command-system--1bc786|Troubleshooting Load Command System]]

- **Tank level sensors blocked or malfunctioning.** → Verify that tank level sensors are in place and
  moving freely.
- **Machine not parked on a level surface while loading solution.** → Load machine on a level surface.

## Load Command Pump table

### Pump does not achieve full rate.
*p. 120-11, continued on p. 120-12* [[troubleshooting-load-command-pump--4d3750|Troubleshooting Load Command Pump]]

- **Restriction on nurse vehicle plumbing.** → Verify that nurse tank vent is open and adequate. See
  [[set-up-nurse-vehicle-plumbing--8389b8|Set Up Nurse Vehicle Plumbing]].
- **Pump running at reduced speed for entire fill due to lack of 265 L (70 gal) tank level signal.** →
  Check 265 L (70 gal) tank level sensor function.
- **Pump running at reduced speed for entire fill due to wrong signal from 4353 L (1150 gal) for the 612R
  tank level sensor, and 5867 L (1550 gal) for the 616R tank level sensor.** → Check 4353 L (1150 gal) for
  the 612R tank level sensor, and check 5867 L (1550 gal) for the 616R tank level sensor.
- *(p. 120-12)* **Improper Load Command pump calibration.** → Perform pump calibration. See
  [[load-command-pump-calibration-procedure--6bc54d|Load Command Pump Calibration Procedure]].

### Pump does not achieve full rate and makes noise during start of fill.
*p. 120-12* [[troubleshooting-load-command-pump--4d3750|Troubleshooting Load Command Pump]]

- **Pump is cavitating, not priming.** → Verify that pump is getting adequate solution flow.

### Excessive continued knocking of the pump.
*p. 120-12* [[troubleshooting-load-command-pump--4d3750|Troubleshooting Load Command Pump]]

- **Knock sensor not functioning correctly.** → Check knock sensor connection. (Contact a John Deere
  dealer or other service provider.)

### Pump locks up or has start-up difficulties due to swelling lobes.
*p. 120-12* [[troubleshooting-load-command-pump--4d3750|Troubleshooting Load Command Pump]]

- **Incompatible chemical with the EPDM pump lobes.** → Use correct grease per Operator's Manual. Properly
  rinse system after each chemical use. Do not let pump sit idle with the chemical in it. Replace pump lobes
  with Viton or replacement EPDM lobes from service parts.

### Pump running but not loading.
*p. 120-12* [[troubleshooting-load-command-pump--4d3750|Troubleshooting Load Command Pump]]

- **Valve to the nurse tank closed.** → Check nurse-side valves. See
  [[open-nurse-vehicle-valves--d6ada2|Open Nurse Vehicle Valves]].
- **Shutoff valve for the poppet cylinder is closed.** → Fully open the valve. See
  [[service-sprayer-coupler--26f987|Service Sprayer Coupler]].
- **Pump lost prime (most likely to occur after major servicing).** → Add 3.8 L (1 gal) of water to priming
  port on the pump outlet. See [[fill-load-command-pump--e83c85|Fill Load Command Pump]].

> [!conflict] Water to prime the Load Command pump
> The pump troubleshooting table says "Add 3.8 L (1 gal) of water to priming port on the pump outlet" [[troubleshooting-load-command-pump--4d3750|Troubleshooting Load Command Pump]].
> The Fill Load Command Pump procedure says "Fill port with minimum of 3.7 L (1 gal) of water"
> [[fill-load-command-pump--e83c85|Fill Load Command Pump]]. Both give 1 gal; the metric figure differs.
> Neither is a generic module.

## Warnings for the fixes

Operating, servicing the coupler, and handling the nurse vehicle:

> [!warning] CAUTION — nurse tank on a hill · [[operating-load-command--d37e14|Operating Load Command]]
> CAUTION: Swinging nurse arm can cause injury to you and others. DO NOT PARK the nurse tank on a hill where the nurse arm could swing out. ALWAYS park the nurse tank on flat ground.
>
> *Printed on:* p. 120-7 [[operating-load-command--d37e14|Operating Load Command]]
> *Applies to:* machines with Load Command

> [!warning] CAUTION — nurse arm control · [[operating-load-command--d37e14|Operating Load Command]]
> CAUTION: Swinging nurse arm can cause injury to you and others. Always maintain control of the nurse arm when it is unlatched or disconnected.
>
> *Printed on:* p. 120-7 [[operating-load-command--d37e14|Operating Load Command]]
> *Applies to:* machines with Load Command

> [!warning] CAUTION — PPE when operating · [[operating-load-command--d37e14|Operating Load Command]]
> CAUTION: Operator must wear appropriate personal protection equipment when operating Load Command.
>
> *Printed on:* p. 120-7 [[operating-load-command--d37e14|Operating Load Command]]
> *Applies to:* machines with Load Command

> [!warning] CAUTION — solution in the coupler · [[operating-load-command--d37e14|Operating Load Command]]
> CAUTION: Solution could remain in the nurse arm coupler after disconnecting from the sprayer coupler. Wear protective equipment to ensure that excess solution does not come into contact with you or others.
>
> *Printed on:* p. 120-9 [[operating-load-command--d37e14|Operating Load Command]]
> *Applies to:* machines with Load Command

> [!warning] CAUTION — solution in the coupler · [[service-nurse-arm-coupler--3c1e91|Service Nurse Arm Coupler]]
> CAUTION: Solution could remain in the nurse arm coupler. Wear protective equipment to ensure that excess solution does not come into contact with you or others.
>
> *Printed on:* p. 120-16 [[service-nurse-arm-coupler--3c1e91|Service Nurse Arm Coupler]]
> *Applies to:* machines with Load Command

> [!warning] CAUTION — no filling across roads · [[determine-appropriate-approach--1c70a2|Determine Appropriate Approach]]
> CAUTION: Do NOT perform fill operation between sprayer and nurse vehicle across public roads.
>
> *Printed on:* p. 120-6 [[determine-appropriate-approach--1c70a2|Determine Appropriate Approach]]
> *Applies to:* machines with Load Command

> [!warning] CAUTION — PPE when servicing the coupler · [[load-command-poppet-maintenance-procedure--ae260c|Load Command Poppet Maintenance Procedure]]
> CAUTION: Operator must wear appropriate personal protection equipment when servicing sprayer coupler.
> Servicing can result in solution loss. Run evacuation and rinse procedures to prevent solution loss. Collect remaining solution.
> Coupler cylinder is spring loaded with compression spring and could cause serious injury to you or others.
>
> *Printed on:* p. 25-B-12 [[load-command-poppet-maintenance-procedure--ae260c|Load Command Poppet Maintenance Procedure]]
> *Applies to:* machines with Load Command

> [!warning] CAUTION — PPE when servicing the coupler · [[service-sprayer-coupler--26f987|Service Sprayer Coupler]]
> CAUTION: Operator must wear appropriate personal protection equipment when servicing sprayer coupler.
>
> *Printed on:* p. 120-15 [[service-sprayer-coupler--26f987|Service Sprayer Coupler]]
> *Applies to:* machines with Load Command

> [!warning] CAUTION — solution loss during service · [[service-sprayer-coupler--26f987|Service Sprayer Coupler]]
> CAUTION: Servicing can result in solution loss. Run evacuation and rinse procedures to prevent solution loss. Collect remaining solution.
>
> *Printed on:* p. 120-15 [[service-sprayer-coupler--26f987|Service Sprayer Coupler]]
> *Applies to:* machines with Load Command

> [!warning] CAUTION — spring-loaded coupler cylinder · [[service-sprayer-coupler--26f987|Service Sprayer Coupler]]
> CAUTION: Coupler cylinder is spring-loaded with compression spring and could cause serious injury to you or others.
>
> *Printed on:* p. 120-15 [[service-sprayer-coupler--26f987|Service Sprayer Coupler]]
> *Applies to:* machines with Load Command

> [!warning] IMPORTANT — dirty sensors · [[clean-sprayer-coupler--977ce7|Clean Sprayer Coupler]]
> IMPORTANT: Air seal (A) and proximity sensors (B) may not function properly when covered with dirt or debris and can lead to equipment malfunction.
>
> *Printed on:* p. 120-6 [[clean-sprayer-coupler--977ce7|Clean Sprayer Coupler]]
> *Applies to:* machines with Load Command

> [!warning] IMPORTANT — no pressure washing · [[clean-sprayer-coupler--977ce7|Clean Sprayer Coupler]]
> IMPORTANT: Do not pressure wash sprayer coupler components. Pressure washing can lead to equipment malfunction.
>
> *Printed on:* p. 120-6 [[clean-sprayer-coupler--977ce7|Clean Sprayer Coupler]]
> *Applies to:* machines with Load Command

> [!warning] IMPORTANT — pump must have fluid · [[fill-load-command-pump--e83c85|Fill Load Command Pump]]
> IMPORTANT: Load Command pump must have fluid prior to operating. Lack of fluid in pump could cause pump to malfunction.
>
> *Printed on:* p. 120-14 [[fill-load-command-pump--e83c85|Fill Load Command Pump]]
> *Applies to:* machines with Load Command

> [!warning] IMPORTANT — nurse vehicle pump · [[turn-off-nurse-vehicle-pumps--3b54d3|Turn Off Nurse Vehicle Pumps]]
> IMPORTANT: LoadCommand system is designed to use ONLY Load Command pump. Nurse vehicle pump can cause decrease in performance and Load Command system to malfunction.
>
> *Printed on:* p. 120-6 [[turn-off-nurse-vehicle-pumps--3b54d3|Turn Off Nurse Vehicle Pumps]]
> *Applies to:* machines with Load Command

> [!warning] IMPORTANT — nurse vehicle valve · [[open-nurse-vehicle-valves--d6ada2|Open Nurse Vehicle Valves]]
> IMPORTANT: Nurse vehicle valve (A) must be open for Load Cmmand system to operate at maximum capacity. Close valve when Load Command system not in use.
>
> *Printed on:* p. 120-6 [[open-nurse-vehicle-valves--d6ada2|Open Nurse Vehicle Valves]]
> *Applies to:* machines with Load Command

> [!warning] IMPORTANT — flow path restrictions · [[set-up-nurse-vehicle-plumbing--8389b8|Set Up Nurse Vehicle Plumbing]]
> IMPORTANT: Load Command system is sensitive to flow path restrictions between the nurse tank and nurse arm coupler. Restrictions could result in slower fill times and reduced performance. Use the following recommendations when plumbing coupler to tank.
>
> *Printed on:* p. 120-4 [[set-up-nurse-vehicle-plumbing--8389b8|Set Up Nurse Vehicle Plumbing]]
> *Applies to:* machines with Load Command

> [!warning] IMPORTANT — poppet shutoff valve · [[service-sprayer-coupler--26f987|Service Sprayer Coupler]]
> IMPORTANT: Shutoff valve must be completely opened for Load Command to function.
>
> *Printed on:* p. 120-16 [[service-sprayer-coupler--26f987|Service Sprayer Coupler]]
> *Applies to:* machines with Load Command

## What the manual does not specify

- Any tank level values for Load Command on models other than the 612R and 616R [[troubleshooting-load-command-system--1bc786|Troubleshooting Load Command System]] [[operating-load-command--d37e14|Operating Load Command]].
- How to test the knock sensor or the tank level sensors. The table sends these to "check … function" or to
  the dealer [[troubleshooting-load-command-pump--4d3750|Troubleshooting Load Command Pump]].
