@echo off
rem Sets the Aug 26 Connections app to use the real armrest box. Restart the app afterwards.
cd /d "%~dp0"
taskkill /im SBMEmulator.exe >nul 2>&1
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I tools\armrest_mode.py real
pause
