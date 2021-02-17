import re
file = open("C:/Users/VinceHov/Desktop/txt/od.txt", "r", encoding="utf-8")

content = file.read()
print(len(content))

lines = content.split("\n")
print(len(lines))

res = ""
for line in lines: 
	if re.findall('ольга', line, re.I): 
		res += str(line.split('"')[1].split('"')[0] + "\n")


file = open('C:/od.txt', 'w+', encoding='utf-8')
file.write(res)
file.close()