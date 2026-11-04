---
module_id: ouo6092,1778242271722-19-12MAY26
title: Operate System with the Remote Control
section: ExactApply Nozzle Control System (If Equipped)
page_labels:
- 125-17
- 125-18
- 125-19
- 125-20
pdf_pages:
- 711
- 712
- 713
- 714
models:
- all
options:
- ExactApply
engine_tier: null
topic_type: procedure
components:
- battery
- boom
- cab
- lights
- nozzle
conditions:
- temperature
signal_words:
- NOTE
figures:
- N155771
- N155772
- N125203
- N125209
- N125210
- N125211
- N125212
- N125213
- N125214
generic: false
title_inferred: false
parent_module_id: null
---

# Operate System with the Remote Control

Remote Control Range
N155771—UN—17MAY21

![[N155771.png]]
**Figure N155771**

Wireless Nozzle Control Range
The remote control allows the operator to activate individual nozzles or sections of nozzles from outside the cab for troubleshooting purposes. The remote control requires a direct line of sight to the receiver which is mounted to the rear of the boom center frame. If the remote control travels outside of the range shown above, it will need to re-establish a connection with the receiver prior to the remote control functioning. To re-establish a connection, move the remote control within the range of the receiver (this can take up to 20 seconds). If the system is still unresponsive to a command, position the remote control within 2—3 meters of the receiver for 20 seconds and the connections should automatically re-establish. Response to a command should be immediate, however, if there is a delay, this may indicate poor signal strength between the receiver and the remote control, interference, edge of operating range and/or low battery in the remote control.
In some instances, if the operator is holding/pressing a button on the remote control and walks out of the range of the receiver, the remote control can lock up. If the remote control is in a locked state, it requires a reboot.
To reboot, remove the battery from the remote control for 20 seconds and re-install.
Upon a cold boot of the machine, the receiver and remote control can take up to 2 minutes to connect and begin functionality. If a remote control is taken out of range of the receiver, it can take approximately 20 seconds to re-establish a connection.
Remote Control Diagnostics
NODC Data Identifier (DID) 1300—1305 can be used to see if a paired remote control is communicating with the gateway. Each NODC Data Identifier (DID) 1300—1305 aligns with a respective button on the remote control. Pull up NODC Data Identifier (DID) 1300 on the display (Menu>System>Diagnostics Center>Controllers>Nozzle Domain Control) and have someone push a button on the remote control while they are standing just behind the center frame where the signal would be strong. In NODC Data Identifier (DID) 1300 you will see “000000” displayed. Those DID will each just show an 0 when not presed or a 1 when pressed. This process will allow the operator to ensure that the remote control and gateway are communicating properly. This process only applies for a remote control that is already paired. With 2 people, have one person stand in a line of sight and another person in the cab to verify that NODC Data Identifier (DID) 1300 changes when left section button is pressed. The DID should change from 0 to 1 when the button is pressed.
N155772—UN—17MAY21

![[N155772.png]]
**Figure N155772**

Proper Battery Position Shown
If the address is not changing, verify that NODC DID 1306 matches the underlined number of the serial number of the remote control you are using. If the number matches, replace the CR2032 battery in the remote control. Ensure that the + side is facing down as shown in the photo above. Batteries should be replaced every season as they typically will last 6 months.
If the number does not match the underlined number or shows 999999999, the remote control must be paired. (See Remote Control Pairing Procedure in this section.)
Overview of Data Identifier (DID):
- NODC DID 1300—Section left check, button functionality; 0 = not pressed, 1 = pressed.
- NODC DID 1301—Section right check, button functionality; 0 = not pressed, 1 = pressed.
- NODC DID 1302—Nozzle left check, button functionality; 0 = not pressed, 1 = pressed.
- NODC DID 1303—Nozzle right check, button functionality; 0 = not pressed, 1 = pressed.
- NODC DID 1304—Enable check, button functionality; 0 = not pressed, 1 = pressed.
- NODC DID 1305—Stop check, button functionality; 0 = not pressed, 1 = pressed.
- NODC DID 1306—Remote control underlined serial number.
- NODC DID 1307—Pair Erase; 0 = pairing cmd none, 1 = pairing cmd pair, 2 = pairing cmd erase.
- NODC DID 1308—Pair Status
Status Codes
State | Name
0 | Pairing Disabled (not active /
conditions not met)
1 | Pairing Enabled (conditions met)
2 | Pairing Active (negotiating with
key fob)
3 | Pairing Failed
4 | Pairing Successful
5 | Max number of paired key fobs
exceeded
6 | Erase Failed
7 | Erase Successful
8 | Pairing Code entered doesn't
match key fob
9 | Pairing Code already exists
14 | Error / Invalid
15 | Unavailable / No Action
Remote Control Operation
Operate the remote control from behind the boom for best results. The buttons on the remote control function as follows:
N125203—UN—24AUG16

