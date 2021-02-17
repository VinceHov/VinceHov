# import pdb; pdb.set_trace()
import os
import subprocess 
import mmap
import os.path
# import codecs
import io
# import unicodedata
baseDir = "C:/NEWAZAZA/even/"
sourceEncoding = "cp1251"
targetEncoding = "utf-8"
index = 1
for filename in os.listdir(baseDir):
    index_of_comments = 0
    error = 0 
    path1 = baseDir + filename
    with io.open(path1, encoding=sourceEncoding, errors='ignore') as file: #Открываем файл
        content= file.read().encode(sourceEncoding, errors='ignore').decode(sourceEncoding, errors='ignore') #Читаем
        file.close() #Закрываем
        split_shit = content #Берём в разделитель 
        commentProcess = split_shit.split("<comment>") #Выгребаем комменты
        for filecounter in commentProcess:  #Проверяем на наличие двух комментов (не актуально)
            index_of_comments = index_of_comments + 1
            if index_of_comments > 2: 
                print("ALERT! CHECK " + filename, "\n\n\n")
        # print("!!__FIRSTSPLIT__!!",  commentProcess , "!!__FIRSTSPLIT__!!" )
        
        try:
            commentProcess = commentProcess[1].split("</comment>") #Забираем коммент
            commentProcess[0].replace("&#13;&#10;", "\n")
            # print("!!__SECONDSPLIT__!!" , commentProcess , "!!__SECONDSPLIT__!!")
            pass
        except:
            print("Ошибка чтения коммента в ", filename)
            error = 1
            pass
         
        commentDate = split_shit.split("<date>")
        
        try: 
            commentDate = commentDate[1].split("</date>")
            commentDate = commentDate[0].split("T")
            commentDate = commentDate[0].split("-")
            pass
        except: 
            print("Ошибка чтения даты в ", filename)
            error = 1
            pass
        filename_new = content.split("<candidate_id>")
        # print(filename_new)
        
        try:
            filename_new = filename_new[1].split("</candidate_id>") #Забираем ид кандидата
            pass
        except:
            error = 2
            filename_new[0] = "UNNAMED_CANDIDATE_" + filename #Если не нашли ид кандидата
            pass
        # content = commentProcess[0] 

        path2 = baseDir +  filename_new[0] + ".txt" 
        if error == 0:
            errortext = "Done"
            pass
        elif error == 1:
            errortext = "Error"
            pass 
        else: 
            errortext = "NoCandidateError"
            pass

        print(filename, " Converted to ", filename_new[0] + ".txt" , ", Status:",errortext)

        if error == 0: #Если забрали коммент
            # try:
            if not os.path.exists(path2):
                print(filename_new[0], " NOT EXIST! CREATING FROM", filename)
                file= open(path2, 'w', encoding=sourceEncoding, errors='ignore')
                file.write(commentDate[2] + "." + commentDate[1] + "." + commentDate[0] + ":" + "\n" + commentProcess[0])
                file.close()
                pass
            else: 
                print(filename_new[0], " EXIST! COMPARING WITH", filename)
                file= open(path2, 'a', encoding=sourceEncoding, errors='ignore')
                # content2= file.read().encode(sourceEncoding, errors='ignore').decode(sourceEncoding, errors='ignore')
                file.write("\n\n\n" + commentDate[2] + "." + commentDate[1] + "." + commentDate[0] + ":" + "\n" + commentProcess[0]) #content2, 
                file.close()
                pass
            # except: 
                # print("Convertion failed:: ", "\nErrorcode: ", error, "\nFile: ", filename)
                # pass
print("All process done")
            
# x = txt.split()

# print(x)



