#!/usr/bin/env /bin/python3
import requests
import dotenv, os
import json
import time
import multiprocessing as mp
import sys

# Load habitica.env file and KEY variable
dotenv.load_dotenv('/home/aarjav/Documents/Habitica/habitica.env')
KEY = os.getenv('KEY')
USER = os.getenv('USER_KEY')
USER_CLIENT = f'{USER}-Testing'

# Use GET to get tasks. Request url = 'https://habitica.com/api/v3/tasks/user'. Query = type:"todos"
response = requests.get('https://habitica.com/api/v3/tasks/user', headers={'x-api-user': USER, 'x-api-key': KEY, 'x-client': USER_CLIENT, 'Content-Type': 'application/json'}, params={'type': 'todos'})

# Convert response json to python dictionary
resp = response.json()

# Print pretty json
# print(json.dumps(resp, indent=4, sort_keys=True))
try:
    if resp['error'] == 'TooManyRequests':
        import subprocess as sp
        sp.run(['notify-send', 'Habitica API', 'Too many requests.'])
        resp = requests.get('https://habitica.com/api/v3/tasks/user', headers={'x-api-user': USER, 'x-api-key': KEY, 'x-client': USER_CLIENT, 'Content-Type': 'application/json'}, params={'type': 'todos'}).json()
        try:
            while resp['error'] == 'TooManyRequests':
                resp = requests.get('https://habitica.com/api/v3/tasks/user', headers={'x-api-user': USER, 'x-api-key': KEY, 'x-client': USER_CLIENT, 'Content-Type': 'application/json'}, params={'type': 'todos'}).json()
        except:
            sp.run(['notify-send', 'Habitica API', 'Functionality restored.'])
except:
    pass

tasks = resp['data']

for pos, task in enumerate(tasks):
    print(f'{pos+1}. {task["text"]}')
print()

tasks_to_edit = input('Enter tasks to edit: ').split(', ')
if tasks_to_edit == ['']:
    tasks_to_edit = [int(x) for x in range(1, len(tasks)+1)]
elif '-' in tasks_to_edit[0]:
    tasks_to_edit = [int(x) for x in tasks_to_edit[0].split('-')]
    tasks_to_edit = [int(x) for x in range(tasks_to_edit[0], tasks_to_edit[1]+1)]
print()

choice = int(input('''What would you like to edit?
1. Difficulty
2. Tags
3. Due Date
4. Delete

Choice: ''')); print()

if choice == 1:
    difficulty_dict = {0.1: 'trivial', 1: 'easy', 1.5: 'medium', 2: 'hard'}
    difficulty = input('''1. Trivial
2. Easy
3. Medium
4. Hard

Enter difficulty: '''); print()

    try:
        difficulty = list(difficulty_dict.keys())[int(difficulty)-1]
    except:
        for i in list(difficulty_dict.values()):
            if difficulty.lower() in i:
                difficulty = list(difficulty_dict.values()).index(i) + 1
                difficulty = list(difficulty_dict.keys())[difficulty-1]
                break
    
    def edit_difficulty(task):
        response = requests.put('https://habitica.com/api/v3/tasks/' + tasks[int(task)-1]['id'], headers={'x-api-user': USER, 'x-api-key': KEY, 'x-client': USER_CLIENT, 'Content-Type': 'application/json'}, data=json.dumps({'priority': difficulty}))
        if response.json()['success'] == False and response.json()['error'] == 'TooManyRequests': print("Too many requests!"); sys.exit()
        print(f'Edited for \"{list(tasks)[int(task)-1]["text"]}\"') if response.json()['success'] == True else print(f'Failed for \"{list(tasks)[int(task)-1]["text"]}\" because {response.json()["error"]}')
    
    for task in tasks_to_edit:
        mp.Process(target=edit_difficulty, args=(task,)).start()
elif choice == 2:
    response = requests.get('https://habitica.com/api/v3/tags', headers={'x-api-user': USER, 'x-api-key': KEY, 'x-client': USER_CLIENT, 'Content-Type': 'application/json'})
    # Pretty print json
    # print(json.dumps(response.json(), indent=4, sort_keys=True))
    tags_dict = dict(zip([i['name'] for i in response.json()['data']], [i['id'] for i in response.json()['data']]))
    # Print tags names prefixed with numbers
    for pos, tag in enumerate(tags_dict):
        print(f'{pos+1}. {tag}')
    print()

    tag = input('Enter tag: '); print()
    try:
        tag = [int(i) for i in tag.split(', ')]
    except:
        tag = tag.split(', ')
        tag_int = []
        for j in tag:
            for i in tags_dict:
                if j.capitalize() in i:
                    tag_int.append([i['name'] for i in response.json()['data']].index(i) + 1)
                    break
        tag = tag_int
                
    def tagger(task):
        for i in tag:
            response = requests.post('https://habitica.com/api/v3/tasks/' + tasks[int(task)-1]['id'] + '/tags/' + str(tags_dict[list(tags_dict)[i - 1]]), headers={'x-api-user': USER, 'x-api-key': KEY, 'x-client': USER_CLIENT, 'Content-Type': 'application/json'})
        if response.json()['success'] == False and response.json()['error'] == 'TooManyRequests': print("Too many requests!"); sys.exit()
        print(f'Tagged \"{list(tasks)[int(task)-1]["text"]}\"') if response.json()['success'] == True else print(f'Failed to tag \"{list(tasks)[int(task)-1]["text"]}\" because {response.json()["error"]}')
    
    for task in tasks_to_edit:
        mp.Process(target=tagger, args=(task,)).start()
elif choice == 3:
    choice = input('Today (1) or tomorrow (2) or enter date (3): '); print()
    if choice in ('1', ''):
        date = time.strftime('%d %b %Y')
    elif choice == '2':
        date = time.strftime('%d %b %Y', time.localtime(time.time() + 86400))
    else:
        date = input('Enter date (dd mm yyyy): '); print()
        date = time.strftime('%d %b %Y', time.strptime(date, '%d %b %Y'))
    def change_due(task):
        response = requests.put('https://habitica.com/api/v3/tasks/' + tasks[int(task)-1]['id'], headers={'x-api-user': USER, 'x-api-key': KEY, 'x-client': USER_CLIENT, 'Content-Type': 'application/json'}, data=json.dumps({'date': date}))
        if response.json()['success'] == False and response.json()['error'] == 'TooManyRequests': print("Too many requests!"); sys.exit()
        print(f'Set for \"{list(tasks)[int(task)-1]["text"]}\"') if response.json()['success'] == True else print(f'Failed for \"{list(tasks)[int(task)-1]["text"]}\" because {response.json()["error"]}')
    for task in tasks_to_edit:
        mp.Process(target=change_due, args=(task,)).start()
elif choice == 4:
    def delete(task):
        response = requests.delete('https://habitica.com/api/v3/tasks/' + tasks[int(task)-1]['id'], headers={'x-api-user': USER, 'x-api-key': KEY, 'x-client': USER_CLIENT, 'Content-Type': 'application/json'})
        if response.json()['success'] == False and response.json()['error'] == 'TooManyRequests': print("Too many requests!"); sys.exit()
        print(f'Deleted \"{list(tasks)[int(task)-1]["text"]}\"') if response.json()['success'] == True else print(f'Failed to delete \"{list(tasks)[int(task)-1]["text"]}\" because {response.json()["error"]}')

    for task in tasks_to_edit:
        mp.Process(target=delete, args=(task,)).start()