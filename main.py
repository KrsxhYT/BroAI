import openai
import speech_recognition as sr
import pyttsx3
import os
import time
from dotenv import load_dotenv

class JarvisAI:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize OpenAI API
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        openai.api_key = self.openai_api_key
        
        # Initialize speech engine
        self.engine = pyttsx3.init()
        self.set_voice_properties()
        
        # Initialize recognizer
        self.recognizer = sr.Recognizer()
        
        # Conversation history
        self.conversation_history = [
            {"role": "system", "content": "You are Jarvis, an advanced AI assistant. You are helpful, concise, and have a witty personality."}
        ]
        
        # Configuration
        self.voice_enabled = True
        self.print_responses = True
    
    def set_voice_properties(self):
        """Configure voice properties"""
        voices = self.engine.getProperty('voices')
        try:
            # Try to set a pleasant voice (varies by system)
            self.engine.setProperty('voice', voices[1].id)  # Typically 0=male, 1=female
        except:
            self.engine.setProperty('voice', voices[0].id)
        
        self.engine.setProperty('rate', 160)  # Speech speed
        self.engine.setProperty('volume', 0.9)  # Volume (0-1)
    
    def speak(self, text):
        """Convert text to speech"""
        if self.print_responses:
            print(f"Jarvis: {text}")
        
        if self.voice_enabled:
            self.engine.say(text)
            self.engine.runAndWait()
    
    def listen(self):
        """Listen for user voice input"""
        with sr.Microphone() as source:
            if self.print_responses:
                print("\nListening... (say 'stop' to exit)")
            
            # Adjust for ambient noise and listen
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source, timeout=10)
        
        try:
            query = self.recognizer.recognize_google(audio, language='en-in')
            if self.print_responses:
                print(f"You: {query}")
            return query.lower()
        except sr.UnknownValueError:
            if self.print_responses:
                print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            if self.print_responses:
                print("Sorry, my speech service is down.")
            return None
        except Exception as e:
            if self.print_responses:
                print(f"Error: {e}")
            return None
    
    def get_chat_response(self, prompt):
        """Get response from OpenAI's API"""
        if not prompt:
            return "I didn't receive any input."
        
        self.conversation_history.append({"role": "user", "content": prompt})
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=150
            )
            reply = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": reply})
            return reply
        except openai.error.OpenAIError as e:
            return f"Sorry, I encountered an OpenAI error: {str(e)}"
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def text_mode(self):
        """Run in text-only mode"""
        self.voice_enabled = False
        print("\nText mode activated. Type your commands.")
        
        while True:
            try:
                query = input("\nYou: ").strip().lower()
                
                if not query:
                    continue
                
                if query in ["exit", "quit", "bye", "stop"]:
                    self.speak("Goodbye!")
                    break
                
                response = self.get_chat_response(query)
                self.speak(response)
                
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break
    
    def voice_mode(self):
        """Run in voice mode"""
        self.voice_enabled = True
        self.speak("Hello, I am Jarvis. How can I assist you today?")
        
        while True:
            try:
                query = self.listen()
                
                if query is None:
                    continue
                
                if any(word in query for word in ["exit", "quit", "bye", "stop"]):
                    self.speak("Goodbye! Have a great day.")
                    break
                
                response = self.get_chat_response(query)
                self.speak(response)
                
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break
    
    def run(self, mode='voice'):
        """Start Jarvis in specified mode"""
        if mode == 'voice':
            self.voice_mode()
        elif mode == 'text':
            self.text_mode()
        else:
            raise ValueError("Invalid mode. Choose 'voice' or 'text'")

if __name__ == "__main__":
    try:
        jarvis = JarvisAI()
        print("""
        #######################################
        #                                     #
        #          JARVIS AI ASSISTANT       #
        #                                     #
        #######################################
        """)
        print("Starting Jarvis...")
        jarvis.run(mode='voice')  # Change to 'text' for text-only mode
    except Exception as e:
        print(f"Failed to initialize Jarvis: {e}")
