#!/usr/bin/env python3
from todoist_api_python.api import TodoistAPI
import datetime
import threading, os

key = os.environ.get('todoist.env')
api = todoist.TodoistAPI(key)

project_id_list = []

def get_data():
    global projects
    global project_id_list
    global tasks
    
    projects = api.get_projects()
    tasks = api.get_tasks()
    projects = [project for project in projects if "Dummy" not in project.name]
    project_id_list = [project.id for project in projects]

threading.Thread(target=get_data).start()

# Ask user if he wants to reschedule tasks due today or tomorrow
ch = input("Would you like to reschedule tasks due today(1) or tomorrow(2)? ")

# Get today's date in the format "YYYY-MM-DD"
today = datetime.datetime.today().strftime("%Y-%m-%d")
tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

def displayer(date):
    global findItems
    global api
    global due_today_list
    global due_today_list_id
    global tasks
    global project_id_list

    due_today_list = []
    due_today_list_id = []

    def findItems(i):
        global due_today_list
        global due_today_list_id

        for task in tasks:
            try:
                if task.due.date == date and task.due.recurring == False and task.project_id == i:
                    due_today_list.append({'project_id': i, 'content': task.content, 'section_id': task.section_id, 'order': task.order})
                    due_today_list_id.append(task.id)
            except:
                pass
    
    for t in threading.enumerate():
        if t is not threading.current_thread():
            t.join()

    for i in project_id_list:
        threading.Thread(target=findItems, args=(i,)).start()
    
    # Wait for all threads to finish
    for t in threading.enumerate():
        if t is threading.current_thread():
            continue
        t.join()
    
    print()
    print(str(len(due_today_list)) + " tasks due today.")
    print()
    
    # Sort all tasks in due_today_list by section_id and order
    due_today_list = sorted(due_today_list, key=lambda k: (k['section_id'], k['order']))

    for i in due_today_list:
        print(i['content'])


if ch == "1" or ch == "":
    displayer(today)
elif ch == "2":
    displayer(tomorrow)
