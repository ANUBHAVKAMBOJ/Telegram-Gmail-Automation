import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CREDS_FILE = 'GMailAPICreds.json'
SCOPES = ['https://mail.google.com/', 'https://www.googleapis.com/auth/userinfo.profile']

creds = None

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
    
    with open('token.json', 'w') as writer:
        writer.write(creds.to_json())

PeopleService = build('people', 'v1', creds)
profile = service.people().get(resourceName='people/me', personFields='metadata').execute()
user_id = profile['metadata']['sources'][0]['id']

print(user_id)





