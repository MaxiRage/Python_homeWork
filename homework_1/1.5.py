#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from math import sqrt

coordinates_A = [(float(input('Введите значение X для точки А: '))), (float(input('Введите значение Y для точки А: ')))]
coordinates_B = [(float(input('Введите значение X для точки B: '))), (float(input('Введите значение Y для точки B: ')))]

distance = sqrt((coordinates_A[0]-coordinates_B[0])**2 + (coordinates_A[1]-coordinates_B[1])**2)

print(round(distance, 2))