---
type: settings
title: "Cold weather and storage"
models: [all]
options: []
engine_tier: null
components: [engine, fuel system, def system, cooling system, hydraulic system, solution system, battery]
sources:
  - "ouo6092,1741962082679-19-27OCT25"
  - "DX,DEF,STORE-19-28AUG25"
  - "BN55050,000027F-19-25MAY18"
  - "DX,FUEL10-19-28AUG25"
  - "ouo6092,1737046293972-19-27OCT25"
  - "ouo6092,1737046116909-19-27OCT25"
  - "ouo6092,1741882595325-19-13MAR25"
  - "ouo6092,1741882981520-19-13MAR25"
  - "ouo6092,1737045984368-19-27OCT25"
  - "ouo6092,1737474660828-19-29OCT25"
  - "DX,COOL3(T)-19-04APR22"
  - "aota2vy,1686231146950-19-08JUN23"
  - "aota2vy,1686230606303-19-08JUN23"
  - "aota2vy,1686230986565-19-08JUN23"
  - "aota2vy,1686231797294-19-08JUN23"
  - "aota2vy,1686232273085-19-08JUN23"
  - "aota2vy,1686069500990-19-06JUN23"
  - "AG,OUO1011,817-19-26MAR04"
reviewed: true
compiled: 2026-09-23
---

# Cold weather and storage

## The condition

Operating, starting, shipping or storing the machine when temperatures may fall to or below freezing.
The concerns the manual addresses are: fuel waxing, cold starting, engine and hydraulic warm-up, DEF
freezing, and water freezing in the solution system
[[ship-machine-during-cold-weather-months--4aedab|Ship Machine During Cold-Weather Months]]
[[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49|Minimizing the Effect of Cold Weather on Diesel Engines]].
Everything here applies to all models unless an engine (6.8 L = 408R only; 9.0 L = all other models)
is named [[machine-specification--bfe721|Machine Specification]].

> [!warning] IMPORTANT — freezing water (p. 165-3)
> IMPORTANT: Water freezing in tanks and lines can damage the machine. When shipping the machine in months when there is a chance of freezing make sure that the machine can withstand the lowest possible temperatures it will be subjected to. [[ship-machine-during-cold-weather-months--4aedab|Ship Machine During Cold-Weather Months]]

## The manual's temperature limits, as printed

| Temperature | What the manual says | Source |
|---|---|---|
| -11°C (12°F) | DEF freezes and will not flow to the SCR system | [[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982]] |
| 0°C (32°F) | Below this, winter grade fuel (No. 1-D in North America) is best suited; treat fuel when outside temperature drops below 0°C (32°F) | [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49]] |
| 10° C (18°F) below cloud point | Approximate extra operability from winter-formula fuel conditioner in No. 2-D | [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49]] |
| 5°C (41°F) | Begin treating biodiesel fuels with winter-formula conditioner | [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49]] |
| below 0°C (32°F) / below -10°C (14°F) | Use B5 or lower blends / use only winter grade petroleum diesel fuel | [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49]] |
| -5°C (23°F) or below (fuel temperature) | 6.8 L engine: glow plug indicator illuminates — wait to start, preheating is active | [[cold-weather-starting-6-8-l-engine--55e351]] |
| at or below -6°C (21°F) | 9.0 L engine without starting aid: use of starter fluid is recommended | [[cold-weather-starting-9-0-l-engine-without-starting-aid--ca07ce]] |
| below freezing | Warm-up at approximately 900 rpm with no load must be extended to 2—4 minutes | [[warm-the-engine--a6676a]] |
| below -7°C (20° F) | Hydraulic oil may overheat due to a restriction at the hydraulic oil cooler; install winter screens | [[hydraulic-system--47f651]] |
| 0°C (32°F) | Flush with SprayMaster Winterizer Fluid (N305634) if the machine is to be stored in a climate colder than this | [[clean-solution-system--d8c29a]] |
| 8°C (15°F) below lowest expected | Minimum rating for a propylene glycol RV antifreeze used as winterizer | [[prepare-machine-for-cold-weather-storage-winterizing--6354cc]] |
| –5°C and 30°C (23°F and 86°F) | Ideal DEF storage temperature range | [[storing-diesel-exhaust-fluid-def--18be20]] |
| below 27°C (80°F) | Store batteries below this for maximum shelf life | [[preventing-battery-damage--7fe4b4]] |

