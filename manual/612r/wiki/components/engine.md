---
type: component
title: "Engine"
models: [all]
options: []
engine_tier: Final Tier 4
components: [engine, aftertreatment, cooling system, fuel system]
sources:
  - "UZEGGEY,1765785596814-19-11MAY26"
  - "UZEGGEY,1768888205923-19-20JAN26"
  - "ouo6092,1775066384434-19-01APR26"
  - "ouo6092,1775066407641-19-11MAY26"
  - "ouo6092,1775067109003-19-01APR26"
  - "ouo6092,1775067666435-19-01APR26"
  - "N0LMWLO,00003D6-19-03DEC20"
  - "ouo6092,1737045984368-19-27OCT25"
  - "ouo6092,1741882981520-19-13MAR25"
  - "ouo6092,1741883135115-19-13MAR25"
  - "BN55050,000027F-19-25MAY18"
  - "ouo6092,1737385811377-19-27OCT25"
  - "ouo6092,1737045797845-19-27OCT25"
  - "TB90758,00028BE-19-08APR21"
  - "DX,ENOIL16(T)-19-05APR22"
  - "DX,ENOIL15,IT4,120toMAX(T)-19-02MAR25"
  - "ouo6092,1737400937052-19-27OCT25"
reviewed: true
compiled: 2026-09-23
---

# Engine

## What it is

The engine is an in-line 6 cylinder John Deere diesel with a high pressure common rail (HPCR)
fuel system and a dry-type dual element air cleaner
[[machine-specification--bfe721|Machine Specification]].

**Which engine your machine has depends on the model.** The manual lists the Final Tier 4/Stage V
engine model as PowerTech Plus 6.8 L for the 408R, JD9 for the 410R, 412R, 400R and 612R, and
PowerTech PSS 9.0L for the 616R/600R
[[machine-specification--bfe721|Machine Specification]]. By displacement, Final Tier 4 is
6.8 L (415 in³) on the 408R and 9.0 L (549 in³) on the 410R, 412R, 400R, 612R, 616R and 600R;
Tier 3/Stage III is 9.0 L (549 in³)
[[machine-specification--bfe721|Machine Specification]]. Compression ratio is 16.7:1 for the
6.8L engine and 16.0:1 for the 9.0L engine, and the firing order is 1-5-3-6-2-4
[[machine-specification--bfe721|Machine Specification]].

Rated power is listed per model: 400R 242 kW (325 hp), 408R 209 kW (280 hp), 410R 231 kW (310 hp),
412R 242 kW (325 hp), 600R 280 kW (375 hp), 612R 265 kW (355 hp) and 616R 280 kW (375 hp)
[[machine-specification--bfe721|Machine Specification]].

Fuel type is No. 1-D, 2-D, or B2 Diesel [[machine-specification--bfe721|Machine Specification]].
See [[fuel-system]] and [[aftertreatment]] for the systems attached to it.

## Where it is

The engine serial number (A) is on the left-hand side of the 6.8 L engine block, and on the
right-hand side of the 9.0 L engine block
[[identification-numbers--b5c28c|Identification Numbers]].

![[N116434.png]]
**Figure N116434** — A: Engine Serial Number (6.8 L Engine)
[[identification-numbers--b5c28c|Identification Numbers]]

![[N116133.png]]
**Figure N116133** — A: Engine Serial Number (9.0 L Engine)
[[identification-numbers--b5c28c|Identification Numbers]]

The engine control unit (ECU) serial number is located on the unit on the right-hand side of the
engine [[identification-numbers--b5c28c|Identification Numbers]].

The engine vent tube (A) is in a different place on each engine — the manual shows one view for the
6.8 L engine and another for the 9.0 L engine
[[clean-engine-vent-tube-annually--8be648|Clean Engine Vent Tube—Annually]].

![[N153551.png]]
**Figure N153551** — A: Vent Tube (Engine Vent Tube—6.8 L Engine)
[[clean-engine-vent-tube-annually--8be648|Clean Engine Vent Tube—Annually]]

![[N153552.png]]
**Figure N153552** — A: Vent Tube (Engine Vent Tube—9.0 L Engine)
[[clean-engine-vent-tube-annually--8be648|Clean Engine Vent Tube—Annually]]

## Engine speeds and capacities

Slow idle is 900 rpm [[machine-specification--bfe721|Machine Specification]].

