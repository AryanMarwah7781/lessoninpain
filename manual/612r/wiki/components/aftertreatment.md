---
type: component
title: "Aftertreatment"
models: [all]
options: []
engine_tier: Final Tier 4
components: [aftertreatment, def system, exhaust filter, scr catalyst, engine]
sources:
  - "DX,SCR,OVERVIEW-19-30MAR20"
  - "ouo6092,1741962082679-19-27OCT25"
  - "ouo6092,1737117734905-19-05NOV25"
  - "ouo6092,1775067148931-19-01APR26"
  - "ouo6092,1775067177068-19-01APR26"
  - "ouo6092,1775067229833-19-01APR26"
  - "ouo6092,1741881126110-19-13MAR25"
  - "DX,DEF(T)-19-01MAR25"
  - "DX,DEF,STORE-19-28AUG25"
  - "DX,DEF,TEST-19-28AUG25"
  - "DX,EXHAUST,FILTER-19-20JAN26"
  - "ouo6092,1737115758324-19-27OCT25"
  - "DX,SCR,EMRGNCY,OVERIDE,US-19-24JAN18"
  - "TB90758,00027DA-19-10MAR21"
  - "BN55050,0000255-19-23MAY18"
reviewed: true
compiled: 2026-09-23
---

# Aftertreatment

The aftertreatment system cleans the exhaust. It has two halves: the exhaust filter, which collects
and periodically burns off soot, and the selective catalytic reduction (SCR) system, which injects
diesel exhaust fluid (DEF) to convert NOx. The SCR topics on this page are titled for Final Tier 4
and Stage V engines [[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]].

## Warnings

> [!warning] CAUTION
> CAUTION: The exhaust temperature can be high under no load or light load conditions at certain times during the exhaust filter cleaning cycle.
> Servicing machine or attachments during exhaust filter cleaning can result in serious personal injury. Avoid exposure and skin contact with hot exhaust gases and components.
> During automated or manual/stationary exhaust filter cleaning operations, the engine runs at elevated idle and hot temperatures for an extended period. Exhaust gases and exhaust filter components reach temperatures hot enough to cause burns to people, or ignite or melt common materials.
> Never perform exhaust filter cleaning procedures in a closed building unless suitable exhaust is provided.
> [[exhaust-filter-system-overview--49a974|Exhaust Filter System Overview]]

> [!warning] CAUTION
> CAUTION: When AUTO, PARKED, or REQUESTED cleaning is enabled, the exhaust temperature can be high under no load or light load conditions at certain times during the exhaust filter cleaning cycle. Disable exhaust filter cleaning system in conditions where it can be unsafe for elevated exhaust temperatures.
> [[auto-exhaust-filter-cleaning--5f0614|AUTO Exhaust Filter Cleaning]]

> [!warning] CAUTION
> CAUTION: Under federal, state and/or local laws or regulations, exhaust filter ash may be classified as a hazardous waste. Hazardous waste must be disposed of in accordance with all applicable federal, state, and local laws or regulations governing hazardous waste disposal. Only a qualified service provider should remove ash from the exhaust filter. Personal protective equipment and clothing, maintained in a sanitary and reliable condition, should be used when handling and cleaning exhaust filter. See a John Deere dealer or other service provider for exhaust filter handling and disposal.
> [[exhaust-filter-ash-handling-and-disposal--8bcac6|Exhaust Filter Ash Handling and Disposal]]

> [!warning] CAUTION
> CAUTION: Avoid contact with eyes. In case of contact, immediately flush eyes with large amounts of water for a minimum of 15 minutes. Reference the Materials Safety Data Sheet (MSDS) for additional information.
> Do not ingest DEF. In the event DEF is ingested, contact a physician immediately. Reference the Materials Safety Data Sheet (MSDS) for additional information.
> [[storing-diesel-exhaust-fluid-def--18be20|Storing Diesel Exhaust Fluid (DEF)]]

