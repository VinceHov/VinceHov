import glob 
import os
a = os.path.join(r"E:\neuronet\stylegan2\alice", '*.jpg').replace("\\", "/")
b  = sorted(glob.glob(a))
print(b)