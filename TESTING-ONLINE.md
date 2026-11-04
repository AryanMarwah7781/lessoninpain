# When you're back: the online test (about 20 minutes)

Already running on your PC: the Connections app (Sprayer 2019 screen, bridge connected), the virtual
armrest (`virtual-commandarm\SBMEmulator.exe`), and the simulator API with the test panel at
http://127.0.0.1:47900/ . If anything was closed: start `SBMEmulator.exe` first, then the app, open
Sprayer (2019), press **Connect to Simulator Bridge**, then `python -I run_simapi.py`.

1. **You:** press **Launch Machine Simulator** and sign in. Wait for the Gen 4 display.
2. **Me:** run the lesson check again, now online:
   `python -I lessons/check_lesson.py`. Online, the steps are also judged by what the cloud sends back
   (button lights, ground speed), not only by what the app sent.
3. **Together, on the display:**
   - Which way is forward on the lever (towards 250 or towards 0)? Watch the MPH on the corner post.
   - Do the button lights come on in the armrest window (Solution pump, Rate keys, Engine idle, Park brake)?
   - Does master spray change anything on the display once the pump is on and the machine moves?
   - Do boom height and the wings show on the display (BoomTrac panel)?
   - Do `/api/screens` find `display` and `pdu`, and do `/api/screen/display.png` and `/api/screen/pdu.png`
     return the right windows? (Offline only the main window exists.) Do the screen-map boxes still line up?
   - The app's CommandARM status lights (Buttons, Lever, ...) stayed grey with the virtual armrest connected. Why?
4. **You:** walk the lessons yourself in the test panel beside the display; press "Show me" when stuck.
   Six lessons now: field-ready (41 steps) plus the five scenarios (no-spray fault, headland HMS,
   obstacle, fold recovery, field zones). `POST /api/lesson/setup` puts the simulator in each one's start state.
5. **Decide:**
   - OK to add the live log stream to the app's `log4.config`? (`simapi/API.md` has the exact lines.)
   - Which steps marked "draft" are right for a real R4045 operator?
   - The other four lessons to write next.
   - When you have the FS25 `DeereVehicleControl` mod: we test fold/unfold in the game itself.
