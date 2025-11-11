import pyttsx3

class Speaker:
    def __init__(self):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 175)
            self.engine.setProperty('volume', 1.0)
            print("🔊 Speaker initialized successfully")
        except Exception as e:
            print(f"❌ Speaker init error: {e}")
            self.engine = None

    def speak(self, text):
        print(f"🤖 Assistant: {text}")
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"❌ Speech error: {e}")
        else:
            print(f"📝 [TTS]: {text}")

# Global instance
speaker = Speaker()
