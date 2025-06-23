#!/usr/bin/env python3
"""
Setup script for AI Prompt Analyzer and Optimizer
Automates virtual environment creation and dependency installation
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


def run_command(command, check=True):
    """Run a command and handle errors"""
    try:
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, check=check, 
                              capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error output: {e.stderr}")
        return None


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("Error: Python 3.7 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"Python version: {version.major}.{version.minor}.{version.micro} ✓")
    return True


def create_virtual_environment():
    """Create virtual environment"""
    env_name = "ai-prompt-env"
    
    if os.path.exists(env_name):
        print(f"Virtual environment '{env_name}' already exists")
        return env_name
    
    print(f"Creating virtual environment: {env_name}")
    result = run_command(f"python -m venv {env_name}")
    
    if result and result.returncode == 0:
        print(f"Virtual environment created successfully ✓")
        return env_name
    else:
        print("Failed to create virtual environment")
        return None


def get_activation_command(env_name):
    """Get the activation command for the current OS"""
    system = platform.system().lower()
    
    if system == "windows":
        return f"{env_name}\\Scripts\\activate"
    else:
        return f"source {env_name}/bin/activate"


def install_dependencies(env_name):
    """Install project dependencies"""
    system = platform.system().lower()
    
    if system == "windows":
        pip_path = f"{env_name}\\Scripts\\pip"
    else:
        pip_path = f"{env_name}/bin/pip"
    
    print("Installing dependencies...")
    result = run_command(f"{pip_path} install -r requirements.txt")
    
    if result and result.returncode == 0:
        print("Dependencies installed successfully ✓")
        return True
    else:
        print("Failed to install dependencies")
        return False


def test_installation(env_name):
    """Test if installation was successful"""
    system = platform.system().lower()
    
    if system == "windows":
        python_path = f"{env_name}\\Scripts\\python"
    else:
        python_path = f"{env_name}/bin/python"
    
    print("Testing installation...")
    result = run_command(f"{python_path} main.py --help", check=False)
    
    if result and result.returncode == 0:
        print("Installation test passed ✓")
        return True
    else:
        print("Installation test failed")
        return False


def main():
    """Main setup function"""
    print("=== AI Prompt Analyzer Setup ===")
    print()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    env_name = create_virtual_environment()
    if not env_name:
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies(env_name):
        sys.exit(1)
    
    # Test installation
    if not test_installation(env_name):
        print("Warning: Installation test failed, but setup may still work")
    
    # Print success message
    print()
    print("=== Setup Complete! ===")
    print()
    print("To activate the virtual environment:")
    print(f"  {get_activation_command(env_name)}")
    print()
    print("To run the application:")
    print("  python main.py --interactive")
    print("  python main.py --help")
    print()
    print("To deactivate the virtual environment:")
    print("  deactivate")
    print()


if __name__ == "__main__":
    main()
