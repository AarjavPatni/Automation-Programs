from requests import get, post
from os import getenv
from dotenv import load_dotenv

load_dotenv(
    r'C:\Users\Aarjav\Documents\Automation-Programs\Habitica\habitica.env')
habToken = getenv('KEY')
habId = getenv('ID')


def askUserForChoice():
    global habitOptions, selectedOption, habitToCheck, loss

    habitOptions = [r"![](https://cdn-icons-png.flaticon.com/24/3408/3408148.png) Alarm-Assassin's Death",
                    r"![](https://cdn-icons-png.flaticon.com/24/4951/4951962.png) The Saboteur",
                    r"![](https://cdn-icons-png.flaticon.com/24/3177/3177429.png) Wielding the Shield",
                    r"![](https://cdn-icons-png.flaticon.com/24/3563/3563395.png) Activating Beast Mode"]
    selectedOption = int(input(
        'Please select one of the following options:\n' +
        '1. Alarm-Assassin\'s Death\n' +
        '2. The Saboteur\n' +
        '3. Wielding the Shield\n' +
        '4. Activating Beast Mode\n' +
        'Choice: '
    ))
    print()

    habitToCheck = habitOptions[selectedOption - 1]
    loss = 0
    if selectedOption == 1:
        loss = 8
    elif selectedOption == 2:
        loss = 10
    elif selectedOption == 3:
        loss = 20
    elif selectedOption == 4:
        loss = 20

    print('You selected: ' + habitToCheck)
    print('Loss: ' + str(loss))


def scheduleCron():
    headers = {
        "x-api-user": habId,
        "x-api-key": habToken,
        'x-client': f'{habId}-Testing',
        'Content-Type': 'application/json'
    }
    response = get(
        "https://habitica.com/api/v3/tasks/user", headers=headers, params={'type': 'habits'})
    response = response.json()
    habit = checkHabitExists(response)
    if habit:
        return scoreHabit(habit['id'])


def scoreHabit(id):
    headers = {
        "x-api-user": habId,
        "x-api-key": habToken,
        'x-client': f'{habId}-Testing',
        'Content-Type': 'application/json'
    }
    for i in range(1, loss + 1):
        response = post(
            f"https://habitica.com/api/v3/tasks/{id}/score/down", headers=headers)
        if response.status_code == 200:
            print('Scoring successful')
        else:
            print(f'There was an issue scoring the habit: {response.content}')


def checkHabitExists(response):
    for habit in response["data"]:
        if habit["text"].strip().lower() == habitToCheck.strip().lower():
            return habit
    return None


askUserForChoice()
scheduleCron()
