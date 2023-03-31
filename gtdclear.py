import os
from pathlib import Path

os.system(r'wsl cp ~/Documents/Second\ Brain/Inbox/02\ Thoughts.md ~/Documents/Second\ Brain/Inbox/gtdtemp.md')

with open(r'C:\Users\Aarjav\Documents\Second Brain\Inbox\02 Thoughts.md', 'r') as f:
    lines = f.readlines()
    with open(r'C:\Users\Aarjav\Documents\Second Brain\Inbox\02 Thoughts.md', 'w') as f:
        pass

move_list = []
todo_list = []

print('''Options:
1. Do Now (n)
2. Move to another list (m)
3. Delete (d)
4. Add to todo list (t)
''')

with open(r'C:\Users\Aarjav\Documents\Second Brain\Inbox\02 Thoughts.md', 'w') as f:
    f.writelines('---\ncssclass: inbox\n---\n')

for i in lines:
    if i.replace(' ', '').replace('\n', '') in ('', '---', 'cssclass:inbox'):
        continue
    print(i.replace('\n', '').replace('- [ ] ', ''), end=' ')
    again = True
    while again:
        option = input().lower()
        if option == 'n':
            with open(r'C:\Users\Aarjav\Documents\Second Brain\Inbox\02 Thoughts.md', 'a') as f:
                try:
                    f.readlines()
                except Exception:
                    f.writelines('## Do Now\n')
                f.writelines(f'{i}')
            print('\x1b[1A' + f"\x1b[{len(i) + 1}C" + " ✅")
        elif option == 'm':
            move_list.append(i)
            print('\x1b[1A' + f"\x1b[{len(i) + 1}C" + " ✅")
        elif option == 'd':
            print('\x1b[1A' + f"\x1b[{len(i) + 1}C" + " ✅")
            pass
        elif option == 't':
            todo_list.append(i)
            print('\x1b[1A' + f"\x1b[{len(i) + 1}C" + " ✅")
        else:
            print('Try Again: ', end='')
            continue

        again = False

if todo_list:
    with open(r'C:\Users\Aarjav\Documents\Second Brain\Inbox\02 Thoughts.md', 'a') as f:
        f.writelines('\n\n---\n## Add to todo list')
        for i in todo_list:
            f.writelines(f'{i}\n')

if move_list:
    print()
    gtdlists = {
        'a': '01 Academics',
        'n': '03 To-Note',
        'r': '04 Research Topics',
        'g': '05 Geeky Todos',
        'd': '06 Post-Decisions Research',
        'f': '07 Future Todos',
    }

    print('Tags: ')
    for i in gtdlists:
        print(f'   {gtdlists[i][3:]} ({i})')

    print()

    for i in move_list:
        i = i.replace('\n', '')
        endChar = input(f'{i} ')

        if endChar in gtdlists:
            with open(
                Path(
                    f"C:/Users/Aarjav/Documents/Second Brain/Inbox/{gtdlists[endChar]}.md"),
                "a", encoding='utf-8'
            ) as f:
                f.writelines(f'\n{i}'.replace('->', '\u2192'))
        else:
            with open(Path("C:/Users/Aarjav/Documents/Second Brain/Inbox/02 Thoughts.md"), "a", encoding='utf-8') as f:
                f.writelines(f'\n{i}'.replace('->', '\u2192'))

        print("\x1b[1A" + f"\x1b[{len(i) + 1}C" + " ✅")

os.system(r'wsl rm ~/Documents/Second\ Brain/Inbox/gtdtemp.md')
