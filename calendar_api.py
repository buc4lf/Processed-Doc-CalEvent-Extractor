from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_calendar_service():
    creds = None
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def add_event_to_google_calendar(event):
    service = get_calendar_service()
    start_dt = datetime.strptime(f"{event['date']} {event['start_time']}", "%Y-%m-%d %H:%M")
    end_time = event.get('end_time') or "23:59"
    end_dt = datetime.strptime(f"{event['date']} {end_time}", "%Y-%m-%d %H:%M")

    event_body = {
        'summary': event['summary'],
        'location': event.get('location', ''),
        'description': event.get('description', ''),
        'start': {'dateTime': start_dt.isoformat(), 'timeZone': 'America/New_York'},
        'end': {'dateTime': end_dt.isoformat(), 'timeZone': 'America/New_York'},
    }

    created_event = service.events().insert(calendarId='primary', body=event_body).execute()
    print(f"Event created: {created_event.get('htmlLink')}")
