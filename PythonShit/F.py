import subprocess
import re
# cmdpath = u.encode('utf-8').decode('utf-8')
subpart = re.split(r'Seed:.*', subprocess.check_output("python3 E:\\нейросетки\\петончег\\нейросетка.py -t E:\\нейросетки\\петончег\\pls.txt -o 1000 -g").decode('utf-8'))[1]
print(subpart[:7])
print(subpart[8:15])
print(subpart[16:17])
print(subpart[18:23])
print(subpart[24:28])
print(subpart[29:30])
print(subpart[31:32])
print(subpart[33:34])
print(subpart[35:36])
print(subpart[37:38])
# $$$$$$$$
# $$$$$$$
# $$
# $$$$$$
# $$$$$
# $$
# $$
# $$
# $$
# $$