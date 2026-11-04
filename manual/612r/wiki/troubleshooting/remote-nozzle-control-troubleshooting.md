---
type: troubleshooting
title: "Remote Nozzle Control"
models: [all]
options: [ExactApply, Individual Nozzle Control]
engine_tier: null
components: [remote control, receiver, nozzle body]
sources:
  - "CS12167,0000B36-19-11APR18"
  - "UZEGGEY,1765865718253-19-16DEC25"
  - "ouo6092,1778242271722-19-12MAY26"
  - "ouo6092,1778242426931-19-11MAY26"
reviewed: true
compiled: 2026-09-23
---
# Remote Nozzle Control — troubleshooting

**Options: ExactApply or Individual Nozzle Control (INC), if equipped with the remote control.** The
manual prints the same table twice — in the ExactApply section (p. 125-35) and in the INC section
(p. 130-32) — with identical text [[remote-nozzle-control--4ad76a|Remote Nozzle Control]] (p. 125-35, ExactApply) · [[remote-nozzle-control-troubleshooting--a36138|Remote Nozzle Control Troubleshooting]] (p. 130-32, INC). It is reproduced once, in its printed order; the manual
gives no cost or check order, so none is implied. The wording "has not repaired" is as printed.

Component: [[nozzle]]. The remote control is for activating individual nozzles or sections of
nozzles from outside the cab for troubleshooting purposes [[operate-system-with-the-remote-control--30853f|Operate System with the Remote Control]].

## Symptoms

### Remote control is not activating nozzle bodies.

1. **Remote control is out of range from the receiver.** — Move remote control closer to the receiver. [[remote-nozzle-control--4ad76a|Remote Nozzle Control]] (p. 125-35, ExactApply) · [[remote-nozzle-control-troubleshooting--a36138|Remote Nozzle Control Troubleshooting]] (p. 130-32, INC)
2. **Remote control has not repaired after being taken out of range.** — Move receiver in to the connection range and wait 20 seconds for pairing to take place. Place remote control within 3 m (9.8 ft) for 20 seconds. [[remote-nozzle-control--4ad76a|Remote Nozzle Control]] (p. 125-35, ExactApply) · [[remote-nozzle-control-troubleshooting--a36138|Remote Nozzle Control Troubleshooting]] (p. 130-32, INC)  
   Fix / related: [[remote-control-pairing-procedure--078e3d|Remote Control Pairing Procedure]]
3. **Remote control is locked-up from pressing and holding a button while moving out of range.** — Remove battery from the remote control, wait 20 seconds, then install battery. [[remote-nozzle-control--4ad76a|Remote Nozzle Control]] (p. 125-35, ExactApply) · [[remote-nozzle-control-troubleshooting--a36138|Remote Nozzle Control Troubleshooting]] (p. 130-32, INC)
4. **Remote control usage attempted too soon after machine start-up.** — Wait at least 2 minutes after machine start-up before using the remote control. [[remote-nozzle-control--4ad76a|Remote Nozzle Control]] (p. 125-35, ExactApply) · [[remote-nozzle-control-troubleshooting--a36138|Remote Nozzle Control Troubleshooting]] (p. 130-32, INC)
5. **Signal to the receiver is blocked.** — Ensure that there is a clear line of sight to the receiver. Avoid having steel structure between the receiver and remote control. [[remote-nozzle-control--4ad76a|Remote Nozzle Control]] (p. 125-35, ExactApply) · [[remote-nozzle-control-troubleshooting--a36138|Remote Nozzle Control Troubleshooting]] (p. 130-32, INC)

> [!note] Conditions the system requires (ExactApply operating topic)
> The following conditions must be met before controlling the system with the remote control:
> solution pump is ON; no remote loading operations are active; machine is in park; boom is
> unfolded. If any condition becomes not met during remote operation the system is disabled [[operate-system-with-the-remote-control--30853f|Operate System with the Remote Control]].
> Only enabled nozzles are controlled when using the remote control [[operate-system-with-the-remote-control--30853f|Operate System with the Remote Control]].
>
> The same topic adds a battery check: if NODC Data Identifier (DID) 1300 does not change when a
> button is pressed, verify that NODC DID 1306 matches the underlined number of the remote
> control's serial number; if it matches, replace the CR2032 battery; if it does not match or shows
> 999999999, the remote control must be paired [[operate-system-with-the-remote-control--30853f|Operate System with the Remote Control]], [[remote-control-pairing-procedure--078e3d|Remote Control Pairing Procedure]].

> [!conflict] Distance for re-pairing
> The troubleshooting tables say to place the remote control within 3 m (9.8 ft) for 20 seconds
> [[remote-nozzle-control--4ad76a|Remote Nozzle Control]] (p. 125-35, ExactApply) · [[remote-nozzle-control-troubleshooting--a36138|Remote Nozzle Control Troubleshooting]] (p. 130-32, INC); the ExactApply operating topic says to position the remote control within 2—3 meters of the
> receiver for 20 seconds [[operate-system-with-the-remote-control--30853f|Operate System with the Remote Control]]. Both machine-specific; the ranges overlap but are not the same.

## What the manual does not specify here

- An INC-specific operating topic for the remote was not found among the sources read; the
  conditions and DID checks above come from the ExactApply section [[operate-system-with-the-remote-control--30853f|Operate System with the Remote Control]].
