---
type: safety
title: "Pressurized fluids and systems — safety"
models: [all]
options: []
engine_tier: null
components: [solution system, nozzle, flowmeter, strainer, hydraulic system, accumulator, onboard air system, air spring, service brake, cooling system, air conditioning]
sources:
  - "DX,FLUID-19-16MAR26"
  - "DX,WW,ACCLA-19-15APR03"
  - "DX,SERV-19-20JAN26"
  - "DX,WW,CHEM02-19-05APR04"
  - "aota2vy,1685563436637-19-31MAY23"
  - "ouo6092,1776103331959-19-13APR26"
  - "OUO6092,0000DE4-19-13MAR19"
  - "ouo6092,1737119817515-19-19NOV25"
  - "ouo6092,1763039484376-19-27APR26"
  - "BN55050,000005D-19-08JUN18"
  - "aota2vy,1686155025825-19-07JUN23"
  - "as09261,1712328149088-19-05APR24"
  - "UZEGGEY,1765865455065-19-29APR26"
  - "ouo6092,1763587157303-19-27APR26"
reviewed: true
compiled: 2026-09-23
---

# Pressurized fluids and systems — safety

Warnings for every system on the machine that holds fluid or air under pressure: the spray
(solution) system, hydraulics and accumulators, the onboard air system and air springs, service
brakes, the cooling system and the air conditioner. Each warning below is copied verbatim, once,
with every page it is printed on. Fuel-system pressure (high pressure common rail) is on
[[fuel-fire-and-battery-safety]]. Generic Deere-wide modules (`generic: true`) are marked where they
are the source.

## Any pressurized line, hose or fitting

> [!warning] Generic Deere-wide safety text (no signal word) — [[avoid-high-pressure-fluids--3fc79d|Avoid High-Pressure Fluids]] (p. 05-4, 05-5). Applies to: all hydraulic and other lines
> Escaping fluid under pressure can penetrate the skin causing serious injury. Avoid the hazard by relieving pressure before disconnecting hydraulic or other lines. Tighten all connections before applying pressure. Search for leaks with a piece of cardboard. Protect hands and body from high-pressure fluids. In case of accidental skin injection, seek immediate surgical treatment.

> [!warning] CAUTION — printed on [[solution-pump-maintenance-and-operation-recommendations--a28f35|Solution Pump Maintenance and Operation Recommendations]] (p. 55-3, 55-4, 55-5). Applies to: solution pump and any line on the machine
> CAUTION: Escaping fluid under pressure can penetrate the skin causing serious injury. Avoid the hazard by relieving pressure before disconnecting hydraulic or other lines. Tighten all connections before applying pressure. Search for leaks with a piece of cardboard. Protect hands and body from high-pressure fluids. If an accident occurs, see a doctor immediately. Any fluid injected into the skin must be surgically removed within a few hours or gangrene can result. Doctors unfamiliar with this type of injury should reference a knowledgeable medical source. Such information is available from Deere & Company Medical Department in Moline, Illinois, U.S.A.

The generic maintenance module adds: "Disengage all power and operate controls to relieve pressure.
Lower equipment to the ground. Stop the engine and secure the machine."
[[practice-safe-maintenance--f22083|Practice Safe Maintenance]] (generic Deere-wide module). Inspect
hydraulic hoses and steel piping periodically–at least once per year–for leakage, kinking, cuts,
cracks, abrasion, blisters, corrosion, exposed wire braid, or any other signs of wear or damage
[[avoid-high-pressure-fluids--3fc79d|Avoid High-Pressure Fluids]].

## Task: servicing the spray (solution) system — relieving spray pressure

How to relieve boom pressure, and what the manual does not cover, is on the procedure page
[[relieve-spray-pressure]]. In short: the manual's one relief procedure is **Boom Pressure Relief**
in the Spray System application [[pressure-relief--da45ff|Pressure Relief]], and the decal on the
machine reads "Spray system is under pressure. Before servicing, conduct boom pressure relief function
to relieve system pressure." [[nozzle-control-system-decal--08af28|Nozzle Control System Decal]]

