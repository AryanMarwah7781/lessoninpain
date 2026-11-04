@echo off
rem Sets PY to a Python 3 to run the simulator API with (standard library only, 3.10 or newer).
set PY=
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set PY="%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if not defined PY (where py >nul 2>&1 && set PY=py -3)
if not defined PY (where python >nul 2>&1 && set PY=python)
if not defined PY (
  echo Python 3 was not found. Install it with:  winget install --id Python.Python.3.12 -e
  exit /b 1
)
exit /b 0
