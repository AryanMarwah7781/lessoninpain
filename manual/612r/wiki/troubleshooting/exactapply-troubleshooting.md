---
type: troubleshooting
title: "ExactApply troubleshooting"
models: [all]
options: [ExactApply]
engine_tier: null
components: [nozzle, nozzle body, solenoid, cartridge, domain controller, CAN, sync circuit, remote nozzle control]
sources:
  - "bn55050,1775500956096-19-27APR26"
  - "bn55050,1775501199548-19-27APR26"
  - "bn55050,1775501259968-19-27APR26"
  - "bn55050,1775501276850-19-27APR26"
  - "bn55050,1775501295428-19-27APR26"
  - "bn55050,1775501511172-19-27APR26"
  - "bn55050,1775501548883-19-27APR26"
  - "ouo6092,1737397385465-19-27OCT25"
  - "CS12167,0000B36-19-11APR18"
  - "bn55050,1775500939377-19-27APR26"
reviewed: true
compiled: 2026-09-23
---

# ExactApply troubleshooting

**Option: ExactApply.** This page applies only to machines with the ExactApply nozzle control system.
The Nozzle System application's ExactApply | Troubleshooting page "further describes the ExactApply
system and assists with active issues", and points to the System Overview and to Error Messages
[[exactapply-troubleshooting--a07389|ExactApply — Troubleshooting]]. The manual's symptom tables for
ExactApply are the Nozzle Body table (125-34, 125-35) and the Remote Nozzle Control table (125-35)
[[nozzle-body--325070|Nozzle Body]] [[remote-nozzle-control--4ad76a|Remote Nozzle Control]]. Error
messages, table symptoms and rows are in the manual's printed order. Components:
[[components/nozzle]], [[components/electrical-system]], [[components/spray-tip]].

## Warnings for the fixes

> [!warning] CAUTION — printed on [[repair-nozzle-solenoid--eba495|Repair Nozzle Solenoid]] (p. 125-27, 125-28, 125-29, 125-30); [[repair-nozzle-solenoid--fa18a1|Repair Nozzle Solenoid]] (p. 130-27, 130-28, 130-29). Applies to: repairing the nozzle solenoid
> CAUTION: DO NOT clean nozzle tips by placing in mouth and blowing. This action could result in swallowing or inhaling hazardous chemicals that will poison, causing serious injury or death. Relieve trapped pressure in the spray boom before servicing nozzle body.

> [!warning] CAUTION — printed on [[rinse-system-solution-system--7b8ab5|Rinse System — Solution System]] (p. 25-H-6, 25-H-7); [[rinse-system-solution-tank-only--6b39f5|Rinse System — Solution Tank Only]] (p. 25-H-7, 25-H-8). Applies to: removing and installing a nozzle body
> CAUTION: Spray system can contain hazardous material that can cause serious injury or death to you or others. Wear protective clothing, eyewear, and gloves. Use rinse system in an area where people, animals, vegetation, water supply, and so on, cannot be contaminated.

> [!warning] CAUTION — printed on [[remove-and-install-nozzle-body-as-required--0a5d16|Remove and Install Nozzle Body—As Required]] (p. 125-25, 125-26). Applies to: removing and installing a nozzle body
> CAUTION: Spray system can contain hazardous material that can cause serious injury or death to you or others. Wear protective clothing, eyewear, and gloves. Perform service in an area where people, animals, vegetation, and water supply, and so on, cannot be contaminated. Do not drain solution onto the ground. Drain into a container. High pressure is trapped in the boom on machines equipped with Direct Injection. Perform pressure relief procedure before servicing the nozzle body.

> [!warning] IMPORTANT — printed on [[clean-nozzle-body--f5b5d2|Clean Nozzle Body]] (p. 125-20); [[clean-nozzle-body--a341ce|Clean Nozzle Body]] (p. 130-21). Applies to: cleaning nozzle bodies
> IMPORTANT: Do not pressure wash these components. Use normal water pressure less than 345 kPa (3.45 bar) (50 psi).

> [!warning] CAUTION — printed on [[nozzle-body-lighting--9d74cb|Nozzle Body Lighting]] (p. 25-G-30, 25-G-31). Applies to: using manual nozzle lighting to diagnose
> CAUTION: Do not transport the machine when the nozzle lights are in manual mode. Your vision and the vision of others will be impaired.

> [!warning] IMPORTANT — printed on [[rinse-nozzle-bodies-daily--422740|Rinse Nozzle Bodies—Daily]] (p. 125-20, 125-21). Applies to: daily nozzle body rinse
> IMPORTANT: Perform a boom rinse procedure daily to help prevent nozzle plugging and solenoid malfunctions. Spray rinse water through both solenoids A and B.

> [!warning] IMPORTANT — printed on [[rinse-nozzle-bodies-daily--5d2892|Rinse Nozzle Bodies—Daily]] (p. 130-21). Applies to: daily nozzle body rinse
> IMPORTANT: Perform a boom rinse procedure daily to help prevent nozzle plugging and solenoid malfunctions.

