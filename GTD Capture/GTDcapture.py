# -*- coding: utf-8 -*-
# import json
# import os
# import readline

# from threading import Thread

# import requests
# from dotenv import load_dotenv
# from pyautogui import hotkey


import time
from pathlib import Path

def printByChar(string, ends="\n"):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(0.01)
    if ends == "\n":
        print()


# response_code_list = []

# load_dotenv(r"/home/aarjav/Documents/GTD Capture/NOTION_KEY.env")
# NOTION_KEY = os.getenv("NOTION_KEY")

# headers = {
#     "Authorization": "Bearer {}".format(NOTION_KEY),
#     "Notion-Version": "2021-08-16",
#     "Content-Type": "application/json",
# }

# url = r"
#   https://api.notion.com/v1/blocks/87ff453d-6ad8-45ee-8aac-97234dd74c54/children
#   "
# page_id = "87ff453d-6ad8-45ee-8aac-97234dd74c54"


# def capture(element):
#     data = {
#         "children": [
#             {
#                 "object": "block",
#                 "type": "paragraph",
#                 "paragraph": {
#                     "text": [
#                         {
#                             "type": "text",
#                             "text": {
#                                 "content": element,
#                                 "link": None,
#                             },
#                         }
#                     ]
#                 },
#             }
#         ]
#     }
#     # Send data to Notion using data variable
#     response = requests.patch(
#                           data=json.dumps(data), headers=headers, url=url
#                       )
#     response_code_list.append(response.status_code)


# def captureTweet(element):
#     url = "https://api.notion.com/v1/pages"

#     payload = {
#         "parent": {
#             "type": "database_id",
#             "database_id": "4b3d588e0c6f43eeb99d8c02910dd26b",
#         },
#         "properties": {
#             "Idea": {
#                 "type": "title",
#                 "title": [{ "type": "text", "text": { "content": element } }]
#             },
#         }
#     }

#     response = requests.post(url, json=payload, headers=headers)

#     print(response.text)


# print("Press Ctrl+C or enter q to quit. Start with 't ' for a Tweet idea.")
# while True:
#     try:
#         # Start a new thread to capture the input
#         inputData = input()
#         if inputData.lower() == "q":
#             break
#         if inputData != "":
#             if inputData[0:2] == "t ":
#                 Thread(target=captureTweet, args=(inputData,)).start()
#             else:
#                 Thread(target=capture, args=(inputData,)).start()
#     except KeyboardInterrupt:
#         inputData = list(set(response_code_list))
#         if len(response_code_list) > 1:
#             sp.run(["notify-send", "GTD Capture", "Error!"])
#         else:
#             sp.run(["notify-send", "GTD Capture", "Captured!"])
#         break

print(
    """Tags:
1. academics (a)
2. research-topics (r)
3. thoughts (t)
4. geeky todos (g)
5. to-note (n)
6. tweet ideas (tw)
"""
)


endCharList = ["a", "t", "n", "r", "g", "tw"]

tagsList = ["01 Academics", "02 Thoughts", "03 To-Note", "04 Research Topics", "05 Geeky Todos", "06 Tweet Ideas"]


'''def findItem(theList, item):
    return [
        (ind, theList[ind].index(item))
        for ind in range(len(theList))
        if item in theList[ind]
    ]

while True:
    tagsDict = {
        "Academics": ["a"],
        "Research Topics": ["r"],
        "Thoughts": ["t"],
        "To-Note": ["n"],
        "Tweet Ideas": ["tw"],
        "Others": ["o"],
    }

    inputData = input()
    tagsLoc = []

    with open("/home/aarjav/Documents/Second Brain/Inbox.md", "r") as f:
        content = f.readlines()  # Read the file contents
        for count, i in enumerate(content, start=0):
            if i.startswith("#"):  # Check if line is heading
                i = i.replace("\n", "")
                tagsDict[i.replace("# ", "")].append(
                    count
                )  # Add line number to the list of tag found

    endChar = inputData.split(" ")[-1]  # Get the inputted tag
    inputData = (
        " ".join(inputData.split(" ")[:-1])
        if inputData.split(" ")[-1] in endCharList
        else inputData
    )

    try:
        if endChar in endCharList:
            content.insert(
                tagsDict[
                    list(tagsDict.keys())[
                        findItem(list(tagsDict.values()), endChar)[0][0] + 1
                    ]
                ][1]
                - 2,
                inputData + "\n",
            )
        else:
            content.append(inputData + "\n")
    except Exception as e:
        print(e)
        content.append(inputData)

    with open("/home/aarjav/Documents/Second Brain/Inbox.md", "w") as f:
        f.writelines(content)

    print("\x1b[1A" + f"\x1b[{len(inputData) + 1}C" + " ✅")'''


while True:
    inputData = input().replace("\u2192", "->")
    endChar = inputData.split(" ")[-1]

    inputData = (
        " ".join(inputData.split(" ")[:-1])
        if inputData.split(" ")[-1] in endCharList
        else inputData
    )

    inputData = f'- [ ] {inputData[2:]}\n' if inputData[0:2] == 'o ' else inputData

    if endChar in endCharList:
        with open(
            Path(f"C:/Users/Aarjav/Documents/Second Brain/Inbox/{tagsList[endCharList.index(endChar)]}.md"),
            "a", encoding='utf-8'
        ) as f:
            f.writelines(f'\n{inputData}'.replace('->', '\u2192'))
    else:
        with open(Path("C:/Users/Aarjav/Documents/Second Brain/Inbox/02 Thoughts.md"), "a", encoding='utf-8') as f:
            f.writelines(f'\n{inputData}'.replace('->', '\u2192'))

    print("\x1b[1A" + f"\x1b[{len(inputData) + 1}C" + " ✅")
