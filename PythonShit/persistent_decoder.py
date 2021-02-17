try:
 import cPickle as pickle
except:
 import pickle
#import io
#import os
import sys
import zlib
#import renpy
#import types
#import pickle
#from cStringIO import StringIO

f = open("C:/persistent", "rb")
data = f.read().decode("zlib")
f.close()

index = pickle.loads(data)
print(data)
# f = open(sys.argv[2], "wb")
# f.write(str(len(index.keys()))+"\\n")
# for key in index.keys():
#  for offset, dlen, start in index[key]:
#   f.write(key+"\\n")
#   f.write(str(offset)+"\\n")
#   f.write(str(dlen)+"\\n")
#   f.write(str(start)+"\\n")
#   f.write("\\n")
 
f.close()