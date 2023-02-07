#!/usr/bin/env python3
from todoist_api_python.api import TodoistAPI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r'C:\Users\Aarjav\Documents\Automation-Programs\Todoist-Hyperscheduler\todoist.env')

key = os.environ.get('TODOIST_API_TOKEN')
api = TodoistAPI(key)

tasks = api.get_tasks(label='next-actions')
for task in tasks:
    print(task.content)
