import random
import time
import os

# Matrix rain effect
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*"

columns = 80   # width of screen
lines = 20     # height of screen

while True:
    # generate random line of chars
    line = "".join(random.choice(chars) for _ in range(columns))
    print(line)
    time.sleep(0.05)  # control speed

    # clear screen when lines overflow
    if random.random() < 0.05:  # occasionally clear
        os.system("cls" if os.name == "nt" else "clear")
