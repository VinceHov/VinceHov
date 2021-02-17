numbers = []
numbers.append('1')
numbers.append('1')
numbers.append(['2', '2'])
operators = [ '+', '*', '/' ]
# print(numbers)
# print(operators)
index = 0
output = 0
prevNumber = 0
###Конец инициализации

def compute(numbers, index):
    prevNumber = 0
    output = 0
    for number in numbers:
        if not type(number) == list:
            number = int(number)
        if prevNumber == 0: 
            prevNumber = number
            continue
        if type(number) == list:
            number = int(compute(number, index))
        if operators[index] == "+":
            output += prevNumber + number
        elif operators[index] == "-":
            output += prevNumber - number
        elif operators[index] == "/":
            output += prevNumber / number
        elif operators[index] == "*":
            output += prevNumber * number
        index +=1
    return output


for number in numbers:
    if not type(number) == list:
        number = int(number)
    if prevNumber == 0: 
        index +=1
        prevNumber = number
        continue
    if type(number) == list:
        number = int(compute(number, index))
    if operators[index] == "+":
        output += prevNumber + number
    elif operators[index] == "-":
        output += prevNumber - number
    elif operators[index] == "/":
        output += prevNumber // number
    elif operators[index] == "*":
        output += prevNumber * number
    prevNumber = output
    index +=1

print(output)

