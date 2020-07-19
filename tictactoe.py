from os import system

def game_winner(board):
    for i in range(3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] and board[i][1] == board[i][2]: # ROWS
            return board[i][0]
        if board[0][i] != ' ' and board[0][i] == board[1][i] and board[1][i] == board[2][i]: # COLUMNS
            return board[0][i]
    if board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]: # DIAGONAL 1
        return board[0][0]
    if board[2][0] != ' ' and board[2][0] == board[1][1] and board[1][1] == board[0][2]: # DIAGONAL 2
        return board[2][0]
    return None

def create_board():
    return [[' ' for i in range(3)] for i in range(3)]

def print_board(board):
    print('-------')
    for i in range(3):
        print('|{}|{}|{}|'.format(board[i][0], board[i][1], board[i][2]))
        print('-------')

def place_on_board(board, x, y, sign):
    board[y][x] = sign

def index_to_coordinates(index):
    return ((index - 1) % 3, 2 - (index - 1) // 3)

def game_in_progress(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def position_taken(board, x, y):
    return board[y][x] != ' '

"""
Return format: (isGameOver, winner)
"""
def game_status(board):
    if game_winner(board):
        return (True, game_winner(board))
    if not game_in_progress(board):
        return (True, None)
    return (False, None)

def get_position_index(board, player):
    system('cls')
    print('Insert index for player {}'.format(player))
    print_board(board)
    user_input = input()
    while not user_input.isdigit() or int(user_input) not in [i for i in range(0, 10)]:
        system('cls')
        print('Insert index for player {}'.format(player))
        print_board(board)
        print('Index needs to be numeric, in the range 0-9!')
        user_input = input()
    index = int(user_input)
    x, y = index_to_coordinates(index)
    while position_taken(board, x, y):
        print('That position is taken!')
        print('Please insert a new position')
        index = int(input())
    return (x, y)
