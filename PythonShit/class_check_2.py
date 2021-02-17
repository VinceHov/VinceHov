file = open('C:/class.txt', 'r', encoding='utf-8')

content = file.read()
peoples = content.split('\n')
dvoechniks = []

number_of_peoples = len(peoples)
counter = 0
for people in peoples:
    fname, lname, mark = people.split(' ')
    if int(mark) == 2:
        dvoechniks.append("Имя: %s\tФамилия: %s\tдвоечника" % (fname, lname) )
    counter += int(mark)

for dvoechnik in dvoechniks:
    print(dvoechnik)
print("Средний бал: %f" % (counter / number_of_peoples))
