#!/usr/bin/env python3
"""
Quick Preview of Zainab's Animated Terminal Intro
This shows a condensed version for GitHub previews
"""

import time
import sys

# Simple color codes for preview
COLORS = {
    'cyan': '\033[96m',
    'yellow': '\033[93m',
    'green': '\033[92m',
    'reset': '\033[0m',
    'bold': '\033[1m',
}

def quick_preview():
    """Show a quick preview of the intro animation"""
    
    print(f"{COLORS['cyan']}╔══════════════════════════════════════════════════════════╗{COLORS['reset']}")
    print(f"{COLORS['cyan']}║                    ZAINAB RAUF                           ║{COLORS['reset']}")
    print(f"{COLORS['cyan']}║              Animated Terminal Intro                     ║{COLORS['reset']}")
    print(f"{COLORS['cyan']}╚══════════════════════════════════════════════════════════╝{COLORS['reset']}")
    print()
    
    # Quick star animation
    stars = ["✦", "✦✦", "✦✦✦", "✦✦✦✦", "✦✦✦✦✦"]
    for star in stars:
        print(f"{COLORS['yellow']}{star:^50}{COLORS['reset']}")
        time.sleep(0.3)
    
    print(f"\n{COLORS['bold']}✨ Features:{COLORS['reset']}")
    print("  • ASCII Art Banner with pyfiglet")
    print("  • Animated Starfield Effects")
    print("  • Typewriter Text Animation")
    print("  • Colorful Terminal Output")
    print("  • Dramatic Pauses & Timing")
    
    print(f"\n{COLORS['green']}🎯 Run 'python intro1.py' for the full experience!{COLORS['reset']}")

if __name__ == "__main__":
    quick_preview() 