import requests
import os
from dotenv import load_dotenv
import json
from time import sleep as s

load_dotenv('C:\\Users\\Aarjav\\Documents\\Quick Add\\secret.env')
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
ch = int(input('Doubt (1) or Distraction (2)? '))

if ch == 1:
    subList = ['Physics', 'Physical Chemistry', 'Inorganic Chemistry', 'Organic Chemistry', 'Mathematics'] 
    subs = 'Physics (1)\nPhysical Chemistry (2)\nInorganic Chemistry (3)\nOrganic Chemistry (4)\nMathematics (5)\n'
    sub = subList[int(input(subs)) - 1]
    dbt = input('Enter your doubt: ')
    id = "2ab41a82-f3d6-4be4-b2ef-f3496fb671a1"
    data = { "parent": { "database_id": "2ab41a82f3d64be4b2eff3496fb671a1" }, "properties": { "Doubt": { "title": [ { "text": { "content": dbt } } ] }, "Subject": { "select": { "name": sub } }, "Type": { "select": { "name": "Doubt" } }, "Cleared": { "checkbox": False }}}
    data = json.dumps(data)
    headers = {
    'Authorization': f"Bearer {NOTION_TOKEN}",
    'Notion-Version': '2021-05-13',
    'Content-Type': 'application/json',
    }
    response = requests.post('https://api.notion.com/v1/pages', headers=headers, data=data)
elif ch == 2:
    subList = ['Physics', 'Physical Chemistry', 'Inorganic Chemistry', 'Organic Chemistry', 'Mathematics'] 
    subs = 'Physics (1)\nPhysical Chemistry (2)\nInorganic Chemistry (3)\nOrganic Chemistry (4)\nMathematics (5)\n'
    subChoice = input(subs)
    dist = input('Enter the distraction: ')
    id = "2ab41a82-f3d6-4be4-b2ef-f3496fb671a1"
    if subChoice == "":
        data = { "parent": { "database_id": "2ab41a82f3d64be4b2eff3496fb671a1" }, "properties": { "Doubt": { "title": [ { "text": { "content": dist } } ] }, "Type": { "select": { "name": "Distraction" } }, "Cleared": { "checkbox": False }}}
    else:
        sub = subList[int(subChoice)- 1]
        data = { "parent": { "database_id": "2ab41a82f3d64be4b2eff3496fb671a1" }, "properties": { "Doubt": { "title": [ { "text": { "content": dist } } ] }, "Subject": { "select": { "name": sub } }, "Type": { "select": { "name": "Distraction" } }, "Cleared": { "checkbox": False }}}
    data = json.dumps(data)
    headers = {
    'Authorization': f"Bearer {NOTION_TOKEN}",
    'Notion-Version': '2021-05-13',
    'Content-Type': 'application/json',
    }
    response = requests.post('https://api.notion.com/v1/pages', headers=headers, data=data)