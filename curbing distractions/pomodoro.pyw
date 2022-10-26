import pyautogui
import time
from win32gui import GetWindowText, GetForegroundWindow
from win10toast import ToastNotifier
import playsound
import subprocess

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.4

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

notifier = ToastNotifier()
playsound("C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\Pomodoro Alarm.mp3")
notifier.show_toast("Let's do this!", "25 mins to go...", duration = 3, icon_path = "C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\target.ico")

for i in range (1, 5):
    time.sleep(0.25)
    end = GetWindowText(GetForegroundWindow())
    if "Unacademy" in end:
        pyautogui.write(['esc'])
    subprocess.Popen("C:\\Program Files\\Cold Turkey\\Cold Turkey Blocker.exe")
    titlechk('Cold Turkey Blocker Free (v4.1)')
    max()
    time.sleep(1)
    if pyautogui.size() == (1136, 965):
        pyautogui.click(x = 119, y = 160)       # Blocks
        pyautogui.click(x = 1269, y = 227)      # LockButton
        pyautogui.click(x = 501, y = 286)       # Timer
        pyautogui.click(x = 599, y = 382)       # Dropdown
        mainx = 589
        mainy = 322
    else:
        pyautogui.click(x = 119, y = 160)       # Blocks
        pyautogui.click(x = 1827, y = 228)      # LockButton
        pyautogui.click(x = 777, y = 425)       # Timer
        pyautogui.click(x = 774, y = 524)       # Dropdown
        mainx = 758
        mainy = 616

    pyautogui.click(x = mainx, y = mainy)

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

    if end == "":
        pyautogui.hotkey('win', 'd')
    else:
        titlechk(end)
    if "Unacademy" in end:
        pyautogui.write('f')
    pyautogui.moveTo(x = 1919, y = 639)
    blocked_apps = ("Visual Studio Code", "Mail", "Task Manager")
    for j in range(1, 1441):
        name = GetWindowText(GetForegroundWindow())
        for k in blocked_apps:
            if k in name:
                pyautogui.hotkey('alt', 'f4')
                break
        time.sleep(1)

    playsound("C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\Pomodoro Alarm.mp3")
    notifier.show_toast("Timer's Up!", "Well Done! You've spent 25 minutes focused. Take a break :)", duration = 4, icon_path = "C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\coffee-cup.ico")
    if i != 4:
        for j in range(1, 601):
            if "Cold Turkey" in GetWindowText(GetForegroundWindow()):
                pyautogui.hotkey('alt', 'f4')
                break
            time.sleep(1)
        playsound("C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\Pomodoro Alarm.mp3")
        notifier.show_toast("Break's Over!", "Get back to focusing. 25 mins to go!", duration = 4, icon_path = "C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\target.ico")
    else:
        break


playsound("C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\Pomodoro Alarm.mp3")
notifier.show_toast("Timer's Up!", "Well Done! You've completed 4 pomodoros. Take a 30 min break :)", duration = 7, icon_path = "C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\coffee-cup.ico")