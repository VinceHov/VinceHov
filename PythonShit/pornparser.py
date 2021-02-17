import requests
from lxml import etree as et
from lxml import html

page = requests.get("https://yaebus.ru/").content
tree = html.fromstring(page)
# htmlparser = etree.HTMLParser()
links = tree.xpath("//div/div/a")

baseurl = []
for link in links:
	baseurl.append(link.attrib["href"])

for url in baseurl:
	page = requests.get(url).content
	tree = html.fromstring(page)
	text = tree.xpath("//article/div/div/p/text()")
	if text == []:
		continue
	print(*text)
# root = et.Element('html', version="5.0")