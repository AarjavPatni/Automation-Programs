import pyautogui
import time
from win32gui import GetWindowText, GetForegroundWindow

def step_by_step(str):
    for i in str:
        if i == ".":
            time.sleep(0.5)
            print(i, end = "", flush = True)
            continue
        print(i, end = "", flush = True)
        time.sleep(0.05)
    
def titlechk(title):
    pyautogui.PAUSE = 0.05
    x = 0
    while GetWindowText(GetForegroundWindow()) != title:
        pyautogui.keyDown('alt')
        for i in range(x):
            pyautogui.write(['tab'])
        pyautogui.keyUp('alt')
        x += 1
    time.sleep(1)
    pyautogui.PAUSE = 0.4

def type_step(str1):
    pyautogui.PAUSE = 0.05
    for i in str1:
        if i == ".":
            time.sleep(1)
        pyautogui.write(i)
    pyautogui.PAUSE = 1

step_by_step("Hello there!\nLet me show you something cool today. I promise to not invade your privacy in any way. I'd love to see your screen shared while this is running. Don't have a panic attack... ;)\nIf you're ready, then press enter: ")
enter = input('')
pyautogui.hotkey('win', 's')
time.sleep(2)
pyautogui.write("Notepad")
time.sleep(2)
pyautogui.write(['enter'])
titlechk("Untitled - Notepad")
type_step("There are so many things you can do with a computer. It's quite fun to do stuff like this with complete permissions haha!\nHere's what all I can do.")
time.sleep(2)
pyautogui.hotkey('win', 'd')
time.sleep(1)
pyautogui.hotkey('alt', 'f4')
time.sleep(2.5)
titlechk("*Untitled - Notepad")
time.sleep(1)
type_step("\nI could've almost shut it down. You're lucky I didn't. ;) There are so many nasty things I can think of, like this...")
pyautogui.hotkey('win', 's')
time.sleep(2)
pyautogui.write("Chrome")
time.sleep(2)
pyautogui.write(['enter'])
time.sleep(3)
pyautogui.hotkey('win', 'up')
pyautogui.hotkey('ctrl', 'l')
time.sleep(1)
pyautogui.write("https://web.whatsapp.com/")
time.sleep(1)
pyautogui.write(['enter'])
time.sleep(5)
pyautogui.hotkey('alt', 'PrtScr')

pyautogui.hotkey('win', 's')
time.sleep(2)
pyautogui.write("Outlook")
time.sleep(15)
pyautogui.hotkey('ctrl', 'n')
time.sleep(4)
pyautogui.write("aarjav.p_nms@gemselearning.com")
titlechk("*Untitled - Notepad")
pyautogui.press('tab')
pyautogui.write("WhatsApp Screenshot")
pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'v')
pyautogui.PAUSE = 0.05
email = "Don't worry. I won't send it! :)"
for i in email:
    pyautogui.write(i)
pyautogui.PAUSE = 1
titlechk("*Untitled - Notepad")
pyautogui.PAUSE = 0.05
exitmsg = "That's pretty much it. Just wanted to show you what I'm capable of hehe. Bye! Wish you were our teacher for a longer. ;( All the Best Ma'am!!"
for i in email:
    pyautogui.write(i)
pyautogui.PAUSE = 1