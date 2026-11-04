---
type: component
title: "Nozzle"
models: [all]
options: [ExactApply, Individual Nozzle Control, See & Spray]
engine_tier: null
components: [nozzle, nozzle body, nozzle turret, solenoid, spray tip]
sources:
  - "bn55050,1775501315148-19-27APR26"
  - "BN55050,0000176-19-17APR18"
  - "bn55050,1775501494465-19-27APR26"
  - "bn55050,1775500178177-19-27APR26"
  - "bn55050,1775500806105-19-27APR26"
  - "bn55050,1775500825367-19-27APR26"
  - "ouo6092,1777915175515-19-04MAY26"
  - "bn55050,1775500420544-19-27APR26"
  - "bn55050,1775500939377-19-27APR26"
  - "ouo6092,1778517030487-19-11MAY26"
  - "bn55050,1775500282421-19-27APR26"
  - "ouo6092,1737397385465-19-27OCT25"
  - "UZEGGEY,1765865595173-19-16DEC25"
  - "aota2vy,1686155025825-19-07JUN23"
  - "CS12167,00002D2-19-04JAN13"
  - "OUO6092,000101B-19-12JAN22"
  - "as09261,1712163885782-19-16APR24"
  - "DX,WW,CHEM02-19-05APR04"
reviewed: true
compiled: 2026-09-23
---

# Nozzle

The nozzle is where the solution leaves the machine. The spray nozzles located on the center frame
and boom are used to meter, atomize, and dispense the solution into specific patterns
[[solution-system--544787|Solution System]]. Solution flow is metered by the size of the orifice in
the nozzle tip [[solution-system--544787|Solution System]]. This page covers the nozzle body, the
turret it carries and the display pages that configure them; the tips themselves are on
[[spray-tip|Spray Tip]].

## Warnings

> [!warning] CAUTION
> CAUTION: DO NOT clean nozzle tips by placing in mouth and blowing. You could swallow or inhale hazardous chemicals which will poison, causing serious injury or death to you or others.
> [[clean-nozzle-body--a341ce|Clean Nozzle Body]]

> [!warning] CAUTION
> CAUTION: Do not transport the machine when the nozzle lights are in manual mode. Your vision and the vision of others will be impaired.
> [[nozzle-body-lighting--9d74cb|Nozzle Body Lighting]]

> [!warning] IMPORTANT
> IMPORTANT: Do not pressure wash these components. Use normal water pressure less than 345 kPa (3.45 bar) (50 psi).
> [[clean-nozzle-body--a341ce|Clean Nozzle Body]]

> [!warning] IMPORTANT
> IMPORTANT: Perform a boom rinse procedure daily to help prevent nozzle plugging and solenoid malfunctions. Spray rinse water through both solenoids A and B.
> [[rinse-nozzle-bodies-daily--422740|Rinse Nozzle Bodies—Daily]]

> [!warning] Chemical sprayer safety — generic Deere-wide module
> If nozzle clogs or system malfunctions, stop engine and relieve spray pressure from system.
> Do not place nozzle tips or other components to the mouth to clear obstructions. Keep spare tips on hand for replacement.
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]]

For chemical application the product label and local regulations govern: always follow all label
directions for effective, safe, and legal use of agricultural chemicals
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].

## What it is

The Nozzle Body is the component that physically applies the product
[[exactapply-nozzle-body--a0b795|ExactApply — Nozzle Body]]. On an ExactApply machine the nozzle
body has an internal control unit that is powered by 12 V, which allows communication to the domain
controller using the Controller Area Network (CAN) protocol for system functionality and proper
solenoid timing and control [[exactapply-nozzle-body--a0b795|ExactApply — Nozzle Body]]. The nozzle
body has eight external circuits that allow the system to function and communicate to the domain
controller using harnessing and connectors
[[exactapply-nozzle-body--a0b795|ExactApply — Nozzle Body]].

