@echo off
rem Starts Lesson Studio: the simulator API in its own window, then the lesson panel.
rem Close the "Simulator API" window to stop the API. For the R4045 on the Apr 20 app, change aug26 to apr20 below.
cd /d "%~dp0"
call "%~dp0tools\find-python.cmd" || (pause & exit /b 1)
rem the 612R lessons in the app's Operations panel: copies only what changed, keeps the app's own page
%PY% -I tools\operations_panel.py install
start "Simulator API (Lesson Studio)" %PY% -I run_simapi.py --build aug26
timeout /t 3 /nobreak >nul
rem the ready-built copy in dist (needs only the .NET 8 Desktop Runtime); else a local developer build
set LS=%~dp0dist\LessonStudio\LessonStudio.exe
if not exist "%LS%" set LS=%~dp0lesson-panel\bin\Debug\net8.0-windows\LessonStudio.exe
start "" "%LS%"
