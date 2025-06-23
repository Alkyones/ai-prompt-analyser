#!/bin/bash
# Setup script for AI Prompt Analyzer (macOS/Linux)

echo "=== AI Prompt Analyzer Setup (macOS/Linux) ==="
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.7+ from your package manager or https://python.org"
    exit 1
fi

echo "Python found!"
python3 --version

# Create virtual environment
echo
echo "Creating virtual environment..."
if [ -d "ai-prompt-env" ]; then
    echo "Virtual environment already exists"
else
    python3 -m venv ai-prompt-env
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment"
        echo "Try installing python3-venv: sudo apt-get install python3-venv (Ubuntu/Debian)"
        exit 1
    fi
    echo "Virtual environment created successfully!"
fi

# Activate virtual environment and install dependencies
echo
echo "Installing dependencies..."
source ai-prompt-env/bin/activate
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Failed to install dependencies"
    exit 1
fi

# Test installation
echo
echo "Testing installation..."
python main.py --help > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Warning: Installation test failed"
else
    echo "Installation test passed!"
fi

echo
echo "=== Setup Complete! ==="
echo
echo "To use the application:"
echo "  1. Activate virtual environment: source ai-prompt-env/bin/activate"
echo "  2. Run the application: python main.py --interactive"
echo "  3. When done, deactivate: deactivate"
echo
echo "Quick start: source ai-prompt-env/bin/activate && python main.py --interactive"
echo
