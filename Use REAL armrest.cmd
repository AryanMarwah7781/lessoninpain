@echo off
rem Sets the Aug 26 Connections app to use the real armrest box. Restart the app afterwards.
rem The app copy is found automatically (the running one, else Documents\jd_resources); or drop its folder on this file.
cd /d "%~dp0"
call "%~dp0tools\find-python.cmd" || (pause & exit /b 1)
taskkill /im SBMEmulator.exe >nul 2>&1
%PY% -I tools\armrest_mode.py real %1
pause