Engine coolant freeze protection depends on the concentration. Cool-Gard II pre-mix limits range
from Cool-Gard II 20/80 at -9°C (16°F) to Cool-Gard II 60/40 at -52°C (-62°F), with Cool-Gard II
50/50 at -37°C (-34°F); concentrate must be mixed at no less than 40% and no greater than 60%
[[diesel-engine-coolant-engine-with-wet-sleeve-cylinder-liners--d74dac|Diesel Engine Coolant (Engine with Wet Sleeve Cylinder Liners)]].
That topic is a generic Deere-wide module (`generic: true`).

## The levers, as printed

Cold weather is handled mostly by what you put in the machine and how you start and store it, not by
display settings. The only display items the manual ties to cold weather are the DEF level gauge (A)
on the corner post display and the FAIL TO THAW DTC
[[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]],
the glow plug indicator (A) on the 6.8 L engine
[[cold-weather-starting-6-8-l-engine--55e351|Cold-Weather Starting—6.8 L Engine]], and the LED on
the battery box [[operate-the-engine--9bbe7e|Operate the Engine]].

### 1. Fuel

- Winter grade fuel (No. 1-D) has a lower cloud point and a lower pour point; it may reduce power and
  fuel efficiency
  [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49|Minimizing the Effect of Cold Weather on Diesel Engines]].
- John Deere Fuel-Protect Diesel Fuel Conditioner (winter formula), or equivalent, treats non-winter
  grade fuel (No. 2-D) during the cold-weather season
  [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49|Minimizing the Effect of Cold Weather on Diesel Engines]].
- An air intake heater and an engine block heater (coolant heater) are available options to aid
  cold weather starting
  [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49|Minimizing the Effect of Cold Weather on Diesel Engines]].

> [!warning] IMPORTANT — fuel treatment (p. 110-4)
> IMPORTANT: Treat fuel when outside temperature drops below 0°C (32°F). For best results, use with untreated fuel. Follow all recommended instructions on label. [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49|Minimizing the Effect of Cold Weather on Diesel Engines]]

That fuel topic is a generic Deere-wide module (`generic: true`). It also says fabric, cardboard, or
solid winterfronts are not recommended with any John Deere engine
[[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49|Minimizing the Effect of Cold Weather on Diesel Engines]].

### 2. Starting — depends on the engine

- **9.0 L with factory starting aid:** an automatic starting aid injection system injects starting aid
  as needed based on fuel and engine coolant temperatures; manually spraying starting fluid into air
  intake screens is not recommended or required
  [[cold-weather-starting-9-0-l-engine-with-starting-aid--152c60|Cold Weather Starting——9.0 L Engine with Starting Aid]].
- **9.0 L without starting aid:** spray starting fluid into the air intake screens (A) once for 2 or 3
  seconds, then follow Start the Engine
  [[cold-weather-starting-9-0-l-engine-without-starting-aid--ca07ce|Cold Weather Starting—9.0 L Engine without Starting Aid]].
- **6.8 L (408R):** turn the key switch to Accessory/Run and wait while the glow plug indicator is lit;
  when it goes out, turn the key to Start. Never use ether
  [[cold-weather-starting-6-8-l-engine--55e351|Cold-Weather Starting—6.8 L Engine]].

> [!warning] CAUTION — starting fluid (9.0 L with starting aid, p. 50-7)
> CAUTION: Starting fluid is flammable. While using this product, do not smoke and make sure to extinguish all flames. Turn off all pilot lights, stoves, heaters, electrical motors, and other sources of ignition while using this product and/or if vapors are still present. [[cold-weather-starting-9-0-l-engine-with-starting-aid--152c60|Cold Weather Starting——9.0 L Engine with Starting Aid]]

