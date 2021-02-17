from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.common.keys import Keys
import time
# import win32com.client

cookies = {'domain': '.mos.ru', 'expiry': 1603324500, 'httpOnly': True, 'name': 'ag_session_id', 'path': '/', 'secure': False, 'value': 's%3Amgyp3EcTzj-8bervpsiwpaNiIlwxgYUi.sAeemR6SPP8qdM76h8vrQ9DSjPKjWiohqf9v4yJcJpM'}

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
opts = Options()
opts.add_argument("user-agent=%s" % user_agent)


dr = webdriver.Chrome(chrome_options=opts)  
dr.get("https://ag.mos.ru/home")
dr.delete_cookie("ag_session_id")
dr.add_cookie(cookies)
bs = BeautifulSoup(dr.page_source,"lxml")
dr.refresh()
dr.maximize_window() 
time.sleep(3)
dr.execute_script('document.getElementsByClassName("action")[0].click()')
dr.execute_script('document.getElementsByClassName("button button--muted button--fill button--special-red")[0].click()')

for i in range(60,130):
    time.sleep(6)
    dr.execute_script('document.getElementById("login").value = "sonicprojectneedle+%d@gmail.com"' % i)  
    dr.execute_script('document.getElementById("password").value = "zFKTRC3m"')
    dr.execute_script('document.getElementsByClassName("btn btn-lg btn-primary btn-block bc-form-btn")[0].click()')
    dr.refresh()
    time.sleep(6)
    dr.execute_script('document.getElementById("login").value = "sonicprojectneedle+%d@gmail.com"' % i)  
    dr.execute_script('document.getElementById("password").value = "zFKTRC3mzFKTRC3m"')
    dr.execute_script('document.getElementsByClassName("btn btn-lg btn-primary btn-block bc-form-btn")[0].click()')
    dr.refresh()