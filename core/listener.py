import speech_recognition as sr
from core.speaker import speaker

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        try:
            self.microphone = sr.Microphone()
            print("🎤 Microphone initialized")
        except:
            print("❌ Microphone not available, using text input")
            self.microphone = None

    def listen_with_mic(self):
        """Listen using microphone"""
        try:
            with self.microphone as source:
                print("\n🎙 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=10)
            
            query = self.recognizer.recognize_google(audio, language="en-in")
            print(f"👤 You said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            speaker.speak("I didn't hear anything. Please try again.")
            return ""
        except sr.UnknownValueError:
            speaker.speak("Sorry, I couldn't understand that.")
            return ""
        except Exception as e:
            print(f"❌ Mic error: {e}")
            return ""

    def listen_with_text(self):
        """Fallback: Listen using text input"""
        try:
            query = input("\n📝 Type your command: ").strip()
            return query.lower()
        except:
            return ""

    def listen(self):
        if self.microphone:
            return self.listen_with_mic()
        else:
            return self.listen_with_text()

# Global instance
listener = Listener()
