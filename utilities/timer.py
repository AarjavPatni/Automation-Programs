from time import sleep as s
import winsound as ws
from pyautogui import press as p
import ctypes

choice = int(input('''Select from the following options:
1. Washroom Break
2. Water Break
3. Breakfast / Lunch / Dinner Break
4. Deserved Break
5. Custom
'''))

list = [3, 2, 40, 15]

if choice < 5:
    p('volumeup', 100)
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_HIDE = 0
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, SW_HIDE)
    s(list[choice - 1] * 60)
    ws.PlaySound('C:\\Users\\Aarjav\\Documents\\Automation Programs\\timer.wav', ws.SND_FILENAME | ws.SND_ASYNC | ws.SND_LOOP)
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMISE = 3
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, SW_MAXIMISE)
    stop = input('Press enter to stop the timer: ')
else:
    count = int(input('Enter the number of minutes: '))
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_HIDE = 0
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, SW_HIDE)
    p('volumeup', 100)
    s(count * 60)
    ws.PlaySound('C:\\Users\\Aarjav\\Documents\\Automation Programs\\timer.wav', ws.SND_FILENAME | ws.SND_ASYNC | ws.SND_LOOP)
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMISE = 3
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, SW_MAXIMISE)
    stop = input('Press enter to stop the timer: ')