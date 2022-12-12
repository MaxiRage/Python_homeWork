"""Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
Пример:
- Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]
"""

list = [1,1,2,4,5,6,7,7,8]
count = 0
outputArr = []

for i in list:
    for check in list:
        if i == check and count < 2:
            count+=1
    if count == 1:
        outputArr.append(i)
    count = 0

print(outputArr)