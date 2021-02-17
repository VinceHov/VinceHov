import vk
import requests
import time

session = vk.Session(access_token="Жопа")
v = '5.95'
api = vk.API(session, v=v)

test_zhopa = api.wall.get(owner_id=-177103704, count=1, offset=1, filter="owner")