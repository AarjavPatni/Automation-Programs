import pyautogui
import time
from win32gui import GetWindowText, GetForegroundWindow
import subprocess

pyautogui.PAUSE = 0.4

input = input('How long? (5, 10, 15, 20, 25, 30, 45, 50, 1h, 2h) -- ')
try:
    input = int(input)
except ValueError:
    pass

def max():
    pyautogui.PAUSE = 0.1
    pyautogui.keyDown('win')
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')
    pyautogui.keyUp('win')
    pyautogui.PAUSE = 0.4
def titlechk(title):
    pyautogui.PAUSE = 0.1
    x = 0
    while GetWindowText(GetForegroundWindow()) != title:
        pyautogui.keyDown('alt')
        for i in range(x):
            pyautogui.write(['tab'])
        pyautogui.keyUp('alt')
        x += 1
    pyautogui.PAUSE = 0.35

subprocess.Popen("C:\\Program Files\\Cold Turkey\\Cold Turkey Blocker.exe")
max()
time.sleep(1)
pyautogui.click(x = 1136, y = 965)

pyautogui.click(x = 119, y = 160)       # Blocks
pyautogui.click(x = 379, y = 57)        # Frozen Turkey
pyautogui.click(x = 1833, y = 188)      # Start
pyautogui.click(x = 797, y = 524)       # Dropdown
available = (5, 10, 15, 20, 25, 30, 45, 50, "1h", "2h")
timerx = (861, 859, 763, 736, 760, 757, 768, 767, 761, 757)
timery = (539, 559, 578, 599, 616, 634, 654, 675, 694, 713)

if input in available:
    loc = available.index(input)
    time.sleep(0.3)
    pyautogui.click(x = timerx[loc], y = timery[loc])

pyautogui.click(x = 1205, y = 628)      # Start

pyautogui.PAUSE = 0.1
pyautogui.hotkey('alt', 'f4')
pyautogui.PAUSE = 0.35

titlechk('C:\\WINDOWS\\py.exe')
print("You've made a good decision! Exiting", end = "", flush=True)
time.sleep(0.5)
print(".", end = "", flush=True)
time.sleep(0.5)
print(".", end = "", flush=True)
time.sleep(0.5)
print(".", end = "", flush=True)
time.sleep(0.5)
pyautogui.hotkey('alt', 'tab')
pyautogui.moveTo(x = 1919, y = 921)

"""
pyautogui.click(x = 861, y = 539)       # 5 mins
pyautogui.click(x = 859, y = 559)       # 10 mins
pyautogui.click(x = 752, y = 578)       # 15 mins
pyautogui.click(x = 736, y = 599)       # 20 mins
pyautogui.click(x = 760, y = 616)       # 25 mins
pyautogui.click(x = 757, y = 634)       # 30 mins
pyautogui.click(x = 770, y = 650)       # 40 mins
"""