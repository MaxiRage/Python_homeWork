"""Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)* многочлена и записать в файл многочлен степени k
    *Пример:* 
    - k=2 => 2*x² + 4*x + 5 = 0 
        или x² + 5 = 0 
            или 10*x² = 0
    -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
"""
import random

def write_file(str):
    with open('file.txt', 'w') as data:
        data.write(str)

def create(k):
    return [random.randint(0,101) for i in range(k+1)]

def create_str(sp):
    list= sp[::-1]
    write = ''
    if len(list) < 1:
        write = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                write += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    write += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                write += f'{list[i]}x'
                if list[i+1] != 0:
                    write += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                write += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                write += ' = 0'
    return write

k = int(input('Введите натуральную степень k: '))
сoef = create(k)
write_file(create_str(сoef))
