import pyautogui as pg

while True:
    try:
        reactants = input("Enter the reactants: ")
        products = input("Enter the products: ")
        conditions = input("Enter the conditions (if text, type in {}): ")
        if conditions == "":
            reaction = f"{reactants} -> {products}"
            ch = input('Is it for a cloze deletion (y/N)? ')
            if ch.lower() != "y":
                pg.sleep(1)
                pg.write(f"\\[\\ce{{{reactants} -> {products}}}\]")
                print('Done! \n')
                continue
            pg.sleep(1)
            pg.write(f"Complete the reaction: \\[\\ce{{{reactants} -> {{{{c1::{products}}}}}}}\]")
            print('Done! \n')
        else:
            reaction = f"{reactants} ->{conditions} {products}"
            ch = input('Is it for a cloze deletion (y/N)? ')
            if ch.lower() != "y":
                pg.sleep(1)
                pg.write(f"\\[\\ce{{{reactants} ->[{conditions}] {products}}}\]")
                print('Done! \n')
                continue
            pg.sleep(1)
            pg.write(f"Complete the reaction: \\[\\ce{{{reactants} ->[{conditions}] {{{{c1::{products}}}}}}}]")
            print('Done! \n')
    except KeyboardInterrupt:
        print('\n')
        continue