> [!warning] IMPORTANT
> IMPORTANT: It is unlawful to tamper with or remove any component of the aftertreatment system. It is also unlawful to use diesel exhaust fluid (DEF) that does not meet the specifications provided or to operate the vehicle with no DEF.
> Using incorrect or unapproved aftertreatment components can damage the vehicle’s aftertreatment system and reduce ability of the aftertreatment system to function correctly. Never interchange aftertreatment components between Interim Tier 4/Stage III B and Final Tier 4/Stage V equipped vehicles.
> [[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]]

> [!warning] IMPORTANT
> IMPORTANT: Do not remove battery leads for at least 4 minutes after engine stops. The SCR system automatically purges itself of Diesel Exhaust Fluid (DEF) immediately after the engine is stopped. If adequate time is not allowed for lines to be purged, residual DEF can freeze and possibly damage components of the SCR system during cold-weather exposure.
> [[selective-catalytic-reduction-scr-system-overview--8b2d6a|Selective Catalytic Reduction (SCR) System Overview]]

> [!warning] IMPORTANT
> IMPORTANT: Do not disconnect battery on machines equipped with Final Tier 4/Stage V engines until Light Emitting Diode (LED) on the battery box has turned off. This indicates the diesel exhaust fluid (DEF) system purge is complete. If adequate time is not allowed for lines to be purged, any DEF remaining in lines can crystallize and plug lines. In freezing weather, DEF will freeze and possibly burst lines.
> [[disconnect-battery-final-tier-4-and-stage-v-engines--fc1019|Disconnect Battery (Final Tier 4 and Stage V Engines)]]

> [!warning] IMPORTANT
> IMPORTANT: Never put DEF in the diesel fuel tank, or diesel fuel in the DEF tank.
> [[fill-diesel-exhaust-fluid-def-tank-final-tier-4-stage-v--b81914|Fill Diesel Exhaust Fluid (DEF) Tank (Final Tier 4/Stage V)]]

> [!warning] IMPORTANT
> IMPORTANT: Damage to exhaust cleaning components can occur if engine is turned OFF while performing exhaust filter cleaning or shortly after cleaning is complete.
> [[auto-exhaust-filter-cleaning--5f0614|AUTO Exhaust Filter Cleaning]]

> [!warning] IMPORTANT
> IMPORTANT: The operator is informed by the operator warning system when the emission control system does not function correctly and/ or an engine malfunction is detected by the engine control unit. Ignoring the operator warning signals will lead to an emission-related derate, resulting in an effective disablement of non-road mobile machinery operation.
> [[aftertreatment-indicators-overview--67561e|Aftertreatment Indicators Overview]]

The generic Deere-wide safety topic adds that during exhaust filter cleaning operations the engine
may run at elevated idle and hot temperatures for an extended period, and that exhaust gases and
exhaust filter components reach temperatures hot enough to burn people, or ignite or melt common
materials [[clean-exhaust-filter-safely--2abccf|Clean Exhaust Filter Safely]]. Keep machine away
from people, animals, or structures which may be susceptible to harm or damage from hot exhaust
gases or components, and closely monitor machine and surrounding area for smoldering debris during
and after exhaust filter cleaning [[clean-exhaust-filter-safely--2abccf|Clean Exhaust Filter Safely]].

## What it is

**SCR system.** In order to comply with national and local emission requirements, this engine series
contains a Selective Catalytic Reduction (SCR) system
[[selective-catalytic-reduction-scr-system-overview--8b2d6a|Selective Catalytic Reduction (SCR) System Overview]].
The main components of the SCR system include the SCR catalyst, DEF dosing injector, DEF dosing
unit, DEF tank, and DEF tank header assembly
[[selective-catalytic-reduction-scr-system-overview--8b2d6a|Selective Catalytic Reduction (SCR) System Overview]].
During combustion, NOx molecules are formed in the exhaust; DEF is injected into the exhaust stream
before the SCR catalyst, and through a chemical reaction in the SCR, NOx is converted into nitrogen
and water
[[selective-catalytic-reduction-scr-system-overview--8b2d6a|Selective Catalytic Reduction (SCR) System Overview]].

