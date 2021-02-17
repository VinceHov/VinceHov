import sys
import os
import codecs
sys.path.append("..")
from xml2csv import *
baseDir = "C:/PERSON/"
for filename in os.listdir(baseDir + "completed/educ/"):
    xml2csv(baseDir + "completed/educ/" + filename, baseDir + "converted/educ/" + filename.split(".xml")[0] + ".csv" , False)
