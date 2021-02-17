import  requests
import re
amd_list = []
intel_list = []
for year in range(2000,2021):
    print("Year is: %d" % year)
    res = requests.get("https://www.techpowerup.com/cpu-specs/?released=%d&sort=name" % year)
    content = res.content.decode('utf-8')
    raw = content.split('<table class="processors">')[1].split('</table>')[0]
    raw = re.split(r'(?s).*(?<=<thead>).*?AMD.*?(?=</thead>).*?(?=<tr>\s+<td>\s+<a href=")', raw)[1]
    raw = re.split(r'(?s)<thead>(?<=<thead>).*?Intel.*?(?=</thead>).*?(?=<tr>\s+<td>\s+<a href=")', raw)
    amd, intel = raw[0], raw[1]
    amds = re.findall(r'(?s)<tr>(?<=<tr>).*?(?=</tr>)</tr>', amd)
    intels = re.findall(r'(?s)<tr>(?<=<tr>).*?(?=</tr>)</tr>', intel)
    for amd_cpu in amds:
        specs = re.findall(r'(?s)(?<=<td>).*?(?=</td>)', amd_cpu)
        Name, Codename, Cores, Clock, Socket, Process, L3_Cache, Tdp, Released = specs
        amd_list.append("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (re.findall(r'(?s)(?<=>).*?(?=</a>)', Name)[0], Codename, Cores, Clock, Socket, Process, L3_Cache, Tdp, Released))

    for intel_cpu in intels:
        specs = re.findall(r'(?s)(?<=<td>).*?(?=</td>)', intel_cpu)
        Name, Codename, Cores, Clock, Socket, Process, L3_Cache, Tdp, Released = specs
        intel_list.append("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (re.findall(r'(?s)(?<=>).*?(?=</a>)', Name)[0], Codename, Cores, Clock, Socket, Process, L3_Cache, Tdp, Released))
        

for amd_res in amd_list:
    print(amd_res)

print("__SPLIT__")

for intel_res in intel_list:
    print(intel_res)
