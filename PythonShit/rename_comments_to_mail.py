import os 
import io
import re
import os.path
baseDir = "C:/NEWAZAZA/even/"
sourceEncoding = "cp1251"
targetEncoding = "utf-8"
for filename in os.listdir(baseDir):
    if not "@" in filename:
        path1 = baseDir + filename
        filename_xml = filename.split(".txt")[0]
        path2 = "C:/NEWAZAZA/cand_new/" + "candidate-" + filename_xml + ".xml"
        try:
            with io.open(path2, encoding=targetEncoding, errors='ignore') as file: #Открываем файл
                content= file.read().encode(targetEncoding, errors='ignore').decode(targetEncoding, errors='ignore') #Читаем
                file.close()
                ###Небольшой апдейт:
                # try:
            pass
        except: 
            print("No such file:: ", path2)
            continue
        filenameNew =  content.split("<email>")[1].split("</email>")[0] + ".txt"
        print("File " + filename + " renamed to " + filenameNew)
        if os.path.exists(baseDir+filenameNew):
            print("But this file already exists... Comparing with!", filenameNew)
            print(filenameNew, " EXIST! COMPARING WITH", filename)
            file1= open(baseDir + filenameNew, encoding=sourceEncoding, errors='ignore')
            file2= open(baseDir + filename, encoding=sourceEncoding, errors='ignore')
            content1 = file1.read()
            content2 = file2.read()
            file1.close()
            file2.close()
            print("успех")
            file = open(baseDir + filenameNew, 'w', encoding=sourceEncoding, errors='ignore')
            # content2= file.read().encode(sourceEncoding, errors='ignore').decode(sourceEncoding, errors='ignore')
            file.write(content2 + "\n\n\n" + content1) #content2, 
            file.close()
            os.remove(path1)
        else:
            print("Norm vse.")     
            os.rename(path1, baseDir+filenameNew)
            pass
        # except: 
            # print("Ошибка в " , filename)
            # print("path1=", path1, " path2=", baseDir+filenameNew)
            # print(content2, )
            # pass
    
       
print("All process done")