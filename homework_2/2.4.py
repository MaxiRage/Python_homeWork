"""Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число."""

num = int(input('Введите число: '))
list = []
multi = 1

with open('file.txt', 'w') as data:
    data.write('1\n')
    data.write('3\n')
    data.write('-1\n')

for i in range (-abs(num), abs(num)+1):
    list.append(i)

for line in open('file.txt', 'r'):
    index = int(line)
    multi *= list[index]

print(list)
print(multi)
