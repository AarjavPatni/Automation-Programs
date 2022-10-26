import pyautogui
import time
from win32gui import GetWindowText, GetForegroundWindow
from win10toast import ToastNotifier
import os
import ctypes
import subprocess

pyautogui.PAUSE = 0.4

input = input('How long? (5, 10, 15, 20, 25, 30, 40, 1h, 2h, 3h, 4h, 5h, 6h) -- ')


if "h" in input:
    app_block = int(input.replace("h", ""))
    app_block = app_block * 3600
else:
    app_block = int(input)
    app_block = app_block * 60

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
    pyautogui.PAUSE = 0.075
    x = 0
    while GetWindowText(GetForegroundWindow()) != title:
        pyautogui.keyDown('alt')
        for i in range(x):
            pyautogui.write(['tab'])
        pyautogui.keyUp('alt')
        x += 1
    time.sleep(1)
    pyautogui.PAUSE = 0.4

pyautogui.hotkey('alt', 'tab')
time.sleep(0.25)
end = GetWindowText(GetForegroundWindow())
if "Unacademy" in end:
    pyautogui.write(['esc'])
pyautogui.hotkey('alt', 'tab')
subprocess.Popen("C:\\Program Files\\Cold Turkey\\Cold Turkey Blocker.exe")
titlechk('Cold Turkey Blocker Free (v4.1)')
max()
time.sleep(1)
if pyautogui.size() == (1136, 965):
    pyautogui.click(x = 119, y = 160)       # Blocks
    pyautogui.click(x = 1269, y = 227)      # LockButton
    pyautogui.click(x = 501, y = 286)       # Timer
    pyautogui.click(x = 599, y = 382)       # Dropdown
    available = (5, 10, 15, 20, 25, 30, 40, "1h", "2h", "3h", "4h", "5h", "6h")
    timerx = (589, 589, 589, 589, 589, 589, 589, 589, 589, 589, 589, 589, 589)
    timery = (246, 265, 286, 302, 322, 340, 363, 377, 397, 417, 438, 452, 471)
else:
    pyautogui.click(x = 119, y = 160)       # Blocks
    pyautogui.click(x = 1827, y = 228)      # LockButton
    pyautogui.click(x = 777, y = 425)       # Timer
    pyautogui.click(x = 774, y = 524)       # Dropdown
    available = (5, 10, 15, 20, 25, 30, 40, "1h", "2h", "3h", "4h", "5h", "6h")
    timerx = (758, 758, 758, 758, 758, 758, 758, 758, 758, 758, 758, 758, 758)
    timery = (539, 559, 578, 599, 616, 634, 650, 671, 689, 708, 725, 745, 763)


if input in available:
    loc = available.index(input)
    pyautogui.click(x = timerx[loc], y = timery[loc])

if pyautogui.size() == (1136, 965):
    pyautogui.click(x = 921, y = 533)      # Save
    pyautogui.click(x = 1263, y = 189)     # On Toggle
    pyautogui.click(x = 801, y = 544)      # Confirm
else:
    pyautogui.click(x = 1202, y = 674)      # Save
    pyautogui.click(x = 1819, y = 189)      # On Toggle
    pyautogui.click(x = 1073, y = 703)      # Confirm

pyautogui.PAUSE = 0.005
pyautogui.hotkey('alt', 'f4')
pyautogui.PAUSE = 0.35

titlechk("C:\\WINDOWS\\py.exe")
for i in "You've made a good decision! Exiting...":
    if i == ".":
        time.sleep(0.5)
        print(i, end = "", flush = True)
        continue
    print(i, end = "", flush = True)
    time.sleep(0.025)
time.sleep(0.25)
    
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 0

hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)
    
titlechk(end)
if "Unacademy" in end:
    pyautogui.write('f')
pyautogui.moveTo(x = 1919, y = 639)

blocked_apps = ('task manager', 'k2pdfopt', 'fontforge', 'sqlite3', 'vocab', 'calibre', 'knowledge base', 'notion-enhancer', 'minecraft', 'visual studio code', 'ghar4u')
for j in range(1, app_block + 1):
    name = GetWindowText(GetForegroundWindow())
    name = name.lower()
    for k in blocked_apps:
        if k in name:
            pyautogui.hotkey('alt', 'f4')
            break
    time.sleep(1)

notifier = ToastNotifier()
notifier.show_toast("Well Done!", "Your timed block is over", duration = 5, icon_path = "C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\coffee-cup.ico")

"""
pyautogui.click(x = 861, y = 539)       # 5 mins
pyautogui.click(x = 859, y = 559)       # 10 mins
pyautogui.click(x = 752, y = 578)       # 15 mins
pyautogui.click(x = 736, y = 599)       # 20 mins
pyautogui.click(x = 760, y = 616)       # 25 mins
pyautogui.click(x = 757, y = 634)       # 30 mins
pyautogui.click(x = 770, y = 650)       # 40 mins
"""