The Specifications section lists fast idle (no load) as 2140 rpm for the 400R, 408R, 410R, 412R,
612R, and all Stage 3 units, and 2240 rpm for the 600R and 616R
[[machine-specification--bfe721|Machine Specification]].

> [!conflict] Fast idle speed is stated two different ways
> The Specifications section groups fast idle (no load) by **model** — 2140 rpm for the 400R, 408R,
> 410R, 412R, 612R and all Stage 3 units, 2240 rpm for the 600R and 616R — and separately states a
> rated engine speed of 2100 rpm (no load) for the 400R, 410R, 410R, 412R, 612R and 2200rpm for the
> 600R, 616R [[machine-specification--bfe721|Machine Specification]].
> The 750-hour check groups the same speeds by **engine displacement** — 2140±50 rpm for machines
> with 6.8 L engines and 2240±50 rpm for machines with 9.0 L engines
> [[check-engine-speeds-750-hours--a056fe|Check Engine Speeds—750 Hours]].
> These do not agree for the 400R, 410R, 412R and 612R, which the Specifications section lists with
> 9.0 L engines but at the lower fast idle. Neither source is generic Deere-wide boilerplate.
> Confirm the correct speed for your machine with your John Deere dealer before adjusting anything.

Capacities that belong to the engine (from
[[machine-specification--bfe721|Machine Specification]]):

- Cooling system with heater — 6.8 L Final Tier 4/Stage V engine: 22.8 L (6.0 gal); 9.0 L Final
  Tier 4/Stage V engine: 31.4 L (8.3 gal); 9.0 L Tier 2/Stage II engine: 33.4 L (8.8 gal)
  [[machine-specification--bfe721|Machine Specification]].
- Crankcase including filter — 6.8 L Final Tier 4/Stage V engine: 30 L (31.7 qt); 9.0 L engine:
  31 L (32.8 qt) [[machine-specification--bfe721|Machine Specification]].
- Fuel tank — 408R: 485 L (128 gal); 400R, 410R, 412R, 600R, 612R and 616R: 565 L (149 gal)
  [[machine-specification--bfe721|Machine Specification]].
- Diesel exhaust fluid tank: 29.5 L (7.8 gal)
  [[machine-specification--bfe721|Machine Specification]].
- Cooling system type is pressurized at 69 kPa (0.7 bar) (10 psi) with two heavy-duty 180°
  thermostats [[machine-specification--bfe721|Machine Specification]].

The oil filter is full flow with a bypass valve; the element is bottom load on the 408R FT4 and top
load on the 400R, 408R (stage 3), 410R, 412R, 600R, 612R and 616R
[[machine-specification--bfe721|Machine Specification]].

## Related procedures

- Start the engine — make sure the multi-function lever (A) is in the Park position, sound the horn,
  turn the key switch to Accessory/Run, then turn it clockwise to Start
  [[start-the-engine--a12543|Start the Engine]].
- Warm the engine — do not place the engine under full load until it is properly warmed; view the
  engine coolant temperature (A) on the primary display unit
  [[warm-the-engine--a6676a|Warm the Engine]].
- Idle the engine — view the engine speed (A) on the corner post display and push the engine speed
  increase button (B) until the desired speed is displayed
  [[idle-engine--875b72|Idle Engine]]. Allowing the engine to idle uses fuel inefficiently and can
  cause a buildup of carbon in the engine [[idle-engine--875b72|Idle Engine]].
- Stop the engine — stop the machine and press the low idle engine speed switch, put the
  multi-function lever in "PARK" position, turn the key switch to "OFF" position and remove the key
  [[operate-the-engine--9bbe7e|Operate the Engine]].
- Restart a stalled engine IMMEDIATELY to prevent excessive heat buildup and possible turbocharger
  damage [[operate-the-engine--9bbe7e|Operate the Engine]].
- Check engine oil level daily — the level is adequate if it is between the ADD hole (C) and the
  FULL hole (D) on the dipstick
  [[check-engine-oil-level-daily--5eab09|Check Engine Oil Level—Daily]].
- Clean dirt and trash from the engine vent tube (A) annually
  [[clean-engine-vent-tube-annually--8be648|Clean Engine Vent Tube—Annually]].
