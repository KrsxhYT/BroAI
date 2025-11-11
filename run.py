from core.listener import listen
from core.brain import handle_command
from core.speaker import speak

if __name__ == "__main__":
    speak("Hey Krsxh! Your assistant is online.")
    while True:
        query = listen()
        if "exit" in query or "stop" in query:
            speak("Goodbye Krsxh, see you later!")
            break
        handle_command(query)