> [!inference] Gap: chassis-side plumbing
> No topic gives a relief procedure for the solution pump, pressure strainers or flowmeter housings.
> The strainer and flowmeter topics rely on turning the solution pump off before closing the
> flowmeter shutoff valve, then draining through the strainer drain valves
> [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]]
> [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]]. The generic modules say
> "relieve spray pressure from system" without naming a control
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
> If you are not sure the chassis plumbing is depressurised, ask your John Deere dealer.

> [!warning] CAUTION — printed on [[pressure-relief--da45ff|Pressure Relief]] (p. 25-I-7, 25-I-8). Applies to: Boom Pressure Relief function
> CAUTION: Avoid unintended spray from nozzles. Do not use when non-John Deere aftermarket solution-system equipment is installed. These include, but are not limited to, direct injection and section control systems. See the direct injection system Operator's Manual or details regarding the use of this feature with a direct injection system.

> [!warning] CAUTION — printed on [[clean-flowmeter-as-required--75e4f8|Clean Flowmeter—As Required]] (p. 55-26, 55-27, 115-16). Applies to: flowmeter cleaning
> CAUTION: Do not close the flowmeter shutoff valve (B) with the solution pump running. This can trap pressure in the plumbing that can be hazardous when removing flowmeters for cleaning.

> [!warning] CAUTION — printed on [[clean-pressure-strainers-daily--be6871|Clean Pressure Strainers—Daily]] (p. 45-6, 45-7, 45-8, 55-24, 55-25, 55-26, 115-13, 115-14). Applies to: pressure strainer cleaning
> CAUTION: Do not close flowmeter shutoff valve (A) with the solution pump running. This can trap pressure in the system that can be hazardous when opening strainers for cleaning. Do not drain solution onto the ground. Drain into a container. Drain solution in an area where people, animals, vegetation water supply, and so on, cannot be contaminated.

> [!warning] CAUTION — printed on [[repair-nozzle-solenoid--eba495|Repair Nozzle Solenoid]] (p. 125-27, 125-28, 125-29, 125-30); [[repair-nozzle-solenoid--fa18a1|Repair Nozzle Solenoid]] (p. 130-27, 130-28, 130-29). Applies to: nozzle body service — ExactApply and Individual Nozzle Control topics
> CAUTION: DO NOT clean nozzle tips by placing in mouth and blowing. This action could result in swallowing or inhaling hazardous chemicals that will poison, causing serious injury or death. Relieve trapped pressure in the spray boom before servicing nozzle body.

> [!warning] IMPORTANT — printed on [[exactapply-strainer-requirements--c2ea09|ExactApply Strainer Requirements]] (p. 125-5); [[individual-nozzle-control-inc-pro-strainer-requirements--86bfb4|Individual Nozzle Control (INC) Pro Strainer Requirements]] (p. 130-16). Applies to: machines with ExactApply or Individual Nozzle Control
> IMPORTANT: 50 and 80 mesh strainers are installed in the pressure plumbing of the machine. These strainers must remain installed during all applications to prevent plugging of spray tips and solenoid valves.

The generic chemical-sprayer module: "If nozzle clogs or system malfunctions, stop engine and relieve
spray pressure from system."
[[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]]
(generic Deere-wide module).

### Spray-system pressures that disagree

> [!conflict] Maximum solution-system pressure — generic limit vs flat fan tip range
> The generic Deere-wide chemical-safety module (`generic: true`) says: do not operate solution
> delivery system at pressures exceeding 345kPa (3.5 bar) (50 psi)
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]].
> The machine-specific Wet System topic says most flat fan spray tips are designed to operate in the
> 207—414 kPa (2—4 bar) (30—60 psi) range [[flat-fan-spray-tip--dc7cce|Flat Fan Spray Tip]].
> Not reconciled here. Confirm your machine's limit with your John Deere dealer; follow the product
> label and the tip chart.

> [!conflict] Rinse and boom air-bleed pressures above the generic limit
> Rinse Nozzle Bodies—Daily (ExactApply) says to rinse one section at a time at 90 psi for a minimum
> of 10 seconds per section [[rinse-nozzle-bodies-daily--422740|Rinse Nozzle Bodies—Daily]], and the
> Boom Air Bleed Process says to run the sprayer in manual spray mode at 620.6 kPa (90 psi)
> [[recommendations-for-eliminating-air-from-solution-system--c98980|Recommendations for Eliminating Air from Solution System]].
> Both are above the generic module's 345kPa (3.5 bar) (50 psi) limit
> [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]]
> (`generic: true`). Both machine topics use water or rinse water, but the pressure statements still
> disagree. Not reconciled here; confirm with your dealer.

