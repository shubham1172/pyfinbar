import os.path
import pickle
from pygfbar.common import SingletonMeta
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# Delete the pickle file if scope is modified
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


class Credentials(metaclass=SingletonMeta):
    def __init__(self):
        self.creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

    def get(self):
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        return self.creds
