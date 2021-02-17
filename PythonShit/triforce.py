def triforce(rows=100000):
    res = ""
    for i in range(rows):
        # print(i)
        i += 1
        numspaces = rows - i
        for _i in range(numspaces):
            res += " "
        for _i in range(i):
            res += "▲ "
        res += "\n"
    print(res)
    file = open("C:/triforce.txt", "w+", encoding='utf-8')
    file.write(res)
    file.close()

triforce(10)