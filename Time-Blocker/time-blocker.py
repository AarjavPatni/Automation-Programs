from __future__ import print_function
from sys import argv

import pendulum
import os.path
from plyer import notification

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(
        r"C:\Users\Aarjav\Documents\Automation-Programs\sensitive-data\time-blocker-token.json"
    ):
        creds = Credentials.from_authorized_user_file(
            r"C:\Users\Aarjav\Documents\Automation-Programs\sensitive-data\time-blocker-token.json", SCOPES
        )
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r"C:\Users\Aarjav\Documents\Automation-Programs\sensitive-data\time-blocker.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(
            r"C:\Users\Aarjav\Documents\Automation-Programs\sensitive-data\time-blocker-token.json", "w"
        ) as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        # Call the Calendar API
        timeMax = pendulum.today() if (int(
            pendulum.now().to_time_string().split(':')[0]) < 22) and (len(argv) != 2) else pendulum.now()
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMax=timeMax,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = events_result.get("items", [])

        for event in events:
            service.events().delete(calendarId="primary",
                                    eventId=event["id"]).execute()
            print(f'🧹 {event["summary"]}')

        notification.notify(
            title="Time-Blocker",
            message='Cleared Calendar!',
            app_icon=r"C:\Users\Aarjav\Documents\Automation-Programs\Time-Blocker\schedule.ico",
        )

        if not events:
            print("No events found.")

            events_result = (
                service.events()
                .list(
                    calendarId="primary",
                    timeMin=pendulum.today(),
                    timeMax=pendulum.tomorrow(),
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            eventsToday = events_result.get("items", [])

            for event in eventsToday:
                event["summary"] = event["summary"].replace("✅ ", "")
                service.events().update(
                    calendarId="primary", eventId=event["id"], body=event
                ).execute()

            return

    except HttpError as error:
        print("An error occurred: %s" % error)


if __name__ == "__main__":
    main()
