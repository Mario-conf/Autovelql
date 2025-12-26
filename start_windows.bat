@echo off
TITLE Autovelql Launcher
:: 1. Checking Environment...
echo [LAUNCHER] Checking Environment...
powershell -NoProfile -ExecutionPolicy Bypass -File "src\scripts\windows\setup.ps1"
:: 2. Checking Environment...
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Setup failed or was cancelled.
    pause
    exit /b %ERRORLEVEL%
)
:: 3. Starting Autovelql...
echo.
echo [LAUNCHER] Starting Autovelql...
python src\main.py
:: 4. Checking Autovelql...
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Application crashed or Python is not found.
    echo If you just installed Python, please close this window and run it again.
    pause
)
