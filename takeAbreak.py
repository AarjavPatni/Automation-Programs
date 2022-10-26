from pyautogui import hotkey
from time import sleep
from os import popen
from sys import argv

popen('notify-send "Take A Break" "Break has started!"')
sleep(int(argv[1]) * 60)

for i in range(5):
    hotkey("win", "q")
