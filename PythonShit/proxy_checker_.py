import urllib.request
import socket
import urllib.error
from urllib.parse import urlparse
import re
import multiprocessing
import requests

def is_bad_proxy(input_queue):    

    pip = input_queue.get()
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://icanhazip.com')
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e
        return e.code

    except Exception as detail:
        return True

    resp = sock.read().decode('utf-8')
    if "2.92.192.37" in resp or len(resp) == 0:
        return True
        
    print("%s is working" % (pip))
    # exit()
    return False

with open("proxy_list.txt", 'r', encoding='utf-8') as proxy_file:
    content_file = proxy_file.read()
    proxy_list = re.split(r'\n', content_file)

def main():
    socket.setdefaulttimeout(6)

    proxyList = proxy_list
   
    input_queue = multiprocessing.Queue()
    workers = []

    for i in range(len(proxy_list)):
        p = multiprocessing.Process(target=is_bad_proxy, args=(input_queue, ))
        workers.append(p)
        p.start()

    for currentProxy in proxy_list:
        input_queue.put(currentProxy)

    for w in workers:
        input_queue.put(None)

    for w in workers:
        w.join()

    print('lmao')

if __name__ == "__main__":
    main()