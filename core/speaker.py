import pyttsx3
import subprocess
import platform

class Speaker:
    def __init__(self):
        self.engine = None
        self.init_engine()
    
    def init_engine(self):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 170)
            self.engine.setProperty('volume', 1.0)
            print("✅ Speaker initialized")
        except:
            print("❌ Pyttsx3 failed, using fallback")
            self.engine = None
    
    def speak(self, text):
        print(f"🤖 Assistant: {text}")
        try:
            if self.engine:
                self.engine.say(text)
                self.engine.runAndWait()
            else:
                self.fallback_speak(text)
        except:
            self.fallback_speak(text)
    
    def fallback_speak(self, text):
        try:
            subprocess.run(['termux-tts-speak', text], check=False)
        except:
            print(f"💬 {text}")

speaker = Speaker()
