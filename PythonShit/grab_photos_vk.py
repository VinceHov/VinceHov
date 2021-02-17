import vk
import requests
import time
from operator import itemgetter
from PIL import Image
from io import BytesIO
import re

access_token = " " #API_KEY 
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)
baseDir = "D:/grab_zls/"


pictures = [] 
last_attach = api.messages.getHistoryAttachments(peer_id=2000000064, media_type='photo', count=2, start_from="-1")

current_attach = ""
current_starts = "0"
try:
    while current_attach != last_attach:
        attachments = api.messages.getHistoryAttachments(peer_id=2000000064, media_type='photo', count=200, start_from=current_starts)
        for attachment in attachments['items']:
            photo = attachment['attachment']['photo']
    
            if "sizes" in photo:
                newlist = sorted(photo["sizes"], key=itemgetter('width'), reverse=True) 
                pictures.append(newlist[0]['url'])
        current_starts = attachments['next_from']
except:
    pass

counter = 0 
for href in pictures:
    counter += 1
    pic = requests.get(href).content
    file = open("%s%d.png" % (baseDir, counter), 'wb+')
    file.write(pic)
    file.close()
    print("%d of %d" % (counter, len(pictures)))