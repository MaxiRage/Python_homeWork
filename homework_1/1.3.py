#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = float(input('Введите значение X: '))
y = float(input('Введите значение Y: '))

if x == 0 or y == 0:
    print('x or y = 0')
elif x > 0 and y > 0:
    print('I четверть')
elif x < 0 and y > 0: 
    print('II четверть')
elif x < 0 and y < 0: 
    print('III четверть')
else:
    print('IV четверть')

