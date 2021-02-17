# import pdb; pdb.set_trace()
import os
import subprocess 
import mmap
import os.path
import io
baseDir = "C:/AZAZA/person/"
sourceEncoding = "cp1251"
targetEncoding = "utf-8"
index = 1
for filename in os.listdir(baseDir):
    index_of_comments = 0
    error = 0 
    baseDir = "C:/AZAZA/person/"
    path1 = baseDir + filename
    with io.open(path1, encoding=sourceEncoding, errors='ignore') as file: #Открываем файл
        content= file.read().encode(sourceEncoding, errors='ignore').decode(sourceEncoding, errors='ignore') #Читаем
        file.close() #Закрываем
        split_shit = content #Берём в разделитель 
        prevJobs = split_shit.split("<prev_jobs>") #Выгребаем комменты
        # for filecounter in prevJobs:  #Проверяем на наличие двух комментов (не актуально)
        #     index_of_comments = index_of_comments + 1
        #     if index_of_comments > 2: 
        #         print("ALERT! CHECK " + filename, "\n\n\n")
        # print("!!__FIRSTSPLIT__!!",  prevJobs , "!!__FIRSTSPLIT__!!" )
        
        try:
            prevJobs = prevJobs[1].split("</prev_jobs>") #Забираем работу
            baseDir = "C:/AZAZA/jobs/"
            pass
        except:
            print("Ошибка чтения работы в ", filename)
            print("ЛОГ РАБОТЫ:", prevJobs)
            error = error + 1
            pass
         
        prevEduc = split_shit.split("<prev_educations>")
        
        try: 
            prevEduc = prevEduc[1].split("</prev_educations>")
            baseDir = "C:/AZAZA/educ/"
            pass
        except: 
            print("Ошибка чтения образования в ", filename)
            print("ЛОГ ОБРАЗОВАНИЯ:", prevEduc)
            error = error + 1
            pass
        filename_new = content.split("<email>")
        # print(filename_new)
        
        try:
            filename_new = filename_new[1].split("</email>") #Забираем ид кандидата
            pass
        except:
            error = 2
            filename_new[0] = "UNNAMED_PERSON_" + filename #Если не нашли ид кандидата
            pass
        # content = prevJobs[0] 

        path2 = baseDir +  filename_new[0] + ".xml" 
        if error == 0:
            errortext = "Done"
            pass
        elif error == 1:
            errortext = "NoCriticalError"
            pass 
        else: 
            errortext = "CriticalError"
            pass

        print(filename, " Converted to ", filename_new[0] + ".xml" , ", Status:",errortext)
        
        if error == 0:
            path2 = "C:/AZAZA/educ/" +  filename_new[0] + ".xml" 
            print(filename_new[0], " First_file from ", filename)
            file= open(path2, 'w', encoding=sourceEncoding, errors='ignore')
            file.write(prevEduc[0] + ":" + "\n" + prevJobs[0])
            file.close()
            path2 = "C:/AZAZA/jobs/" +  filename_new[0] + ".xml" 
            print(filename_new[0], " Second_file from ", filename)
            file= open(path2, 'w', encoding=sourceEncoding, errors='ignore')
            file.write(prevEduc[0] + ":" + "\n" + prevJobs[0])
            file.close()
        elif error == 1: #Если забрали коммент
            # try:
            # if not os.path.exists(path2):
            print(filename_new[0], " NOT EXIST! CREATING FROM", filename)
            file= open(path2, 'w', encoding=sourceEncoding, errors='ignore')
            file.write(prevEduc[0] + ":" + "\n" + prevJobs[0])
            file.close()
            pass 
        else:
            os.remove(path1)
            pass
            # else: 
            #     print(filename_new[0], " EXIST! COMPARING WITH", filename)
            #     file= open(path2, 'a', encoding=sourceEncoding, errors='ignore')
            #     # content2= file.read().encode(sourceEncoding, errors='ignore').decode(sourceEncoding, errors='ignore')
            #     file.write("\n\n\n" + prevEduc[2] + "." + prevEduc[1] + "." + prevEduc[0] + ":" + "\n" + prevJobs[0]) #content2, 
            #     file.close()
            #     pass
            # except: 
                # print("Convertion failed:: ", "\nErrorcode: ", error, "\nFile: ", filename)
                # pass
print("All process done")
            
# x = txt.split()

# print(x)



