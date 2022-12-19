#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from functools import reduce

coordinates_A = [(float(input('Введите значение X для точки А: '))), (float(input('Введите значение Y для точки А: ')))]
coordinates_B = [(float(input('Введите значение X для точки B: '))), (float(input('Введите значение Y для точки B: ')))]

rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(coordinates_A, coordinates_B))))

print(round(rng, 2))

exit()

from math import sqrt

coordinates_A = [(float(input('Введите значение X для точки А: '))), (float(input('Введите значение Y для точки А: ')))]
coordinates_B = [(float(input('Введите значение X для точки B: '))), (float(input('Введите значение Y для точки B: ')))]

distance = sqrt((coordinates_A[0]-coordinates_B[0])**2 + (coordinates_A[1]-coordinates_B[1])**2)

print(round(distance, 2))