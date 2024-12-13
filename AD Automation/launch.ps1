# Check if Python is installed
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Output "Python is not installed. Installing Python..."
    $pythonInstallerUrl = "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe"
    $pythonInstallerPath = "$env:TEMP\python-installer.exe"
    Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $pythonInstallerPath

    # Run the installer
    Start-Process -FilePath $pythonInstallerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

    # Clean up
    Remove-Item -Path $pythonInstallerPath

    # Refresh environment variables
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)

    # Verify installation
    $python = Get-Command python -ErrorAction SilentlyContinue
    if (-not $python) {
        Write-Error "Python installation failed."
        exit 1
    }
}

# Check if virtual environment exists
if (-Not (Test-Path -Path "./venv")) {
    Write-Output "Setting up virtual environment..."
    python -m venv venv
}

# Activate the virtual environment
$venvActivate = Join-Path -Path "./venv/Scripts" -ChildPath "Activate.ps1"
if (Test-Path -Path $venvActivate) {
    & $venvActivate
} else {
    Write-Error "Failed to activate the virtual environment."
    exit 1
}

# Install required packages (if any)
# python -m pip install -r requirements.txt

# Add the current directory to the Python path
$env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"

# Prompt the user to select a function to run
Write-Output "Select a function to run from AD_functions.py:"
Write-Output "1. get_highest_uidNumber"
Write-Output "2. get_users_with_blank_uidNumber"
Write-Output "3. create_ad_user"
Write-Output "4. add_user_to_ad"

$selection = Read-Host "Enter the number of the function you want to run"

switch ($selection) {
    1 {
        Write-Output "Running get_highest_uidNumber..."
        python -c "from AD_functions import get_highest_uidNumber; print(get_highest_uidNumber())"
    }
    2 {
        Write-Output "Running get_users_with_blank_uidNumber..."
        python -c "from AD_functions import get_users_with_blank_uidNumber; print(get_users_with_blank_uidNumber([]))"
    }
    3 {
        Write-Output "Running create_ad_user..."
        python -c "from AD_functions import create_ad_user; create_ad_user()"
    }
    4 {
        Write-Output "Running add_user_to_ad..."
        python -c "from AD_functions import add_user_to_ad; add_user_to_ad({})"
    }
    default {
        Write-Output "Invalid selection."
    }
}

# Deactivate the virtual environment
deactivate
