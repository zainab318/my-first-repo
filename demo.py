#!/usr/bin/env python3
"""
Demo script for Zainab's Animated Terminal Intro
Run this to see the full animated experience!
"""

import sys
import os

def main():
    print("🚀 Starting Zainab's Animated Terminal Intro...")
    print("=" * 50)
    
    try:
        # Import and run the main intro script
        from intro1 import main as run_intro
        run_intro()
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you have installed the requirements:")
        print("   pip install -r requirements.txt")
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted. Thanks for checking it out!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main() 