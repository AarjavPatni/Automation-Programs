import pyautogui as pg

while True:
    no = int(input('Enter the number of items in the list: '))
    items = []
    for i in range(no):
        e = input(f'{i + 1}. ')
        items.insert(i, e)
    pg.sleep(1)
    pg.write('<ol>')
    for i in items:
        pg.write(f'<li>{i}</li>')
    pg.write('</ol>')
    print('Done!\n')