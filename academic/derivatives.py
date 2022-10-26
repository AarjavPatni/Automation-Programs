import pyautogui as pg

while True:
    arg = input('Enter the arg: ')
    pg.hotkey('alt', 'tab')
    pg.sleep(1)
    pg.write(f'\\[\\frac{{\\mathrm{{d}}}}{{\\mathrm{{d}} x}} ({arg}) =\\]')
