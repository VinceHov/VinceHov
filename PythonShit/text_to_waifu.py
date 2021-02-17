import vk
import random
import datetime, time
import requests
from random import randint as r
import os
access_token = " " #API_KEY 
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)

baseDir = "D:/grab_tyan_vince"

for filename in os.listdir(baseDir):
    print(filename.split('.jpg')[0])

api.messages.send(peer_id=user_id, message=message, random_id=r(0,99999999))