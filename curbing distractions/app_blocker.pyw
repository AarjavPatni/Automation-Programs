import ctypes, os, psutil, time, sys, pyautogui
from win10toast import ToastNotifier
from win32gui import GetWindowText, GetForegroundWindow
pyautogui.FAILSAFE = False

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 0

hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)

def checkRunningProcess(process):
    for title in title_list:
        if ('administrator: windows powershell' in GetWindowText(GetForegroundWindow()).lower()) or ('cmd' in GetWindowText(GetForegroundWindow()).lower()):
            pyautogui.hotkey('alt', 'f4')
            continue
        # if ((title == 'visual studio code') and ('school.py' in GetWindowText(GetForegroundWindow()).lower())) or ((title == 'visual studio code') and ('learn.html' in GetWindowText(GetForegroundWindow()).lower())) or (title == 'chocolatey-update'):
        #     continue
        if title in GetWindowText(GetForegroundWindow()).lower():
            pyautogui.hotkey('alt', 'f4')
            notifier = ToastNotifier()
            # notifier.show_toast("Warning!", f"Focus on your goal! (Err: {title} was blocked)", duration = 2.5, icon_path = "C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\target.ico")
    for proc in psutil.process_iter():
        try:
            if process in proc.name().lower():
                proc.kill()
                notifier = ToastNotifier()
                # notifier.show_toast("Warning!", f"Focus on your goal! 🎯 (Err: {process} was blocked)", duration = 2.5, icon_path = "C:\\Users\\Aarjav\\Documents\\Automation Programs\\curbing distractions\\target.ico")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

appsList = ('calibre', 'taskmgr', 'windowsterminal')
title_list = ('ahk', 'cmd', 'visual studio code', 'administrator: windows powershell', 'task scheduler', 'autohotkey help', 'microsoft store', 'chocolatey-update', 'curbing distractions', 'app_blocker', 'app_blocker.py', 'shut down windows', 'website_blocker')
""" def appBlock(mins):
    timeNow = time.strftime('%H:%M')
    targetTime = str(int(timeNow[0:2]) + (mins // 60)) + ":" + time.strftime('%M')
    while targetTime != timeNow:
        for i in range (1, mins + 1):
            for app in appsList:
                checkRunningProcess(app)

appBlock(1440) """

def appBlock(mins):
    # Identify the date and time
    now = time.strftime("%H:%M")
    minutes = []
    for i in range (30, 60):
        minutes.insert(i - 30, f"22:{i}")
    while now not in minutes:
        for app in appsList:
            checkRunningProcess(app)