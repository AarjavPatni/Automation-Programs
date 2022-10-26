from subprocess import run
from time import sleep

# Ask the user for how long he'd like to search
sleep(int(input("How long? ")) * 60)

# Kill the brave browser
run(["pkill", "brave"])