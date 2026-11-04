---
module_id: ouo6092,1764000734385-19-27APR26
title: Vision Processing Unit Status
section: See & Spray (If Equipped)
page_labels:
- 135-20
pdf_pages:
- 786
models:
- all
options:
- See & Spray
engine_tier: null
topic_type: display_ui
components:
- battery
- boom
conditions: []
signal_words:
- NOTE
figures:
- NX1435674
generic: false
title_inferred: false
parent_module_id: null
---

# Vision Processing Unit Status

NX1435674—UN—12DEC25

![[NX1435674.png]]
**Figure NX1435674** — A: LED Indicator

NOTE: Each vision processing unit (VPU) has a built-in LED indicator (A) to check status for each controller and aid in troubleshooting.
Solid green—VPU is powered on and the application is running.
Solid blue—VPU booting starting up (some flasheds may be observed).
Flashing blue—VPU booting / startup battery voltage at start up insuffient < below 9V DC.
Two purple flashes—VPU BUS (Boom Trac CAN) communications are not functioning
Four short yellow flashes—Ethernet communications are not functioning
2 Long 2 H red flashes—Vanilla Image
If multiple faults are present, the VPU will cycle through each fault with a 3-second pause between each fault.

> Source: OMKK105338 p. 135-20 · module ouo6092,1764000734385-19-27APR26