![[N125203.png]]
**Figure N125203** — A: Left-Hand Section ON Button; B: Right-Hand Section ON Button; C: Left-Hand Nozzle ON Button; D: Right-Hand Nozzle ON Button; E: Start Button; F: Stop Button

Remote Control
- Turn spray sections ON beginning with the right-hand most section and progressing across the boom to the left-hand side using left-hand section ON button (A).
- Turn spray sections ON beginning with the left-hand most section and progressing across the boom to the right-hand side using right-hand section ON button (B).
- Turn on the next available nozzle progressing from the right-hand side to the left-hand side of the boom using the left-hand nozzle ON button (C).
- Turn on the next available nozzle progressing from the left-hand side to the right-hand side of the boom using the right-hand nozzle ON button (D).
- Enable the remote system by pressing the start button (E) twice. Spray from the entire boom width by holding the start button for two seconds.
NOTE: Machine horn honks twice and all nozzle lights flash twice when the system is enabled.
- End nozzle tests by holding the stop button (F) for two seconds. Press the stop button once to pause spraying.
NOTE: Machine horn honks once and all nozzle lights flash once when the system is disabled.
The following conditions must be met before controlling the system with the remote control:
- Solution pump is ON.
- No remote loading operations are active.
- Machine is in park.
- Boom is unfolded.
NOTE: If any condition becomes not met during remote operation the system is disabled.
Example 1: Activate a Section then a Single Nozzle
NOTE: Only enabled nozzles are controlled when using the remote control.
All examples start from the left-hand side of the machine. The procedure is similar to start on the right-had side of the machine.
Machine horn honks twice and all nozzle lights flash twice when the system is enabled.
1. Press the start button twice.
N125209—UN—07SEP16

![[N125209.png]]
**Figure N125209** — A: Left-Hand Section; B: Left-Hand Nozzle

N125210—UN—07SEP16

![[N125210.png]]
**Figure N125210** — A: Left-Hand Section; B: Left-Hand Nozzle

2. Press right-hand section ON button, turning ON the left-hand most section (A) on the boom.
3. Press right-hand nozzle ON button, turning ON the left-hand most nozzle (B) on the next available section.
4. Press the stop button to pause spraying.
Example 2: Activate Single Nozzles then a Section
NOTE: Only enabled nozzles are controlled when using the remote control.
Machine horn honks twice and all nozzle lights flash twice when the system is enabled.
1. Press the start button twice.
N125211—UN—07SEP16

![[N125211.png]]
**Figure N125211** — A: Left-Hand Nozzle; B: Next Nozzle; C: Spray Section

N125212—UN—07SEP16

![[N125212.png]]
**Figure N125212** — A: Left-Hand Nozzle; B: Next Nozzle; C: Spray Section

N125213—UN—07SEP16

![[N125213.png]]
**Figure N125213** — A: Left-Hand Nozzle; B: Next Nozzle; C: Spray Section

2. Press right-hand nozzle ON button, turning ON the left-hand most nozzle (A) on the boom.
3. Press right-hand nozzle ON button again, turning ON the next available nozzle (B) to the right on the boom.
4. Press right-hand section ON button, turning ON the next available section (C).
5. Press the stop button to pause spraying.
Example 3: Activate All Nozzles
NOTE: Only enabled nozzles are controlled when using the remote control.
Machine horn honks twice and all nozzle lights flash twice when the system is enabled.
1. Press the start button twice.
N125214—UN—07SEP16

![[N125214.png]]
**Figure N125214**

All Sections ON
2. Press and hold the start button for more than one second to spray from the entire boom.
3. Release start button after spraying begins.
4. Press the stop button to pause spraying.

> Source: OMKK105338 p. 125-17, 125-18, 125-19, 125-20 · module ouo6092,1778242271722-19-12MAY26
