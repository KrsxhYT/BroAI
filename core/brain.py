from core.utils import *
from core.speaker import speak

def handle_command(query):
    if query == "":
        return

    if "time" in query:
        tell_time()
    elif "date" in query:
        tell_date()
    elif "play music" in query or "song" in query:
        play_music()
    elif "search" in query and "wikipedia" in query:
        topic = query.replace("search", "").replace("wikipedia", "").strip()
        search_wikipedia(topic)
    elif "google" in query and "search" in query:
        topic = query.replace("search", "").replace("google", "").strip()
        google_search(topic)
    elif "open" in query:
        site = query.replace("open", "").strip()
        open_website(site)
    elif "hello" in query or "hi" in query:
        speak("Hello Krsxh! Ready for some action?")
    elif "how are you" in query:
        speak("I’m always running smoothly, thanks for asking!")
    else:
        speak("Sorry, I don't know that yet.")