Each nozzle body is integrated with a light
[[exactapply-nozzle-body--a0b795|ExactApply — Nozzle Body]]. Nozzle body lights turn on by way of a
Controller Area Network (CAN) message sent by the domain controller to the nozzle body, and are only
able to illuminate if the power and ground circuits are functioning properly
[[nozzle-body-lighting--9d74cb|Nozzle Body Lighting]].

If a nozzle body loses power, controller area network (CAN) information from the other nozzle bodies
remain in communication with the domain controller; this is referred to as nozzle body pass-through
[[exactapply-nozzle-body-pass-through--634622|ExactApply — Nozzle Body Pass-Through]]. If a nozzle
body is disconnected, it will not be able to pass CAN communication messages to downstream nozzle
bodies [[exactapply-nozzle-body-pass-through--634622|ExactApply — Nozzle Body Pass-Through]].

Most nozzles are designed for optimum performance at specific pressures, and the range of adjustment
is relatively narrow [[solution-system--544787|Solution System]]. Line pressures that are too high
or too low affect the atomization of the solution and create variations in the spray pattern
[[solution-system--544787|Solution System]]. The shape of the spray pattern is determined by the
shape of the orifice [[solution-system--544787|Solution System]].

## Where it is

Nozzle positions 1 - 6 (A) are stamped on the nozzle body turret (B) aiding in correct spray tip
placement and control unit configuration [[nozzle-body-indicators--7301c8|Nozzle Body Indicators]].

![[N120518.png]]

**Figure N120518** — A: Nozzle Positions; B: Nozzle Body Turret
[[nozzle-body-indicators--7301c8|Nozzle Body Indicators]]

Indicator marks on the nozzle body align with one or more indicator marks on the turret when in the
correct position [[nozzle-body-indicators--7301c8|Nozzle Body Indicators]]. When one mark is
aligned, solution flow is only provided from one solenoid to that nozzle; when two marks are
aligned, the solution flow from both solenoids is provided to that nozzle; if no marks are aligned,
there is no solution flow to that nozzle [[nozzle-body-indicators--7301c8|Nozzle Body Indicators]].
Indicator marks must be aligned to like shapes for solution to be sprayed from that nozzle
[[nozzle-body-indicators--7301c8|Nozzle Body Indicators]].

> [!warning] NOTE
> NOTE: Front indicator marks are difficult to see due to boom frame. Align rear indicator marks correctly to ensure that front nozzle is aligned.
> [[nozzle-body-indicators--7301c8|Nozzle Body Indicators]]

On an ExactApply machine the nozzle bodies sit on the boom with the domain controller, relay, fuse
and CAN terminator behind them
[[exactapply-nozzle-body--a0b795|ExactApply — Nozzle Body]]:

![[WZ675762.png]]

**Figure WZ675762** — A: Nozzle Body; B: Domain Controller; C: Relay; D: CAN Terminator; Red Wire:
Power (12 V); Black Wire: Ground; Blue Wire: Sync Circuit; Yellow Wire: CAN Hi Circuit; Green Wire:
CAN Lo Circuit [[exactapply-nozzle-body--a0b795|ExactApply — Nozzle Body]]

The nozzle system application is reached through the display: Menu, then the Machine Settings tab,
then Nozzle System [[access-nozzle-system--233888|Access Nozzle System]].

## Related procedures

- **Find a faulted nozzle.** Each nozzle is numbered based on its position on the spray boom, and
  nozzles are counted starting on the left-hand tip of the boom and ending at the right-hand boom
  tip [[determining-nozzle-location--984404|Determining Nozzle Location]]. There is a maximum of
  nine nozzles operated by each INC unit, and consecutive nozzles with a fault may indicate that the
  fault is at the INC unit [[determining-nozzle-location--984404|Determining Nozzle Location]]. The
  topic tabulates the last nozzle number on the left-hand wing for each boom length and nozzle
  spacing [[determining-nozzle-location--984404|Determining Nozzle Location]].
