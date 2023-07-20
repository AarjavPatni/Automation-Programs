# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json
from dotenv import dotenv_values
import pendulum

sensitive_data = dotenv_values(r'sensitive-data\trello.env')
KEY = sensitive_data['KEY']
TOKEN = sensitive_data['TOKEN']

headers = {
    "Accept": "application/json"
}

query = {
    'key': KEY,
    'token': TOKEN
}


def get_lists():
    url = "https://api.trello.com/1/boards/64704290510a15fdfbdbc9d0/lists"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    print(json.dumps(json.loads(response.text),
                     sort_keys=True, indent=4, separators=(",", ": ")))


def filter_label():
    url = "https://api.trello.com/1/lists/6471af1d2b42ced4485bc25c/cards"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    # Create set of labels from response
    labels = set()
    for card in json.loads(response.text):
        for i in range(len(card['labels'])):
            labels.add(card['labels'][i]['name'])

    # Print all labels
    print("Labels:")
    labels_list = list(labels)
    for index, label in enumerate(labels_list, 1):
        print(f"{index}. {label}")

    choice = int(input("Choose a label: "))
    filtered_cards = []

    for card in json.loads(response.text):
        for i in range(len(card['labels'])):
            if card['labels'][i]['name'] == labels_list[choice - 1]:
                filtered_cards.append(card)

    return filtered_cards


def set_dates():
    filtered_cards = filter_label()
    print()
    due = input("First due date (DD/MM/YYYY): ")
    due = pendulum.from_format(
        due, 'DD/MM/YYYY').at(hour=23, minute=59).subtract(days=2).add(hours=20)

    query = {
        'key': KEY,
        'token': TOKEN,
        'due': due.format("DD/MM/YYYY"),
        'start': 'null'
    }

    print("\nEnter Durations:")

    for card in filtered_cards:
        duration = int(input(f"{card['name']}: "))
        due = due.add(days=duration)

        if duration > 1:
            query['start'] = due.subtract(
                days=duration-1)
        else:
            query['start'] = 'null'

        query['due'] = due.to_iso8601_string()

        requests.request(
            "PUT",
            f"https://api.trello.com/1/cards/{card['id']}",
            headers=headers,
            params=query
        )


set_dates()
