# Get a list of all running processes
from psutil import process_iter
from time import perf_counter, sleep
from os import system
from datetime import datetime as dt
from threading import Thread

if dt.now().hour >= 22:
    system("wsl '/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe' -start 'Distractions' -lock 300 &")
    duration = 300
else:
    system("wsl '/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe' -start 'Distractions' -lock 60 &")
    duration = 60

start = perf_counter()

# Create function to kill process called winget


def kill_winget():
    while perf_counter() - start < duration*60:
        for proc in process_iter():
            if 'winget' in proc.name():
                proc.kill()


Thread(target=kill_winget).start()

# print(pnames)
while perf_counter() - start < duration*60:
    killed = False
    # pids = [p.pid for p in process_iter()]
    pnames = [p.name() for p in process_iter()]

    if 'CTMsgHostEdge.exe' not in pnames:
        # kill msedge.exe
        for proc in process_iter():
            if proc.name() == 'msedge.exe':
                try:
                    sleep(15)
                    pnames = [p.name() for p in process_iter()]
                    proc.kill() if 'CTMsgHostEdge.exe' not in pnames else None
                except:
                    pass
