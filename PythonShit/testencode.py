# import pdb; pdb.set_trace()
import os
import subprocess 
import mmap
# import codecs
import io
# import unicodedata
baseDir = "C:/NEWAZAZA/cand_new/"
sourceEncoding = "cp1251"
targetEncoding = "utf-8"
index = 1
for filename in os.listdir(baseDir):
    path1 = baseDir + filename
    with io.open(path1, encoding=sourceEncoding, errors='ignore') as file:
        file2 = open(path1, errors='ignore')
        checkUTF = mmap.mmap(file2.fileno(), 0, access=mmap.ACCESS_READ)
        if checkUTF.find(b'charset=utf-8') != -1: 
        # if "charset=utf-8" in file.read():
        #     targetEncoding = "utf-8"
        #     pass
        # else:
        #     targetEncoding = sourceEncoding
        #     pass
            content= file.read().encode(sourceEncoding, errors='ignore').decode(targetEncoding, errors='ignore')
        else:
            content= file.read().encode(sourceEncoding, errors='ignore').decode(sourceEncoding, errors='ignore')
        # print(file.read())
        file.close()
        # print(content)
        split_shit = content
        newFileName = split_shit.split("<email>")
        try:
            newFileName = newFileName[1].split("</email>")
            pass
        except:
            newFileName[0] = str(index) + "@gmail.com"
            index = index + 1
            pass
        path2 = baseDir +  newFileName[0] + ".xml" 
        print(filename, " Converted to ", newFileName[0], ", Status:Done")
        file= open(path2, 'w', encoding=sourceEncoding, errors='ignore')
        file.write(content)
        file.close()
print("All process done")

# x = txt.split()

# print(x)



