import vk
import random
import datetime, time
import requests
access_token = " " #API_KEY 
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)

import random

def ban():
    api.messages.send(random_id=0, peer_id=2000000064, message="@id495246971 (В профилактический бан)", intent='default', chat_id=64)
    api.messages.removeChatUser(chat_id=64, user_id=495246971)

def return_kl():
    api.messages.send(random_id=random.randint(0,99999), peer_id=2000000064, message="@id495246971 (Добро пожаловать. Снова.)", intent='default', chat_id=64)
    api.messages.addChatUser(chat_id=64, user_id=495246971)
try:
	ban()
except:
	return_kl()
while True:
    time.sleep(18000)
    ban()
    time.sleep(600)
    return_kl()