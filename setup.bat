@echo off
REM Setup script for AI Prompt Analyzer (Windows)

echo === AI Prompt Analyzer Setup (Windows) ===
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo Python found!
python --version

REM Create virtual environment
echo.
echo Creating virtual environment...
if exist ai-prompt-env (
    echo Virtual environment already exists
) else (
    python -m venv ai-prompt-env
    if errorlevel 1 (
        echo Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
)

REM Activate virtual environment and install dependencies
echo.
echo Installing dependencies...
call ai-prompt-env\Scripts\activate.bat && pip install -r requirements.txt

if errorlevel 1 (
    echo Failed to install dependencies
    pause
    exit /b 1
)

REM Test installation
echo.
echo Testing installation...
call ai-prompt-env\Scripts\activate.bat && python main.py --help > nul

if errorlevel 1 (
    echo Warning: Installation test failed
) else (
    echo Installation test passed!
)

echo.
echo === Setup Complete! ===
echo.
echo To use the application:
echo   1. Activate virtual environment: ai-prompt-env\Scripts\activate
echo   2. Run the application: python main.py --interactive
echo   3. When done, deactivate: deactivate
echo.
echo Quick start: ai-prompt-env\Scripts\activate ^&^& python main.py --interactive
echo.
pause