> [!warning] CAUTION — ether on the 6.8 L engine (p. 50-6)
> CAUTION: Do not use ether or starting fluids to start engine with a cold-weather starting device. Ether is highly flammable and could ignite on engines with cold-weather starting device. [[cold-weather-starting-6-8-l-engine--55e351|Cold-Weather Starting—6.8 L Engine]]

> [!warning] IMPORTANT — ether (6.8 L, p. 50-6)
> IMPORTANT: Never use ether starting fluid to start engine. Damage to engine results. [[cold-weather-starting-6-8-l-engine--55e351|Cold-Weather Starting—6.8 L Engine]]

The 9.0 L without-aid procedure carries a longer version of the starting-fluid caution, adding: avoid
contact of aerosol with battery terminals, solenoid, or other electrical/electronic components; do not
overuse this product; keep a cap on the container and store in cool location when not in use
[[cold-weather-starting-9-0-l-engine-without-starting-aid--ca07ce|Cold Weather Starting—9.0 L Engine without Starting Aid]].

### 3. Warm-up

> [!warning] IMPORTANT — lubrication after start (p. 50-8)
> IMPORTANT: To provide proper lubrication after the engine starts, operate the engine at approximately 900 rpm with no load for 1—2 minutes. At temperatures below freezing point, this period must be extended to 2—4 minutes. [[warm-the-engine--a6676a|Warm the Engine]]

As the engine and hydraulic fluid warm up, cycle the steering wheel back and forth until steering
turns freely [[warm-the-engine--a6676a|Warm the Engine]]. Below -7°C (20° F), install winter screens
to the hydraulic coolers to maintain correct temperature
[[hydraulic-system--47f651|Hydraulic System]].

### 4. DEF in cold weather (Final Tier 4/Stage V)

- DEF freezes at -11°C (12°F); machine systems sense low temperature and allow the engine to start even
  with no DEF flow, and engine coolant is used to thaw fluid in the DEF tank when the engine is running
  [[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]].
- If DEF flow is not sensed within 60 to 90 minutes, FAIL TO THAW DTC is displayed; the machine is
  allowed to operate normally for 4 hours after the DTC; if DEF flow is still not sufficient, engine
  power will be reduced to 50% until DEF flow is achieved
  [[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]].
- "Freezing and thawing of DEF does not degrade it."
  [[selective-catalytic-reduction-scr-system-final-tier-4-and-st--c3c982|Selective Catalytic Reduction (SCR) System (Final Tier 4 and Stage V Engines)]]
- Do not add any chemicals or additives to DEF in an effort to prevent freezing
  [[storing-diesel-exhaust-fluid-def--18be20|Storing Diesel Exhaust Fluid (DEF)]].

> [!warning] IMPORTANT — battery disconnect and DEF purge (p. 50-15)
> IMPORTANT: Do not disconnect battery on machines equipped with Final Tier 4/Stage V engines until Light Emitting Diode (LED) on the battery box has turned off. This indicates the diesel exhaust fluid (DEF) system purge is complete. If adequate time is not allowed for lines to be purged, any DEF remaining in lines can crystallize and plug lines. In freezing weather, DEF freezes and possibly bursts lines. [[operate-the-engine--9bbe7e|Operate the Engine]]

### 5. The solution system — winterize before freezing

- For machines stored in cold temperatures, perform a winterizing procedure
  [[prepare-machine-for-storage--fd6f6c|Prepare Machine for Storage]] — see
  [[prepare-machine-for-cold-weather-storage-winterizing]] (base machine first, option steps in
  conditional sections) and [[prepare-machine-for-storage]].
- When shipping in months when there is a chance of freezing, avoid damage by emptying all solution
  tanks and lines, then add SprayMaster Winterizer Fluid
  [[ship-machine-during-cold-weather-months--4aedab|Ship Machine During Cold-Weather Months]].
- The high flow pump seal-chamber job ends with a winterizer flush if the machine is to be stored in a
  climate colder than 0°C (32°F) — see [[inspect-and-replenish-high-flow-spray-pump-seal-chamber-flui]]
  [[inspect-and-replenish-high-flow-spray-pump-seal-chamber-flui--5cdd03|Inspect and Replenish High Flow Spray Pump Seal Chamber Fluid—Annually]].
