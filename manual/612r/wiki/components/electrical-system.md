---
type: component
title: "Electrical System"
models: [all]
options: [ExactApply, Individual Nozzle Control, See & Spray]
engine_tier: null
components: [electrical system, battery, alternator, fuse, relay, load center, CAN]
sources:
  - "TB90758,00027DA-19-10MAR21"
  - "BN55050,0000255-19-23MAY18"
  - "UZEGGEY,1764571242337-19-29APR26"
  - "bjn2cs6,1767892023661-19-08JAN26"
  - "ouo6092,1737124093709-19-27OCT25"
  - "bn55050,1767633767570-19-05JAN26"
  - "UZEGGEY,1765865615581-19-17DEC25"
  - "bn55050,1767711848930-19-06JAN26"
  - "DX,WW,BATTERIES-19-02DEC10"
  - "ouo6092,1737122246884-19-27OCT25"
  - "CS12167,0000219-19-13JUN13"
  - "AG,OUO1011,817-19-26MAR04"
  - "TB90758,00027E1-19-10MAR21"
  - "OUO6075,00003DD-19-01JUL09"
  - "OUO6092,0000874-19-23JUL05"
  - "BN55050,00000B7-19-26FEB18"
  - "bn55050,1775501179731-19-27APR26"
  - "bn55050,1775501315148-19-27APR26"
reviewed: true
compiled: 2026-09-23
---

# Electrical System

The machine's electrical system runs from two batteries and an alternator through the battery box
fuses and load centers to the control units, lights and the nozzle network on the boom. This page
covers the battery, the fuses and relays, and the service rules that apply before anyone works on
any of it.

## Warnings

> [!warning] WARNING
> WARNING: Battery posts, terminals, and related accessories contain lead and lead compounds, chemicals known to the State of California to cause cancer and reproductive harm. Wash hands after handling.
> [[handling-batteries-safely--3a873e|Handling Batteries Safely]]

> [!warning] CAUTION
> CAUTION: Batteries can explode causing serious injury or death to you or others. Do not attempt to service batteries unless you have the proper equipment and experience to perform the job. Have it done by a John Deere dealer or other service provider.
> [[servicing-batteries--e9a1c5|Servicing Batteries]]

> [!warning] CAUTION
> CAUTION: Gas given off by batteries is explosive. Keep sparks and flames away from batteries. Make last connection and first disconnection at a point away from booster batteries.
> [[operate-a-booster-battery-or-charger--6af242|Operate a Booster Battery or Charger]]

> [!warning] IMPORTANT
> IMPORTANT: Do not disconnect battery on machines equipped with Final Tier 4/Stage V engines until Light Emitting Diode (LED) on the battery box has turned off. This indicates the diesel exhaust fluid (DEF) system purge is complete. If adequate time is not allowed for lines to be purged, any DEF remaining in lines can crystallize and plug lines. In freezing weather, DEF will freeze and possibly burst lines.
> [[disconnect-battery-final-tier-4-and-stage-v-engines--fc1019|Disconnect Battery (Final Tier 4 and Stage V Engines)]]

> [!warning] IMPORTANT
> IMPORTANT: Do not replace the original fuse with a higher rated fuse or machine damage may occur. If the original size fuse does not carry electrical load and continues to blow, have the electrical system checked by a John Deere dealer or other service provider.
> [[fuse-identification--576581|Fuse Identification]]

> [!warning] IMPORTANT
> IMPORTANT: Only attempt to disassemble fuses when instructed by a John Deere dealer or other service provider. Ensure that both the negative (-) and positive (+) battery connections are disconnected from both batteries before fuse inspection or replacement.
> [[battery-box-fuses-and-relay--6ee8f8|Battery Box Fuses and Relay]]

> [!warning] IMPORTANT
> IMPORTANT: BATTERY IS NEGATIVE GROUNDED. Always connect starter cable to positive (+) terminal of battery and battery ground cable to negative (-) terminal of battery. Reversed polarity in battery or alternator can result in permanent damage to electrical system.
> [[servicing-batteries--e9a1c5|Servicing Batteries]]

