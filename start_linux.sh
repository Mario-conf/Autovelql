#!/bin/bash

# 1. Ensure script is executable
chmod +x src/scripts/linux/init.sh

# 2. Run Setup
./src/scripts/linux/init.sh

if [ $? -ne 0 ]; then
    echo "[ERROR] Setup failed."
    exit 1
fi

# 3. Determine VENV path 
VENV_PATH="src/scripts/venv/bin/activate"

if [ -f "$VENV_PATH" ]; then
    echo "[LAUNCHER] Activating virtual environment..."
    source "$VENV_PATH"
else
    echo "[LAUNCHER] Virtual environment not found at $VENV_PATH. Using system python..."
fi

echo "[LAUNCHER] Starting Autovelql..."
python3 src/main.py
