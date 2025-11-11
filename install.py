#!/usr/bin/env python3
"""
BroAI Installer
"""

import subprocess
import sys

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except:
        return False

def main():
    print("🚀 Installing BroAI...")
    
    # Update system
    print("📦 Updating system...")
    run_cmd("pkg update -y && pkg upgrade -y")
    
    # Install Python
    print("🐍 Installing Python...")
    run_cmd("pkg install python -y")
    
    # Install dependencies
    print("📚 Installing dependencies...")
    run_cmd("pkg install termux-api -y")
    
    # Install Python packages
    print("📥 Installing Python packages...")
    packages = [
        "pip install SpeechRecognition",
        "pip install pyttsx3", 
        "pip install wikipedia",
        "pip install requests",
        "pip install pygame"
    ]
    
    for pkg in packages:
        print(f"Installing {pkg}...")
        run_cmd(pkg)
    
    print("✅ Installation complete!")
    print("🎯 Run: python run.py")

if __name__ == "__main__":
    main()
