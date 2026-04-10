@echo off
REM Setup script for Intelligent Home Monitoring System Lab

echo.
echo ========================================
echo Intelligent Home Monitoring Lab Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version

echo.
echo Installing required packages...
echo.

pip install -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo [SUCCESS] Setup Complete!
echo ========================================
echo.
echo To run the system:
echo.
echo LAPTOP A (Camera Node) - Terminal 1:
echo   python app.py
echo.
echo LAPTOP B (AI Node) - Terminal 2:
echo   python yolo_stream.py
echo.
echo Make sure to update the IP address in yolo_stream.py first!
echo.
pause
