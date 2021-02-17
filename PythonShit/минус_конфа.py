import vk
import requests
import time
from operator import itemgetter
from PIL import Image
from io import BytesIO
import re

access_token = " " # API_KEY
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)

chat_id = 138
current_photo = "https://sun1-94.userapi.com/aU5eHO34lIBZ6l7O61FlbT-ikQhht0mH17EhXg/r5YVs7ewFgw.jpg?ava=1"

def image_to_byte_array(image:Image):
  imgByteArr = BytesIO()
  image.save(imgByteArr, format=image.format)
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr

def repixel_image(image_url, on_coeff=1.3):
    
    img = Image.open(BytesIO(requests.get(image_url).content))
    
    pixels = img.load() # pixelmap
    
    R_low, R_hig = (100, 255)
    G_low, G_hig = (30, 156)
    B_low, B_hig = (0, 128)
    
    R_colmap = range(R_low, R_hig)
    G_colmap = range(G_low, G_hig)
    B_colmap = range(B_low, B_hig)
    
    # on_coeff = 1.3
    
    for x_pixel in range(img.size[0]):
        stroka = ""
        for y_pixel in range(img.size[1]):
            pixel = pixels[x_pixel, y_pixel]

            try:
                diffR = pixel[0] / pixel[1]
                diffG = pixel[1] / pixel[2]
            except:
                diffR = (pixel[0] + 1) / (pixel[1] + 1)
                diffG = (pixel[1] + 1) / (pixel[2] + 1)
            finally:
                if ((pixel[0] > pixel[1] > pixel[2]) and (diffR > on_coeff) and (diffG > on_coeff) and (pixel[0] in R_colmap) and (pixel[1] in G_colmap) and (pixel[2] in B_colmap)):
                    pixels[x_pixel, y_pixel] = (int(pixel[0] * 0.2), int(pixel[1] * 0.6), int(pixel[2] * 2.4))#(int(pixel[0] * 1.1) , pixel[1] , 240)

    return image_to_byte_array(img)

def push_image(photo):
	global current_photo
	upload_photo = api.photos.getChatUploadServer(chat_id=chat_id)
	response = requests.post(upload_photo['upload_url'], files={'photo' : (r'test_image.jpg', repixel_image(photo))})
	resp = api.messages.setChatPhoto(file=response.json()['response'])
	current_photo = api.messages.getChat(chat_id=chat_id)['photo_200']

while True:
	chat = api.messages.getChat(chat_id=chat_id)
	title = chat['title']
	photo = chat['photo_200']
	
	if not current_photo or photo != current_photo:
		push_image(photo)
	
	if "Алис" in title or "алис" in title:
		new_title = re.sub("[а,А][л,Л][и,И][с,С]\S", "Криппи", title)
		api.messages.editChat(chat_id=chat_id, title=new_title)
	
# print(photo)