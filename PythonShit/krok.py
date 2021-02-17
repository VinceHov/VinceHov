from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

cookies = [
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': '__ddg1', 'path': '/', 'secure': False, 'value': 
    'J6gxPBgAQMiznILFoQYR'}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': '__ddg2', 'path': '/', 'secure': False, 'value': 
    'nzaPlb4GyLomGDh7'}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': '__zzatgib-w-hh', 'path': '/', 'secure': False, 'value': 
    'MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9DKjAwbB8kYUgUKEdZTXknIBJ7JiQJCxNgcHQpMVtCaCEYTl0leBNUayELUTQ1ZhBKT01HDTdAXjdXYSAMFhFNVlN5KSEVfWwjUwwTXTkzPDRtc3hcJgoaVDVfGUNqTg1pN2wXPHVlL3kmPmEtOhlRCyBWfBt8OVZcSWl1bkFNPB8Kdl99G0JpJGZIXSFMR0lrZU5TQixmG3EVJ38OKm8bfyZaHDljIElVUQkpHxJ3byhXCn9NDHo5Mzx6LFggfEspDx8aNiELVUgzWEERdSN5ci45bXA1YVEcLg==jbPuow=='}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': '_xsrf', 'path': '/', 'secure': False, 'value': 
    '9543645fe314f05aa9f8b9ddf324381e'}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'cfidsgib-w-hh', 'path': '/', 'secure': False, 'value': 
    'zVyXQ57yfvMo3lBwSEyeL0Mxg1+sqAfnJIwpRB4W+LUrwaDJx00u58DUbsSIbbmCQn2yCiatF25ENC5w1elIvm+UlHaq0ZNRo077Ob99yzR6Roe7XNuSPmbpmIeGk3QXyLG7NpktSdYuzoASEIU7c7POC2W5z1Fahody37NNUw=='}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'clscgib-w-hh', 'path': '/', 'secure': False, 'value': 
    'i18BKm8XZMcRI2ul0Y2OzNUXrK1U6bIXzsIYMhNVcDQ+IKBixCunbaSBuvgMWmCT33n5LwBNDYtWTc09+wHk74NqGLA1cCwidc8v+HJqIbD4V/lqKOW2scab+3IN1ABFBI+izEXoCYiOSrM7QOMm4rQOXVqaZa2oMr2tAUiNA6Rgv5MwcW3fCoUFpc2vVeic3H4b/RkDz56wsrUklWMw3Kvw64yD/vkBbMftZ87O/I427P1TaijJHvwBv4YLYLHYpg0BrS0e1Pt6WV98C4WIcGpWHnh8PZy56WnAtJXy19NOADZrR63r64s3+nJoeCUGidcMXzZD7Pc8CnrtujxcSQ=='}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'crypted_id', 'path': '/', 'secure': False, 'value': 
    '73EA4B4F3ADCF939828E43A75D518B50A5471C6F722104504734B32F0D03E9F8'}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'fgsscgib-w-hh', 'path': '/', 'secure': False, 'value': 
    '63788d207aec0f95b7a02ea4b6494618dcd80f7e'}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'gsscgib-w-hh', 'path': '/', 'secure': False, 'value': 
    'xEqvznbnUa2Otv2m/WkcNul+funCXJRO05ZMpjuttWiLjljMG2TQ//uVIx6UdSH1h7FyKNv7IC/did2O6EB5wnCminlQ7apiWH1aTEwO1TmxeBIt6E3cUObdN1PWqbJQa91Fl/jp9GK/qd7VG9KUu8FSEKGaaDCqJ6tzWdOXuOz7UpPBh7Dn8/C4eAJczKCBn5S0Rqo1ObhXeYDSoU6PWgaFZ3HNJvLbiG7PwHES9vbQ+U6FL9KAG0FuQnsc2w=='}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'hhtoken', 'path': '/', 'secure': False, 'value': 
    'CH6arFSCj0lellrUbgGi!dExoHyp'}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'hhuid', 'path': '/', 'secure': False, 'value': 
    '0fz1DgVtkBtfWF8eWBoxoA--'}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'hhul', 'path': '/', 'secure': False, 'value': 
    'ac68a997877e49f9dcd30f797fa5c57b5261fa54e700f38576b00a2efb8e4a19'}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'iap.uid', 'path': '/', 'secure': False, 'value': 
    '50a5961d2f49416281f7827e7fa84c8f'}, 
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'region_clarified', 'path': '/', 'secure': False, 'value': 
    'NOT_SET'}, 
]

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
opts = Options()
opts.add_argument("user-agent=%s" % user_agent)

