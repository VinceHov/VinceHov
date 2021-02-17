# -*- coding: utf-8 -*-
# Script by Nikita Dubov, Molga Consulting, 2020.
from xml.dom.minidom import *
import os
import subprocess
import codecs
import xml.etree.ElementTree as ET
# import xmltodict
import json

i = 0 #TEST
filename = "candidate-0x4E6DDD7430E763A9.xml"
for filename in os.listdir("C:/Users/User/lmao/"): 

def parseXml(filename):
    sitemap_file = parse(codecs.open("C:/Users/User/lmao/" + "candidate-0x4E6DDD7430E763A9.xml", encoding="utf-8"))
    urls = sitemap_file.getElementsByTagName('candidate')
    email = urls[0].getElementsByTagName('email')
    print(email[0].firstChild.nodeValue)
    kek = email[0].firstChild.nodeValue.split("n\\",1)
    dst = kek[0] + ".pdf" #email[0].firstChild.nodeValue
    print("KEK IS ", kek)
    dst ='C:/Users/User/lmao/'+ dst 
    return dst
    i += 1

src ='C:/Users/User/lmao/' + filename
dst = parseXml(filename)
os.rename(src, dst) 
exit()

# def parseXml(filename): 
# xml = parse(codecs.open("C:/Users/User/lmao/candidate-0x4E6DDD7430E763A9.xml", encoding="utf-8")) # 
# tree = ET.fromstring(xml)
# for node in tree.iter('candidate'):
#     print('\n')
#     for elem in node.iter():
#         if elem.tag=="email":
#             print("{}: {}".format(elem.tag, elem.text))



       # doc = xml.dom.minidom.parse(filename);
       # nodeName = doc.nodeName
       # firstChild = doc.firstChild.tagName
       # email = doc.getElementsByTagName("email")
       # # email2 = doc.getElementsByTagName("email2")
       # for skill in email: 
       #     print_(skill.getAttribute("name")