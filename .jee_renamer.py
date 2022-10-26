from cgitb import reset
import os
from signal import pause
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from re import finditer, sub
from pathlib import Path

os.popen('notify-send "JEE Renamer" "Script started!"')

time.perf_counter()
tic = time.perf_counter() - 25

class OnMyWatch:
    watchDirectory = "/home/aarjav/pCloudDrive/IIT JEE Notes"
  
    def __init__(self):
        self.observer = Observer()
  
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        self.observer.join()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()

  
class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        
        elif event.event_type == 'created':
            rename(event.src_path) if bool((time.perf_counter() - tic) > 10) and ('refresh' not in event.src_path) else None
            # print("Watchdog received created event - % s." % event.src_path) if 'refresh' not in event.src_path else None
        elif event.event_type == 'modified':
            rename(event.src_path) if bool((time.perf_counter() - tic) > 10) and ('refresh' not in event.src_path) else None
            # print("Watchdog received modified event - % s." % event.src_path) if 'refresh' not in event.src_path else None
        elif event.event_type == 'moved':
            rename(event.src_path) if bool((time.perf_counter() - tic) > 10) and ('refresh' not in event.src_path) else None
            # print("Watchdog received moved event - % s." % event.src_path) if 'refresh' not in event.src_path else None
        elif event.event_type == 'deleted':
            rename(event.src_path) if bool((time.perf_counter() - tic) > 10) and ('refresh' not in event.src_path) else None
            # print("Watchdog received moved event - % s." % event.src_path) if 'refresh' not in event.src_path else None


def rename(file):
    global tic
    tic = time.perf_counter()
    os.popen('notify-send "JEE Renamer" "Detected Changes!"')
    time.sleep(10)
    path = file[:max([i.start() for i in finditer('/', file)])]
    file_paths = sorted(Path(path).iterdir(), key=os.path.getctime)
    counter = 1
    dcs_counter = 1
    for name in file_paths:
        if str(name).endswith('.pdf'):
            baseName = str(name)[max([i.start() for i in finditer('/', str(name))])+1:]
            baseName = sub('L\d* ', '', baseName)
            baseName = baseName.replace('_', ' ')
            baseName = baseName.replace('  ', ' ')
            baseName = baseName.replace(' with anno', '')
            baseName = baseName.replace('Doubt Clearing Session', 'DCS')
            baseName = sub(' \(\d*\)', '', baseName)
            baseName = sub('(DCS).*[^.pdf]', f'DCS-{dcs_counter}', baseName)
            dcs_counter += 1 if 'DCS' in baseName else 0
            print(dcs_counter)
            baseName = f'L{counter} {baseName}'
            newName = f'{path}/{baseName}'
            os.rename(str(name), newName)
            print(str(name)[max([i.start() for i in finditer('/', str(name))])+1:], baseName)
            counter += 1

if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()