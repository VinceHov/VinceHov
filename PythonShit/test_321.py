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

posts = api.wall.get(owner_id=-186959420, count=100, offset=0, filter="owner")['items']

for post in posts:
	ID = post['id']
	api.likes.add(type='post', item_id=ID, owner_id='-186959420')
	time.sleep(1)