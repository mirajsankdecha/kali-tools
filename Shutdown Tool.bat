@echo off
chcp 65001 > nul

echo.
echo.	 
echo     ╔═════════════════════════════════════════╗
echo     ║                                         ║
echo     ║          Miraj Sankdecha                ║
echo     ║                                         ║
echo     ╚═════════════════════════════════════════╝

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Error: This script requires administrator privileges. Please run it as an administrator.
    pause
    exit /b
)

echo.
echo Your PC's IP address:
ipconfig | findstr IPv4
echo.
echo List of IP addresses connected to the network:
arp -a
echo.

set /p ip=Enter the IP address of the Shutdown computer: 

if "%ip%"=="" (
    echo.
    echo Error: IP address not provided.
    pause
    exit /b
)

