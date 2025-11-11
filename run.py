#!/usr/bin/env python3
"""
BroAI - Voice Assistant
Author: Krsxh
"""

from core.listener import listener
from core.brain import brain
from core.speaker import speaker
import sys
import time

def show_banner():
    banner = """
    🤖 BRO AI - Voice Assistant
    🎤 Say 'exit' to quit
    🔊 Speak clearly for better recognition
    """
    print(banner)

def main():
    show_banner()
    
    try:
        speaker.speak(f"Hey {brain.user_name}! Bro AI is now online and ready to help!")
        
        while True:
            query = listener.listen()
            
            if query:
                result = brain.handle_command(query)
                if result == "exit":
                    break
            
            # Small delay between commands
            time.sleep(1)
                
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down Bro AI...")
        speaker.speak("Goodbye! Bro AI signing off.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        speaker.speak("There was an unexpected error. Restarting might help.")

if __name__ == "__main__":
    main()
