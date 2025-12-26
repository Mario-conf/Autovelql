#!/bin/bash

# 0. COLORS
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' 

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REQUIREMENTS_FILE="$SCRIPTS_DIR/requirements/requirements.txt"

echo -e "${GREEN}--- ENVIRONMENT LAUNCHER ---${NC}"

command_exists() {
	command -v "$1" >/dev/null 2>&1
}

# 1. CHECK DOCKER
if command_exists docker; then
    echo -e "[OK] Docker detected."
    if ! docker info > /dev/null 2>&1; then
        echo -e "${YELLOW}[WARNING] Docker is installed but stopped. Please start Docker Desktop/Service.${NC}"
        read -p "Press Enter to exit..."
        exit 1
    fi
else
    echo -e "${RED}[ERROR] Docker is not installed.${NC}"
    exit 1
fi

# 2. CHECK PYTHON & VENV SUPPORT
echo -e "[INFO] Checking Python environment..."

if [ -f /etc/debian_version ]; then
    python3 -m venv test_env_check > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo -e "${YELLOW}[WARNING] Python Full environment missing. Installing...${NC}"
        echo "   (You will be asked for sudo password)"
        sudo apt update
        sudo apt install -y python3-full python3-pip
        rm -rf test_env_check
    else
        rm -rf test_env_check
    fi
fi

# 3. CREATE VIRTUAL ENVIRONMENT
cd "$SCRIPTS_DIR"

if [ ! -d "venv" ]; then
    echo -e "[INFO] Creating virtual environment (venv)..."
    python3 -m venv venv
    
    if [ ! -d "venv" ]; then
        echo -e "${RED}[ERROR] Failed to create 'venv' folder.${NC}"
        echo "   Please run: 'sudo apt install python3-full' manually and try again."
        exit 1
    fi
fi

# 4. ACTIVATE VENV & INSTALL
echo -e "[INFO] Activating venv..."
source venv/bin/activate

if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo -e "${RED}[ERROR] Could not activate virtual environment.${NC}"
    exit 1
fi

echo -e "[INFO] Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1

if [ -f "$REQUIREMENTS_FILE" ]; then
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "   (Installing CustomTkinter default)"
    pip install customtkinter
fi

echo -e "----------------------------------------"
echo -e "${GREEN}SUCCESS: Environment is ready.${NC}"
read -p "Press Enter to exit..."
