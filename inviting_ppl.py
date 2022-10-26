import pyautogui, time

students = ['Aarjav Patni', 'Kevalya Tejas Shah', 'Nandika Rajesh', 'Ritvik Bhatnagar', 'Shivang Majumdar', 'Shahadeel Mohammed', 'Sharique Khatri', 'Zayeem Sahib Mitayeegiri', 'Ali Hussain Syed', 'Nikhilesh Gavankar', 'Richa Kewalramani', 'Shreya Kamath', 'Dylan Dias', 'Saad Omer Mohammed', 'Adithya Manoj Nair', 'Rohan Ashar', 'Sairam Nagarajan', 'Siddhant Misra', 'Muhammed Anas', 'Ayman Ali Syed Ali']
x = 0
for i in students:
    print(i, f"({x})")
    x += 1
    
check = input('\nAny absentees? (y/n)')
if check == 'y':
    a = input('Enter the number corresponding to the absent students, seperated by a comma: ')
    a = a.replace(' ', '')
    a = a.split(',')
    dupli = students.copy()
    for i in a:
        i = int(i)
        dupli.remove(students[i])
    students = dupli

wait = 'Return to teams and click the invite box. I will invite everyone automatically. Waiting for you do that for 5 seconds... \n'
countdown = '5... 4... 3... 2... 1...'

for i in wait:
    print(i, flush=True, end='')
    time.sleep(0.025)
    
time.sleep(2)
for i in countdown:
    if i == ' ':
        time.sleep(1)
        print(i, end='', flush=True)
    else:
        print(i, end='', flush=True)
else:
    time.sleep(2)
    for i in students:
        pyautogui.write(['backspace'])
        pyautogui.keyDown('alt')
        pyautogui.keyDown('a')
        pyautogui.keyUp('alt')
        pyautogui.keyUp('a')
        pyautogui.write(['backspace'])
        pyautogui.write(i)
        time.sleep(3)
        pyautogui.write(['enter'])