> [!conflict] Nozzle working pressures stated above the generic limit
> The INC Pro direct-injection topic refers to the 1034 kPa (10.34 bar) (150 psi) working range of the
> nozzles [[operate-system-with-direct-injection-installed--d099f8|Operate System with Direct Injection Installed]],
> and the ExactApply field-operation note says plungers do not open properly when operating above
> 965.3 kPa (9.65 bar) (140 psi) when a low voltage condition occurs
> [[field-operation--87b1c4|Field Operation]]. Both imply operation above the generic module's
> 345kPa (3.5 bar) (50 psi) [[service-and-operate-chemical-sprayers-safely--6b47f1|Service and Operate Chemical Sprayers Safely]]
> (`generic: true`). Applies to: Individual Nozzle Control Pro with Direct Injection; ExactApply. Not
> reconciled here.

## Task: washing the machine and components — water pressure

The printed pressure-wash limits use slightly different unit formats; each is copied as printed.

> [!warning] IMPORTANT — printed on [[clean-nozzle-body--f5b5d2|Clean Nozzle Body]] (p. 125-20); [[clean-nozzle-body--a341ce|Clean Nozzle Body]] (p. 130-21). Applies to: nozzle bodies — ExactApply and Individual Nozzle Control
> IMPORTANT: Do not pressure wash these components. Use normal water pressure less than 345 kPa (3.45 bar) (50 psi).

> [!warning] IMPORTANT — printed on [[machine-informational-decals--8583ad|Machine Informational Decals]] (p. 50-2, 50-3, 50-4). Applies to: components named on the machine informational decals
> IMPORTANT: Do not pressure wash these components. Use normal water pressure less than 50 psi (345 kPa).

> [!warning] IMPORTANT — printed on [[clean-vehicle-of-hazardous-chemicals-including-pesticides--37d899|Clean Vehicle of Hazardous Chemicals, Including Pesticides]] (p. 05-16, 70-1, 70-2, 115-1, 165-2). Applies to: electronic/electrical components, bearings, hydraulic seals, fuel injection pumps
> IMPORTANT: Directing pressurized water at electronic/electrical components or connectors, bearings and hydraulic seals, fuel injection pumps or other sensitive parts and components may cause product malfunctions. Reduce pressure, and spray at a 45 to 90 degree angle.

## Task: working on the onboard air system

> [!warning] CAUTION — printed on [[air-system-decal--c43439|Air System Decal]] (p. 10-6). Applies to: onboard air system (decal)
> CAUTION Air system at high pressure can discharge debris or components. Wear protective eyewear. Before servicing, relieve all system air pressure.

> [!warning] CAUTION — printed on [[drain-moisture-from-onboard-air-tanks-daily--8845e9|Drain Moisture from Onboard Air Tanks— Daily]] (p. 45-6); [[drain-moisture-from-onboard-air-tanks-daily--81f37c|Drain Moisture from Onboard Air Tanks— Daily]] (p. 115-12). Applies to: draining moisture from the onboard air tanks
> CAUTION: Unloader valve and tank exhaust are at high pressure. Wear protective eyewear when servicing or relieving pressure through the valves.

> [!warning] CAUTION — printed on [[remove-liquid-system--bbc29b|Remove Liquid System]] (p. 70-4, 70-5, 70-6, 70-7, 70-8, 70-9, 70-10, 70-11, 70-12, 70-13). Applies to: removing the liquid system
> CAUTION: The onboard air system is charged at 689—896 kPa (8.9 bar) (100—130 psi). To avoid injury to yourself or others, wear safety goggles and gloves and be sure that others are clear of the area before relieving the onboard air pressure system.

> [!warning] CAUTION — printed on [[install-liquid-system--71cdcf|Install Liquid System]] (p. 70-14, 70-15, 70-16, 70-17, 70-18, 70-19). Applies to: installing the liquid system
> CAUTION: On board air system is charged at 689—896 kPa (8.9 bar) (100—130 psi). To avoid injury to yourself or others, wear safety goggles and gloves and be sure that others are clear of the area before relieving the on board air system pressure.

