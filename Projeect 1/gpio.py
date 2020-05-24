import os,httplib2
from apiclient import discovery
import g_oauth 
import time
from datetime import datetime
import picamera
import requests

token = 'Your Token'

def gmail_get_service():
    credentials = g_oauth.gmail_user_auth()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    return service

mail_list = []

def gmail_get_messages():
    service = gmail_get_service()
    messages = service.users().messages()
    msg_list = messages.list(userId='me', maxResults=1).execute()
    for msg in msg_list['messages']:
        topid = msg['id']
        msg = messages.get(userId='me', id=topid).execute()
        if msg['snippet'] == 'Security Check2':
            if not msg['id'] in mail_list:
                mail_list.append(msg['id'])
                send_msg()
    

def send_msg():
    filename = datetime.now()
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)
        camera.capture(str(filename)+'.jpg')

    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization':'Bearer '+token}
    data = {"message":"Here is your room."}
    img = f'/home/pi/Desktop/RaspberryPi_for_convenient_life/Projeect 1/{filename}.jpg'
    file = {'imageFile': open(img, 'rb')}
    r = requests.post(url, headers=headers, params=data, files=file,)
            

run = True
while run:
    try:
        time.sleep(30)
        gmail_get_messages()
    except KeyboardInterrupt:
        run = False
