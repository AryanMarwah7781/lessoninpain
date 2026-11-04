@echo off
rem Lesson Studio setup (README steps 1-4). Options: -Armrest virtual   -AppFolder "<folder>"   -SkipMods   -NoShortcut
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup.ps1" %*
echo.
pause
