import speech_recognition as sr
from core.speaker import speak

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)
        return query.lower()
    except:
        speak("Sorry, I didn’t catch that.")
        return ""
