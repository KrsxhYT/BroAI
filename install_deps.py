#!/usr/bin/env python3
"""
BroAI Dependency Installer for Termux
"""

import os
import sys
import subprocess

def run_command(cmd):
    """Run system command and return success status"""
    try:
        subprocess.check_call(cmd, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_dependencies():
    print("🔧 Installing BroAI Dependencies...")
    
    # Update package list
    print("📦 Updating package list...")
    run_command("pkg update -y && pkg upgrade -y")
    
    # Install Python and required packages
    print("🐍 Installing Python...")
    run_command("pkg install python -y")
    
    # Install system dependencies
    print("📚 Installing system dependencies...")
    run_command("pkg install libjpeg-turbo libpng -y")
    
    # Install Python packages
    print("🚀 Installing Python packages...")
    packages = [
        "pip install SpeechRecognition",
        "pip install pyttsx3", 
        "pip install wikipedia",
        "pip install requests"
    ]
    
    for package in packages:
        print(f"📥 Installing {package}...")
        if not run_command(package):
            print(f"❌ Failed to install {package}")
    
    print("✅ Installation completed!")
    print("\n🎯 Now you can run: python run.py")

if __name__ == "__main__":
    install_dependencies()