> [!warning] IMPORTANT
> IMPORTANT: Do not jump-start engines with arc welding equipment. Currents and voltages are too high and may cause permanent damage.
> [[welding-near-electronic-control-units--175df5|Welding Near Electronic Control Units]]

> [!warning] IMPORTANT
> IMPORTANT: Set battery charger at the nominal 12 volt and no more than 16 volt maximum.
> [[operate-a-booster-battery-or-charger--6af242|Operate a Booster Battery or Charger]]

## What it is

**Battery.** Use John Deere batteries or an equivalent with a rating of at least 925 cold cranking
amps at -18°C (0°F) [[servicing-batteries--e9a1c5|Servicing Batteries]]. Proper battery maintenance
is vital to dependable service: keep battery water level even with bottom of cell filler neck and
never below the top of cell plates [[servicing-batteries--e9a1c5|Servicing Batteries]]. Keep
batteries clean, keep all connections clean and tight, remove any corrosion, wash terminals with
solution of baking soda and water, and coat with grease prior to attaching cables
[[servicing-batteries--e9a1c5|Servicing Batteries]]. Keep batteries fully charged, especially
during cold weather [[servicing-batteries--e9a1c5|Servicing Batteries]]. Store batteries below
27°C (80°F) for maximum shelf life [[preventing-battery-damage--7fe4b4|Preventing Battery Damage]].

**Battery disconnect switch.** Rotate the battery disconnect switch clockwise to turn the machine
electrical system on, and counterclockwise to turn the system off
[[battery-disconnect-switch--c9c8e5|Battery Disconnect Switch]].

**Alternator.** Always disconnect battery ground strap when working with the alternator or
regulator; never attempt to polarize alternator to the regulator; never ground the alternator field
terminal or field circuit; and never connect or disconnect alternator or regulator wires with
battery connected or alternator operating
[[safeguard-alternator-and-regulator--9a757f|Safeguard Alternator and Regulator]]. Do not operate
the engine with alternator or battery disconnected
[[preventing-battery-damage--7fe4b4|Preventing Battery Damage]].

**Fuses and relays.** Fuse ratings are colour-coded — 3 A purple, 5 A brown, 10 A red, 15 A blue,
20 A yellow, 25 A clear, 30 A green [[fuse-identification--576581|Fuse Identification]]. The mega
fuse load center carries F100 Main Interface Fuse (350 A), F104 Alternator Fuse (350 A) and K5005
Starter Relay (60 A) [[mega-fuse-load-center--e876b4|Mega Fuse Load Center]]; the same three parts
are identified in the battery box [[battery-box-fuses-and-relay--6ee8f8|Battery Box Fuses and Relay]].

**Nozzle network (ExactApply).** Each nozzle body has three sets of circuits: power (red) and ground
(black), controller area network (CAN) binary unit system (bus) high circuit (yellow) and low
circuit (green), and the sync circuit (blue); all of the ExactApply system circuits start at the
domain controller [[exactapply-system-overview--3a6d49|ExactApply — System Overview]]. Power and
ground circuits are in parallel to each nozzle body, and before reaching the nozzle bodies, power
starts at the domain controller and goes to a relay and then through a fuse; each subnet has a
separate ground circuit and fuse
[[exactapply-system-overview--3a6d49|ExactApply — System Overview]]. The CAN bus and sync circuits
are in series and go from one nozzle body to the next, and the CAN bus circuit for each domain
controller end with CAN terminators
[[exactapply-system-overview--3a6d49|ExactApply — System Overview]]. The nozzle body's internal
control unit is powered by 12 V
[[exactapply-nozzle-body--a0b795|ExactApply — Nozzle Body]].

## Where it is

The battery disconnect switch and its LED
[[battery-disconnect-switch--c9c8e5|Battery Disconnect Switch]]:

![[N153287.png]]

