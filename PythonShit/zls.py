import vk
import requests
import time
from operator import itemgetter

access_token = " " # API_KEY
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)

def upload_image(image_url):
    photos_server = api.photos.getWallUploadServer(access_token=access_token, group_id=196722515,)
    response = requests.post(photos_server['upload_url'], files={'photo' : (r'test_image.jpg', requests.get(image_url).content)})
    response_text = response.json()
    responce_photo = api.photos.saveWallPhoto(access_token = access_token, group_id=196722515, server=response_text['server'], photo=response_text['photo'], hash=response_text['hash'])
    return ('photo' + str(responce_photo[0]['owner_id']) + "_" + str(responce_photo[0]['id']))

posts_needed = []
for iterator in range(1,627):
    posts_needed.append(iterator)

posts_needed.sort(reverse=True)

counter = 1
for post_needed in posts_needed[621:622]:#
# print(posts_needed[40])
    print(post_needed)
    get = api.wall.get(owner_id=-177103704, count=1, offset=post_needed, filter="owner")
    
    print(("\n\n" + str(counter) + u" пост, который я спиздил из этого паблика:\n"))
    for post in get['items']:
        attachmentz = []
        text = None
        for item in get["items"]:
            # attachmentz = []
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
        print(text)
        # print(get['items'][0])
        post = api.wall.post(owner_id=-196722515, from_group=1, message=text, attachments=attachmentz)  
    counter += 1
