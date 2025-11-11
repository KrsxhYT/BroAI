import os
import random
import webbrowser
import wikipedia
from datetime import datetime
from core.speaker import speaker

class Utils:
    def __init__(self):
        wikipedia.set_lang("en")
    
    def play_music(self):
        music_dirs = ['/sdcard/Music', '/storage/emulated/0/Music', './music']
        
        for music_dir in music_dirs:
            if os.path.exists(music_dir):
                try:
                    songs = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]
                    if songs:
                        song = random.choice(songs)
                        speaker.speak(f"Playing {os.path.splitext(song)[0]}")
                        os.system(f"termux-media-player play '{os.path.join(music_dir, song)}'")
                        return
                except:
                    pass
        
        speaker.speak("No music found")
    
    def stop_music(self):
        os.system("termux-media-player stop")
    
    def tell_time(self):
        time_str = datetime.now().strftime("%I:%M %p")
        speaker.speak(f"It's {time_str}")
    
    def tell_date(self):
        date_str = datetime.now().strftime("%B %d, %Y")
        speaker.speak(f"Today is {date_str}")
    
    def search_wikipedia(self, query):
        try:
            speaker.speak("Searching Wikipedia")
            result = wikipedia.summary(query, sentences=2)
            speaker.speak(result)
        except:
            speaker.speak("No Wikipedia results")
    
    def google_search(self, query):
        speaker.speak("Searching Google")
        webbrowser.open(f"https://google.com/search?q={query}")
    
    def open_website(self, site):
        sites = {
            'youtube': 'https://youtube.com',
            'instagram': 'https://instagram.com',
            'google': 'https://google.com',
            'github': 'https://github.com',
            'facebook': 'https://facebook.com',
            'whatsapp': 'https://web.whatsapp.com'
        }
        
        site = site.lower()
        for name, url in sites.items():
            if name in site:
                speaker.speak(f"Opening {name}")
                webbrowser.open(url)
                return
        
        speaker.speak(f"Opening {site}")
        webbrowser.open(f"https://{site}.com")
    
    def tell_joke(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why don't eggs tell jokes? They'd crack each other up!"
        ]
        speaker.speak(random.choice(jokes))

utils = Utils()
