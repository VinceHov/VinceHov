import vk
import time
import random
access_token = "" # API_KEY
session = vk.Session(access_token=access_token)
api = vk.API(session, v='5.95')

kochka = False

while True:
    ts=api.messages.getLongPollServer(need_pts=1, lp_version=3)
    time.sleep(36)
    response = api.messages.getLongPollHistory(ts=ts['ts'], fields=[""], events_limit=1000, msgs_limit=200, last_n=0 )
    for _mes in response['messages']['items']:
        if _mes['peer_id'] == 2000000084 and _mes['text'] == "Чёт ты хилый, тебе бы в качалочку":
            api.messages.send(random_id=random.randint(1,100000),peer_id=2000000084, message="Ле, внатуре, пойду качаться!")
            kochka = True
        if _mes['peer_id'] == 2000000084 and _mes['text'] == "Нихуя жоский, остановись пока остановка не стала последней, ежжи":
            api.messages.send(random_id=random.randint(1,100000),peer_id=2000000084, message="Пацаны, знаете, я решил бросить качалку")
            kochka = False
    if kochka:
        api.messages.send(random_id=random.randint(1,100000),peer_id=-173644663, message="гачи борьба @nvkalashnikov")    
    print(response['messages'])