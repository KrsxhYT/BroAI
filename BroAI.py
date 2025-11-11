import time
import datetime
import os
import subprocess

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

def wish():
    h = int(datetime.datetime.now().hour)
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    print(f"{Colors.MAGENTA}📅 Date: {current_date} | 🕒 Time: {current_time}{Colors.END}")
    
    if h < 12:
        greeting = "Good morning sir! How may I help you?"
        print(f"{Colors.YELLOW}🌅 {greeting}{Colors.END}")
        subprocess.call(["termux-tts-speak", greeting])
    elif h >= 12 and h < 17:
        greeting = "Good afternoon sir! How may I help you?"
        print(f"{Colors.YELLOW}☀️  {greeting}{Colors.END}")
        subprocess.call(["termux-tts-speak", greeting])
    elif h >= 17 and h < 20:
        greeting = "Good evening sir! How may I help you?"
        print(f"{Colors.YELLOW}🌇 {greeting}{Colors.END}")
        subprocess.call(["termux-tts-speak", greeting])
    else:
        greeting = "Welcome sir! How may I help you?"
        print(f"{Colors.YELLOW}🌙 {greeting}{Colors.END}")
        subprocess.call(["termux-tts-speak", greeting])

# Clear screen and show banner
os.system('clear')
print_banner()

# Show system info with screenfetch
print(f"{Colors.GREEN}{Colors.BOLD}🖥️  SYSTEM INFORMATION:{Colors.END}")
os.system('screenfetch')

print(f"\n{Colors.RED}{Colors.BOLD}" + "🚀 CREATED BY KRSXH @TechByKrsxh" + Colors.END)
print("-" * 50)

# Greet the user
wish()

print(f"{Colors.CYAN}💡 Bro AI is now starting...{Colors.END}")
print("-" * 50)
time.sleep(2)

# Start main assistant
os.system("python main.py")
