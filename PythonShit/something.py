# 🦐 + 🍺 (26.02.2020 19:57):
# rmats, I added a list of source formats to be tried in sequence (sourceFormats), and on UnicodeDecodeError I try the next format:

from __future__ import with_statement 
import os 
import sys 
import codecs 
from chardet.universaldetector import UniversalDetector 

targetFormat = 'utf-8' 
outputDir = 'converted' 
detector = UniversalDetector()

def get_encoding_type(current_file): 
    detector.reset() 
    for line in file(current_file): 
        detector.feed(line) 
        if detector.done: break 
    detector.close() 
    return detector.result['encoding'] 

def convertFileBestGuess(filename):
    sourceFormats = ['ascii', 'iso-8859-1'] 
    for format in sourceFormats: 
        try: 
            with codecs.open(fileName, 'rU', format) as sourceFile: 
                writeConversion(sourceFile) 
                print('Done.') 
                return 
        except UnicodeDecodeError: 
            pass 

def convertFileWithDetection(fileName): 
    print("Converting '" + fileName + "'...") 
    format=get_encoding_type(fileName) 
    try: 
        with codecs.open(fileName, 'rU', format) as sourceFile: 
            writeConversion(sourceFile) 
            print('Done.') 
            return 
    except UnicodeDecodeError: 
        pass 
        print("Error: failed to convert '" + fileName + "'.") 

def writeConversion(file): 
    with codecs.open(outputDir + '/' + fileName, 'w', targetFormat) as targetFile: 
        for line in file: 
            targetFile.write(line) # Off topic: get the file list and call convertFile on each file # ...

for filename in os.listdir("C:/Users/User/lmao/"):
	something = convertFileWithDetection("C:/Users/User/lmao/" + filename)