**DEF.** Engines requiring DEF shall use a product that meets the requirements for aqueous urea
solution 32 (AUS 32) according to ISO 22241-1
[[diesel-exhaust-fluid-def-use-in-selective-catalytic-reductio--96ed7a|Diesel Exhaust Fluid (DEF) — Use in Selective Catalytic Reduction (SCR) Equipped Engines]].
If John Deere Diesel Exhaust Fluid is not available, use DEF that is certified by the American
Petroleum Institute (API) Diesel Exhaust Fluid Certification Program or by the AdBlue Diesel Exhaust
Fluid Certification Program
[[diesel-exhaust-fluid-def-use-in-selective-catalytic-reductio--96ed7a|Diesel Exhaust Fluid (DEF) — Use in Selective Catalytic Reduction (SCR) Equipped Engines]].
DEF tank capacity is 29.5 L (7.8 gal)
[[fill-diesel-exhaust-fluid-def-tank-final-tier-4-stage-v--b81914|Fill Diesel Exhaust Fluid (DEF) Tank (Final Tier 4/Stage V)]].

**DEF in the cold.** DEF freezes at -11°C (12°F) and will not flow to the SCR system
[[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]].
Machine systems sense low temperature and allow engine to start, even with no DEF flow, and engine
coolant is used to thaw fluid in the DEF tank when engine is running
[[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]].
If system senses that DEF has thawed and SCR system is operating normally within 60 to 90 minutes,
machine operates normally; if DEF flow is not sensed within 60 to 90 minutes, FAIL TO THAW DTC is
displayed, the machine is allowed to operate normally for 4 hours after the DTC is displayed, and if
DEF flow is not sufficient after 4 hours, engine power will be reduced to 50% until DEF flow is
achieved
[[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]].
Freezing and thawing of DEF does not degrade it
[[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]].
The DEF tank contains a heating element that provides rapid thawing of DEF upon start-up, and the
heating element cycles to maintain fluidity during operation as needed
[[selective-catalytic-reduction-scr-system-overview--8b2d6a|Selective Catalytic Reduction (SCR) System Overview]].

**Exhaust filter.** Your machine is equipped with an emission-compliant engine that cleans and
filters the exhaust, and under normal machine operation and with system in AUTO mode, minimal
interaction is required [[exhaust-filter-system-overview--49a974|Exhaust Filter System Overview]].
To avoid unnecessary buildup of diesel particulates or soot in the exhaust filter system: utilize
AUTO Exhaust Filter Cleaning mode, avoid unnecessary idling, use proper engine oil, and use only
ultra-low sulfur fuel [[exhaust-filter-system-overview--49a974|Exhaust Filter System Overview]].

## Where it is

The SCR system layout
[[selective-catalytic-reduction-scr-system-overview--8b2d6a|Selective Catalytic Reduction (SCR) System Overview]]:

![[RG22427A.png]]

**Figure RG22427A** — A: SCR Catalyst; B: DEF Dosing Injector; C: DEF Dosing Unit; D: DEF Tank;
E: DEF Tank Header Assembly; F: Inline DEF Filter (If Equipped); G: Modular Canning Configuration;
H: Inline Canning Configuration
[[selective-catalytic-reduction-scr-system-overview--8b2d6a|Selective Catalytic Reduction (SCR) System Overview]]

The DEF level gauge is on the corner post display
[[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]]:

![[NX1396835.png]]

**Figure NX1396835** — A: DEF Level Gauge; B: DEF Icon
[[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]]

The exhaust filter cleaning controls are in the Engine application on the display
[[exhaust-filter-system-overview--49a974|Exhaust Filter System Overview]] — see [[engine|Engine]].

## Related procedures

- **Fill the DEF tank.** Before using containers, funnels, and so on, to dispense DEF, wash and
  rinse items thoroughly with distilled water to remove contaminants; wipe the DEF tank cap and
  areas around the filler neck to reduce chance of contaminating DEF; remove the cap; using a
  funnel, carefully pour DEF into the tank, watching the level through the filler neck; securely
  tighten the DEF tank cap; and carefully clean any spills using distilled water only
  [[fill-diesel-exhaust-fluid-def-tank-final-tier-4-stage-v--b81914|Fill Diesel Exhaust Fluid (DEF) Tank (Final Tier 4/Stage V)]].
  Fill the tank every time the machine is refueled; if this cannot be done, monitor the DEF level
  indicator on the corner post display and refill as necessary, always keeping the DEF level above
  the topmost red mark on the level indicator
  [[fill-diesel-exhaust-fluid-def-tank-final-tier-4-stage-v--b81914|Fill Diesel Exhaust Fluid (DEF) Tank (Final Tier 4/Stage V)]].
