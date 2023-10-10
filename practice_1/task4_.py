number = int(input("Введите число: "))
sum = 0
array_number = []
div = number
for i in range (0, len(str(number))):
    sum = sum + divmod(div, 10)[1]
    array_number.append(divmod(div, 10)[1])
    div = divmod(div, 10)[0]

print(array_number [3], ' + ', array_number [2], ' + ', array_number [1], ' + ', array_number [0], ' = ', sum)
