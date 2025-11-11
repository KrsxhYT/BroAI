#!/usr/bin/env python3
"""
Audio Fix for BroAI
"""

import subprocess

def main():
    print("🔧 Fixing audio issues...")
    
    # Test TTS
    print("🔊 Testing speaker...")
    subprocess.run(["termux-tts-speak", "BroAI audio test"])
    
    # Test microphone
    print("🎤 Testing microphone...")
    subprocess.run(["termux-microphone-record", "-l", "3"], timeout=5)
    
    # Set volume
    print("🔈 Setting volume...")
    subprocess.run(["termux-volume", "music", "10"])
    
    print("✅ Audio fix complete!")

if __name__ == "__main__":
    main()
