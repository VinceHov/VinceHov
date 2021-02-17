import requests 
from xml.sax import saxutils
APIdata = []
APIdata.append("trofimov_ea")
file = open("D:/APIdata.txt", 'w', encoding='utf-8')
index = 1
# for data in APIdata:
    # print (index, 'of', len(APIdata))
    # index += 1
    # try:
content = ""
import re
for tabel in APIdata:
    print(index, ' of ' , len(APIdata))
    try:
        content += tabel + " ^_^ " + saxutils.unescape(requests.get("https://api18.sapsf.com/odata/v2/User?$filter=userId eq ''", headers={'Authorization':'Basic aWR1ZG5pa0BOTE1LOjAwMDAwMDAw'}).content.decode('utf-8')).split("<d:empId>")[1].split("</d:empId>")[0] + "\n"   
    except:
        content +=  tabel + " ^_^ " + "NOT_FOUND" + "\n"
    index += 1
file.write(content)
#print( , saxutils.unescape(requests.get("https://api18.sapsf.com/odata/v2/User?$filter=userId eq ''", headers={'Authorization':'Basic aWR1ZG5pa0BOTE1LOjAwMDAwMDAw'}).content.decode('utf-8')).split("<d:empId>")[1].split("</d:empId>")[0])



    # except:
        # continue
    # file.write(content)
# file.close()
#