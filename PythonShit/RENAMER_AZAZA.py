import os 
import subprocess 
basePath = "C:/NEWAZAZA/even/"
for filename in os.listdir(basePath):
    filename_new = filename.split("event-")
    try:
        os.rename(basePath + filename, basePath + filename_new[1] )
        pass
    except:
    	pass