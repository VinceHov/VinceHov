filenames = []
filenames.append("C:/neuroshelochka_1.rpy")
filenames.append("C:/neuroshelochka_2.rpy")
filenames.append("C:/neuroshelochka_3.rpy")
filenames.append("C:/neuroshelochka_4.rpy")
filenames.append("C:/neuroshelochka_5.rpy")
filenames.append("C:/neuroshelochka_6.rpy")
filenames.append("C:/neuroshelochka_7.rpy")
filenames.append("C:/neuroshelochka_8.rpy")
filenames.append("C:/neuroshelochka_9.rpy")
filenames.append("C:/neuroshelochka_10.rpy")
filenames.append("C:/neuroshelochka_11.rpy")
filenames.append("C:/neuroshelochka_12.rpy")
filenames.append("C:/neuroshelochka_13.rpy")
filenames.append("C:/neuroshelochka_14.rpy")
filenames.append("C:/neuroshelochka_15.rpy")
filenames.append("C:/neuroshelochka_16.rpy")
filenames.append("C:/neuroshelochka_17.rpy")
filenames.append("C:/neuroshelochka_18.rpy")
filenames.append("C:/neuroshelochka_19.rpy")
filenames.append("C:/neuroshelochka_20.rpy")
filenames.append("C:/neuroshelochka_21.rpy")
filenames.append("C:/neuroshelochka_22.rpy")
filenames.append("C:/neuroshelochka_23.rpy")
filenames.append("C:/neuroshelochka_24.rpy")
filenames.append("C:/neuroshelochka_25.rpy")
filenames.append("C:/neuroshelochka_26.rpy")
filenames.append("C:/neuroshelochka_27.rpy")
filenames.append("C:/neuroshelochka_28.rpy")
filenames.append("C:/neuroshelochka_29.rpy")
filenames.append("C:/neuroshelochka_30.rpy")
filenames.append("C:/neuroshelochka_31.rpy")
filenames.append("C:/neuroshelochka_32.rpy")
filenames.append("C:/neuroshelochka_33.rpy")
filenames.append("C:/neuroshelochka_34.rpy")
filenames.append("C:/neuroshelochka_35.rpy")
filenames.append("C:/neuroshelochka_36.rpy")
filenames.append("C:/neuroshelochka_37.rpy")
filenames.append("C:/neuroshelochka_38.rpy")
filenames.append("C:/neuroshelochka_39.rpy")
filenames.append("C:/neuroshelochka_40.rpy")
filenames.append("C:/neuroshelochka_41.rpy")
filenames.append("C:/neuroshelochka_42.rpy")
filenames.append("C:/neuroshelochka_43.rpy")
filenames.append("C:/neuroshelochka_44.rpy")
filenames.append("C:/neuroshelochka_45.rpy")
filenames.append("C:/neuroshelochka_46.rpy")
filenames.append("C:/neuroshelochka_47.rpy")
filenames.append("C:/neuroshelochka_48.rpy")
filenames.append("C:/neuroshelochka_49.rpy")
filenames.append("C:/neuroshelochka_50.rpy")

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
outputEncoding = "utf-8"
index = 0
lmaoindex = 1
attachments = []
# outputEncoding = ""
def decode(l, encoding):
    if isinstance(l, list):
        return [decode(x) for x in l]
    else:
        return l.decode(encoding)
for filename in filenames:
    print(lmaoindex, "of", len(filenames))
    lmaoindex += 1 
    # if lmaoindex > 4: 
    #     break
    oldDate = 0 
    index = 0
    complIndex = 0
    attachments.clear()
    path1 = filename
    path2 = filename.split(".rpy")[0] + "_fixed.rpy"
    text = ""
    output = ""
    with io.open(path1, mode='rb') as file: #, encoding=sourceEncoding , errors='ignore'
        file2 = open(path1, errors='ignore')
        content= file.read()
        file.close()

        print(filename, " Converted to ", path2, ", Status:Done")
        file= open(path2, 'w', encoding=outputEncoding, errors='ignore')
        print(content)#.decode('utf-8'))
        # print('НейроЮля и её Киберщёлочка_5'.encode('utf-8'))
        file.write(content.decode('utf-8')) #.encode('cp1251'), errors='ignore'
        file.close()
print("All process done")