- Coming out of storage: drain SprayMaster Winterizer Fluid from the solution system and flush it,
  and test DEF urea concentration if the DEF tank was not drained — see [[remove-machine-from-storage]]
  [[remove-machine-from-storage--234a44|Remove Machine from Storage]].

> [!warning] IMPORTANT — first start after storage (p. 165-7)
> IMPORTANT: When first starting the machine after removing from storage, run the machine at no more than low idle for 4 minutes. Turn on the air conditioning system during this time to prevent compressor seal failure. [[remove-machine-from-storage--234a44|Remove Machine from Storage]]

### DEF storage time — conflict

> [!warning] IMPORTANT — DEF storage in the vehicle (p. 165-4)
> IMPORTANT: Long-term storage in the vehicle (over six months) is not recommended. If long-term storage is necessary, periodic testing of diesel exhaust fluid (DEF) is recommended to ensure that urea concentration does not fall out of specification. [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]]

> [!conflict] How long DEF may stay in the tank
> The winterizing procedure and the general storage procedure both say long-term storage in the vehicle
> over six months is not recommended, and that DEF may be stored in the vehicle for as long as six
> months depending upon storage conditions
> [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]]
> [[prepare-machine-for-storage--fd6f6c|Prepare Machine for Storage]].
> The Storing Diesel Exhaust Fluid (DEF) topic says "Long-term storage in the DEF tank (over 12
> months) is not recommended" and that under ideal conditions DEF is expected to remain useable for a
> minimum of 18 months [[storing-diesel-exhaust-fluid-def--18be20|Storing Diesel Exhaust Fluid (DEF)]].
> The 12-month text is a generic Deere-wide module (`generic: true`); the six-month text is
> machine-specific. Not resolved here — for storage longer than six months, drain the DEF tank or test
> DEF before operating, and confirm with your dealer.

## What the manual does NOT specify

- **No temperature at which winterizing becomes required.** The storage procedure says only "for
  machines that are stored in cold temperatures"
  [[prepare-machine-for-storage--fd6f6c|Prepare Machine for Storage]]; the winterizing procedure
  itself gives no threshold
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]].
  The nearest printed figure is the 0°C (32°F) winterizer flush condition in the cleaning procedure
  [[clean-solution-system--d8c29a|Clean Solution System]].
- **The Foam Marker cold-weather procedure is missing.** Three procedures send you to "Prepare Foam
  Marker System for Cold-Weather Storage", but that procedure is not printed in this manual
  [[ship-machine-during-cold-weather-months--4aedab|Ship Machine During Cold-Weather Months]]
  [[prepare-machine-for-storage--fd6f6c|Prepare Machine for Storage]]. Ask your dealer.
- No minimum operating temperature for the solution system or for spraying.
- No recommended coolant concentration for a given climate — only the freeze protection limits of each
  pre-mix
  [[diesel-engine-coolant-engine-with-wet-sleeve-cylinder-liners--d74dac|Diesel Engine Coolant (Engine with Wet Sleeve Cylinder Liners)]].
- No temperature at which the 9.0 L automatic starting aid activates; it is "based on fuel and engine
  coolant temperatures"
  [[cold-weather-starting-9-0-l-engine-with-starting-aid--152c60|Cold Weather Starting——9.0 L Engine with Starting Aid]].

## What overrides it

- **Product labels:** treat fuel following "all recommended instructions on label"
  [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49|Minimizing the Effect of Cold Weather on Diesel Engines]];
  treat the fuel tank with diesel winterizer according to product label instructions
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]].
- **Local availability and your dealer:** see your John Deere or other service provider for
  additional information and local availability of cold-weather aids
  [[minimizing-the-effect-of-cold-weather-on-diesel-engines--221d49|Minimizing the Effect of Cold Weather on Diesel Engines]].
- **Chemical residue:** the solution system must already have been through the chemical cleaning
  process before winterizing
  [[prepare-machine-for-cold-weather-storage-winterizing--6354cc|Prepare Machine for Cold-Weather Storage – Winterizing]].

## Related

- [[engine]] · [[fuel-system]] · [[aftertreatment]] · [[solution-pump]]
