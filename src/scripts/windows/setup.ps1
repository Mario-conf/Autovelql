# 0. Check for Administrator permissions
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "Administrator permissions are required to verify the environment." -ForegroundColor Yellow
    Write-Host "Restarting script as Administrator..." -ForegroundColor Yellow
    Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

Write-Host "--- ENVIRONMENT CHECK ---" -ForegroundColor Cyan

$scriptsDir = Split-Path -Parent $PSScriptRoot
$requirementsFile = Join-Path $scriptsDir "requirements\requirements.txt"


# 1. DOCKER VERIFICATION AND STARTUP

Write-Host "Verifying Docker status..."
try {
    docker --version | Out-Null
    docker info | Out-Null
    
    if ($?) {
        Write-Host "Docker is running correctly." -ForegroundColor Green
    }
    else {
        
        Write-Host "Docker is installed but STOPPED." -ForegroundColor Yellow
        Write-Host "Attempting to start Docker Desktop automatically..." -ForegroundColor Cyan
        
        $dockerPath = "C:\Program Files\Docker\Docker\Docker Desktop.exe"
        
        if (Test-Path $dockerPath) {
            Start-Process -FilePath $dockerPath
            Write-Host "Starting Docker... Waiting 20 seconds for engine startup..." -ForegroundColor Yellow
            
            $retry = 0
            while ($retry -lt 15) {
                Start-Sleep -Seconds 2
                docker info 2>$null | Out-Null
                if ($?) {
                    Write-Host "Docker started successfully!" -ForegroundColor Green
                    break
                }
                Write-Host "." -NoNewline
                $retry++
            }
            Write-Host "" 
            
            if (-not $?) {
                Write-Host "Docker is taking too long to start. Please wait until the whale icon stops animating and try again." -ForegroundColor Red
                Read-Host "Press Enter to exit"
                exit
            }
        }
        else {
            Write-Host "Cannot find Docker executable in standard path." -ForegroundColor Red
            Write-Host "Please open Docker Desktop manually."
            Read-Host "Press Enter to exit"
            exit
        }
    }
}
catch {
    Write-Host "ERROR: Docker does not appear to be installed." -ForegroundColor Red
    Write-Host "Opening download page..."
    Start-Process "https://www.docker.com/products/docker-desktop/"
    Read-Host "Press Enter to exit"
    exit
}


# 2. PYTHON VERIFICATION

try {
    python --version | Out-Null
    Write-Host "Python is already installed." -ForegroundColor Green
}
catch {
    Write-Host "Python NOT detected. Starting automatic installation..." -ForegroundColor Yellow
    $url = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
    $output = "$PWD\python_installer.exe"
    
    Write-Host "Downloading Python..."
    Invoke-WebRequest -Uri $url -OutFile $output
    
    Write-Host "Installing Python..."
    Start-Process -FilePath $output -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    Remove-Item $output
    
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}


# 3. INSTALL DEPENDENCIES

Write-Host "Verifying libraries..." -ForegroundColor Cyan
python -m pip install --upgrade pip | Out-Null

if (Test-Path $requirementsFile) {
    pip install -r $requirementsFile | Out-Null
}
else {
    Write-Host "Installing CustomTkinter..."
    pip install customtkinter | Out-Null
}


# 4. FINISH

Write-Host "----------------------------------------"
Write-Host "SUCCESS: Environment is ready." -ForegroundColor Green
Read-Host "Press Enter to close"
