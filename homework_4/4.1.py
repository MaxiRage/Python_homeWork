"""Вычислить число Пи c заданной точностью d
Пример:
    - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10
"""
from math import pi

d = 0.00001
count = 2

if (d <=0 ):
    print('Некорректное число d')
else:
    while d < 1:
        d *= 10
        count += 1
    str = str (pi)
    print(str[0:count])