> [!warning] CAUTION — printed on [[replace-air-drier-cartridge-annually--fdd7c5|Replace Air Drier Cartridge—Annually]] (p. 115-34, 115-35). Applies to: replacing the air drier cartridge
> CAUTION: The onboard air system is charged at 689—896 kPa (6.89—8.96 bar) (100—130 psi). To avoid injury to yourself or others, wear safety goggles and gloves and be sure that others are clear of area before relieving the onboard air system pressure.

> [!conflict] Onboard air system pressure — bar value printed two ways
> Remove Liquid System and Install Liquid System print the onboard air charge as 689—896 kPa (8.9 bar)
> (100—130 psi) [[remove-liquid-system--bbc29b|Remove Liquid System]]
> [[install-liquid-system--71cdcf|Install Liquid System]], while Replace Air Drier Cartridge—Annually
> prints 689—896 kPa (6.89—8.96 bar) (100—130 psi)
> [[replace-air-drier-cartridge-annually--fdd7c5|Replace Air Drier Cartridge—Annually]]. The kPa and
> psi ranges agree; the bar value differs. Copied as printed; not corrected here.

## Task: air springs and suspension (jacking, tread adjust, tire work, transport)

> [!warning] CAUTION — printed on [[attach-jack-bracket--febe2e|Attach Jack Bracket]] (p. 100-13, 100-14). Applies to: jacking the machine
> CAUTION: Air spring can explode if over inflated, causing serious injury or death to you or others. When adjusting suspension assemblies, do not exceed 689 kPa (6.89 bar) (100 psi). Keep hands and body away from suspension linkage.

> [!warning] CAUTION — printed on [[install-optional-tires-600r-612r-and-616r--7f90cc|Install Optional Tires—600R, 612R, and 616R]] (p. 100-17, 100-18). Applies to: installing optional tires — 600R, 612R and 616R
> CAUTION: Air spring can explode if over-inflated, causing serious injury or death to you or others. When adjusting suspension assemblies, do not exceed 689 kPa (6.89 bar) (100 psi). Keep hands and body away from suspension linkage.

> [!warning] CAUTION — printed on [[adjust-tread-adjust-shims-tire-off-ground-preferred-method--f760b4|Adjust Tread Adjust Shims—Tire off Ground (Preferred Method)]] (p. 105-6, 105-7, 105-8). Applies to: adjusting tread adjust shims
> CAUTION: Air spring can explode if overinflated, causing serious injury or death to you or others. When adjusting suspension assemblies, do not exceed 689 kPa (6.89 bar) (100 psi). Keep hands and body away from suspension linkage.

> [!warning] CAUTION — printed on [[check-air-springs-daily--582452|Check Air Springs—Daily]] (p. 115-12). Applies to: daily air-spring check
> CAUTION: Air spring can explode if over inflated causing serious injury or death to you or others. When adjusting suspension assemblies, do not exceed 689 kPa (6.89 bar) (100 psi). Keep hands and body away from suspension linkage.

> [!warning] CAUTION — printed on [[prepare-machine-for-transport-on-semi-tractor-trailer--bd0993|Prepare Machine for Transport on Semi- Tractor Trailer]] (p. 105-3, 105-4, 105-5). Applies to: transport on a semi-tractor trailer
> CAUTION: Suspension linkages can cause injury to you or others from movement when inflating or deflating air springs. Keep hands and body away from suspension linkage.

> [!warning] CAUTION — printed on [[auto-air-level-decal--fd02d1|Auto Air Level Decal]] (p. 10-7, 10-8). Applies to: auto air level system (decal)
> CAUTION Avoid injury from impact with sprayer frame. Chassis moves during inflation and deflation of air bag suspension system. Stand clear of machine when operating system.

> [!warning] CAUTION — printed on [[inspect-tires-daily--f00933|Inspect Tires—Daily]] (p. 100-1, 100-2, 100-3, 100-4, 100-5, 100-6, 100-7, 100-8, 100-9, 100-10, 100-11, 100-12, 100-13). Applies to: tires
> CAUTION: Explosive separation of a tire and rim parts can cause serious injury or death. Only attempt to mount a tire if you have the proper equipment and experience to perform the job.

## Task: hydraulics, accumulators and boom breakaway

