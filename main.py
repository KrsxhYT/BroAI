import subprocess
import os
import time
from datetime import datetime
import sys

# Color codes for better UI
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════╗
║             🤖 BRO AI ASSISTANT              ║
║                 Version 2.0                  ║
║          Made with ❤️ by TechByKrsxh         ║
╚══════════════════════════════════════════════╝
{Colors.END}
"""
    print(banner)

def get_time():
    now = datetime.now()
    return now.strftime('%I:%M %p'), now.strftime('%Y-%m-%d')

# Clear screen and show banner
os.system('clear')
print_banner()

now = datetime.now()
t = now.strftime('%I:%M %p')
current_date = now.strftime('%Y-%m-%d')

print(f"{Colors.MAGENTA}📅 Date: {current_date} | 🕒 Time: {t}{Colors.END}")
print(f"{Colors.YELLOW}🎤 Listening for your command...{Colors.END}")
print(f"{Colors.CYAN}💡 Say 'close' or 'exit' to quit{Colors.END}")
print("-" * 50)

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print(f"{Colors.GREEN}🗣️  You said: {Colors.BOLD}{str(inp)}{Colors.END}")

def system():
     if inp == "":
         subprocess.call(["termux-tts-speak","Please tell something sir"])
         print(f"{Colors.RED}❌ No input detected{Colors.END}")

     elif "hello" in inp.lower():
         subprocess.call(["termux-tts-speak","Hello sir! How can I help you today?"])
         print(f"{Colors.GREEN}✅ Greeted user{Colors.END}")
         
     elif "close" in inp.lower() or "exit" in inp.lower():
         subprocess.call(["termux-tts-speak","Okay sir, shutting down. Goodbye!"])
         print(f"{Colors.RED}🛑 Shutting down...{Colors.END}")
         time.sleep(1)
         sys.exit()
         
     elif "how are you" in inp.lower():
        subprocess.call(["termux-tts-speak","I am doing great sir, thank you for asking!"])
        print(f"{Colors.GREEN}✅ Status response{Colors.END}")
        
     elif "battery" in inp.lower():
         print(f"{Colors.YELLOW}🔋 Checking battery status...{Colors.END}")
         subprocess.call(["termux-battery-status"])
         
     elif "sleep" in inp.lower():
         subprocess.call(["termux-tts-speak","Okay sir, I am going to sleep for 5 seconds"])
         print(f"{Colors.BLUE}😴 Sleeping for 5 seconds...{Colors.END}")
         time.sleep(5)
         print(f"{Colors.GREEN}✅ Woke up!{Colors.END}")
         
     elif "call me" in inp.lower():
         print(f"{Colors.CYAN}📞 Opening dialer...{Colors.END}")
         os.system("termux-telephony-call +91")
         
     elif "torch on" in inp.lower():
         print(f"{Colors.YELLOW}🔦 Turning torch ON{Colors.END}")
         os.system("termux-torch on")
         
     elif "torch off" in inp.lower():
         print(f"{Colors.YELLOW}🔦 Turning torch OFF{Colors.END}")
         os.system("termux-torch off")
         
     elif "youtube" in inp.lower():
         print(f"{Colors.RED}🎬 Opening YouTube...{Colors.END}")
         os.system("termux-open https://m.youtube.com")
         
     elif "google" in inp.lower():
         print(f"{Colors.BLUE}🌐 Opening Google...{Colors.END}")
         os.system("termux-open https://www.google.co.in/")    
         
     elif "contact" in inp.lower():
         print(f"{Colors.GREEN}📱 Showing contacts...{Colors.END}")
         os.system("termux-contact-list")
         
     elif "who are you" in inp.lower():
         subprocess.call(["termux-tts-speak","I am your virtual assistant Bro AI, at your service sir"])
         print(f"{Colors.CYAN}🤖 Identity revealed{Colors.END}")
         
     elif "time" in inp.lower():
         subprocess.call(["termux-tts-speak",f"The time is {t}"])
         print(f"{Colors.MAGENTA}🕒 Time: {t}{Colors.END}")
         
     elif "date" in inp.lower():
         subprocess.call(["termux-tts-speak",f"Today's date is {current_date}"])
         print(f"{Colors.MAGENTA}📅 Date: {current_date}{Colors.END}")
         
     elif "what are you doing" in inp.lower():
        subprocess.call(["termux-tts-speak","I am busy assisting you sir"])
        print(f"{Colors.GREEN}✅ Activity response{Colors.END}")
        
     elif "are you busy" in inp.lower():
         subprocess.call(["termux-tts-speak","I am always free for you sir"])
         print(f"{Colors.GREEN}✅ Availability confirmed{Colors.END}")
     
     elif "name" in inp.lower():
         subprocess.call(["termux-tts-speak","You can call me Bro AI"])
         print(f"{Colors.CYAN}🤖 Name: Bro AI{Colors.END}")
     
     
     elif "who made you" in inp.lower():
         subprocess.call(["termux-tts-speak","I was created by TechByKrsxh"])
         print(f"{Colors.CYAN}👨‍💻 Creator: TechByKrsxh{Colors.END}")
         
     elif "video" in inp.lower():
         print(f"{Colors.RED}🎥 Searching videos...{Colors.END}")
         os.system("termux-open https://www.google.com/search?q=video")
     
     elif "thank you" in inp.lower() or "thanks" in inp.lower():
         subprocess.call(["termux-tts-speak","You're welcome sir! Always happy to help"])
         print(f"{Colors.GREEN}✅ Acknowledged thanks{Colors.END}")
         
     elif "weather" in inp.lower():
         print(f"{Colors.BLUE}🌤️  Checking weather...{Colors.END}")
         os.system("termux-open https://www.google.com/search?q=weather")
         
     elif "music" in inp.lower():
         print(f"{Colors.MAGENTA}🎵 Opening music...{Colors.END}")
         os.system("termux-open https://www.youtube.com/results?search_query=music")
     
     elif "calculator" in inp.lower():
         print(f"{Colors.YELLOW}🧮 Opening calculator...{Colors.END}")
         os.system("termux-open https://www.google.com/search?q=calculator")
     
     elif "news" in inp.lower():
         print(f"{Colors.RED}📰 Opening news...{Colors.END}")
         os.system("termux-open https://www.google.com/search?q=news")
     
     else:
       subprocess.call(["termux-tts-speak","I am not programmed for that command yet"])
       print(f"{Colors.RED}❌ Command not recognized: {inp}{Colors.END}")

system()

print("-" * 50)
print(f"{Colors.YELLOW}🔄 Restarting Bro AI...{Colors.END}")
time.sleep(2)
os.system("python main.py")
