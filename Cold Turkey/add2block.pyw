from os import system

print('Enter each phrase / word separated by a line:')
while True:
    blocktext = input()
    if blocktext[-2:] != ' q':
        system(
            f"wsl bash -c \"'/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe' -add Distractions -web 'https://*{blocktext}*' & disown\"")
        print("\x1b[1A" + f"\x1b[{len(blocktext) + 1}C" + " ✅")
    elif 'http' in blocktext:
        system(
            f"wsl bash -c \"'/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe' -add Distractions -web '{blocktext}' & disown\"")
        print("\x1b[1A" + f"\x1b[{len(blocktext) + 1}C" + " ✅")
    else:
        system(
            f"wsl bash -c \"'/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe' -add Distractions -web 'https://*.*/*p=*{blocktext[:-2]}*' & disown\"")
        system(
            f"wsl bash -c \"'/mnt/c/Program Files/Cold Turkey/Cold Turkey Blocker.exe' -add Distractions -web 'https://*.*/*q=*{blocktext[:-2]}*' & disown\"")
        print("\x1b[1A" + f"\x1b[{len(blocktext[:-3]) + 1}C" + " ✅")
