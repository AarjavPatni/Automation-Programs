from ctypes import windll, WinDLL
import win32gui
import win32con
import pyautogui
from pyautogui import click as ck
from pyautogui import hotkey as hk
# from pyautogui import locateCenterOnScreen as lc
from pyautogui import press as p
from pyautogui import typewrite as tp
import pytesseract
import cv2
import numpy as np
from PIL import ImageGrab
from time import sleep as s
from os import startfile as sf, system
from sys import argv

system('wsl "/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe" -start "Distractions" -lock 60')

if WinDLL("User32.dll").GetKeyState(0x14):
    p('capslock')

hk('win', 'ctrl', 'd')
screen_width, screen_height = pyautogui.size()

# def get_window_rect():
#     rect = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
#     w = rect[2]
#     h = rect[3]
#     return (w, h)

windll.user32.BlockInput(True)
sf(r'C:\\Users\Aarjav\\Desktop\\Microsoft Edge.lnk')
exit = False

while True:
    fw = pyautogui.getAllWindows()
    for i in fw:
        if 'New Tab - Personal' in i.title:
            i.activate() if i.isActive else None
            i.maximize()
            fw = i
            exit = True
            break
    if exit:
        break

ck(screen_width // 2, 0)
s(1)
hk('win', 'ctrl', 't')

# while not (width == 1928 and height == 1040):
#     hk('win', 'up')
#     s(1)
#     width, height = get_window_rect()

hk('ctrl', 'l')
tp(r'extension://laankejkbhbdhmipfmgcngdelahlfoji/options.html#nuclearOptionTab')
p('enter')

while 'There is no way' not in pytesseract.image_to_string(
    cv2.cvtColor(np.array(ImageGrab.grab(
        bbox=(screen_width // 2, 0, screen_width, screen_height // 2))), cv2.COLOR_BGR2GRAY)
):
    continue

s(1)

p('tab', 16)
tp('1')
ck(1174, 727)

hk('ctrl', 'f')
tp('nuke')
p('escape')

p('enter', 5)
hk('win', 'ctrl', 't')

windll.user32.BlockInput(False)

fw.close()
hk('win', 'ctrl', 'f4')
for i in range(4):
    hk('win', 'ctrl', 'left')

# try:
#     if argv[1] == 'one':
#         break
# except IndexError:
#     pass
# s((25*60)+(10*60))       # Wait for 25m focus session and 10m break

if len(argv) > 1:
    sf(r"C:\Users\Aarjav\Focus To-Do.lnk")
    sf(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Everything.lnk")
    sf(r"C:\Users\Aarjav\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Todoist.lnk")

    # Wait for all to open
    while True:
        titles = (win32gui.FindWindow(None, 'Focus To-Do'), win32gui.FindWindow(None,
                  'Everything'), win32gui.FindWindow(None, 'next-actions: Todoist'))
        if all(titles):
            break

    for handle in titles:
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)

    s(2)
    system('taskkill /F /IM explorer.exe & start explorer')