- **Rinse the nozzle bodies daily.** ExactApply nozzle bodies require both A and B solenoids to be
  rinsed, even if one channel has not been used during spray operation, and must be rinsed daily
  when a chemical has been used [[rinse-nozzle-bodies-daily--422740|Rinse Nozzle Bodies—Daily]]. The
  procedure verifies that the spray pulsing mode is set to fixed and the nozzle flow is set to
  50—75%, removes the nozzle tips on an aspirator, then rinses one section at a time at 90 psi for a
  minimum of 10 seconds per section with a recommended minimum of 454—644 L (120—170 gal) of rinse
  water [[rinse-nozzle-bodies-daily--422740|Rinse Nozzle Bodies—Daily]].
- **Clean a nozzle body.** Nozzle bodies only need to be removed from the boom when the entire
  nozzle body must be replaced; all components of the nozzle body can be serviced without removing
  the nozzle body [[clean-nozzle-body--a341ce|Clean Nozzle Body]]. Clean contaminants from the
  nozzle body using water, mild detergent, and compressed air as needed
  [[clean-nozzle-body--a341ce|Clean Nozzle Body]].
- **Check for worn nozzles.** A major cause of improper spray application is nozzle wear, and
  maintenance and timely inspection helps to identify worn nozzles and extend service life
  [[check-and-replace-worn-nozzles--baa644|Check and Replace Worn Nozzles]]. Worn spray tips have a
  higher output with more spray concentrated under each tip, and damaged spray tips have a very
  erratic output — overlapping and under applying
  [[check-and-replace-worn-nozzles--baa644|Check and Replace Worn Nozzles]].
- **Check nozzle alignment.** Check nozzles to confirm alignment is correct; if nozzles have angled
  forward or rearward, undesirable results may occur
  [[nozzle-alignment--dcbaeb|Nozzle Alignment]].
- Installing and positioning the tips and strainers in the nozzle bodies is on
  [[spray-tip|Spray Tip]].

## Related settings

All of these are display settings, reached from the Nozzle System application
[[access-nozzle-system--233888|Access Nozzle System]].

- **Nozzle Setup** allows you to view and change nozzle configuration; nozzles must be properly
  configured for the spray rate control unit to apply the desired rate of solution
  [[nozzle-setup--6c5e3e|Nozzle Setup]]. The active nozzle configurations are All Nozzles Open,
  Number of Outer Nozzles Closed and — if equipped with ExactApply or INC Pro — Even Nozzles Open,
  Odd Nozzles Open and Custom Nozzles [[nozzle-setup--6c5e3e|Nozzle Setup]]. Modify it when
  performing broadcast application, performing band spraying application, or spraying at a reduced
  width that cannot be achieved with section shutoffs [[nozzle-setup--6c5e3e|Nozzle Setup]].

  > [!warning] NOTE
  > NOTE: These configurations are not compatible when the spray mode is set to See & Spray.
  > [[nozzle-setup--6c5e3e|Nozzle Setup]]

- **Nozzle Customization** allows you to turn ON/OFF individual nozzles to create a custom
  configuration; to use the custom configuration, select the Custom Nozzles option on the Nozzle
  Setup page [[nozzle-customization--4be897|Nozzle Customization]].
- **Advanced Settings | Nozzle Customization Settings** enable or disable nozzle coverage mapping
  and grouping of outer nozzles when experiencing poor global positioning system (GPS) signal
  [[advanced-settings-nozzle-customization-settings--63de6e|Advanced Settings — Nozzle Customization Settings]].
  Map Applied Rate Across Boom Width records map coverage for all nozzles including nozzles that
  have been disabled; Group Outer Rows groups the outermost nozzles or outermost enabled sections in
  order to avoid unintentional nozzle shut-offs caused by poor GPS signal
  [[advanced-settings-nozzle-customization-settings--63de6e|Advanced Settings — Nozzle Customization Settings]].
