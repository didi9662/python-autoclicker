@echo off
REM This batch file is used to install the Python AutoClicker
REM It will install the required packages and set up the environment
echo ====== Python AutoClicker Installer ======
echo.
echo 1. Install packages
echo 2. exit
set /p choice="Please select an option: "
if "%choice%"=="1" (
    echo Installing required packages...
    REM Install the required packages using pip
    pip install pyautogui
    echo Packages installed successfully.
    echo You can delete this installer after installation.
    echo Press any key to exit.
    pause >nul
    exit
) else (
    echo Exiting installer...
    timeout /t 5 >nul
    exit
)