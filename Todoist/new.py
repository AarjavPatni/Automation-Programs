from todoist_api_python.api import TodoistAPI
import os

key = os.environ.get('todoist.env')
api = TodoistAPI(key)

try:
    projects = api.get_projects()
    for i in projects:
        print(getattr(i, 'name'))
except Exception as error:
    print(error)