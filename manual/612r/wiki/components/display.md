---
type: component
title: "Display"
models: [all]
options: [Dual Product, Dry Spreader]
engine_tier: null
components: [display, commandarm, corner post display, micro display]
sources:
  - "aota2vy,1684851521172-19-23MAY23"
  - "DX,PC,DISPLAY,REFERENCE-19-23JUN23"
  - "as09261,1711378603599-19-03MAY24"
  - "as09261,1711132331286-19-22MAR24"
  - "as09261,1711132101383-19-05APR24"
  - "bn55050,1777657987068-19-01MAY26"
  - "as09261,1712165513768-19-03APR24"
  - "bn55050,1768507860026-19-15JAN26"
  - "DP99999,0001055-19-08MAR22"
  - "ouo6092,1777578346785-19-30APR26"
  - "aota2vy,1685545502185-19-31MAY23"
reviewed: true
compiled: 2026-09-23
---

# Display

The machine has more than one display: the CommandCenter display on the armrest, the corner post
display, and micro displays at the fill and load stations. They do different jobs, so the first
question for any display question is *which* display.

## Warnings

> [!warning] CAUTION
> CAUTION: If the red brake warning indicator is illuminated, stop the machine immediately.
> [[corner-post-display--2f66ad|Corner Post Display]]

## What it is

### CommandCenter display (armrest)

The CommandCenter display sits on the armrest control console attached to the right-hand side of
the seat [[commandarm-console-and-display--f3fc44|CommandARM Console and Display]]. Rotate the
display left/right to the desired operating position
[[console-and-display--92d57a|Console and Display]]. The armrest control console itself is adjusted
by loosening the knobs and sliding it up/forward or down/back in slots on the outer plate, then
tightening the knobs to lock the armrest into position
[[console-and-display--92d57a|Console and Display]].

The section titles of the Operator's Manual match the names of the applications found on the
display; to find a feature described in the Operator's Manual on the display, locate the section
title at the top of the page and access the application with the same name on the display
[[commandcenter-display-applications--9eff28|CommandCenter Display Applications]]. For information
on how to navigate to the desired application, refer to the Access information at the beginning of
each section [[commandcenter-display-applications--9eff28|CommandCenter Display Applications]].

For additional information on display hardware and software functionality, reference the Display
Operator's Manual and the Help Center application on the display
[[generation-4-and-g5-displays--fa4f54|Generation 4 and G5 Displays]]. To obtain a copy of the
Operator's Manual, contact your dealer, use the Help Center application on the display, or visit
techpubs.deere.com [[generation-4-and-g5-displays--fa4f54|Generation 4 and G5 Displays]].

> [!inference] Display hardware is outside this manual
> [[generation-4-and-g5-displays--fa4f54|Generation 4 and G5 Displays]] is flagged `generic: true`
> in its frontmatter, and the only thing it states is where to get the Display Operator's Manual
> [[generation-4-and-g5-displays--fa4f54|Generation 4 and G5 Displays]]. I read that as meaning
> display hardware and software questions are not answerable from OMKK105338 itself — this page
> covers what the sprayer topics say about the displays, not how the display software works.

### Corner post display

The corner post display holds the status indicators on the display located on the front right-hand
corner post [[sprayer-overview--6fbbe6|Sprayer Overview]]. Its indicators include the left-hand and
right-hand turn indicators, park brake indicator, red and yellow brake warning indicators, the
AutoTrac indicator, the steering warning indicator, Stop Operation (Red) and Operator Alert
[[corner-post-display--2f66ad|Corner Post Display]]. Stop Operation (Red) illuminates and requires
the machine be stopped at once and the problem corrected, and the diagnostic trouble code is shown
on the armrest display until the problem is resolved
[[corner-post-display--2f66ad|Corner Post Display]].

### Micro displays (fill and load stations)

The micro display (A) is located at the Fill Station and allows the operator to view various
information during the loading process
[[fill-station-micro-display--6a592f|Fill Station Micro Display]]. There are three main screens
that are visible during most operations showing a combination of pump speed, pump pressure and tank
volume, and the operator can toggle between these screens using the buttons on the micro display
[[fill-station-micro-display--6a592f|Fill Station Micro Display]].

On machines with the dual product option, micro displays (A and B) on the side load station do the
same job, and values such as target fill amount are entered with the numeric input buttons (D) on
the keypad (C) [[side-load-station-micro-displays--a061bc|Side Load Station Micro Displays]]. The
front load station has its own micro display (A)
[[front-load-station-micro-display--ad6ef9|Front Load Station Micro Display]].

## Where it is

![[H129095.png]]

**Figure H129095** — Display, on the armrest console
[[console-and-display--92d57a|Console and Display]]

![[H137356.png]]

**Figure H137356** — Corner Post Display [[sprayer-overview--6fbbe6|Sprayer Overview]]

![[N103598.png]]

**Figure N103598** — A: Micro Display, at the Fill Station
[[fill-station-micro-display--6a592f|Fill Station Micro Display]]

![[N161537.png]]

**Figure N161537** — A: Micro Display (system 1); B: Micro Display (system 2); C: Keypad;
D: Numeric Input Buttons, at the side load station
[[side-load-station-micro-displays--a061bc|Side Load Station Micro Displays]]

## Related settings

- **Dual display.** Attach a secondary display to connector (A)
  [[dual-display--fe591a|Dual Display]]. These video inputs are in addition to the armrest
  CommandCenter Display, and display harnesses can be obtained via regular spare part channels
  [[dual-display--fe591a|Dual Display]].
- **Rate Control/Display Speed** (dry spreader option) displays available speed sources for the
  rate control unit, and the speed source must be adjusted based on ground conditions, availability
  of Global Positioning System (GPS) signal, and options installed
  [[rate-control-display-speed--8b68eb|Rate Control/Display Speed]]. Select GPS when wheel slip is
  likely to occur or when performing normal operations; select Wheel Speed when the GPS signal is
  degraded, GPS is not installed, or wheel slip is not likely to occur
  [[rate-control-display-speed--8b68eb|Rate Control/Display Speed]]. See also [[wheel]].
- Button and function assignments on the display and armrest: see [[commandarm]].
- Light presets are configured from the display: see [[lights]].
- Boom and BoomTrac settings are configured from the display: see [[boom-height]] and [[boom]].

## Related procedures

- Adjusting the console and display position
  [[console-and-display--92d57a|Console and Display]].
- USB Charging ports and the 12 V auxiliary outlet are inside the console storage compartment; the
  USB ports are not connected to the radio or the display
  [[console-and-display--92d57a|Console and Display]].

## Related troubleshooting

- A fault shown as Stop Operation (Red) on the corner post display keeps its diagnostic trouble
  code on the armrest display until the problem is resolved
  [[corner-post-display--2f66ad|Corner Post Display]].
- The red brake warning indicator illuminates when a serious fault has been detected that affects
  brake system performance, and flashes when the park brake cannot engage
  [[corner-post-display--2f66ad|Corner Post Display]].
- The steering warning indicator illuminates when a serious fault has been detected in the steering
  system [[corner-post-display--2f66ad|Corner Post Display]].
