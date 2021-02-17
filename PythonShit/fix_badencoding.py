# -*- coding: utf-8 -*-
from xml.sax import saxutils
# import pdb; pdb.set_trace()
import os
import subprocess 
import mmap
import io
import codecs
import re
baseDir = 'D:/badencoding/'
outputDir = 'D:/converted2'
sourceEncoding = 'cp1251'
targetEncoding = 'utf-8'
lmaoindex = 1
errors = 0
bytedict = [b'\xd1', b'<', b' ', b',', b'.', b':', b'"', b';', b')', b'(', b'C', b'&', b'-', b'\xd0']
def fixbyte(byte, bytedict):
    tmpbyte = byte
    tmpbyte2 = re.split(b'\xd0[%s]' % bytedict, tmpbyte )
    outputbyte = ""
    outputbyte = (b'\xd0\x98%s' % bytedict).join(tmpbyte2)
    return outputbyte

for filename in os.listdir(baseDir):
    print(lmaoindex, 'file of ', len(os.listdir(baseDir)))
    if errors == 1: 
        break
    with io.open(baseDir + filename, 'r', encoding=targetEncoding) as file:
        content = file.read()
        file.close()
        output = content
        path2 = "D:/converted2/" +  filename.split(".xml")[0] + ".html"
        output = output.encode('cp1251')
        for word in bytedict:
            output = fixbyte(output, word)
        try:
            output = output.decode('utf-8', errors='ignore')
        except Exception as e:
            # print(filename)
            print(e)
            if lmaoindex == 1: 
                tmpbyte = output
                tmpbyte2 = re.split(b'\xe2\x8004', tmpbyte )
                # outputbyte = ""
                output = (b'\xe2\x80\x9404').join(tmpbyte2).decode('utf-8')
            if lmaoindex == 2:
                tmpbyte = output
                tmpbyte2 = re.split(b'\xe2\x85', tmpbyte, maxsplit=2 )
                output = (b'\xe2\x94\x85').join(tmpbyte2)
                tmpbyte = output
                tmpbyte2 = re.split(b'\xe2\x80ve', tmpbyte )
                output = (b'\xe2\x94\x85ve').join(tmpbyte2)
                output = output.decode('utf-8')
            if lmaoindex == 3:
                tmpbyte = output
                tmpbyte2 = re.split(b'\xe2\x80\xd1', tmpbyte )
                # outputbyte = ""
                output = (b'\xe2\x80\x99\xd1').join(tmpbyte2).decode('utf-8')
                # \xe2\x80\x99\xd1
                # print(output)
                # errors = 1

        outputEncoding = targetEncoding
        output = "\n".join(output.split("&#13;&#10;"))
        output = "\t".join(output.split("&#9;"))
        lmaoindex += 1
        # print(filename, " Converted to ", filename, ", Status:Done")
        file= open(path2, 'w', encoding=outputEncoding, errors='ignore')
        file.write(output)
        file.close()
print("All process done")