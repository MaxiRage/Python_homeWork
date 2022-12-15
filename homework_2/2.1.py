"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.(Сделать для строки)"""

num = input('Введите число: ')
sum = sum(map(int, num.replace('.', '').replace('-', '')))
print (sum)

exit()

num = float(input('Введите число: '))
sum = 0

string = str(num)

for i in string:
    try:
        sum += int(i)
    except ValueError: 
        continue

print(sum)