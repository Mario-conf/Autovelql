@echo off
:: 0. Bypass security restrictions

echo Starting IDE installer...
echo Please, if asked for Administrator permissions, accept to install dependencies.
:: 1. Executes the PowerShell script in Bypass mode 
PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& './setup.ps1'"

pause
