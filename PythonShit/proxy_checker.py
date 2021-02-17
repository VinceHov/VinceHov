import requests
proxy_list = open("C:/p_list.txt", 'r', encoding='utf-8').read()
proxy_list = proxy_list.split('\n')
proxy = proxy_list[0]
proxies = {
 "http": ("http://%s" % proxy),
 "https": ("http://%s" % proxy)
}
r = requests.get("https://a.aliexpress.com/_mNDbkZJ", proxies=proxies)
print(r)