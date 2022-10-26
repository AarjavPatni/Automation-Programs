import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.25

allowed = ("SUNLIGHT", "CARBON", "DIOXIDE", "WATER", "ENERGY", "LIGHT", "TEMPERATURE", "HUMIDITY", "CATALYST", "HEAT")
elements_caps = ("HE", "LI", "BE", "NE", "NA", "AL", "BR", "AR", "ZN", "CA", "GE", "CU", "AU", "SN", "TN", "PB", "CR", "HG", "FE")
elements = ("He", "Li", "Be", "Ne", "Na", "Al", "Br", "Ar", "Zn", "Ca", "Ge", "Cu", "Au", "Sn", "Tn", "Pb", "Cr", "Hg", "Fe")
def notion_format(arg):
    for i in arg:
        if i == '^':
            pyautogui.write(pyperclip.paste())
            pyautogui.write('$')
            pyautogui.write(['space'])
            time.sleep(5.5)
            continue
        try:
            p = int(i)
        except ValueError:
            pyautogui.write(i)
            continue
        pyautogui.write('$$')
        time.sleep(0.5)
        pyautogui.write(f'\\sf{{_{p}}}')
        pyautogui.write(['enter'])

def notion_format1(arg, q):
    for i in arg:
        try:
            p = int(i)
        except ValueError:
            q = q + i
            continue
        q = q + f'_{p} '
    pyperclip.copy(q)

formula = input("Enter the formula or equation: ")
while True:
    formula = formula.upper()
    if ("-->" in formula) or ("→" in formula):
        up = input("Enter the condition above: ").upper()
        for i in allowed:
            if i in up:
                up = up.replace(i, i.lower())
            else:
                continue
        up1 = ""
        notion_format1(up, up1)
        up1 = pyperclip.paste()
        down = input("Enter the condition below: ").upper()
        for i in allowed:
            if i in down:
                down = down.replace(i, i.lower())
            else:
                continue
        down1 = ""
        notion_format1(down, down1)
        down1 = pyperclip.paste()
        pyautogui.hotkey('ctrl', 'shift', 'e')
        formula = formula.replace('-->', '^')
        formula = formula.replace('→', '^')
        arrow = f'$$\\large{{\\xrightarrow[\sf{{{down1}}}]{{\sf{{{up1}}}}}}}$'
        for i in elements_caps:
            if i in arrow:
                loc = elements_caps.index(i)
                arrow = arrow.replace(i, elements[loc])
        pyperclip.copy(arrow)
    
    for i in allowed:
        if i in formula:
            formula = formula.replace(i, i.lower())
        else:
            continue

    for i in elements_caps:
        if i in formula:
            loc = elements_caps.index(i)
            formula = formula.replace(i, elements[loc])
    
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    
    notion_format(formula)

    retry = input("Again? ")
    if (retry == "") or (retry == "n"):
        break
    else:
        formula = retry
        continue