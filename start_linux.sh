#!/bin/bash

chmod +x src/scripts/linux/init.sh
# 1. Run Setup
./src/scripts/linux/init.sh

# 2. Check Setup
if [ $? -ne 0 ]; then
    echo "[ERROR] Setup failed."
    exit 1
fi

# 3. Activate VENV
VENV_PATH="src/scripts/venv/bin/activate"

if [ -f "$VENV_PATH" ]; then
    echo "[LAUNCHER] Activating virtual environment..."
    source "$VENV_PATH"
else
    echo "[LAUNCHER] Virtual environment not found at $VENV_PATH. Using system python..."
fi

# 4. Start Autovelql
echo "[LAUNCHER] Starting Autovelql..."
python3 src/main.py