dr = webdriver.Chrome(chrome_options=opts)
have_cookie = False 
maximized = False
count = 0 
hrefs = []
refreshed = False 
Moscow = False
hrefs = ["https://hh.ru/vacancy/40306047", "https://hh.ru/vacancy/39055550", "https://hh.ru/vacancy/28442910", "https://hh.ru/vacancy/38177037", "https://hh.ru/vacancy/32808900", "https://hh.ru/vacancy/38544519", "https://hh.ru/vacancy/40301042", "https://hh.ru/vacancy/40286776", "https://hh.ru/vacancy/39034303", "https://hh.ru/vacancy/38488076", "https://hh.ru/vacancy/38488077", "https://hh.ru/vacancy/38488078", "https://hh.ru/vacancy/40190113", "https://hh.ru/vacancy/38488075", "https://hh.ru/vacancy/40267556", "https://hh.ru/vacancy/40267049", "https://hh.ru/vacancy/40262177", "https://hh.ru/vacancy/39180694", "https://hh.ru/vacancy/39862244", "https://hh.ru/vacancy/40185217", "https://hh.ru/vacancy/40260029", "https://hh.ru/vacancy/40255470", "https://hh.ru/vacancy/39715218", "https://hh.ru/vacancy/40246927", "https://hh.ru/vacancy/40245987", "https://hh.ru/vacancy/40243080", "https://hh.ru/vacancy/40241078", "https://hh.ru/vacancy/39425272", "https://hh.ru/vacancy/38909867", "https://hh.ru/vacancy/39989467", "https://hh.ru/vacancy/39712424", "https://hh.ru/vacancy/40081373", "https://hh.ru/vacancy/39629986", "https://hh.ru/vacancy/40212746", "https://hh.ru/vacancy/40212747", "https://hh.ru/vacancy/40212748", "https://hh.ru/vacancy/40212749", "https://hh.ru/vacancy/39224617", "https://hh.ru/vacancy/39224638", "https://hh.ru/vacancy/39574916", "https://hh.ru/vacancy/38675415", "https://hh.ru/vacancy/39751995", "https://hh.ru/vacancy/38811889", "https://hh.ru/vacancy/39415564", "https://hh.ru/vacancy/39055417", "https://hh.ru/vacancy/34202681", "https://hh.ru/vacancy/40185246", "https://hh.ru/vacancy/40185241", "https://hh.ru/vacancy/40185218", "https://hh.ru/vacancy/40185219", "https://hh.ru/vacancy/40185220", "https://hh.ru/vacancy/40185221", "https://hh.ru/vacancy/40174407", "https://hh.ru/vacancy/39014004", "https://hh.ru/vacancy/37930562", "https://hh.ru/vacancy/39413069", "https://hh.ru/vacancy/39036659", "https://hh.ru/vacancy/38177059", "https://hh.ru/vacancy/32422892", "https://hh.ru/vacancy/28442931", "https://hh.ru/vacancy/40147752", "https://hh.ru/vacancy/40147751", "https://hh.ru/vacancy/40143621", "https://hh.ru/vacancy/40127460", "https://hh.ru/vacancy/39527236", "https://hh.ru/vacancy/40119853", "https://hh.ru/vacancy/39621212", "https://hh.ru/vacancy/40116204", "https://hh.ru/vacancy/40111012", "https://hh.ru/vacancy/40106368", "https://hh.ru/vacancy/40097119", "https://hh.ru/vacancy/40097093", "https://hh.ru/vacancy/38986962", "https://hh.ru/vacancy/40086171", "https://hh.ru/vacancy/40085818", "https://hh.ru/vacancy/40085564", "https://hh.ru/vacancy/39432352", "https://hh.ru/vacancy/37446995", "https://hh.ru/vacancy/32423130", "https://hh.ru/vacancy/39653860", "https://hh.ru/vacancy/39653790", "https://hh.ru/vacancy/39989431", "https://hh.ru/vacancy/39055485", "https://hh.ru/vacancy/40041074", "https://hh.ru/vacancy/40041075", "https://hh.ru/vacancy/39593940", "https://hh.ru/vacancy/38245869", "https://hh.ru/vacancy/38327976", "https://hh.ru/vacancy/39614001", "https://hh.ru/vacancy/39614945", "https://hh.ru/vacancy/37000793", "https://hh.ru/vacancy/39055519", "https://hh.ru/vacancy/30206455", "https://hh.ru/vacancy/37402540", "https://hh.ru/vacancy/38524859", "https://hh.ru/vacancy/39986317", "https://hh.ru/vacancy/39979668", "https://hh.ru/vacancy/39623037", "https://hh.ru/vacancy/39942020", "https://hh.ru/vacancy/38298706", "https://hh.ru/vacancy/39425284", "https://hh.ru/vacancy/38682698", "https://hh.ru/vacancy/39912753", "https://hh.ru/vacancy/39911590", "https://hh.ru/vacancy/39911219", "https://hh.ru/vacancy/39888454", "https://hh.ru/vacancy/39888427", "https://hh.ru/vacancy/39888421", "https://hh.ru/vacancy/39888406", "https://hh.ru/vacancy/39888395", "https://hh.ru/vacancy/39072305", "https://hh.ru/vacancy/39364692", "https://hh.ru/vacancy/38177016", "https://hh.ru/vacancy/37824229", "https://hh.ru/vacancy/39876209", "https://hh.ru/vacancy/39876152", "https://hh.ru/vacancy/39876150", "https://hh.ru/vacancy/39860551", "https://hh.ru/vacancy/38015431", "https://hh.ru/vacancy/39307940", "https://hh.ru/vacancy/38658887", "https://hh.ru/vacancy/38658839", "https://hh.ru/vacancy/36158346", "https://hh.ru/vacancy/36880348", "https://hh.ru/vacancy/37886794"]
dr.maximize_window()
for href in hrefs:
    try:
        dr.get(href)
        if not have_cookie:
            for cookie in cookies:
                dr.add_cookie(cookie)
            have_cookie = True 
        dr.refresh()
        time.sleep(1)
        dr.find_element_by_class_name('vacancy-action.vacancy-action_stretched').click()
        dr.find_elements_by_class_name('bloko-form-spacer')[1].click()
        time.sleep(1)
        pass
    except: 
        pass