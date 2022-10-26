import pyautogui
import time
from win32gui import GetWindowText, GetForegroundWindow
import subprocess
pyautogui.PAUSE = 0.4

dist = input('Enter the distracting word/phrase: ')
dist = dist.replace(', ', ',')
dist = dist.replace(' ', '*')
dist = dist.split(',')

def titlechk(title):
    pyautogui.PAUSE = 0.075
    x = 0
    while GetWindowText(GetForegroundWindow()) != title:
        pyautogui.keyDown('alt')
        for i in range(x):
            pyautogui.write(['tab'])
        pyautogui.keyUp('alt')
        x += 1
    time.sleep(1.5)
    pyautogui.PAUSE = 0.3

pyautogui.hotkey('alt', 'tab')
time.sleep(0.25)
end = GetWindowText(GetForegroundWindow())
if "Unacademy" in end:
    pyautogui.write(['esc'])
pyautogui.hotkey('alt', 'tab')
subprocess.Popen("C:\\Program Files\\Cold Turkey\\Cold Turkey Blocker.exe")
titlechk('Cold Turkey Blocker Free (v4.1)')
pyautogui.hotkey('win', 'up')
time.sleep(1)
pyautogui.click(x = 1136, y = 965)

pyautogui.click(x = 119, y = 160)       # Blocks
pyautogui.click(x = 305, y = 194)       # Clicks "Distractions"

for i in dist:
    if 'u=' in i:
        i = i.replace('u=', '')
        pyautogui.PAUSE = 0.0025
        pyautogui.click(x = 878, y = 428)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(f'*{i}*')
        pyautogui.write(['enter'])
        pyautogui.PAUSE = 0.1
    else:
        pyautogui.PAUSE = 0.0025
        pyautogui.click(x = 878, y = 428)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(f'*.*/*p=*{i}*')
        pyautogui.write(['enter'])
        pyautogui.click(x = 878, y = 428)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(f'*.*/*q=*{i}*')
        pyautogui.write(['enter'])
        pyautogui.PAUSE = 0.1

time.sleep(2)
pyautogui.click(x = 1149, y = 773)      # Save

titlechk('C:\\WINDOWS\\py.exe')

for i in "You've made a good decision! Exiting...":
    if i == ".":
        time.sleep(0.5)
        print(i, end = "", flush = True)
        continue
    print(i, end = "", flush = True)
    time.sleep(0.025)
    
titlechk('Cold Turkey Blocker Free (v4.1)')
pyautogui.hotkey('alt', 'f4')
    
titlechk(end)
if "Unacademy" in end:
    pyautogui.write('f')
pyautogui.moveTo(x = 1919, y = 639)