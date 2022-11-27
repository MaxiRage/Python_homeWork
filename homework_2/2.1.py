"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.(Сделать для строки)"""

num = float(input('Введите число: '))
sum = 0

string = str(num)

for i in string:
    try:
        sum += int(i)
    except ValueError: 
        continue

print(sum)