---
type: troubleshooting
title: "Locating Faulted Nozzles troubleshooting"
models: [all]
options: [Individual Nozzle Control]
engine_tier: null
components: [nozzle, nozzle body, individual nozzle control unit, boom]
sources:
  - "UZEGGEY,1765865713169-19-16DEC25"
  - "bn55050,1775500282421-19-27APR26"
  - "UZEGGEY,1765865715767-19-16DEC25"
reviewed: true
compiled: 2026-09-23
---

# Locating Faulted Nozzles troubleshooting

**This is a reference procedure, not a symptom table.** The manual prints no symptom–problem–solution
table for it. It explains how to go from a fault message on the display to the nozzle on the boom [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]]. It
is printed in the Individual Nozzle Control (INC) System section (p. 130-30 to 130-31), so it applies to
**machines with INC**. A similar topic, Determining Nozzle Location, is printed in the Nozzle System
application (p. 25-G-4 to 25-G-5, and also listed at p. 130-11) [[determining-nozzle-location--984404|Determining Nozzle Location]]. Once you have found the nozzle, use the
symptom tables in [[nozzle-body-troubleshooting]].

## How nozzles are numbered

When a nozzle, or individual nozzle control (INC) unit fault is detected the operator is notified on
display. Each nozzle is numbered based on its position on the spray boom. Nozzles are counted starting on
the left-hand tip of the boom and ending at the right-hand boom tip [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]].

![[N156561.png]]
**Figure N156561** — A: Nozzle 1; B: Nozzle 97 (Example: 36 m (120 ft) Boom with 38 cm (15 in) Spacing)
[[locating-faulted-nozzles--477984|Locating Faulted Nozzles]]

## Is the fault at a nozzle or at the INC unit?

"There is a maximum of five nozzles operated by each INC unit. Four or five consecutive nozzles with a
fault indicate that the fault is at the INC unit." [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]]

> [!conflict] How many nozzles each INC unit operates
> Locating Faulted Nozzles (p. 130-30) says "a maximum of five nozzles operated by each INC unit" and that
> four or five consecutive faulted nozzles "indicate" the fault is at the INC unit [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]]. Determining Nozzle
> Location (p. 25-G-4) says "There is a maximum of nine nozzles operated by each INC unit. Consecutive
> nozzles with a fault may indicate that the fault is at the INC unit." [[determining-nozzle-location--984404|Determining Nozzle Location]]. Neither is a generic module.
> The manual does not say which applies to which configuration. Check the INC unit layout on your boom or
> ask your dealer.

## Finding the nozzle quickly: last nozzle on the left-hand wing

The tables indicate the last nozzle number (A) on the left-hand wing, allowing for a quicker location of
the faulted nozzle [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]].

![[N157815.png]]
**Figure N157815** — A: Last Nozzle on Left-Hand Boom [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]]

As printed in Locating Faulted Nozzles [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]]:

| Boom | Nozzle Spacing | Last Nozzle on Left-Hand Wing |
|---|---|---|
| 30.5 m (100 ft) | 38 cm (15 in) | 36 |
| 30.5 m (100 ft) | 45.7 cm (18 in) | 30 |
| 30.5 m (100 ft) | 48.3 cm (19 in) | 28 |
| 30.5 m (100 ft) | 50.8 cm (20 in) | 26 |
| 36.6 m (120 ft) | 38 cm (15 in) | 44 |
| 36.6 m (120 ft) | 45.7 cm (18 in) | 37 |
| 36.6 m (120 ft) | 48.3 cm (19 in) | 35 |
| 36.6 m (120 ft) | 50.8 cm (20 in) | 32 |

Determining Nozzle Location adds two booms not in the table above [[determining-nozzle-location--984404|Determining Nozzle Location]]:

| Boom | Nozzle Spacing | Last Nozzle on Left-Hand Wing |
|---|---|---|
| 27.4 m (90 ft) | 38 cm (15 in) | 32 |
| 27.4 m (90 ft) | 50.8 cm (20 in) | 23 |
| 40.2 m (132 ft) | 38 cm (15 in) | 49 |
| 40.2 m (132 ft) | 50.8 cm (20 in) | 36 |

For the 100 ft and 120 ft booms the last-nozzle numbers are the same in both topics [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]] [[determining-nozzle-location--984404|Determining Nozzle Location]].

> [!conflict] Metric length of the 100 ft boom
> Locating Faulted Nozzles labels it "30.5 m (100 ft) Boom" [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]]; Determining Nozzle Location labels it
> "30.6 m (100 ft) Boom" [[determining-nozzle-location--984404|Determining Nozzle Location]]. The nozzle numbers are the same. Neither is a generic module.

> [!inference] Working out which side of the boom
> The manual gives the last left-hand nozzle number and says nozzles are counted from the left-hand tip
> to the right-hand tip [[locating-faulted-nozzles--477984|Locating Faulted Nozzles]]. It follows that any higher nozzle number is on the center frame or the
> right-hand wing. The manual does not print the numbers where the center section starts or ends.

## What the manual does not specify

- Nozzle numbering for spacings or booms not in either table.
- A procedure for testing the INC unit itself. Nozzle-level causes and fixes are in the Nozzle Body table
  (see [[nozzle-body-troubleshooting]]) [[nozzle-body-troubleshooting--48cd75|Nozzle Body Troubleshooting]].
