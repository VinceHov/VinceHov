from __future__ import unicode_literals
from __future__ import absolute_import
import os
import subprocess 
import codecs
import unicodedata
sourceEncoding = "utf-8"
targetEncoding = "cp1251"
for filename in os.listdir("C:/Users/User/lmao/"):
	source = open("C:/Users/User/lmao/" + filename)
	target = open("C:/Users/User/lmao/" + filename, "w")
	source.read().encode(targetEncoding)
	# target.write(source.read().encode(targetEncoding))
