@echo off
rem Starts Lesson Studio for the 612R (Aug 26 build): the simulator API in its own window, then the lesson panel.
rem Close the "Simulator API" window to stop the API.
cd /d "%~dp0"
set PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe
if not exist "%PY%" set PY=python
start "Simulator API (Lesson Studio)" "%PY%" -I run_simapi.py --build aug26
timeout /t 3 /nobreak >nul
rem the ready-built copy in dist (needs only the .NET 8 Desktop Runtime); else a local developer build
set LS=%~dp0dist\LessonStudio\LessonStudio.exe
if not exist "%LS%" set LS=%~dp0lesson-panel\bin\Debug\net8.0-windows\LessonStudio.exe
start "" "%LS%"