> [!warning] Generic Deere-wide safety text (no signal word) — [[service-accumulator-systems-safely--6bd0ed|Service Accumulator Systems Safely]] (p. 05-8, 05-9). Applies to: hydraulic accumulators
> Escaping fluid or gas from pressurized hydraulic accumulator systems can cause serious injury. Extreme heat can cause the accumulator to burst, and pressurized lines can be accidentally cut. Do not weld or use a torch near a pressurized accumulator or pressurized line. Relieve pressure from the hydraulic system before removing accumulator. Never attempt to relieve hydraulic system or accumulator pressure by loosening a fitting. Accumulators cannot be repaired.

> [!warning] IMPORTANT — printed on [[accumulator-decals--25a6f0|Accumulator Decals]] (p. 10-7). Applies to: accumulators (decals)
> IMPORTANT: There are more accumulator decals with different factory precharge pressures in different locations that are not illustrated in this manual. Follow the same caution message on those decals, but consider the precharge pressure indicated on each decal. For more information, contact a John Deere Dealer or other service provider.

> [!warning] CAUTION — printed on [[full-boom-breakaway--f070b7|Full Boom Breakaway]] (p. 80-6). Applies to: full boom breakaway
> CAUTION: Serious injury or death to you or others can occur from standing in front of boom when it is returning to its original position. Full boom breakaway system is under hydraulic pressure. If the boom must be lifted or aided over an object or an obstruction, stand behind the boom to avoid injury.

## Task: service brakes and towing

> [!warning] CAUTION — printed on [[bleed-service-brakes--28b467|Bleed Service Brakes]] (p. 105-2). Applies to: bleeding the service brakes
> CAUTION: Service brake system operates at high pressure. To avoid the risk of injury to yourself or bystanders, DO NOT attempt to bleed the brake system at the caliper.

> [!warning] CAUTION — printed on [[inspect-service-brake-components-annually--9b53ea|Inspect Service Brake Components— Annually]] (p. 115-35, 115-36). Applies to: annual service brake inspection
> CAUTION: Service brake system operates at high pressure. To avoid the risk of injury to yourself or bystanders, DO NOT crack lines in this system if a brake bleeding is necessary (See Bleed Service Brakes in Chassis section of this manual). The hydraulic brake components in this system should be serviced by a John Deere dealer or other service provider.

> [!warning] IMPORTANT — printed on [[tow-the-sprayer--4c2976|Tow The Sprayer]] (p. 105-2). Applies to: towing
> IMPORTANT: To tow or pull the sprayer, engine MUST be running and hydraulic system MUST have correct hydraulic pressure or damage WILL occur to brakes and wheel hubs. If engine is not running or proper hydraulic system pressure cannot be maintained, contact a John Deere dealer or other service provider and consult the sprayer Technical Manual for proper brake and wheel hub disengagement procedure. The machine should only be towed if stuck, WITH the engine running, correct hydraulic pressure, and the secondary brake released. Only pull the machine a short distance and at slow speed of 0—5 km/h (0—3 mph).

## Task: cooling system and air conditioning

> [!warning] CAUTION — printed on [[service-cooling-system-safely--04c2de|Service Cooling System Safely]] (p. 05-8). Applies to: engine cooling system
> CAUTION: Explosive release of fluids from pressurized cooling system can cause serious burns. Shut off engine, set park brake, and remove key. NEVER add coolant when engine is overheated. Wait for it to cool. NEVER remove surge tank cap when coolant or engine is hot. Wait until engine coolant is cool to remove cap. SLOWLY loosen cap to relieve pressure before removing completely.

> [!warning] CAUTION — printed on [[service-air-conditioner--4b53da|Service Air Conditioner]] (p. 90-5). Applies to: air conditioning
> CAUTION: Escaping refrigerant under pressure can penetrate eyes and skin causing serious injury to you or others. Do not attempt to repair or service refrigerant system. (Contact a John Deere dealer or other service provider.)

## What the manual does not say

- No relief procedure for the spray system's chassis side (pump, strainers, flowmeter) — see the gap
  above and [[relieve-spray-pressure]].
- No single maximum pressure for the solution system that all topics agree on — see the conflicts
  above.
- No accumulator precharge values beyond those printed on the decals; the manual says to consider the
  precharge pressure indicated on each decal
  [[accumulator-decals--25a6f0|Accumulator Decals]].
