from core.speaker import speaker
from core.utils import utils

class Brain:
    def __init__(self):
        self.user_name = "Krsxh"
        self.setup_commands()

    def setup_commands(self):
        self.commands = {
            "time": utils.tell_time,
            "date": utils.tell_date,
            "music": utils.play_music,
            "song": utils.play_music,
            "stop music": utils.stop_music,
            "joke": utils.tell_joke,
            "system info": utils.system_info
        }

    def handle_command(self, query):
        if not query or query.strip() == "":
            return

        query = query.lower().strip()
        print(f"🧠 Processing: {query}")

        # Exit commands
        if any(word in query for word in ["exit", "stop", "quit", "goodbye", "bye"]):
            speaker.speak(f"Goodbye {self.user_name}, see you later!")
            return "exit"

        # Greetings
        if any(word in query for word in ["hello", "hi", "hey"]):
            speaker.speak(f"Hello {self.user_name}! Ready for some action?")
            return

        # How are you
        elif "how are you" in query:
            responses = [
                "I'm always running smoothly, thanks for asking!",
                "Doing great! Ready to help you!",
                "I'm awesome! What can I do for you?"
            ]
            import random
            speaker.speak(random.choice(responses))
            return

        # Name query
        elif "your name" in query:
            speaker.speak("I'm BroAI, your personal assistant!")
            return

        # Direct command matching
        for command, function in self.commands.items():
            if command in query:
                function()
                return

        # Wikipedia search
        if "wikipedia" in query:
            topic = self.extract_topic(query, ["search", "wikipedia", "on"])
            if topic:
                utils.search_wikipedia(topic)
            else:
                speaker.speak("What would you like me to search on Wikipedia?")
            return

        # Google search
        elif "google" in query:
            topic = self.extract_topic(query, ["search", "google", "on"])
            if topic:
                utils.google_search(topic)
            else:
                speaker.speak("What would you like me to search on Google?")
            return

        # Open websites
        elif "open" in query:
            site = query.replace("open", "").strip()
            if site:
                utils.open_website(site)
            else:
                speaker.speak("Which website would you like me to open?")
            return

        # Default response
        speaker.speak("Sorry, I don't know how to handle that yet. Try asking for time, music, or search something!")

    def extract_topic(self, query, remove_words):
        """Extract topic from query by removing specified words"""
        topic = query
        for word in remove_words:
            topic = topic.replace(word, "")
        return topic.strip()

# Global instance
brain = Brain()
