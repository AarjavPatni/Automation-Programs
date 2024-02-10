import pyautogui
import time
import sys
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

day = time.localtime().tm_mday
month =  time.localtime().tm_mon
year = time.localtime().tm_year
date = f"{month}/{day}/{year}"
g, p, c, m, e, me = "2020/G11A/(Naveen Noronha)", "physics", "chem", "math", "english", "moral"
def win_search():
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.001
    pyautogui.keyDown('win')
    pyautogui.keyDown('d')
    pyautogui.keyUp('d')
    pyautogui.keyUp('win')
    pyautogui.keyDown('win')
    pyautogui.keyDown('s')
    pyautogui.keyUp('s')
    pyautogui.keyUp('win')
    time.sleep(3)
    pyautogui.typewrite("Microsoft Teams")
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True
def window_max():
    pyautogui.PAUSE = 0.001
    pyautogui.keyDown('win')
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')
    pyautogui.keyUp('win')
    pyautogui.PAUSE = 1
def check():
    teams_check = pyautogui.locateOnScreen('teams.png', region = (52, 0, 274, 42))
    teams_check_black = pyautogui.locateOnScreen('teams_black.png', region = (52, 0, 162, 44))
    teams_check_purple = pyautogui.locateOnScreen('teams_purple.png', region = (52, 0, 224, 47))
    while(teams_check == None and teams_check_black == None and teams_check_purple == None):
        teams_check = pyautogui.locateOnScreen('teams.png', region = (52, 0, 274, 42))
        teams_check_black = pyautogui.locateOnScreen('teams_black.png', region = (52, 0, 162, 44))
        teams_check_purple = pyautogui.locateOnScreen('teams_purple.png', region = (52, 0, 224, 47))
    else:
        pyautogui.click(245, 0)
        window_max()
        pass
def form_check():
    pyautogui.PAUSE = 0.01
    forms_check = pyautogui.locateOnScreen('form.png', region = (784, 437, 557, 48))
    forms_check_chem = pyautogui.locateOnScreen('form_chem.png', region = (889, 461, 458, 51))
    forms_check_math = pyautogui.locateOnScreen('form_math.png', region = (970, 461, 375, 50))
    while(forms_check == None and forms_check_chem == None and forms_check_math == None):
        window_max()
        forms_check = pyautogui.locateOnScreen('form.png', region = (784, 437, 557, 48))
        forms_check_chem = pyautogui.locateOnScreen('form_chem.png', region = (889, 461, 458, 51))
        forms_check_math = pyautogui.locateOnScreen('form_math.png', region = (970, 461, 375, 50))
    else:
        pass
    pyautogui.PAUSE = 1
def fill_form_custom(sub, tx, ty, nx, ny, dx, dy, enterx, entery):
    def navigate():
        pyautogui.hotkey('ctrl', '/')
        pyautogui.write("goto ")
        pyautogui.write(sub)
        pyautogui.write(['enter'])
        time.sleep(3)
    def form_fill():
        pyautogui.click(tx, ty)
        pyautogui.click(1862, 77)
        form_check()
        pyautogui.PAUSE = 0.01
        pyautogui.click(nx, ny)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write("Aarjav Patni")
        pyautogui.write(['tab'])
        pyautogui.typewrite(date)
        pyautogui.click(enterx, entery)
        pyautogui.PAUSE = 1
    navigate()
    form_fill()
    time.sleep(3)
    pyautogui.PAUSE = 0.01
    pyautogui.hotkey('alt', 'tab')
    pyautogui.PAUSE = 1
    time.sleep(3)
def fill_form():
    fill_form_custom(g, 997, 86, 787, 457, 892, 610, 662, 716)
    fill_form_custom(p, 751, 80, 801, 461, 884, 604, 685, 715)
    fill_form_custom(c, 1013, 86, 1075, 483, 932, 630, 691, 742)
    fill_form_custom(m, 1302, 84, 835, 485, 804, 631, 673, 739)
    fill_form_custom(e, 751, 80, 801, 461, 884, 604, 685, 715)

day_week = time.localtime().tm_wday
if (day_week == 0):
    try:
        print("Marking attendance...")
        win_search()
        check()
        fill_form()
        fill_form_custom(me, 859, 81, 772, 487, 789, 629, 673, 737)
        pyautogui.PAUSE = 0.01
        pyautogui.hotkey('alt', 'tab')
    except(pyautogui.FailSafeException):
        print("Fail-safe triggered and program terminated...")
        input("Press enter to exit")
        sys.exit()
    except:
        print("Some error occurred :(")
        input("Press enter to exit")
        sys.exit()
else:
    try:
        print("Marking attendance...")
        win_search()
        check()
        fill_form()
        pyautogui.PAUSE = 0.01
        pyautogui.hotkey('alt', 'tab')
    except(pyautogui.FailSafeException):
        print("Fail-safe triggered and program terminated...")
        input("Press enter to exit")
        sys.exit()
    except:
        print("Some error occurred :(")
        input("Press enter to exit")
        sys.exit()