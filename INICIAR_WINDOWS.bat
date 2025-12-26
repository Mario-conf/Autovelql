@echo off
TITLE Autovelql Launcher

echo [LAUNCHER] Checking Environment...
powershell -NoProfile -ExecutionPolicy Bypass -File "src\scripts\windows\setup.ps1"

IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Setup failed or was cancelled.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [LAUNCHER] Starting Autovelql...
python src\main.py

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Application crashed or Python is not found.
    echo If you just installed Python, please close this window and run it again.
    pause
)