**Figure N153287** — A: Switch; B: Light Emitting Diode (LED)
[[battery-disconnect-switch--c9c8e5|Battery Disconnect Switch]]

The main power fuses are located inside the battery box
[[fuse-locations--9c9608|Fuse Locations]]:

![[NX1439377.png]]

**Figure NX1439377** — A: Main Power Fuse [[fuse-locations--9c9608|Fuse Locations]]

Other load centers, by system:

- For machines with a single solution system, nozzle body and control unit fuses and relays are
  located on the top right-hand side of the center frame in a fuse box; for machines with dual
  solution systems they are located on the left-hand side of the center frame
  [[fuse-locations--9c9608|Fuse Locations]].
- The INC load center is located on the left-hand side of the machine's center frame
  [[fuse-locations--049188|Fuse Locations]].
- The See & Spray load center is located on the right-hand side of the center frame for
  single-product systems, and on the left-hand side of the center frame for dual-product systems
  [[replace-fuses--9cfc9e|Replace Fuses]]. The Low Light Load Center is located the same way, and
  the cover must be removed to access it [[replace-fuses--9cfc9e|Replace Fuses]].
- The cab load center and the rear mid-chassis cab fuses are covered on [[cab|Cab]].

## Related procedures

- **Before disconnecting the battery on a Final Tier 4/Stage V machine**, wait for the battery box
  LED to turn off — it indicates that the diesel exhaust fluid (DEF) system purge is complete
  [[battery-disconnect-switch--c9c8e5|Battery Disconnect Switch]]. See [[aftertreatment|Aftertreatment]]
  for what the DEF purge is.
- **Booster battery.** Attach one cable (red) to the remote positive terminal of the starter and
  positive terminal of booster battery; attach the second (black) battery cable to negative terminal
  of booster battery, and attach the other end to ground terminal or ground stud on engine, if
  supplied; remove cable from negative terminal first when disconnecting, then disconnect positive
  terminal [[operate-a-booster-battery-or-charger--6af242|Operate a Booster Battery or Charger]]. If
  a booster battery is used, two or more batteries cannot be used in series — they must be parallel
  [[operate-a-booster-battery-or-charger--6af242|Operate a Booster Battery or Charger]].
- **Battery charger.** Attach positive charger lead to positive remote terminal with charger in OFF
  position, attach negative charger lead to ground terminal, switch charger to ON and charge
  according to the charger manufacturer's instructions, then switch to OFF and remove the negative
  lead first [[operate-a-booster-battery-or-charger--6af242|Operate a Booster Battery or Charger]].
- **Welding.** Disconnect the negative (-) battery cable(s), then the positive (+) cable(s), short
  the positive and negative vehicle battery cables together (do not attach to vehicle frame), clear
  or move any wiring harness sections away from the welding area, and connect welder ground close to
  welding point and away from control units
  [[welding-near-electronic-control-units--175df5|Welding Near Electronic Control Units]]. After the
  repair, connect positive (+) battery cable(s) first, then negative (-)
  [[welding-near-electronic-control-units--175df5|Welding Near Electronic Control Units]]. For
  maximum protection, disconnect all electronic controller connectors before welding
  [[basic-electrical-component-handling-precautions-for-vehicles--3effa3|Basic Electrical Component Handling / Precautions For Vehicles Equipped With Computer Controlled Systems]].
- **Replace a fuse.** Replace fuses with like fuses
  [[replace-fuses--9cfc9e|Replace Fuses]]; the load-center layout tables give each slot's rating and
  consumer [[replace-fuses--9cfc9e|Replace Fuses]].
- **Connector service.** The seal on Tyco Ampseal connectors must be lubricated before connecting
  the connector after disassembly for troubleshooting, repair, or component replacement, using
  dielectric grease on the connector seal
  [[electrical-connector-service--600971|Electrical Connector Service]]. The recommended dielectric
  grease is John Deere AT66865 Dielectric Grease
  [[electrical-connector-service--600971|Electrical Connector Service]].
