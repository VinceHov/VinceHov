import re
file = open("C:/intel_threads.txt", 'r')
content = file.read()
cpus = content.split('\n')
result = []
translate = {
"Jan" : "1",
"Feb" : "2",
"Mar" : "3",
"Apr" : "4",
"May" : "5",
"Jun" : "6",
"Jul" : "7",
"Aug" : "8",
"Sep" : "9",
"Oct" : "10",
"Nov" : "11",
"Dec" : "12" }

for cpu in cpus:
	specs = cpu.split('\t')
	# print(specs)
	Name, Codename, Cores, Threads, Clock_min, Clock_max, Socket, Process, L3_Cache, Tdp, dd, mm, yy, date, lmao = specs
	# if "to" in Clock:
	# 	Clock_min = Clock.split(' to')[0]
	# 	Clock_max = Clock.split('to ')[1]
	# 	if not "." in Clock_min:
	# 		Clock_min += ".0"
	# 	Clock_min += " " + Clock_max.split(' ')[1]
	# else:
	# 	Clock_min = Clock_max = Clock
	# # print(Clock)
	# # print(Released.split(' '))
	# if Released != "Never Released":
	# 	if len(Released.split(' ')) == 2:
	# 		mm, yy = Released.split(' ')
	# 		dd = "1"
	# 	else:
	# 		mm, dd, yy = Released.split(' ')
	# 	mm = translate[mm]
	# 	dd = re.findall(r'\d+', dd)[0]
	# 	yy = yy 
	# 	date = '%s.%s.%s' % (mm,dd,yy) 
	# else:
	# 	mm = dd = yy = date = "Never Released"
	
	# result.append("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (Name, Codename, Cores, Threads, Clock_min, Clock_max, Socket, Process, L3_Cache, Tdp, dd, mm, yy, date))


# for res in result: 
# 	print(res)