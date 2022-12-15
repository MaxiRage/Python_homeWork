"""Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
Пример:
2 + 2 => 4;
1 + 2 * 3 => 7;
1 - 2 * 3 => -5;"""

expression = input('Введите выражение для высчитывания: ').replace(' ', '')

def parse(expression):
    if expression == '':
        return -1

    list = []
    digit = ""
    for symbol in expression:
        if symbol.isdigit():
            digit += symbol
        else:
            
            try:
                list.append(int(digit))
            except:
                return -1

            digit = ""
            list.append(symbol)

    list.append(int(digit))
    print(list)

    if 0 in list:
        if list[list.index(0)-1] == '/':
            return -1

    return list

def calculate(list):
    if list == -1:
        return 'Некорректное выражение'

    result = 0
    while '*' in list:
        index = list.index('*')
        result = list[index - 1] * list[index + 1]
        list = list[:index - 1] + [result] + list[index + 2:]
    while '/' in list:
        index = list.index('/')
        result = list[index - 1] / list[index + 1]
        list = list[:index - 1] + [result] + list[index + 2:]
    while '+' in list:
        index = list.index('+')
        result = list[index - 1] + list[index + 1]
        list = list[:index - 1] + [result] + list[index + 2:]
    while '-' in list:
        index = list.index('-')
        result = list[index - 1] - list[index + 1]
        list = list[:index - 1] + [result] + list[index + 2:]
    return round(result, 2)

print(calculate(parse(expression)))