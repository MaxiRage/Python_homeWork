"""Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)"""

with open('file.txt','r') as data:
    file = data.readline()
    file1 = file.replace(' = 0', '')

with open('file1.txt','r') as data:
    file2 = data.readline()

print(f'{file1} + {file2}')

with open('sum.txt', 'w') as data:
    data.write(f'{file1} + {file2}')