- Check engine speeds at the interval given in
  [[check-engine-speeds-750-hours--a056fe|Check Engine Speeds—750 Hours]]; if speeds are not
  correct, contact a John Deere dealer or other service provider
  [[check-engine-speeds-750-hours--a056fe|Check Engine Speeds—750 Hours]].

### Oil for the engine

New engines are filled at the factory with John Deere Break-In Plus Engine Oil
[[john-deere-break-in-plus-engine-oil-interim-tier-4-final-tie--e97242|John Deere Break-In Plus Engine Oil — Interim Tier 4, Final Tier 4, Stage IIIB, Stage IV, and Stage V]].
During the initial operation of a new or rebuilt engine, change the oil and filter between a
minimum of 100 hours and maximum equal to the interval specified for John Deere Plus-50 II oil
[[john-deere-break-in-plus-engine-oil-interim-tier-4-final-tie--e97242|John Deere Break-In Plus Engine Oil — Interim Tier 4, Final Tier 4, Stage IIIB, Stage IV, and Stage V]].

After break-in, the service interval is 500 hours for John Deere Plus-50 II and 250 hours for
"Other Oils"
[[engine-oil-and-filter-service-intervals-interim-tier-4-final--6abcc9|Engine Oil and Filter Service Intervals — Interim Tier 4, Final Tier 4, Stage IIIB, Stage IV, and Stage V Engines]].
Change the oil and oil filter at least once every 12 months even if the hours of operation are
fewer than the otherwise recommended service interval
[[engine-oil-and-filter-service-intervals-interim-tier-4-final--6abcc9|Engine Oil and Filter Service Intervals — Interim Tier 4, Final Tier 4, Stage IIIB, Stage IV, and Stage V Engines]].
That topic is a generic Deere-wide module (`generic: true`), so confirm it against the machine's own
service-interval chart before using it.

> [!warning] IMPORTANT
> IMPORTANT: Use of diesel fuel with sulfur content less than 15 mg/kg (15 ppm) is REQUIRED.
> [[engine-oil-and-filter-service-intervals-interim-tier-4-final--6abcc9|Engine Oil and Filter Service Intervals — Interim Tier 4, Final Tier 4, Stage IIIB, Stage IV, and Stage V Engines]]

> [!warning] IMPORTANT
> IMPORTANT: Do not use any other engine oils during the initial break-in of a new or rebuilt engine.
> [[john-deere-break-in-plus-engine-oil-interim-tier-4-final-tie--e97242|John Deere Break-In Plus Engine Oil — Interim Tier 4, Final Tier 4, Stage IIIB, Stage IV, and Stage V]]

## Related settings — the Engine application on the display

Reach the Engine application through the display: Menu, then the Machine Settings tab, then Engine;
or press the Engine button on the navigation bar below the display
[[access-engine--5734e3|Access Engine]].

![[WZ675726.png]]
**Figure WZ675726** — Engine [[engine-main-page--8b9453|Engine Main Page]]

The Engine application is used to access and adjust engine settings
[[engine-main-page--8b9453|Engine Main Page]]. Items on the main page are Engine Power (the amount
of engine power the machine is using) and Engine Hours (accumulated engine hours)
[[engine-main-page--8b9453|Engine Main Page]]. Engine Power is not displayed until 40% of the
available engine power is being used [[engine-power--4234ca|Engine Power]]; engine operating hours
are necessary for monitoring machine maintenance [[engine-power--4234ca|Engine Power]].

Exhaust filter cleaning is reached from the same page: Auto Exhaust Filter Cleaning, Parked Filter
Cleaning and Request Exhaust Filter Cleaning
[[engine-main-page--8b9453|Engine Main Page]]. Parked filter cleaning requires 1 hour to complete,
and request exhaust filter cleaning requires 2 to 3 hours to complete
[[engine-main-page--8b9453|Engine Main Page]]. See [[aftertreatment]].

Max Engine Speed Enable/Disable sets a preset engine speed that is not exceeded during operation,
and using the maximum engine speed presets increases fuel economy
[[max-engine-speed-enable-disable--29d9c1|Max Engine Speed Enable/Disable]]. Modify it when limited
engine speed is desired, when a higher or lower engine speed is required during the application, or
when hilly and flat terrains are present in the same field
[[max-engine-speed-enable-disable--29d9c1|Max Engine Speed Enable/Disable]].

