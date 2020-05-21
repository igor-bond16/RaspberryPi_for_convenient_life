import httplib2, os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

CLIENT_SECRET_FILE = '/home/igor-bond/Desktop/client_id.json'

USER_SECRET_FILE = '/home/igor-bond/Desktop/credentials_gmail.json'

def gmail_user_auth():
    store = Storage(USER_SECRET_FILE)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = 'Python Gmail API'
        credentials = tools.run_flow(flow, store, None)
        print('認証結果を保存しました:' + USER_SECRET_FILE)
    return credentials

#gmail_user_auth()