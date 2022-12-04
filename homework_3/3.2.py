"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
    - [2, 3, 4, 5, 6] => [12, 15, 16];
    - [2, 3, 5, 6] => [12, 15]
"""
list = [2, 3, 4, 5, 6]
listFinal = []
start = 0
end = len(list)-1

for value in list:
    if start <= end:
        listFinal.append(list[start] * list[end])
        start += 1
        end -= 1
    else: 
        break

print(listFinal)