Relieve trapped pressure in the spray boom before servicing nozzle body — see
[[relieve-spray-pressure]].

## Error messages

The Error Messages page lists: CAN Bus Disabled, Communication Failure, Nozzle Addressing Failure,
Nozzle Short, Sticking, Stuck, or Open, and Sync Signal Missing
[[exactapply-error-messages--2d4d3d|ExactApply — Error Messages]].

### CAN Bus Disabled

CAN Bus Disabled indicates that a Controller Area Network (CAN) bus error was detected by the domain
controller and has disabled the Subnet; the fault will show the entire subnet as faulted
[[exactapply-can-bus-disabled--ec318b|ExactApply — CAN Bus Disabled]]. Causes printed: Failed
terminator; Internal Nozzle Body failure; CAN circuit short
[[exactapply-can-bus-disabled--ec318b|ExactApply — CAN Bus Disabled]].

### Communication Failure

Communication Failure indicates that at least one Nozzle Body on the Subnet is not communicating to
the domain controller by means of the Controller Area Network (CAN)
[[exactapply-communication-failure--426290|ExactApply — Communication Failure]]. This failure can only
occur if the machine powers up and is functioning correctly, and then the properly addressed and
functioning nozzle body on a subnet loses power, ground, or CAN communication
[[exactapply-communication-failure--426290|ExactApply — Communication Failure]]. If the issue is CAN
communication, all nozzle bodies outboard from the site of failure on the subnet will also lose
communication or show as faulted; if power or ground to the nozzle body is lost, the other nozzle
bodies can remain in communication with the domain controller
[[exactapply-communication-failure--426290|ExactApply — Communication Failure]].

### Nozzle Addressing Failure

Nozzle Addressing Failure indicates that one or more Nozzle Bodies did not complete the Addressing
Process when the ignition key was turned on
[[exactapply-nozzle-addressing-failure--72ff33|ExactApply — Nozzle Addressing Failure]]. If a nozzle
body does not have power, ground, CAN, or Sync, it and the remaining nozzle bodies on that subnet
cannot establish their location
[[exactapply-nozzle-addressing-failure--72ff33|ExactApply — Nozzle Addressing Failure]]. Check: set
the Nozzle Body Lighting mode to manual — faulted nozzle bodies that remain illuminated indicate an
issue with the Sync Circuit, and faulted nozzle bodies that are not illuminated indicate an issue with
the CAN Bus, Power, or Ground circuits
[[exactapply-nozzle-addressing-failure--72ff33|ExactApply — Nozzle Addressing Failure]]
[[nozzle-body-lighting--9d74cb|Nozzle Body Lighting]].

### Nozzle Short, Sticking, Stuck, or Open

The internal Nozzle Body control unit can identify a fault with the solenoid and cartridge assembly;
faults caused by an open circuit or short circuit require troubleshooting, and the topic says to
verify that the solenoid resistance is 6 —8 ohms
[[exactapply-nozzle-short-sticking-stuck-or-open--afca0a|ExactApply — Nozzle Short, Sticking, Stuck, or Open]].
For limited movement and stuck plunger faults: disassemble the cartridge assembly, clean, and
reassemble; if the fault remains, swap the cartridge and solenoid with a different nozzle cartridge
and solenoid to determine whether the issue is the internal nozzle body control unit circuit or the
solenoid and cartridge assembly
[[exactapply-nozzle-short-sticking-stuck-or-open--afca0a|ExactApply — Nozzle Short, Sticking, Stuck, or Open]].
Repair steps: [[repair-nozzle-solenoid--eba495|Repair Nozzle Solenoid]].

> [!conflict] Solenoid coil resistance
> The Nozzle Short, Sticking, Stuck, or Open topic says to verify that the solenoid resistance is
> 6 —8 ohms
> [[exactapply-nozzle-short-sticking-stuck-or-open--afca0a|ExactApply — Nozzle Short, Sticking, Stuck, or Open]],
> while the Nozzle Body troubleshooting table says "Test coil resistance (6.0—7.0 ohm)"
> [[nozzle-body--325070|Nozzle Body]]. Both are ExactApply topics. Not reconciled here; confirm the
> specification with your John Deere dealer.

### Sync Signal Missing

Sync Signal Missing indicates that the faulted Nozzle Body is not receiving the 15-Hz heartbeat signal
from the adjacent nozzle body inboard, and is typically caused by faulty nozzle body or an issue with
the wiring harness [[exactapply-sync-signal-missing--d95a7c|ExactApply — Sync Signal Missing]]. The
three scenarios printed are Failed Input (the nozzle body reporting the error), Failed Output (the
nozzle body directly inboard), and Failed Circuit (between the two)
[[exactapply-sync-signal-missing--d95a7c|ExactApply — Sync Signal Missing]]. Determine the location of
the fault using the Nozzle Turret | Status screen in the Nozzle System display application, and start
troubleshooting the sync circuit at the fault location that is closest to the center of the machine
[[exactapply-sync-signal-missing--d95a7c|ExactApply — Sync Signal Missing]]. After a restart, the
issue may change to a Nozzle Addressing Failure
[[exactapply-sync-signal-missing--d95a7c|ExactApply — Sync Signal Missing]].

