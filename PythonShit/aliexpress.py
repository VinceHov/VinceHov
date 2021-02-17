import requests
response = requests.get("https://campaign.aliexpress.com/wow/gf/cashdailyoutc/index?_addShare=no")
print(response.content)