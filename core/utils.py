import os
import random
import webbrowser
import wikipedia
import requests
from datetime import datetime
from core.speaker import speaker

class Utils:
    def __init__(self):
        wikipedia.set_lang("en")
        self.music_folders = [
            "/sdcard/Music",
            "/storage/emulated/0/Music",
            "./music"  # Local folder
        ]

    def find_music_folder(self):
        """Find available music folder"""
        for folder in self.music_folders:
            if os.path.exists(folder):
                return folder
        return None

    def play_music(self):
        try:
            music_folder = self.find_music_folder()
            if not music_folder:
                speaker.speak("No music folder found. Please check your music directory.")
                return

            songs = [f for f in os.listdir(music_folder) 
                    if f.endswith(('.mp3', '.wav', '.m4a', '.ogg'))]
            
            if not songs:
                speaker.speak("No songs found in music folder.")
                return
                
            song = random.choice(songs)
            song_name = os.path.splitext(song)[0]
            speaker.speak(f"Playing {song_name}")
            
            # For Termux
            os.system(f"termux-media-player play '{os.path.join(music_folder, song)}'")
            
        except Exception as e:
            speaker.speak("Unable to play music right now.")
            print(f"❌ Music error: {e}")

    def stop_music(self):
        try:
            os.system("termux-media-player stop")
            speaker.speak("Music stopped")
        except:
            pass

    def tell_time(self):
        now = datetime.now().strftime("%I:%M %p")
        speaker.speak(f"The time is {now}")

    def tell_date(self):
        today = datetime.now().strftime("%B %d, %Y")
        speaker.speak(f"Today's date is {today}")

    def search_wikipedia(self, query):
        try:
            speaker.speak("Searching Wikipedia...")
            result = wikipedia.summary(query, sentences=2)
            speaker.speak("According to Wikipedia: " + result)
        except wikipedia.exceptions.DisambiguationError:
            speaker.speak("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speaker.speak("Sorry, I couldn't find anything on Wikipedia.")
        except Exception as e:
            speaker.speak("Error searching Wikipedia.")
            print(f"❌ Wikipedia error: {e}")

    def google_search(self, query):
        try:
            speaker.speak("Searching Google...")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        except Exception as e:
            speaker.speak("Unable to open browser.")
            print(f"❌ Browser error: {e}")

    def open_website(self, site):
        sites = {
            "youtube": "https://youtube.com",
            "instagram": "https://instagram.com", 
            "google": "https://google.com",
            "github": "https://github.com",
            "facebook": "https://facebook.com",
            "whatsapp": "https://web.whatsapp.com",
            "twitter": "https://twitter.com"
        }
        
        site = site.lower().strip()
        for key, url in sites.items():
            if key in site:
                speaker.speak(f"Opening {key}")
                webbrowser.open(url)
                return
        
        # Default case
        speaker.speak(f"Opening {site}")
        webbrowser.open(f"https://{site}.com")

    def tell_joke(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!"
        ]
        joke = random.choice(jokes)
        speaker.speak(joke)

    def system_info(self):
        import platform
        system = platform.system()
        speaker.speak(f"You are running {system} system")

# Global instance
utils = Utils()
