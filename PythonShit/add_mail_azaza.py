import os 
import io
import re
import os.path
import codecs
baseDir = "C:/NEWAZAZA/cand_nomail/"
index = 1
sourceEncoding = "cp1251"
targetEncoding = "utf-8"
# checkFile = open("C:/NEWAZAZA/No_Email.txt", 'w', encoding=targetEncoding, errors='ignore')
tmp_check = io.open("C:/NEWAZAZA/No_Email.txt", encoding=targetEncoding, errors='ignore').read().encode(targetEncoding, errors='ignore').decode(targetEncoding, errors='ignore')
lines = tmp_check.split("\n")
print(lines)
for line in lines:
    fullname = line.split(",")[0]
    mail = line.split(",")[1]
    for filename in os.listdir(baseDir):
        path1 = baseDir + filename
        path2 = "C:/NEWAZAZA/cand_nomail/" + filename
        with io.open(path1, encoding=sourceEncoding, errors='ignore') as file: #Открываем файл
            content= file.read().encode(sourceEncoding, errors='ignore').decode(sourceEncoding, errors='ignore') #Читаем
            file.close()
            # print("И типо даже считал")
            if not "<email>" in content: 
                # print("Всё заебись")
                try:
                    checkFullname = content.split("<fullname>")[1]
                    pass
                except:
                    print("ПИЗДА ВООБЩЕ НЕТУ ИМЕНИ В ", filename)
                    pass
                checkFullname = content.split("</fullname>")[0]
                if fullname in checkFullname:
                    fuckDis = content.split("</is_candidate>", maxsplit=1)
                    content = str(fuckDis[0]) + "</is_candidate>" + "<email>" + mail + "</email>" + str(fuckDis[1])
                    index = index + 1
                    print("Candidate " + filename + " get a new mail: " + mail )
                    file = open(path2, "w", encoding=sourceEncoding, errors='ignore')
                    file.write(content)
                    pass
                else:
                    pass
            else: 
                print("Не всё заебись с ", filename)
                pass

print("All process done")