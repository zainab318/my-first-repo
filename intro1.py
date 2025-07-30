"""
🎬 ZAINAB RAUF - ANIMATED TERMINAL INTRO PREVIEW
=================================================

WHAT THIS SCRIPT DOES:
----------------------
This creates a cinematic terminal experience with:
• Animated ASCII banner using pyfiglet
• Twinkling starfield effects with colors
• Typewriter text animation
• Dramatic pauses and timing
• Personal story about Zainab's journey

SAMPLE OUTPUT:
--------------
   ✦      ✦        ✦✦        ✦      ✦   
✦      ✦✦    ✦        ✦✦    ✦      ✦
   ✦✦      ✦✦✦      ✦      ✦✦✦   
✦✦✦    ✦      ✦✦✦✦    ✦      ✦✦✦
   ✦      ✦        ✦✦        ✦      ✦   

██████╗  █████╗ ██╗███╗   ██╗ █████╗ ██████╗ 
╚════██╗██╔══██╗██║████╗  ██║██╔══██╗██╔══██╗
 █████╔╝███████║██║██╔██╗ ██║███████║██████╔╝
██╔═══╝ ██╔══██║██║██║╚██╗██║██╔══██║██╔══██╗
███████╗██║  ██║██║██║ ╚████║██║  ██║██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ 

👾 [Narrator]: In a galaxy not so far away...
✨ Name: Zainab Rauf
🎓 Computer Science student (GPA: 3.93)
💻 Languages: C & C++
🤖 AI & Robotics Summer Camp: PTCL, 2021
🚗 Dream: Blend AI with automotive engineering!

🌟 The adventure is just beginning...
Stay curious. Stay bold.
To be continued... 🚀

HOW TO RUN:
-----------
python intro1.py

FEATURES:
---------
• ASCII Art Banner (pyfiglet)
• Animated Starfield Effects
• Typewriter Text Animation  
• Colorful Terminal Output
• Dramatic Pauses & Timing
• Cross-platform compatibility

AUTHOR: Zainab Rauf
PURPOSE: Showcase animated terminal intro with personal story
"""

import time
import sys
import os

# Try to import pyfiglet, install if missing
try:
    from pyfiglet import Figlet
except ImportError:
    print("Installing pyfiglet for cool banners...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])
    from pyfiglet import Figlet

# Terminal color codes for extra flair
COLORS = {
    'star': '\033[95m',
    'cyan': '\033[96m',
    'yellow': '\033[93m',
    'green': '\033[92m',
    'reset': '\033[0m',
    'bold': '\033[1m',
}

# Fancy animated starfield border
def print_starfield():
    star_lines = [
        f"{COLORS['star']}   ✦      ✦        ✦✦        ✦      ✦   {COLORS['reset']}",
        f"{COLORS['star']}✦      ✦✦    ✦        ✦✦    ✦      ✦{COLORS['reset']}",
        f"{COLORS['star']}   ✦✦      ✦✦✦      ✦      ✦✦✦   {COLORS['reset']}",
        f"{COLORS['star']}✦✦✦    ✦      ✦✦✦✦    ✦      ✦✦✦{COLORS['reset']}",
        f"{COLORS['star']}   ✦      ✦        ✦✦        ✦      ✦   {COLORS['reset']}"
    ]
    for line in star_lines:
        print(line)
        time.sleep(0.08)

def typewriter(text, delay=0.02, newline=True):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def dramatic_pause(sec=1.0):
    time.sleep(sec)

def banner_typewriter(text, font='starwars', color='cyan', delay=0.002):
    f = Figlet(font=font)
    banner = f.renderText(text)
    for char in banner:
        if char != '\n':
            print(COLORS[color] + char + COLORS['reset'], end='', flush=True)
            time.sleep(delay)
        else:
            print()
            time.sleep(delay * 10)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print_starfield()
    dramatic_pause(0.5)
    # Animated banner
    banner_typewriter('Zainab Rauf', font='starwars', color='cyan', delay=0.0015)
    print_starfield()
    dramatic_pause(0.7)

    # Narrator intro
    narrator = (
        f"\n{COLORS['yellow']}👾 [Narrator]:{COLORS['reset']} "
        "In a galaxy not so far away, where code twinkles like stars and dreams race at the speed of light...\n"
        "A new journey is about to begin.\n"
    )
    typewriter(narrator, 0.035)
    dramatic_pause(1.2)

    # Personal details, spaced for effect
    details = [
        f"{COLORS['bold']}✨ Name:{COLORS['reset']} Zainab Rauf",
        f"{COLORS['bold']}🎓 Computer Science student{COLORS['reset']} (GPA: 3.93)",
        f"{COLORS['bold']}💻 Languages:{COLORS['reset']} C & C++ (school adventures!)",
        f"{COLORS['bold']}🤖 AI & Robotics Summer Camp:{COLORS['reset']} PTCL, 2021",
        f"{COLORS['bold']}🚗 Dream:{COLORS['reset']} To blend AI with automotive engineering and design intelligent vehicles!"
    ]
    for line in details:
        typewriter(line, 0.03)
        dramatic_pause(0.5)
    print(f"\n{COLORS['green']}" + "═" * 48 + f"{COLORS['reset']}\n")
    dramatic_pause(0.7)

    # Storytelling
    story = (
        f"{COLORS['yellow']}Once upon a terminal...{COLORS['reset']}\n"
        "A spark was lit at a summer camp, and curiosity became a calling.\n"
        "Now, Zainab codes not just for grades, but for the thrill of invention—\n"
        "to one day craft vehicles that think, learn, and inspire.\n"
        "\n"
        "Every journey begins with a single line of code."
    )
    typewriter(story, 0.035)
    dramatic_pause(1.2)

    # Motivational ending
    ending = (
        f"\n{COLORS['cyan']}🌟 The adventure is just beginning...{COLORS['reset']}\n"
        "Stay curious. Stay bold.\n"
        f"{COLORS['bold']}To be continued... 🚀{COLORS['reset']}\n"
    )
    typewriter(ending, 0.045)
    print_starfield()

if __name__ == "__main__":
    main()