- If acid is spilled on skin or in eyes, flush skin with water, apply baking soda or lime to help
  neutralize the acid, flush eyes with water for 15—30 minutes, and get medical attention
  immediately [[handling-batteries-safely--3a873e|Handling Batteries Safely]]. If acid is swallowed,
  do not induce vomiting, drink large amounts of water or milk but do not exceed 2 L (2 qt.), and
  get medical attention immediately
  [[handling-batteries-safely--3a873e|Handling Batteries Safely]].

## Related settings

The electrical system itself has no operator settings in these topics. The display settings that
drive electrical consumers are on [[lights|Lights]] and [[nozzle|Nozzle]] (nozzle body lighting
modes and brightness).

## Related warnings

Beyond the callouts under [Warnings](#warnings), these precautions apply to any work on a machine
with computer controlled systems
[[basic-electrical-component-handling-precautions-for-vehicles--3effa3|Basic Electrical Component Handling / Precautions For Vehicles Equipped With Computer Controlled Systems]]:

- Never disconnect the batteries while the key switch is running, and do not connect jumper cables
  while the key switch is on — this can cause electrical voltage spikes that can damage electronic
  components
  [[basic-electrical-component-handling-precautions-for-vehicles--3effa3|Basic Electrical Component Handling / Precautions For Vehicles Equipped With Computer Controlled Systems]].
- Never jump start the machine with a voltage higher than the machine is designed to operate on
  [[basic-electrical-component-handling-precautions-for-vehicles--3effa3|Basic Electrical Component Handling / Precautions For Vehicles Equipped With Computer Controlled Systems]].
- Do not connect or disconnect electrical connectors while the key switch is on or the machine is
  running
  [[basic-electrical-component-handling-precautions-for-vehicles--3effa3|Basic Electrical Component Handling / Precautions For Vehicles Equipped With Computer Controlled Systems]].
- Do not apply power or ground to any component as a test unless specifically instructed to do so
  [[basic-electrical-component-handling-precautions-for-vehicles--3effa3|Basic Electrical Component Handling / Precautions For Vehicles Equipped With Computer Controlled Systems]].
- Directing pressurized water at electronic/electrical components or connectors may cause product
  malfunctions — reduce pressure, and spray at a 45 to 90 degree angle
  [[basic-electrical-component-handling-precautions-for-vehicles--3effa3|Basic Electrical Component Handling / Precautions For Vehicles Equipped With Computer Controlled Systems]].
- Battery gas can explode; keep sparks and flames away from batteries, and use a flashlight to check
  battery electrolyte level [[handling-batteries-safely--3a873e|Handling Batteries Safely]]. Always
  remove grounded (-) battery clamp first and replace grounded clamp last
  [[handling-batteries-safely--3a873e|Handling Batteries Safely]].
- Disconnect battery cables before using an electric welder on the machine
  [[preventing-battery-damage--7fe4b4|Preventing Battery Damage]].

## Related troubleshooting

- A fuse that keeps blowing is not an invitation to fit a bigger one: if the original size fuse does
  not carry electrical load and continues to blow, have the electrical system checked by a John
  Deere dealer or other service provider [[fuse-identification--576581|Fuse Identification]].
- On ExactApply, nozzle body lighting in Manual mode separates a sync-circuit fault from a
  CAN/power/ground fault — see [[nozzle|Nozzle]].
- If a nozzle body loses power, CAN information from the other nozzle bodies remains in
  communication with the domain controller (nozzle body pass-through), but a disconnected nozzle
  body will not pass CAN messages downstream
  [[exactapply-nozzle-body-pass-through--634622|ExactApply — Nozzle Body Pass-Through]].

> [!inference] Scope of this page
> The manual has no single "electrical system" topic. This page gathers the Electrical System
> Service section (battery, alternator, fuses, welding, connectors), the Safety Signs entry for the
> mega fuse load center, and the fuse locations given inside the ExactApply, INC and See & Spray
> sections. It adds no facts of its own. Wiring repair beyond fuse replacement is a dealer job in
> every topic read here.
