import vk
import requests
import time
from operator import itemgetter

access_token = " " # API_KEY
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)

text = "test_API"
attachmentz = [] 
post = api.wall.post(owner_id=-196722515, from_group=1, message=text, attachments=attachmentz)  