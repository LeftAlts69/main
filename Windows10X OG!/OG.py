# typewriter_repeat.py
import sys
import time

text = "Windows10X OG!"
type_speed = 0.03   # seconds between characters (smaller = faster)
pause_between_lines = 0.10  # seconds to wait after finishing a line

try:
    while True:
        # Typewriter: print one character at a time
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(type_speed)
        # "Press Enter" (move to next line), then pause, then repeat
        sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(pause_between_lines)
except KeyboardInterrupt:
    sys.stdout.write("\nStopped by user.\n")
    
