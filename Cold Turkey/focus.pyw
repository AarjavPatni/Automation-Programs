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
    system("wsl '/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe' -start 'Distractions' -lock 120 &")
    duration = 120

start = perf_counter()

# Create function to kill process called winget


def kill_winget():
    while perf_counter() - start < duration*60:
        for proc in process_iter():
            if ('winget' in proc.name()) or ('unins000' in proc.name()):
                proc.kill()


Thread(target=kill_winget).start()

# print(pnames)
while perf_counter() - start < duration*60:
    killed = False
    # pids = [p.pid for p in process_iter()]
    pnames = [p.name() for p in process_iter()]

    if 'CTMsgHostEdge.exe' not in pnames:
        # kill msedge.exe
        sleep(20)
        pnames = [p.name() for p in process_iter()]
        if 'CTMsgHostEdge.exe' not in pnames:
            for proc in process_iter():
                try:
                    proc.kill() if proc.name() == 'msedge.exe' else None
                except:
                    pass