- **Nozzle Boost Buttons** turn ON/OFF nozzle boost for individual nozzles; a greyed-out button
  means the nozzle cannot be activated [[nozzle-boost-buttons--f732df|Nozzle Boost Buttons]].
- **Nozzle Body Lighting** selects the operation mode and brightness of the nozzle lights, with
  modes OFF, ON, Strobe and Manual [[nozzle-body-lighting--9d74cb|Nozzle Body Lighting]]. Modify it
  when troubleshooting nozzle faults, when viewing nozzle spray patterns and pulsing, or when a
  change in brightness is desired [[nozzle-body-lighting--9d74cb|Nozzle Body Lighting]].
- Tip selection, tip combinations and the tip library are on [[spray-tip|Spray Tip]].

## Related warnings

The callouts under [Warnings](#warnings) above are the signal-word blocks carried by the nozzle
topics themselves. Nothing in these topics gives an operating pressure for the nozzles — see
[[spray-tip|Spray Tip]] for the tip pressure ranges and for the conflict between the generic
chemical-safety limit and the flat fan tip range.

## Related troubleshooting

The Nozzle Body troubleshooting table lists, for each symptom, the problem and the solution
[[nozzle-body--325070|Nozzle Body]]:

- Valve lodged open or closed — debris in the valve; clean debris from effected valve
  [[nozzle-body--325070|Nozzle Body]]. A damaged pressure strainer is also listed under a lodged
  open valve: check pressure strainers for holes or other damage
  [[nozzle-body--325070|Nozzle Body]].
- Boosted nozzles won't spray — debris in nozzle tip; clean around nozzle and nozzle tips
  [[nozzle-body--325070|Nozzle Body]].
- Coil circuit open or closed — defective nozzle body (test nozzle body, contact a John Deere dealer
  or other service provider, replace nozzle body) or defective coil (test coil resistance
  (6.0—7.0 ohm)) [[nozzle-body--325070|Nozzle Body]].
- System cannot maintain constant pressure — worn or sticky poppet valves, incorrect spray tip
  installed, or incorrect specific gravity entered in the display
  [[nozzle-body--325070|Nozzle Body]].
- Nozzle drips or does not shut off — plunger lodged with debris or worn, damaged O-ring, bent or
  out-of-round cartridge tube, or an over-tightened valve seat
  [[nozzle-body--325070|Nozzle Body]].
- Nozzle sprays erratically — plunger is worn; inspect and replace plunger
  [[nozzle-body--325070|Nozzle Body]].
- Solution leaks from other nozzles and around turret — turret seals failure (replace turret seals
  as needed) or debris on turret seal (clean and lubricate turret seal)
  [[nozzle-body--325070|Nozzle Body]].
- Solution leaking around solenoid coil — damaged or missing valve seat O-rings; inspect and replace
  as necessary [[nozzle-body--325070|Nozzle Body]].

Two display aids help locate the fault. **Nozzle Turret | Status** displays the system status and a
message about that status, and indicates the status of each nozzle body; select a nozzle body to
view additional status information [[nozzle-turret-status--29b8a0|Nozzle Turret — Status]]. **Nozzle
body lighting in Manual mode** assists in diagnosing wiring issues and spray tip cleaning in low
light situations: faulted nozzles that are illuminated indicate a Sync Circuit issue, and faulted
nozzles that do not illuminate indicate an issue with Controller Area Network (CAN) Communication,
the Power circuit, or the Ground circuit [[nozzle-body-lighting--9d74cb|Nozzle Body Lighting]].

> [!inference] Scope of this page
> The manual splits nozzle material between the Wet System section (wear, tips), the ExactApply and
> Individual Nozzle Control (INC) sections (nozzle body, turret, troubleshooting) and the Nozzle
> System display application (setup, customization, boost, lighting). This page gathers them and
> adds no facts of its own. Where a topic is marked as ExactApply-only or INC-only in its source,
> that is stated in the sentence above.
