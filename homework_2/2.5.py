"""Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.(Не используя библиотеки связанные с рандомом)"""

def random(seed, n, a=16645, c=39023, m=2**32):
    for i in range(n):
        seed += (a * seed / c) % m
    return seed

rnd = random(int(input('Введите число: ')), int(input('Введите число: ')))

print(int(rnd))