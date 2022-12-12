"""Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
    Необходимо сложить все значения словаря и вывести  сумму на экран."""

num = int(input('Введите число: '))
map = {}
count = 1

while num >= count:
    map [count] = round((1+(1/count))**count,2)
    count+=1

print(map)

sum = 0
for value in map:
    sum += map[value]

print(round(sum,2))