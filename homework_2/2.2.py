"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""

num = int(input('Введите число: '))
multi = []

while len(multi) < num:
    temp = 1
    
    multi.append(len(multi) + 1)

    for i in range(1, len(multi) + 1):
        temp *= i
    
    multi[-1] = temp

print(multi)