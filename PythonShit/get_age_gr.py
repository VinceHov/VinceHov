import vk
import random
import requests
from datetime import datetime, timedelta
import math
import matplotlib.pyplot as plt
import re
access_token = " " #API_KEY 
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)

# // То чуство когда ты пишешь целую программу для того чтобы доказать девушке что она - ребёнок, но она скажет что я мудак и забудет об этом.

# w2h_groups = ["151564985", "102771442"]
# lake_groups = ["25489609"]
# groups = w2h_groups
# groups = lake_groups
# groups = api.groups.get(user_id=21646383, count=1000)#['items'] # Таня 
# groups = api.groups.get(user_id=249480172, count=1000)['items'] # Лаке 
# groups = api.groups.get(user_id=507920843, count=1000)['items'] # Винс 
# groups = api.groups.get(user_id=31774358, count=1000)['items'] # Саник 
groups = ["47949197", "86886389", "54014337"]
# groups = ["22248472", "81413361", "174297071"]

res_users = [] 
index = 1 
for group in groups: 
        print("Processing %s group of %s" % (index, len(groups)))
        index += 1
        try:
            groupMembers = api.groups.getMembers(group_id=group, count=1000, fields=('sex', 'city', 'country', 'photo_max_orig', 'can_write_private_message', 'bdate', 'relation'))['items']
        except:
            continue

        for members in groupMembers:
            try:
                # if members['sex'] == 1 and members['city']['id'] == 1:
                res_users.append(members['bdate'])
            except:
                continue

res_bdate = {}
index = 1 
for _res in res_users: 
    print("Processing %s users of %s" % (index, len(res_users)))
    index += 1
    if re.findall(r'\d+\.\d+\.\d+', _res) != []:
        try:
            res_bdate[re.split(r'\d+\.\d+\.', _res)[1]] += 1
        except:
            res_bdate[re.split(r'\d+\.\d+\.', _res)[1]] = 1

res_bdate = {k: res_bdate[k] for k in sorted(res_bdate)}

x = []
y = []

index = 1 
middle = 0
count = 0
for _bdate in res_bdate:
    print("Compiling %s bdate of %s" % (index, len(res_bdate)))
    index += 1
    if int(_bdate) > 1965:
        middle += int(int(2020 - int(_bdate)) * int(res_bdate[_bdate]))
        count += int(res_bdate[_bdate])
        y.append(res_bdate[_bdate])
        x.append(_bdate)

plt.rcParams["figure.figsize"] = (900,900)
plt.plot(x, y)
plt.grid(True) # отображение сетки
plt.xlabel("Возраст (Среднее - %s), всего - %d" % (str(int((middle / count))), len(res_bdate)), fontsize=14)  # ось абсцисс
plt.ylabel("Количество", fontsize=14) # ось ординат
plt.show()


