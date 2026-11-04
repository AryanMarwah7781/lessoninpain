@echo off
rem Sets the Aug 26 Connections app to use the virtual armrest and starts it. Restart the app afterwards.
cd /d "%~dp0"
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I tools\armrest_mode.py virtual
tasklist /fi "imagename eq SBMEmulator.exe" | find /i "SBMEmulator.exe" >nul || start "" /d "%~dp0virtual-commandarm" "%~dp0virtual-commandarm\SBMEmulator.exe"
pause
