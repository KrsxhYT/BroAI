from core.speaker import speaker
from core.utils import utils

class Brain:
    def __init__(self):
        self.user = "Krsxh"
    
    def handle_command(self, query):
        if not query:
            return
        
        query = query.lower()
        
        # Exit
        if any(word in query for word in ['exit', 'stop', 'quit', 'bye']):
            speaker.speak(f"Goodbye {self.user}!")
            return "exit"
        
        # Greetings
        elif any(word in query for word in ['hello', 'hi', 'hey']):
            speaker.speak(f"Hello {self.user}! How can I help?")
        
        # How are you
        elif 'how are you' in query:
            speaker.speak("I'm awesome! Ready to help you!")
        
        # Time
        elif 'time' in query:
            utils.tell_time()
        
        # Date
        elif 'date' in query:
            utils.tell_date()
        
        # Music
        elif any(phrase in query for phrase in ['play music', 'play song']):
            utils.play_music()
        
        # Stop music
        elif 'stop music' in query:
            utils.stop_music()
        
        # Wikipedia
        elif 'wikipedia' in query:
            topic = query.replace('wikipedia', '').replace('search', '').strip()
            if topic:
                utils.search_wikipedia(topic)
            else:
                speaker.speak("What should I search on Wikipedia?")
        
        # Google
        elif 'google' in query:
            topic = query.replace('google', '').replace('search', '').strip()
            if topic:
                utils.google_search(topic)
            else:
                speaker.speak("What should I search on Google?")
        
        # Open website
        elif 'open' in query:
            site = query.replace('open', '').strip()
            if site:
                utils.open_website(site)
            else:
                speaker.speak("Which website should I open?")
        
        # Joke
        elif 'joke' in query:
            utils.tell_joke()
        
        else:
            speaker.speak("I didn't understand that command")

brain = Brain()
