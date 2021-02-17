import requests 
import re 
from xml.sax import saxutils
content = saxutils.unescape(requests.get("https://api18.sapsf.com/odata/v2/Background_Specialisedtest?$filter=userId eq 'mmatveev'", headers={'Authorization':'Basic a3RvcmluQG5vdm9saXBldHNEOjAwMDA='}).content.decode('utf-8'))
print(re.findall("(?s)(?<=<d:rating).*?(?=<)",content))
print(content)