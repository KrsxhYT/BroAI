import os
import random
import webbrowser
import wikipedia
from datetime import datetime
from core.speaker import speak

def play_music():
    music_folder = "/sdcard/Music"  # change if needed
    try:
        songs = os.listdir(music_folder)
        if not songs:
            speak("No songs found in music folder.")
            return
        song = random.choice(songs)
        speak(f"Playing {song}")
        os.system(f"termux-media-player play '{music_folder}/{song}'")
    except:
        speak("Unable to play music right now.")

def tell_time():
    now = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def tell_date():
    today = datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def search_wikipedia(query):
    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        speak("Sorry, I couldn't find anything on Wikipedia.")

def google_search(query):
    speak("Searching Google...")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def open_website(site):
    if "youtube" in site:
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")
    elif "instagram" in site:
        speak("Opening Instagram...")
        webbrowser.open("https://instagram.com")
    elif "google" in site:
        speak("Opening Google...")
        webbrowser.open("https://google.com")
    else:
        speak(f"Opening {site}")
        webbrowser.open(f"https://{site}.com")
