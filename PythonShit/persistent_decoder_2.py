# RenPy persistent unpickler 0.1


try:
    import cPickle as pickle
except:
    import pickle
import sys
import zlib
import codecs
import renpy

f = open("D:/persistent", "rb")

data = f.read()
data = codecs.decode(data, encoding='zlib')
f.close()

index = pickle.loads(data)

f = open("D:/persistent.txt", "wb")
f.write(str(len(index.keys()))+"\\n")
for key in index.keys():
    for offset, dlen, start in index[key]:
        f.write(key+"\\n")
        f.write(str(offset)+"\\n")
        f.write(str(dlen)+"\\n")
        f.write(str(start)+"\\n")
        f.write("\\n")

f.close()