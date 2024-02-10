import pyautogui as pg

while True:
    try:
        comp = input("Compound: ")
        color = input("Color: ")
        state = input("State: ")
        struc = input("Structure: ")
        pg.sleep(1)
        pg.write(f'\(\ce{{{comp}}}\) is an {{{{c1::{color}::colour}}}} {{{{c1::{state}::physical state}}}} having a {{{{c1::{struc}::structure}}}}.')
        print('\n')
    except KeyboardInterrupt:
        print('\n')
        continue