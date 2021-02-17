import os
import subprocess 
import mmap
import os.path
import io
import shutil 
import re

def get_educ(split_shit): 
    educ_shit = re.findall("(?s)(?<=<prev_education>).*?(?=</prev_education>)", split_shit) #Выгребаем все обучалки.
    if len(educ_shit) == 0:
        print("educ false in ", filename)
        print(educ_shit)
    else:
        return educ_shit

def get_job(split_shit):
    job_shit = re.findall("(?s)(?<=<prev_job>).*?(?=</prev_job>)", split_shit) #Выгребаем работки.
    if len(job_shit) == 0:
        print("jobs false in ", filename)
        print(job_shit)
    else:
        return job_shit

def convertDate(date): #Меняем формат даты
    date = date + "T12:00:00"
    return date

baseDir = "C:/PERSON/"
sourceEncoding = "utf-8"
targetEncoding = "utf-8"
fileMode = []
printEduc = []
printJob = []
educProcess = []
jobsProcess = []
for filename in os.listdir(baseDir + "person/"):
    # if not "0x5A5DEF4D49CB7449" in filename:
    #     continue
    writeEduc = ""
    writeJob = ""
    index = 1
    #INITIALISATION
    error = 0
    printEduc.clear()
    printJob.clear()
    fileMode.clear() 
    try:
        educProcess.clear()
    except:
        pass
    try:
        jobsProcess.clear()
    except: 
        pass
    path1 = baseDir + "person/" + filename
    fileForMail = filename.split(".xml")[0].split("person-")[1]
    # print(fileForMail)

    #MAIN FILE OPERATIONS
    with io.open(path1, encoding=sourceEncoding, errors='ignore') as file: #Открываем файл
        content= file.read().encode(sourceEncoding, errors='ignore').decode(targetEncoding, errors='ignore') #Читаем
        file.close() #Закрываем

        #MAIL BLOCK
        try:
            mailConst = content.split("<email>")[1].split("</email>")[0]
            if len(mailConst) == 0: 
                continue
            pass
        except:
            try: #Получаем мыло
                candID = fileForMail #content.split("</id>", maxsplit=1)[0].split("<id>")[1]
                print(candID)
                mailContent = open(baseDir + "cand/" + "candidate-" + candID + ".xml").read().encode(sourceEncoding, errors='ignore').decode(targetEncoding, errors='ignore')
                mailConst = mailContent.split("</email>", maxsplit=1)[0].split("<email>")[1]
                print(mailConst)
                pass
            except: 
                shutil.move(baseDir + "person/" + filename, baseDir + "noid")
                # print(content, "MAILCONTENT\n", mailContent)
                continue
            pass
        split_shit = content #Берём в разделитель

        #CHECK FILEMODE
        try:
            educProcess = get_educ(split_shit) #Выгребаем обучалки
            if not len(educProcess) == 0:
                # print(educProcess)
                fileMode.append("educ")
                pass
            pass
        except: 
            pass

        try:
            jobsProcess = get_job(split_shit)
            if not len(jobsProcess) == 0: 
                # print(jobsProcess)
                fileMode.append("job")
                pass
            pass
        except: 
            pass 

        #EXCEPTIONS HANDLE NOMODE
        if len(fileMode) == 0:
            shutil.move(baseDir + "person/" + filename, baseDir + "nomode")
            continue
        # print(jobsProcess)
        #EDUCATION GET PROCESS
        if "educ" in fileMode:
            for educSource in educProcess: 
                outputContentEduc = "<candidateId>" + mailConst + "</candidateId>\n" + "<education>education</education>\n" + "<direction>" + re.findall("(?s)(?<=<speciality_name>).*?(?=</speciality_name>)", educSource)[0] + "</direction>\n" + "<school>" + re.findall("(?s)(?<=<org_name>).*?(?=</org_name>)", educSource)[0] + "</school>\n" 
                index = index + 1
                try:
                    endDate = educSource.split("<end_date>")[1].split("</end_date>")[0]
                except: 
                    print("No Date in " , filename, index)
                    endDate = educSource.split("<start_date>")[1].split("</start_date>")[0]
                    pass# continue
                try:
                    startDate = educSource.split("<start_date>")[1].split("</start_date>")[0]
                    pass
                except: 
                    startDate = endDate
                    pass

                ##CONVERT DATA
                try: 
                    startDate = convertDate(startDate)
                    endDate = convertDate(endDate)
                    pass
                except: 
                    print("Ошибка чтения даты в ", filename)
                    error = 1
                    pass
                outputContentEduc = outputContentEduc + "<start_date>" + startDate + "</start_date>\n" + "<end_date>" + endDate + "</end_date>\n" 
                printEduc.append(outputContentEduc)
                pass
                
    
        #JOBS GET PROCESS
        if "job" in fileMode:
            # print(jobsProcess)
            for jobSource in jobsProcess:
                outputContentJob = "<candidateId>" + mailConst + "</candidateId>\n" + "<outsideWorkExperience>outsideWorkExperience</outsideWorkExperience>\n" + "<employer></employer>\n"  + "<startTitle>" + re.findall("(?s)(?<=<position_name>).*?(?=</position_name>)", jobSource)[0] + "</startTitle>\n" 
                index = index + 1
                try:
                    endDate = jobSource.split("<end_date>")[1].split("</end_date>")[0]
                except: 
                    print("No Date in " , filename, index)
                    endDate = jobSource.split("<start_date>")[1].split("</start_date>")[0]
                    # print(jobsProcess)
                    pass #continue
                try:
                    startDate = jobSource.split("<start_date>")[1].split("</start_date>")[0]
                    pass
                except: 
                    startDate = endDate
                    
                ##CONVERT DATA
                try: 
                    startDate = convertDate(startDate)
                    endDate = convertDate(endDate)
                    pass
                except: 
                    print("Ошибка чтения даты в ", filename)
                    error = 1
                    pass
                outputContentJob = outputContentJob + "<start_date>" + startDate + "</start_date>\n" + "<end_date>" + endDate + "</end_date>\n" 
                printJob.append(outputContentJob)
            pass

        filename_new = mailConst + ".xml"
        path2 = baseDir + "completed/" 

        if error == 0:
            errortext = "Done"
            pass
        elif error == 1:
            errortext = "Error"
            pass 
        else: 
            errortext = "NoCandidateError"
            pass

        print(filename, " Converted to ", filename_new , ", Status:",errortext)

        # try:
        if "educ" in fileMode:
            # print(printEduc)
            print("Creating ",filename_new, " on Educ")
            file1= open(path2 + "educ/" + filename_new, 'w', encoding=targetEncoding, errors='ignore')
            for elementEduc in printEduc:
                writeEduc += str(elementEduc)
            # print("WRITEEDUC == ", writeEduc)
            file1.write(writeEduc)
            file1.close()
            print("Success!")
            pass
        if "job" in fileMode:
            # print(printJob)
            print("Creating ",filename_new, " on Jobs")
            file2= open(path2 + "jobs/" + filename_new, 'w', encoding=targetEncoding, errors='ignore')
            for elementJobs in printJob:
                writeJob += str(elementJobs)
            # print("WRITEJOB == ", writeJob)    
            file2.write(writeJob) #content2, 
            file2.close()
            print("Success!")
            pass
        # except: 
        #     print("Convertion failed:: ", "\nErrorcode: ", error, "\nFile: ", filename)
        #     pass
print("All process done")




