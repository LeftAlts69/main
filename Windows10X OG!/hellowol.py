import string
import time

text = "Windows10X OG!"

# First, animate the typing effect once
temp = ""
for ch in text:
    for i in string.printable:  # cycle through characters
        time.sleep(0.01)
        print(temp + i)
        if i == ch:
            temp += ch
            break

# After animation, just keep spamming the final text
while True:
    time.sleep(0.01)
    print(text)
