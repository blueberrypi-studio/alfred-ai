from google.oauth2.credentials import Credentials

# Replace the values below with your own client ID, client secret, and
# redirect URI. You can obtain these values by creating a new OAuth 2.0
# client ID on the Google API Console:
#   https://console.developers.google.com/apis/credentials
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'YOUR_REDIRECT_URI'

# Use the client ID, client secret, and redirect URI to create an OAuth 2.0
# credentials object:
creds = Credentials.from_client_info(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI
)

# Use the credentials object to authorize an HTTP session:
from googleapiclient.discovery import build
service = build('calendar', 'v3', credentials=creds)

# Use the Calendar API to list the calendar events for the authenticated user:
calendar = service.calendars().get(calendarId='primary').execute()
events = service.events().list(calendarId='primary').execute()
print(events)