- **Test DEF.** If DEF quality is questionable, draw a sample out of the DEF tank or storage tank
  into a clear container; DEF shall be crystal clear with a light ammonia smell, and if DEF appears
  cloudy, has a colored tint, or has a profound ammonia smell, it is likely not within specification
  [[testing-diesel-exhaust-fluid-def--4c0b70|Testing Diesel Exhaust Fluid (DEF)]]. If the DEF passes
  the visual and smell test, check the DEF concentration with a handheld refractometer calibrated to
  measure DEF [[testing-diesel-exhaust-fluid-def--4c0b70|Testing Diesel Exhaust Fluid (DEF)]]. The
  correct DEF concentration is 31.8—33.2% urea; if the DEF concentration is not within
  specification, drain the DEF tank, flush with distilled water and fill with new or good DEF
  [[testing-diesel-exhaust-fluid-def--4c0b70|Testing Diesel Exhaust Fluid (DEF)]].
- **Parked filter cleaning** is a process that allows the system to perform exhaust filter cleaning
  when required, and requires 1 hour to complete
  [[exhaust-filter-system-overview--49a974|Exhaust Filter System Overview]]. **Request Exhaust
  Filter Cleaning** performs a more intense cleaning procedure than parked filter cleaning when
  required, and requires 2 to 3 hours to complete
  [[exhaust-filter-system-overview--49a974|Exhaust Filter System Overview]].
- **Disable AUTO exhaust filter cleaning** from the display: select to open Exhaust Filter Cleaning,
  select to enable or disable Automatic Filter Cleaning, then select to close
  [[disable-auto-exhaust-filter-cleaning--227f87|Disable AUTO Exhaust Filter Cleaning]].
- **Ash handling** is not an operator job: only a qualified service provider should remove ash from
  the exhaust filter [[exhaust-filter-ash-handling-and-disposal--8bcac6|Exhaust Filter Ash Handling and Disposal]].

## Related settings

- **AUTO Mode** is an automated process to perform exhaust filter cleaning during normal operation
  [[exhaust-filter-system-overview--49a974|Exhaust Filter System Overview]]. The system defaults to
  AUTO mode when parked exhaust filter cleaning is complete or key switch is cycled
  [[auto-exhaust-filter-cleaning--5f0614|AUTO Exhaust Filter Cleaning]].
- **Disable AUTO Exhaust Filter Cleaning** applies in conditions where it can be unsafe for elevated
  exhaust temperatures [[exhaust-filter-system-overview--49a974|Exhaust Filter System Overview]].
  The listed conditions are: indoors or under a roof unless a high temperature externally vented
  exhaust system is connected; there is not enough time available for the machine to complete a
  cleaning cycle before it is shut down; operating in high crop dust or chaff conditions; and next
  to a fueling area [[disable-auto-exhaust-filter-cleaning--227f87|Disable AUTO Exhaust Filter Cleaning]].
  Disabling auto mode is not recommended for any situation unless it is safety-related or if the
  fuel tank lacks the required fuel to complete the cleaning process
  [[aftertreatment-indicators-overview--67561e|Aftertreatment Indicators Overview]].
- **DEF storage.** It is preferred to store DEF out of extreme ambient temperatures; ideal conditions
  are to store at temperatures between –5°C and 30°C (23°F and 86°F) in dedicated containers sealed
  to avoid contamination and evaporation
  [[storing-diesel-exhaust-fluid-def--18be20|Storing Diesel Exhaust Fluid (DEF)]]. Exposure to
  temperatures greater than 30°C (86°F) can degrade DEF over time, and storing DEF at higher
  temperatures can reduce its useful life by approximately 6 months for every 5°C (9°F) temperature
  above 30°C (86°F) [[storing-diesel-exhaust-fluid-def--18be20|Storing Diesel Exhaust Fluid (DEF)]].
  Long-term storage in the DEF tank (over 12 months) is not recommended
  [[storing-diesel-exhaust-fluid-def--18be20|Storing Diesel Exhaust Fluid (DEF)]].
