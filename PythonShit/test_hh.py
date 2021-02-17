from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

cookies = [
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': '__ddg1', 'path': '/', 'secure': False, 'value': 
    'J6gxPBgAQMiznILFoQYR'}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': '__ddg2', 'path': '/', 'secure': False, 'value': 
    'nzaPlb4GyLomGDh7'}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': '__zzatgib-w-hh', 'path': '/', 'secure': False, 'value': 
    'MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9DKjAwbB8kYUgUKEdZTXknIBJ7JiQJCxNgcHQpMVtCaCEYTl0leBNUayELUTQ1ZhBKT01HDTdAXjdXYSAMFhFNVlN5KhoVenEoVQkTYjkzPDRtc3hcJgoaVDVfGUNqTg1pN2wXPHVlL3kmPmEtOhlRCyBWfBt8OVZcSWl1bkFNPB8Kdl99G0JpJGZIXSFMR0lrZU5TQixmG3EVJ38OKm8bfyZaHDljIElVUnopHBd8cSVXD39NDHo5Mzx6LFggfEspDx8aNiELVUgzWEERdSN5ci45bXA1YVEcLg==gHByeA=='}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': '_xsrf', 'path': '/', 'secure': False, 'value': 
    '9543645fe314f05aa9f8b9ddf324381e'}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'cfidsgib-w-hh', 'path': '/', 'secure': False, 'value': 
    'qBekT5JceIBIw6aDB7dUDX/xaZcUMEg0vqxLbfRSAdRG8B/YDb2LFvpolgpWUWgQus5WvKZ9bl5knMhvqAnXbXg7CUQ+vdGhmXL0R9G3tbIauEXDUjiyxS2icRIqvMUjbK7NaDDDTJtldjDcRRis7EHjexaTewwOagNF5FjNEQ=='}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'clscgib-w-hh', 'path': '/', 'secure': False, 'value': 
    'PIvaBGfbYpnoMYnSm7trGewj8NKtN+tm6muORLvYDxoUv8uGRabGdMVWJNcjtg5i6PxvCzPM6EHrVNeThx3Vsz4XkSp/hzGwQHUNv+IHeeHS22DenL64rWN0ECtgHrA/50gD3d+HgsCv9gP4zCavNrJXG1s6o372CcvhAmM7SC5gv5MwcW3fCoUFpc2vVeic3H4b/RkDz56wsrUklWMw3Kvw64yD/vkBbMftZ87O/I427P1TaijJHvwBv4YLYLHYpg0BrS0e1Pt6WV98C4WIcGpWHnh8PZy56WnAtJXy19NOADZrR63r64s3+nJoeCUGidcMXzZD7Pc8CnrtujxcSQ=='}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'crypted_id', 'path': '/', 'secure': False, 'value': 
    '73EA4B4F3ADCF939828E43A75D518B50A5471C6F722104504734B32F0D03E9F8'}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'fgsscgib-w-hh', 'path': '/', 'secure': False, 'value': 
    'd0cfffc84c28e027ac633dd8a5318fdee434bad4'}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'gsscgib-w-hh', 'path': '/', 'secure': False, 'value': 
    'N6SIOlMY+ayx3ESRE8NkTbNdLy4ZiMtL584bArY2wVxTKBS0DmLOBkd2jkP5R3ySPBnw0hk1yWGEB29N9ZEijZ9xSD08C0KsEsZ+gIFQF4xFT6EyODcsKOpY/2LFiv777gHJstHMITQOkdO/lGYPb/averaggXSnZImrNMSzaJ0ebIzkZVF7+gB+owTKwaK1WkgbT2TKpRT6GMX1ucq0EidjF0ppoP52rFifSO8vIMdfy3ku3ctH0Z5UhaDIgg=='}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'hhtoken', 'path': '/', 'secure': False, 'value': 
    'CH6arFSCj0lellrUbgGi!dExoHyp'}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'hhuid', 'path': '/', 'secure': False, 'value': 
    '0fz1DgVtkBtfWF8eWBoxoA--'}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'hhul', 'path': '/', 'secure': False, 'value': 
    'ac68a997877e49f9dcd30f797fa5c57b5261fa54e700f38576b00a2efb8e4a19'}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'iap.uid', 'path': '/', 'secure': False, 'value': 
    '50a5961d2f49416281f7827e7fa84c8f'}, 
{'domain': '.hh.ru', 'expiry': 1803324500, 'httpOnly': True, 'name': 'region_clarified', 'path': '/', 'secure': False, 'value': 
    'NOT_SET'}, 
]

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
# opts = Options()
# opts.add_argument("user-agent=%s" % user_agent)


dr = webdriver.Chrome()
dr.get('https://hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&resume=3b5da9c4ff07fc756d0039ed1f526e3769367a&page=0')
for cookie in cookies:
    dr.add_cookie(cookie)
dr.refresh()
dr.maximize_window() 

elements = dr.find_elements_by_link_text('Откликнуться')
if len(elements) == 0:
    dr.close()
    exit()

for href in elements:
    print(href.get_attribute("href"))

