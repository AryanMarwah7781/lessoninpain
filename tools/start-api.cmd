@echo off
rem Starts only the simulator API (in its own window), e.g. after an update while Lesson Studio stays open.
cd /d "%~dp0.."
call "%~dp0find-python.cmd" || (pause & exit /b 1)
start "Simulator API (Lesson Studio)" %PY% -I run_simapi.py --build aug26
