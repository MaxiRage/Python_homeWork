"""Создайте программу для игры в ""Крестики-нолики"""""

board = list(range(1,10))

def view(board):
    print ()
    print ()
    print ()
    print('-'*13)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*13)

def choice(player):
    while True:
        player_index = input('Ваш ход, выберите ячейку ' + player + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Повторите ввод')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = player
                break
            else:
                print('Занято')
        else:
            print('Повторите ввод')

def check_winner(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    counter =0
    while True:
        view(board)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('О')
        counter +=1
        if counter > 4:
            check = check_winner(board)
            if check:
                view(board)
                print(check,'Победа')
                break
            if counter == 9:
                print('Ничья')
        view(board)

game(board)