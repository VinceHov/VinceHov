import vk
import random
import datetime, time
import requests
access_token = " " # API_KEY
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)

response = api.newsfeed.search(q=u"набор администрации паблик", count=3)

print(response['items'][2]['text'])