"""Создайте программу для игры с конфетами человек против человека.
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
    Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом"""""

import random

def play_game(players):
    count = 0
    all_candy = 221
    max_candy_one_turn = 28

    while all_candy > 0:
        print(f'Ход игрока {players[count % 2]}:')
        if players[count % 2] != 'БОТ':
            while True:
                try:
                    move = int(input())
                    if move > all_candy or move > max_candy_one_turn or move <= 0:
                        print(f'Не корретное число, попробуйте ещё раз')
                    else: break
                except ValueError:
                    print(f'Не корректное число, попробуйте ещё раз')
            all_candy = all_candy - move
        else:
            all_candy = all_candy - random.randint(1, 28)

        if all_candy > 0: print(f'Осталось {all_candy} конфет')
        else: print('Все конфеты разобраны.')
        count +=1

    return players[not count % 2]

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока или напишите слово БОТ, что бы играть с ботом: ') 

if player2 != 'БОТ':
    players = [player1, player2]
else:
    players = [player1, 'БОТ']

winer = play_game(players)
print(f'Поздравляю! Победил {winer}!')