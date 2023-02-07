#!/usr/bin/env python3
from todoist_api_python.api import TodoistAPI
import os

key = os.environ.get('todoist.env')
api = TodoistAPI(key)

tasks = api.get_tasks(label='next-actions')
print(tasks)
