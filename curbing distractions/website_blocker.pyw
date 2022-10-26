import ctypes, os, subprocess, pyautogui, time, sys, datetime
from subprocess import CalledProcessError, run
import tkinter as tk
from tkinter import simpledialog

# Find time difference between now and 11pm
now = datetime.datetime(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")), int(time.strftime('%H')), int(time.strftime('%M')))
target = datetime.datetime(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")), 22, 50)
difference = str(target - now)
print(difference.split(':'))
total = (int(difference.split(':')[0]) * 60) + int(difference.split(':')[1])
print(total)

if total <= 0 or total >= 990:
    ROOT = tk.Tk()
    ROOT.withdraw()
    keywords = simpledialog.askstring(title="Keywords", prompt="List all study-related phrases separated by commas:")
    print(keywords)
    keywords = keywords.replace(', ', ',')
    keywords = keywords.replace(',  ', ',')
    dists = keywords.split(',')
    ctb_path = "\"C:\\Program Files\\Cold Turkey\\Cold Turkey Blocker.exe\""
    for i in dists:
        if (i != '') and (i != '**') and (i != '*.*') and (i != '\n'):
            try:
                run(f'{ctb_path} -add Distractions -exception \"*{i}*\"', check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except CalledProcessError:
                print("Failed!")
else:
    ctb_path = "\"C:\\Program Files\\Cold Turkey\\Cold Turkey Blocker.exe\""
    run(f'{ctb_path} -start Distractions -lock {total}', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)