## Nozzle Body table

Symptoms and rows as printed [[nozzle-body--325070|Nozzle Body]].

### Valve is lodged open.

| Problem | Solution |
|---|---|
| Debris in the valve. | Clean debris from effected valve. |
| Pressure strainer damaged. | Check pressure strainers for holes or other damage. |

[[nozzle-body--325070|Nozzle Body]] — [[clean-pressure-strainers-daily]].

### Boosted nozzles won't spray.

| Problem | Solution |
|---|---|
| Debris in nozzle tip. | Clean around nozzle and nozzle tips. |

[[nozzle-body--325070|Nozzle Body]]

### Valve is lodged closed.

| Problem | Solution |
|---|---|
| Debris in the valve. | Clean debris from effected valve. |

[[nozzle-body--325070|Nozzle Body]]

### Coil circuit is open.

| Problem | Solution |
|---|---|
| Defective nozzle body. | Test nozzle body. Contact a John Deere dealer or other service provider. Replace nozzle body. |
| Coil is defective. | Test coil resistance (6.0—7.0 ohm). |

[[nozzle-body--325070|Nozzle Body]] — see the resistance conflict above.

### Coil circuit is closed.

| Problem | Solution |
|---|---|
| Defective nozzle body. | Test nozzle body. Contact a John Deere dealer or other service provider. Replace nozzle body. |
| Coil is defective. | Test coil resistance (6.0—7.0 ohm). |

[[nozzle-body--325070|Nozzle Body]]

### System cannot maintain constant pressure.

| Problem | Solution |
|---|---|
| Worn poppet valves. | Inspect and replace poppet valves. |
| Sticky poppet valves. | Inspect and clean poppet valves. |
| Incorrect spray tip installed. | Install correctly sized spray tips. |
| Incorrect specific gravity entered. | Enter the correct specific gravity in the display. |

[[nozzle-body--325070|Nozzle Body]] — [[components/spray-tip]].

### Nozzle drips or does not shut off.

| Problem | Solution |
|---|---|
| Plunger is lodged with debris. | Remove and clean the plunger. |
| Plunger is worn. | Inspect and replace plunger. |
| An O-ring is damaged. | Replace O-ring. |
| Cartridge tube bent. | Roll tube on flat surface to check straightness, replace as necessary. |
| Cartridge tube out of round. | Inspect for damage due to improper tool usage. Verify plunge moves freely in tube. Replace as necessary. |
| Valve seat over-tightened. | Check for damaged or deformed threads. Replace as necessary. |

[[nozzle-body--325070|Nozzle Body]] — [[repair-nozzle-solenoid--eba495|Repair Nozzle Solenoid]].
The Wet System section also has a base-machine table for nozzles that drip, leak, or seep after the
valve is shut off
[[troubleshooting-nozzles-that-drip-leak-or-seep-after-valve-i--948232|Troubleshooting Nozzles That Drip, Leak, Or Seep After Valve is Shut Off]].

### Nozzle sprays erratically.

| Problem | Solution |
|---|---|
| Plunger is worn. | Inspect and replace plunger. |

[[nozzle-body--325070|Nozzle Body]]

### Solution leaks from other nozzles and around turret.

| Problem | Solution |
|---|---|
| Turret seals failure. | Replace turret seals as needed. |
| Debris on turret seal. | Clean and lubricate turret seal. |

[[nozzle-body--325070|Nozzle Body]]

### Solution leaking around solenoid coil.

| Problem | Solution |
|---|---|
| Damaged or missing valve seat O-rings. | Inspect and replace as necessary. |

[[nozzle-body--325070|Nozzle Body]]

## Remote Nozzle Control table

### Remote control is not activating nozzle bodies.

| Problem | Solution |
|---|---|
| Remote control is out of range from the receiver. | Move remote control closer to the receiver. |
| Remote control has not repaired after being taken out of range. | Move receiver in to the connection range and wait 20 seconds for pairing to take place. Place remote control within 3 m (9.8 ft) for 20 seconds. |
| Remote control is locked-up from pressing and holding a button while moving out of range. | Remove battery from the remote control, wait 20 seconds, then install battery. |
| Remote control usage attempted too soon after machine start-up. | Wait at least 2 minutes after machine start-up before using the remote control. |
| Signal to the receiver is blocked. | Ensure that there is a clear line of sight to the receiver. Avoid having steel structure between the receiver and remote control. |

[[remote-nozzle-control--4ad76a|Remote Nozzle Control]]
