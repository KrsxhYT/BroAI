import speech_recognition as sr
from core.speaker import speaker

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.setup_microphone()
    
    def setup_microphone(self):
        try:
            self.mic = sr.Microphone()
            with self.mic as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("✅ Microphone ready")
        except:
            print("❌ Microphone not available")
            self.mic = None
    
    def listen(self):
        if not self.mic:
            return self.text_input()
        
        try:
            with self.mic as source:
                print("\n🎤 Listening...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)
            
            query = self.recognizer.recognize_google(audio, language='en-in')
            print(f"👤 You said: {query}")
            return query.lower()
        
        except sr.UnknownValueError:
            speaker.speak("Sorry, couldn't understand")
            return ""
        except sr.RequestError:
            speaker.speak("Check internet connection")
            return ""
        except sr.WaitTimeoutError:
            speaker.speak("I didn't hear anything")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return self.text_input()
    
    def text_input(self):
        try:
            query = input("\n📝 Type command: ").strip()
            return query.lower() if query else ""
        except:
            return ""

listener = Listener()
