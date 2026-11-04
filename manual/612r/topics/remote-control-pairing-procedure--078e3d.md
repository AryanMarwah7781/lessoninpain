---
module_id: ouo6092,1778242426931-19-11MAY26
title: Remote Control Pairing Procedure
section: ExactApply Nozzle Control System (If Equipped)
page_labels:
- 125-32
- 125-33
pdf_pages:
- 726
- 727
models:
- all
options:
- ExactApply
engine_tier: null
topic_type: procedure
components:
- battery
conditions: []
signal_words:
- NOTE
figures:
- N130599
generic: false
title_inferred: false
parent_module_id: null
---

# Remote Control Pairing Procedure

Remote control operation requires the remote control and receiver to be paired. The receiver stores up to six unique remote controls at a time. Remote controls can be added or removed from this registered list as needed when lost or replaced.
Once the remote control system is activated, the first two paired remotes to be used are allowed to control the system. If a different remote is to be used, then the key power must be cycled OFF then ON before activating the system with a different remote. Only two remotes can be active at a time.
NOTE: Only one remote control could be paired at a time. A key cycle is required for each additional pairing.
Pairing Procedure:
1. Turn the key switch to the run position.
2. Go to the Diagnostic Center and access the NODC Data Identifier (DID) 1306.
NOTE: “999999999” is displayed if a serial number has not been entered during the current power cycle.
N130599—UN—22MAY17

![[N130599.png]]
**Figure N130599** — A: Serial Number

3. Enter the underlined portion of the serial number (A) on the back of the remote control.
4. Advance to the NODC Data Identifier (DID) 1307.
5. Change the address value to one.
NOTE: The system allows the operator up to 2 minutes to complete the pairing process. Remote control needs to be moved closer to the receiver depending on the battery level and environment.
6. Advance to the NODC Data Identifier (DID) 1308. Observe the pairing progress. Possible pairing statuses include the following:
- Pairing disabled
- Pairing enabled
- Pairing active
- Pairing failed
- Pairing successful
- Max number of remote controls exceeded
- Erase Failed
- Erase Successful
- Pairing code entered does not match key fob
- Pairing Code already exists
- Error / Invalid
- Unavailable / No action
7. If the pairing fails, the key must be turned OFF before another attempt can be made. It is not necessary to turn OFF the key after a successful pairing function.
Erasing Procedure:
1. Turn the key switch to the run position.
2. Go to the Diagnostic Center and access the NODC Data Identifier (DID) 1306.
NOTE: “999999999” is displayed if a serial number has not been entered during the current power cycle.
Enter zero to erase all remote control pairs.
N130599—UN—22MAY17
3. Enter the underlined portion of the serial number (A) on the back of the remote control.
4. Advance to the NODC Data Identifier (DID) 1307.
5. Change the address value to two.
NOTE: The system allows the operator up to 2 minutes to complete the erasing process. Remote control needs to be moved closer to the receiver depending on the battery level and environment.
6. Advance to the NODC Data Identifier (DID) 1308. Observe the pairing progress. Possible pairing statuses include the following:
- Erase failed
- Erase successful
7. If erase fails, the key must be turned OFF before another attempt can be made. It will not be necessary to turn OFF the key after a successful erase function when there is any new remote controls that are to be paired. The operator must cycle the key when pairing a new remote control after erasing.

> Source: OMKK105338 p. 125-32, 125-33 · module ouo6092,1778242426931-19-11MAY26
