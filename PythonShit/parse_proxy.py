import urllib.request
import socket
import urllib.error
from multiprocessing import Process
import time

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.example.com')  # change the URL to test here
        sock=urllib.request.urlopen(req, timeout=2)
       
    except urllib.error.HTTPError as e:
        # print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        # print("ERROR:", detail)
        return True
    return False


file = open("C:/proxies_lmao.txt")
content = file.read()


    # two sample proxy IPs
proxyList = content.split('\n')
nice_proxy = []
index = 1
procs = []

for currentProxy in proxyList:
    print("%d of %d" %( index, len(proxyList)))
    index += 1
    if not is_bad_proxy(currentProxy):
        nice_proxy.append(currentProxy)

content_print = ""
for proxy_ in nice_proxy:
    content_print += (proxy_ + "\n")

file_new = open("C:/res_proxy.txt", "w+", encoding='utf-8')
file_new.write(content_print)
file_new.close()