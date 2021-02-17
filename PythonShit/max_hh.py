from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

cookies = [
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': '__ddg1', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': '__ddg2', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': '__zzatgib-w-hh', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': '_xsrf', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'cfidsgib-w-hh', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'clscgib-w-hh', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'crypted_id', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'fgsscgib-w-hh', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'gsscgib-w-hh', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'hhtoken', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'hhuid', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'hhul', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'iap.uid', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
{'domain': '.hh.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'region_clarified', 'path': '/', 'secure': False, 'value': 'ВСТАВИТЬ_КУКИ'}, ################ВАЖНО
]

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
opts = Options()
opts.add_argument("user-agent=%s" % user_agent)

dr = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)
have_cookie = False 
maximized = False
count = 0 
hrefs = []
refreshed = False 
while True:
#https://hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&resume=3b5da9c4ff07fc756d0039ed1f526e3769367a&page= // Для того чтобы искать доступные вакансии

    dr.get("https://hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&text=python&page=%d" % count)
    count += 1 
    if not have_cookie:
        for cookie in cookies:
            dr.add_cookie(cookie)
        have_cookie = True
    if not maximized:
        dr.maximize_window() 
        maximized = True
    bs = BeautifulSoup(dr.page_source,"lxml")
    if not refreshed:
        dr.refresh()
    time.sleep(3)
    appended = 0
    for elem in  dr.find_elements_by_link_text('Откликнуться'):
        appended +=1 
        hrefs.append(elem.get_attribute("href"))
    if appended == 0:
        break

badhrefs = []
for orderhref in hrefs:
    try:
        dr.get(orderhref)
        dr.execute_script('document.getElementsByClassName("bloko-button                            bloko-button_primary                            HH-VacancyResponsePopup-Submit                            HH-SubmitDisabler-Submit                            HH-SimpleValidation-Submit")[0].click()')
    except:
        badhrefs.append(orderhref)
        pass