- **Emergency SCR derate override (US EPA only).** Once activated, the engine can operate free of
  emissions-related derates for 120 hours, and the option expires along with any remaining time
  240 hours after the Emergency SCR Derate Override is activated
  [[us-epa-qualified-emergency-use-scr-derate-override-option--860795|US EPA Qualified Emergency Use — SCR Derate Override Option]].
  A qualified emergency situation is one in which the condition of an engine's emission controls
  poses a significant direct or indirect risk to human life, and activating it for anything else is
  prohibited by the Clean Air Act and US EPA regulations
  [[us-epa-qualified-emergency-use-scr-derate-override-option--860795|US EPA Qualified Emergency Use — SCR Derate Override Option]].

## Related warnings

All of the callouts under [Warnings](#warnings) come from the aftertreatment topics themselves. The
DEF purge rule also governs battery work — see [[electrical-system|Electrical System]].

## Related troubleshooting

Read the indicators first [[aftertreatment-indicators-overview--67561e|Aftertreatment Indicators Overview]]:

- The diesel exhaust fluid (DEF) indicator illuminates when the DEF is low — fill DEF tank
  [[aftertreatment-indicators-overview--67561e|Aftertreatment Indicators Overview]]. When the DEF
  indicator is combined with the warning indicator or engine stop indicator, engine performance is
  reduced by the engine control unit (ECU) because the DEF is below a measurable level
  [[aftertreatment-indicators-overview--67561e|Aftertreatment Indicators Overview]].
- When the engine emissions temperature indicator illuminates, exhaust gas temperature is high,
  elevated idle is active, or exhaust filter cleaning is in process; the machine can be operated as
  normal unless the operator determines the machine is not in a safe location for high exhaust
  temperatures and disables auto cleaning
  [[aftertreatment-indicators-overview--67561e|Aftertreatment Indicators Overview]].
- When the exhaust filter indicator illuminates, the exhaust filter cleaning is in process,
  aftertreatment system has a fault, or the exhaust filter is in need of cleaning and the operator
  has disabled auto exhaust filter cleaning; if conditions are safe, the operator should enable the
  auto exhaust filter clean setting, perform manual service regeneration, or follow DTC procedure
  [[aftertreatment-indicators-overview--67561e|Aftertreatment Indicators Overview]].
- When the exhaust filter indicator is combined with the engine stop indicator, engine performance
  is further reduced by the ECU because there is an aftertreatment system fault or the soot level of
  the exhaust filter is extremely high; if this combination is present, see a servicing provider
  [[aftertreatment-indicators-overview--67561e|Aftertreatment Indicators Overview]].
- **Wrong fluid in the tank.** The SCR system monitors quality of DEF flowing through it; if a fluid
  other than DEF at correct urea concentration is detected, the system displays a diagnostic trouble
  code and engine derates to 50% power
  [[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]].
  If an unapproved fluid, such as diesel fuel or engine coolant, is added to the vehicle DEF tank,
  drain and rinse the tank
  [[fill-diesel-exhaust-fluid-def-tank-final-tier-4-stage-v--b81914|Fill Diesel Exhaust Fluid (DEF) Tank (Final Tier 4/Stage V)]].
- **White smoke in cold weather.** During cold-weather operation at low exhaust temperatures, water
  vapor can condense and resemble white smoke from the exhaust; this will dissipate as operating
  temperature increases and the water is further vaporized, and this situation is considered normal
  [[selective-catalytic-reduction-scr-system-overview--8b2d6a|Selective Catalytic Reduction (SCR) System Overview]].

> [!inference] Scope of this page
> The aftertreatment material is split between the generic Deere-wide DEF and exhaust-filter topics
> (`generic: true`), the machine's Operate the Machine section (indicators, SCR behaviour) and the
> Engine display application (cleaning modes). This page gathers them and adds no facts of its own.
> The SCR topics are titled for Final Tier 4 and Stage V engines; check your machine's engine tier
> before applying them.
