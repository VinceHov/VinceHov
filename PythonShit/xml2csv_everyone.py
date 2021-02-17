import os
import io
tags = []
names = []
tmp_names = []
tmp_name = ""
index = 0
output = "" #Закомментил чтобы собрать все в 1
tagindex = 0
for filename in os.listdir("C:/PERSON/completed/educ"):
    # if not "natarezn11" in filename:
    #     continue
    index += 1
    print(index , " file out of ", len(os.listdir("C:/PERSON/completed/educ")))
    # output = "" #Закомментил чтобы собрать все в 1
    # tags.clear()
    names.clear()
    with open("C:/PERSON/completed/educ/" + filename, 'r', encoding="utf-8", errors='ignore') as file:
        content = file.read().encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
        lines = content.split("\n")
        for line in lines: 
            try:
                first = line.split(">", maxsplit=1)[0].split("<")[1]
                print(first + "\n\n")
                second = line.split(">")[1].split("<")[0]
                print(second+ "\n\n")
                print(line+ "\n\n")
                pass
            except:
                continue
            if not first in tags:
                tags.append(first)
            if len(tmp_names) == 5:
                tmp_names.append(second)
                for name in tmp_names:
                    # print(name)
                    if tmp_names[5] == tmp_names[4]:
                        if name == tmp_names[0]:
                            tmp_name += "\"" + name + "\",\""
                        elif name == tmp_names[5] and name in tmp_name:
                            tmp_name += name + "\"" 
                        else:
                            tmp_name += name + '\",\"'
                    else:
                        if name == tmp_names[0]:
                            tmp_name += "\"" + name + "\",\""
                        elif name == tmp_names[5]: #and name in tmp_name:
                            tmp_name += name + "\"" 
                        else:
                            tmp_name += name + '\",\"'
                names.append(tmp_name)
                tmp_name = ""
                # print(names)
                # print(names)
                tmp_names.clear()
            else:
                tmp_names.append(second)
        # print(names , "\n\n")

        if tagindex == 0:
            for tag in tags:
                if tag == tags[0]:
                    output += "\"" + tag + "\",\""
                elif tag == tags[5]:
                    output += tag + "\"" 
                else:
                    output += tag + "\",\""
                tagindex = 1
                # print(output, "\n\n")
            output = output + "\n"
        for name in names: 
            output += name + "\n"
            # print(output, "\n\n")
        names.clear()
        file.close()   
# outputfile = open("C:/PERSON/converted/educ/" + filename.split(".xml")[0] + ".csv", "w", encoding='utf-8')
outputfile = open("C:/PERSON/converted/educ/" + "EVERYONE" + ".csv", "w", encoding='utf-8')
outputfile.write(output)
outputfile.close()
    # break