Engine speed is also controlled from the CommandARM switches: Low Idle, Engine Speed Increase,
Engine Speed Decrease and High Idle
[[engine-and-ground-drive--b66121|Engine and Ground Drive]]. Pushing and holding the Engine Speed
Increase switch or the Engine Speed Decrease switch increases or decreases engine speed at a
predefined rate [[engine-and-ground-drive--b66121|Engine and Ground Drive]].

Auto Idle automatically lowers the engine rpm to minimum engine speed after a period of inactivity
from the operator while operating in Auto mode; the inactivity period can be adjusted by the
operator between 1—30 seconds [[idle-engine--875b72|Idle Engine]]. Auto Idle is only available when
the transmission is in Auto mode and no other machine functions require the engine speed to be
higher than 900 rpm [[idle-engine--875b72|Idle Engine]].

Operating in hilly terrain, wet ground conditions or at excessive ground speed increases power
consumption [[engine-power--4234ca|Engine Power]].

## Related warnings

> [!warning] CAUTION — exhaust fumes
> CAUTION: Prevent asphyxiation. Engine exhaust fumes can cause sickness or death to you or others.
> [[start-the-engine--a12543|Start the Engine]]

> [!warning] CAUTION — key switch
> CAUTION: Remove key from the key switch to help prevent accidents.
> [[operate-the-engine--9bbe7e|Operate the Engine]]

> [!warning] IMPORTANT — starter
> IMPORTANT: Do not operate the starter more than 30 seconds at a time or starter can be damaged.
> If engine does not start, wait at least 2 minutes before trying again. If engine does not start in
> four attempts, refer to Troubleshooting section.
> [[start-the-engine--a12543|Start the Engine]]

> [!warning] IMPORTANT — turbocharger at start-up
> IMPORTANT: Protect turbocharger during start-up by not accelerating above 1000 rpm until normal
> engine idle speed is established (900 rpm).
> [[start-the-engine--a12543|Start the Engine]]

> [!warning] IMPORTANT — lubrication after start
> IMPORTANT: To provide proper lubrication after the engine starts, operate the engine at
> approximately 900 rpm with no load for 1—2 minutes. At temperatures below freezing point, this
> period must be extended to 2—4 minutes.
> [[warm-the-engine--a6676a|Warm the Engine]]

> [!warning] IMPORTANT — battery disconnect on Final Tier 4/Stage V
> IMPORTANT: Do not disconnect battery on machines equipped with Final Tier 4/Stage V engines until
> Light Emitting Diode (LED) on the battery box has turned off. This indicates the diesel exhaust
> fluid (DEF) system purge is complete. If adequate time is not allowed for lines to be purged, any
> DEF remaining in lines can crystallize and plug lines. In freezing weather, DEF freezes and
> possibly bursts lines.
> [[operate-the-engine--9bbe7e|Operate the Engine]]

> [!warning] IMPORTANT — engine power alerts
> IMPORTANT: If alerts or excessive exhaust smoke are visible, contact your John Deere dealer or
> other service provider for further diagnosis.
> [[engine-power--4234ca|Engine Power]]

> [!warning] IMPORTANT — oil level
> IMPORTANT: Do not operate the engine with the oil level below the “ADD” mark on dipstick.
> Do not overfill oil level.
> [[check-engine-oil-level-daily--5eab09|Check Engine Oil Level—Daily]]

## Related troubleshooting

The Troubleshooting section has an Engine table covering: engine hard to start or will not start;
engine knocks; engine runs irregularly or stalls frequently; lack of power; engine overheats;
engine temperature below normal; low oil pressure; engine uses too much oil; engine uses too much
fuel; engine emits black or gray exhaust smoke; engine emits white exhaust smoke; battery will not
charge; and starter starts slowly or will not start
[[engine--a0a40d|Engine]].

Two entries that are often the cheapest to check first: for hard starting, a safety switch not
activated is fixed by moving the multi-function lever to neutral and inspecting the switch; for
engine overheats, a low coolant level is fixed by filling the radiator with coolant to the proper
level and checking hoses and radiator for leaks or loose connections
[[engine--a0a40d|Engine]].

## Applicability

Everything on this page applies to all models unless a model, engine tier or displacement is named
in the sentence. The displacement, power, capacity and fast-idle values differ by model — take them
from the per-model rows above, not from a single figure
[[machine-specification--bfe721|Machine Specification]].
