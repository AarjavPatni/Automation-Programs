import ctypes, os, subprocess, pyautogui, time, sys, datetime
from subprocess import CalledProcessError, run
import tkinter as tk
from tkinter import simpledialog

total = -30

if total < 0:
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