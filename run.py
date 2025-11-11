#!/usr/bin/env python3
"""
BroAI - Voice Assistant
"""

from core.listener import listener
from core.brain import brain
from core.speaker import speaker

def main():
    print("🤖 BroAI Starting...")
    speaker.speak(f"Hello {brain.user}! BroAI is ready!")
    
    while True:
        query = listener.listen()
        
        if query:
            result = brain.handle_command(query)
            if result == "exit":
                break

if __name__ == "__main__":
    main()
