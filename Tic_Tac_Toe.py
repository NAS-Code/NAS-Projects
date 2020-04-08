def build_Board(board_info, available):
    print('  Board         Available Moves')

    print(board_info[1] + ' | ' + board_info[2] + ' | ' + board_info[3] +
          '          ' + available[1] + ' | ' + available[2] + ' | ' + available[3])

    print('---------          ---------')

    print(board_info[4] + ' | ' + board_info[5] + ' | ' + board_info[6] +
          '          ' + available[4] + ' | ' + available[5] + ' | ' + available[6])

    print('---------          ---------')

    print(board_info[7] + ' | ' + board_info[8] + ' | ' + board_info[9] +
          '          ' + available[7] + ' | ' + available[8] + ' | ' + available[9])


def win_Check(board_info, mark):
    # [(1,2,3),(4,5,5),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    top = (board_info[1] == board_info[2] == board_info[3] == mark)
    mid = (board_info[4] == board_info[5] == board_info[6] == mark)
    bot = (board_info[7] == board_info[8] == board_info[9] == mark)
    v1 = (board_info[1] == board_info[4] == board_info[7] == mark)
    v2 = (board_info[2] == board_info[5] == board_info[8] == mark)
    v3 = (board_info[3] == board_info[6] == board_info[9] == mark)
    d1 = (board_info[1] == board_info[5] == board_info[9] == mark)
    d2 = (board_info[3] == board_info[5] == board_info[7] == mark)
    return top or mid or bot or v1 or v2 or v3 or d1 or d2


def ready_Up():
    ready = input('Are you ready to play? (Yes or No): ')
    if ready[0].lower() == 'y':
        game_on = True
    elif ready[0].lower() == 'n':
        game_on = False
    else:
        return ready_Up()
    return game_on


def first_Player():
    import random
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def play_Again():
    replay_check = input('Would you like to play again(Yes or No): ')
    if replay_check[0].lower() == 'y':
        print('\n' * 10)
        return True
    else:
        return False


def pick_Marker(player_turn):
    mark = input(player_turn + ' would you like to be X or O: ')
    if mark[0].lower() == 'x':
        return ('X', 'O')
    elif mark[0].lower() == 'o':
        return ('O', 'X')
    else:
        return pick_Marker(player_turn)


def place_Marker(board_info, mark, position, available):
    board_info[position] = mark
    available[position] = ' '


def choose_Spot(available):
    position = 0
    valid = False
    while valid == False:
        while available[position] == ' ':
            input1 = input(player_turn + ', please choose a spot (1-9): ')
            if input1 in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                valid = True
                position = int(input1)
    return position


def full_Board(available):
    if available == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
        return True
    else:
        return False


while True:
    available = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    board_info = [' '] * 10
    current_game = True
    if not ready_Up():
        break
    else:
        player_turn = first_Player()
        print(player_turn + ' goes first')
        if player_turn == 'Player 1':
            p1_marker, p2_marker = pick_Marker(player_turn)
        else:
            p2_marker, p1_marker = pick_Marker(player_turn)
        while current_game:
            print('\n' * 2 + player_turn + '\'s Turn \n')
            if player_turn == 'Player 1':
                build_Board(board_info, available)
                position = choose_Spot(available)
                place_Marker(board_info, p1_marker, position, available)
                while win_Check(board_info, p1_marker):
                    print('\nCongratulations ' + player_turn + ' you have won Tic Tac Toe!')
                    build_Board(board_info, available)
                    current_game = False
                    break
                while full_Board(available) == True and win_Check(board_info, p1_marker) == False:
                    print('\nThis game is a draw')
                    build_Board(board_info, available)
                    current_game = False
                    break
                player_turn = 'Player 2'
            else:
                build_Board(board_info, available)
                position = choose_Spot(available)
                place_Marker(board_info, p2_marker, position, available)
                while win_Check(board_info, p2_marker):
                    print('\nCongratulations ' + player_turn + ' you have won Tic Tac Toe!')
                    build_Board(board_info, available)
                    current_game = False
                    break
                while full_Board(available):
                    print('\nThis game is a draw')
                    build_Board(board_info, available)
                    current_game = False
                    break
                player_turn = 'Player 1'
    if not play_Again():
        break