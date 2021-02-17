# -*- coding: utf-8 -*-
from xml.sax import saxutils
# import pdb; pdb.set_trace()
import os
import subprocess 
import mmap
import io
import codecs
import re
date = ""
baseDir = "D:/cand/"
outputDir = "D:/converted/"
sourceEncoding = "cp1251"
targetEncoding = "utf-8"
index = 0
lmaoindex = 1
attachments = []
outputEncoding = ""
def decode(l, encoding):
    if isinstance(l, list):
        return [decode(x) for x in l]
    else:
        return l.decode(encoding)
for filename in os.listdir(baseDir):
    print(lmaoindex, "of", len(os.listdir(baseDir)))
    lmaoindex += 1 
    # if lmaoindex > 4: 
    #     break
    oldDate = 0 
    index = 0
    complIndex = 0
    attachments.clear()
    path1 = baseDir + filename
    text = ""
    output = ""
    with io.open(path1, mode='r', encoding=sourceEncoding, errors='ignore') as file:
        file2 = open(path1, errors='ignore')
        # checkUTF = mmap.mmap(file2.fileno(), 0, access=mmap.ACCESS_READ)
        # if checkUTF.find(b'charset=utf-8') != -1: 
        # if "charset=utf-8" in file.read():
        #     targetEncoding = "utf-8"
        #     pass
        # else:
        #     targetEncoding = sourceEncoding
        #     pass
        content= file.read()
        file.close()
        attachments = re.findall("(?s)(?<=<attachment>).*?(?=</attachment>)", content)
        if len(attachments) == 0:
            continue
        for attachment in attachments:
            AttDate = re.findall("(?s)(?<=<date>).*?(?=</date>)", attachment)
            tmpdate = AttDate[0].split("T", maxsplit=1)[0]
            tmpListDate = tmpdate.split("-")
            for subdate in tmpListDate:
                date += subdate
            if oldDate: 
                if date > oldDate:
                    oldDate = date
                    complIndex = index
            else:
                oldDate = date
            index = index + 1
        processAttachment = attachments[complIndex]

        try:
            text = ( "&lt;" +  re.findall("(?s)(?<=&lt;).*?(?=</text>)", processAttachment)[0])
            pass
            path2 = "D:/converted/" +  filename.split(".xml")[0] + ".html"
        except: 
            print(filename, "errors occured")
            # print(processAttachment)        # print(text)
            path2 = "D:/failed/" +  filename.split(".xml")[0] + ".html"
        
        output = saxutils.unescape(str(text))
        
        if output.find("charset=utf-8") > 0:
            # byteoutput = output.encode(sourceEncoding)
            # txtbytes = byteoutput.split(b'\xd0\x98')
            # outpututf = ""
            # byteindex = 0 
            # for byte in txtbytes: 
            #     print(byte)
            #     outpututf +=  byte.decode('utf-8') + 'И'
            #     # print(txtbytes[byteindex])
            #     byteindex += 1 

            tmpoutput = output.encode('cp1251')
            tmpbytes = tmpoutput.split(b'\xd0\xd0')
            bytez = ""
            bytez = b'\xd0\x98\xd0'.join(tmpbytes)

            tmpoutput2 = bytez
            tmpbytes2 = tmpoutput2.split(b'\xd0\xd1')
            bytez2 = ""
            bytez2 = b'\xd0\x98\xd1'.join(tmpbytes2)

            # tmptext3 = re.split(re'(\xd0\\w)|(\xd0\\d)(\xd0\\s)|(\xd0\\S)|(\xd0\\W)|(\xd0)')
            # print(bytez)
            tmpoutput3 = bytez2
            tmpbytes3 = tmpoutput3.split(b'\xd0<')
            bytez3 = ""
            bytez3 = b'\xd0\x98<'.join(tmpbytes3)

            tmpoutput4 = bytez3
            tmpbytes4 = tmpoutput4.split(b'\xd0 ')
            bytez4 = ""
            bytez4 = b'\xd0\x98 '.join(tmpbytes4)

            tmpoutput5 = bytez4
            tmpbytes5 = tmpoutput5.split(b'\xd0,')
            bytez5 = ""
            bytez5 = b'\xd0\x98,'.join(tmpbytes5)

            tmpoutput6 = bytez5
            tmpbytes6 = tmpoutput6.split(b'\xd0.')
            bytez6 = ""
            bytez6 = b'\xd0\x98.'.join(tmpbytes6)
            
            tmpoutput7 = bytez6
            tmpbytes7 = tmpoutput7.split(b'\xd0\xd0')
            bytez7 = ""
            bytez7 = b'\xd0\x98\xd0'.join(tmpbytes7)

            tmpoutput8 = bytez7
            tmpbytes8 = tmpoutput8.split(b'\xd0:')
            bytez8 = ""
            bytez8 = b'\xd0\x98:'.join(tmpbytes8)

            tmpoutput9 = bytez8
            tmpbytes9 = tmpoutput9.split(b'\xd0"')
            bytez9 = ""
            bytez9 = b'\xd0\x98"'.join(tmpbytes9)

            tmpoutput10 = bytez9
            tmpbytes10 = tmpoutput10.split(b'\xd0;')
            bytez10 = ""
            bytez10 = b'\xd0\x98;'.join(tmpbytes10)

            tmpoutput11 = bytez10
            tmpbytes11 = tmpoutput11.split(b'\xd0)')
            bytez11 = ""
            bytez11 = b'\xd0\x98)'.join(tmpbytes11)
            
            tmpoutput12 = bytez11
            tmpbytes12 = tmpoutput12.split(b'\xd0(')
            bytez12 = ""
            bytez12 = b'\xd0\x98('.join(tmpbytes12)
            
            tmpoutput13 = bytez12
            tmpbytes13 = tmpoutput13.split(b'\xd0\xc2')
            bytez13 = ""
            bytez13 = b'\xd0\x98\xc2'.join(tmpbytes13)

            tmpoutput14 = bytez13
            tmpbytes14 = tmpoutput14.split(b'\xd0C')
            bytez14 = ""
            bytez14 = b'\xd0\x98C'.join(tmpbytes14)

            tmpoutput15 = bytez14
            tmpbytes15 = tmpoutput15.split(b'\xd0&')
            bytez15 = ""
            bytez15 = b'\xd0\x98&'.join(tmpbytes15)

            tmpoutput16 = bytez15
            tmpbytes16 = tmpoutput16.split(b'\xd0-')
            bytez16 = ""
            bytez16 = b'\xd0\x98-'.join(tmpbytes16)

            try:
                output = bytez16.decode('utf-8')
            except:
                output = bytez16.decode('utf-8', errors='ignore')
                # print(bytez16)
                path2 = "D:/badencoding/" + filename.split('.xml')[0] + ".html"
            outputEncoding = targetEncoding
            # try:
            # output = str(output).encode(targetEncoding).decode(targetEncoding) 
            # except: 
            #     output = output.encode(targetEncoding).decode(targetEncoding)
        elif output.find("charset=windows-1251") > 0: 
            # print("123awds")
            outputEncoding = sourceEncoding
            # output = output.encode(sourceEncoding).decode(sourceEncoding)
        # except:
            # path2 = "D:/badencoding/" + filename

        output = "\n".join(output.split("&#13;&#10;"))
        output = "\t".join(output.split("&#9;"))

        print(filename, " Converted to ", filename, ", Status:Done")
        file= open(path2, 'w', encoding=outputEncoding, errors='ignore')
        file.write(output) 
        file.close()
print("All process done")