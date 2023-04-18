# Get a list of all running processes
from psutil import process_iter
from time import perf_counter, sleep
from os import system
from datetime import datetime as dt

if dt.now().hour >= 22:
    system("wsl '/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe' -start 'Distractions' -lock 300 &")
    duration = 300
else:
    system("wsl '/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe' -start 'Distractions' -lock 60 &")
    duration = 60

start = perf_counter()

# print(pnames)
while perf_counter() - start < duration*60:
    killed = False
    pids = [p.pid for p in process_iter()]
    pnames = [p.name() for p in process_iter()]

    if 'CTMsgHostEdge.exe' not in pnames:
        print('Killing...')
        # kill msedge.exe
        for proc in process_iter():
            if proc.name() == 'msedge.exe':
                try:
                    proc.kill()
                    killed = True
                except:
                    pass

    if killed:
        sleep(15)
