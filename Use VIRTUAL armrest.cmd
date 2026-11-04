@echo off
rem Sets the Aug 26 Connections app to use the virtual armrest and starts it. Restart the app afterwards.
rem The app copy is found automatically (the running one, else Documents\jd_resources); or drop its folder on this file.
cd /d "%~dp0"
call "%~dp0tools\find-python.cmd" || (pause & exit /b 1)
%PY% -I tools\armrest_mode.py virtual %1
tasklist /fi "imagename eq SBMEmulator.exe" | find /i "SBMEmulator.exe" >nul || start "" /d "%~dp0virtual-commandarm" "%~dp0virtual-commandarm\SBMEmulator.exe"
pause
