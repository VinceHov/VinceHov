import os
import subprocess 
import mmap
# import codecs
import io
basePath = "C:/AZAZA/even/"
sourceEncoding = "cp1251"
for filename in os.listdir(basePath):
    endWhile = 0 
    error = 0 
    path1 = basePath + filename
    with io.open(path1, encoding=sourceEncoding, errors='ignore') as file:
        content= file.read().encode(sourceEncoding, errors='ignore').decode(sourceEncoding, errors='ignore')
        file.close()
        split_shit = content
        try:
            commentProcess = split_shit.split("<candidate_id>", maxsplit=1)
            # print(commentProcess , "\n\n\n")
            try: 
                commentProcess = commentProcess[1].split("</candidate_id>", maxsplit=1)
                print("File " + filename + " is status: OK")
            except:
                os.remove(path1)
                print("Deleting " + filename)
            pass
        except:
            os.remove(path1)
            print("Deleting " + filename)
            raise 
print("All process done")