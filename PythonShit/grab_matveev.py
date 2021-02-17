import os 
import re 
import base64

file = open("D:/tmpapixml.xml", 'r', encoding='utf-8')
content = file.read()
file.close()
tmp_content = re.findall("(?s)(?<='mmatveev').*?(?=</d:photo>)", content)
#print(len(tmp_content))
index = 0
for karitinka in tmp_content:
	tmp_kartinka = karitinka.split("<d:photo m:type=\"Edm.Binary\">")[1]
	index += 1 
	tmp_base64 = base64.b64decode(tmp_kartinka.encode('utf-8'))
	file2 = open("D:/kartinka" + str(index) + ".jpg", 'wb')
	file2.write(tmp_base64)
	file2.close()
    
# print(tmp_content[0])