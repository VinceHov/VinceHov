import pickle
import os
import codecs 

file = open("D:/persistent", 'rb')
test1 = file.read()#.decode('zlib')
data = codecs.decode(test1, encoding='zlib')
file.close()
index = pickle.loads(data)
print(data)