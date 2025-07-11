import os
import openai
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import random

# ========== CONFIG ==========
openai.api_key = os.getenv("OPENAI_API_KEY")

# ========== TEXT-TO-SPEECH ==========
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(f"Bro AI: {audio}")
    engine.say(audio)
    engine.runAndWait()

# ========== GREETING BASED ON TIME ==========
def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning sir, I am your assistant Bro AI")
    elif hour < 18:
        speak("Good afternoon sir, I am your assistant Bro AI")
    else:
        speak("Good evening sir, I am your assistant Bro AI")

# ========== SPEECH RECOGNITION ==========
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en-in')
        print(f"You said: {text}")
        return text.lower()
    except Exception:
        speak("Sorry, I didn't catch that")
        return "none"

# ========== CHATGPT INTEGRATION ==========
def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Bro AI, an advanced personal assistant with emotional intelligence and humor."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response['choices'][0]['message']['content']
        speak(reply)
    except Exception as e:
        print("OpenAI API Error:", e)
        speak("Sorry, I had a problem thinking about that.")

# ========== SMART TASK HANDLER ==========
def handle_task(query):
    if 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif 'open github' in query:
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub")
    elif 'open facebook' in query:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif 'open instagram' in query:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif 'open gmail' in query:
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail")
    elif 'open amazon' in query:
        webbrowser.open("https://www.amazon.com")
        speak("Opening Amazon")
    elif 'open flipkart' in query:
        webbrowser.open("https://www.flipkart.com")
        speak("Opening Flipkart")

    elif 'music from pc' in query or "play music" in query:
        music_dir = './music'
        musics = os.listdir(music_dir)
        if musics:
            speak("Playing your music")
            os.startfile(os.path.join(music_dir, random.choice(musics)))
        else:
            speak("No music found in the folder")

    elif 'video from pc' in query or "play video" in query:
        video_dir = './video'
        videos = os.listdir(video_dir)
        if videos:
            speak("Playing your video")
            os.startfile(os.path.join(video_dir, random.choice(videos)))
        else:
            speak("No video found in the folder")

    elif 'time' in query:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Sir, the time is {time_now}")

    elif 'shutdown' in query:
        speak("Shutting down system")
        os.system('shutdown /s /t 1')

    elif any(word in query for word in ['exit', 'quit', 'bye', 'stop', 'abort']):
        speak("Goodbye! Take care.")
        exit()

    else:
        chat_with_gpt(query)

# ========== MAIN LOOP ==========
if __name__ == "__main__":
    wish()
    while True:
        query = takecom()
        if query != "none":
            handle_task(query)
