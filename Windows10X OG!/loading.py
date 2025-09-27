import time
import sys

spinner = ["x", "+"]

while True:
    for frame in spinner:
        sys.stdout.write("\rLoading " + frame)
        sys.stdout.flush()
        time.sleep(0.1)

