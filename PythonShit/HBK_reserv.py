import vk
import requests
import time
from operator import itemgetter
from PIL import Image
from io import BytesIO
import re
import os 

access_token = " " #API_KEY 
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)


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
                    pixels[x_pixel, y_pixel] = (int(pixel[0] * 0.6), int(pixel[1] * 0.7), int(pixel[2] * 4.5))#(int(pixel[0] * 1.1) , pixel[1] , 240)

    return image_to_byte_array(img)

def upload_image(image_url):
    photos_server = api.photos.getWallUploadServer(access_token=access_token, group_id=196722515,)
    response = requests.post(photos_server['upload_url'], files={'photo' : (r'test_image.jpg', repixel_image(image_url))})
    response_text = response.json()
    responce_photo = api.photos.saveWallPhoto(access_token = access_token, group_id=196722515, server=response_text['server'], photo=response_text['photo'], hash=response_text['hash'])
    return ('photo' + str(responce_photo[0]['owner_id']) + "_" + str(responce_photo[0]['id']))

def check_last(offset=1):
    try:
        while api.wall.get(owner_id=-101489525, count=1, offset=offset, filter="owner")['items'] != []:
            offset += 1
            print(offset)
            continue
    except:
        print("exception on " + str(offset))
        time.sleep(2)
        offset = check_last(offset)
    return offset

def check_if_new(offset):
    try:
        if api.wall.get(owner_id=-101489525, count=1, offset=(offset + 1), filter="owner")['items'] != []:
            return True 
        else:
            return None
    except:
        exit()

def post_pub(offset):
    get = api.wall.get(owner_id=-101489525, count=1, offset=offset, filter="owner")
    for post in get['items']:
        attachmentz = []
        text = None
        for item in get["items"]:
            if 'text' in item:
                text = item['text']
            if 'attachments' in item:
                for attachment in item['attachments']:
                    if "photo" in attachment:
                        photo = attachment['photo']
                        # print(photo)
                        if "sizes" in photo:
                            newlist = sorted(photo["sizes"], key=itemgetter('width'), reverse=True) 
                            attachmentz.append(upload_image(newlist[0]['url']))
                    elif "audio" in attachment:
                        audio = attachment['audio']
                        attachmentz.append(('audio' + str(audio['owner_id']) + "_" + str(audio['id']))) 
                    elif "doc" in attachment:
                        doc = attachment['doc']
                        attachmentz.append(('doc' + str(doc['owner_id']) + "_" + str(doc['id'])))
                    elif "poll" in attachment:
                        poll = attachment['poll']
                        attachmentz.append(('poll' + str(poll['owner_id']) + "_" + str(poll['id'])))
                    elif "video" in attachment:
                        video = attachment['video']
                        attachmentz.append(('video' + str(video['owner_id']) + "_" + str(video['id'])))
            time.sleep(3)
        attachmentz = tuple(attachmentz)
        if "Алисенок" in text:
            text = text.replace("Алисенок", "Крипписенок")
        if "ХБА" in text:
            text = text.replace("ХБА", "ХБК")
        if "Алис" in text or "алис" in text: 
            text = re.sub(r"[а,А][л,Л][и,И][с,С]\S", "Криппи", text)
        # print(text)
        # print(attachmentz)

        post = api.wall.post(owner_id=-196722515, from_group=1, message=text, attachments=attachmentz)  
        # print(post)
        print("Posted нахцуй!!")


# print(get['items'])

current_offset = 14246

# print(api.wall.get(owner_id=-101489525, count=1, offset=12959, filter="owner")['items'])
# exit()
def post_spizdil():
    global current_offset
    while True:
        resp_state = check_if_new(current_offset)
        # print(resp_state)
        # exit()
        if resp_state == True: 
            current_offset += 1
            print("New offset is " + str(current_offset))
            post_pub(1)
        time.sleep(20)

# post_spizdil()
try:
    while True:
        try:
            post_spizdil()
            # exit()
        except:
            post_spizdil()
            # exit()
            pass
except:
    # exit()
    pass

file = open("C:/Users/Administrator/Desktop/HBK.py", "r", encoding='utf-8')
content = file.read()

content_new = re.sub("current_offset = \d+", "current_offset = %d" % current_offset, content)
file.close()
file_new = open("C:/Users/Administrator/Desktop/HBK.py", "w+", encoding='utf-8')
file_new.write(content_new)
file_new.close()
os.system("cls")
os.system("python C:/Users/Administrator/Desktop/HBK.py")
exit()

# print(check_if_new(current_offset))