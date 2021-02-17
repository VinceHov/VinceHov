from xml.sax import saxutils
import os
import io
index = 0
baseDir = "C:/Candidate/"
for filename in os.listdir(baseDir):
	index += 1
	print(index, "out of", len(os.listdir(baseDir)))
	with io.open(baseDir + filename,  mode='r', encoding ='utf-8', errors='ignore') as file:
		content = file.read().encode(encoding='utf-8', errors='ignore').decode(encoding='utf-8', errors='ignore')
        file.close()
        output = saxutils.unescape(content)
        file1 = open("C:/Completed/" + filename, mode='w', encoding='utf-8', errors='ignore')
        file1.write(output)
        file1.close()