import pyautogui as pg

while True:
    rows = int(input("Enter the number of rows: ")) - 1
    matrix = r"\begin{vmatrix} "
    current_row = ""
    count2 = 0
    while rows >= 0:
        row_count = 1
        current_row = ""
        if count2 != rows:
            matrix += current_row
            row = input(f"Enter row {row_count}: ")
            row = row.split(" ")
            length = len(row)
            for count, j in enumerate(row):
                if count != length - 1:
                    current_row += f"{j} & "
                else:
                    current_row += f"{j}"
            current_row += " \\\\ "
        else:
            matrix += current_row
            row = input(f"Enter row {row_count}: ")
            row = row.split(" ")
            length = len(row)
            for count, j in enumerate(row):
                if count != length - 1:
                    current_row += f"{j} & "
                else:
                    current_row += f"{j}"
        matrix += current_row
        rows -= 1
        row_count += 1
    matrix += " \\end{vmatrix}"
    pg.hotkey("alt", "tab")
    pg.sleep(1)
    pg.write(matrix)
