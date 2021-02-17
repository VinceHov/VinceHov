import vk
import time 

access_token = " " # API_KEY
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)


photos = api.photos.getAll(owner_id=249480172, count=20)
orderlist = []

for item in photos['items']:
	orderlist.append(item['id'])

index = 1 

print(orderlist)

for order in orderlist:
	repsonse = api.likes.add(type='photo', owner_id=249480172, item_id=order)
	print(order, "is completed:", index, "of ", len(orderlist))
	if index % 5 == 0: 
		time.sleep(5)
	index += 1

print("All orders to like are Completed")
# print(orderlist)