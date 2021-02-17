import os 
import io
import re
import os.path
baseDir = "C:/NEWAZAZA/cand/"
index = 1
sourceEncoding = "cp1251"
targetEncoding = "utf-8"
for filename in os.listdir(baseDir):
    path1 = baseDir + filename
    # filename_xml = filename.split(".txt")[0]
    path2 = "C:/NEWAZAZA/cand_nomail/" + filename
    # try:
    with io.open(path1, encoding=sourceEncoding, errors='ignore') as file: #Открываем файл
        print("Ну типа открыл, да")
        content= file.read().encode(sourceEncoding, errors='ignore').decode(sourceEncoding, errors='ignore') #Читаем
        file.close()
        print("И типо даже считал")
        if not "<email>" in content: 
            print("Всё заебись")
            #fuckDis = content.split("</is_candidate>", maxsplit=1)
            #content = str(fuckDis[0]) + "</is_candidate>" + "<email>fiction_mail" + str(index) + "@noma.il</email>" + str(fuckDis[1])
            #index = index + 1
            #print("Candidate " + filename + " get a new mail: " + "fiction_mail" + str(index) + "@noma.il")
            ## os.rename(path1, baseDir+filenameNew)
            file = open(path2, "w", encoding=sourceEncoding, errors='ignore')
            file.write(content)

            pass
    # except: 
    #     print(fuckDis)
    #     print("I cant open dis shit:: ", path1)s
    #     pass
               
print("All process done")