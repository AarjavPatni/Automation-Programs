import subprocess
import pyautogui as pg
from subprocess import Popen as p

command = r"Disable-PnpDevice -Confirm:$false -InstanceId (Get-PnpDevice -Class AudioEndpoint -Status OK).InstanceId"

p("powershell.exe")
pg.sleep(2)
pg.write(command)
pg.press("enter")
pg.sleep(2)
pg.write("exit")
pg.press("enter")