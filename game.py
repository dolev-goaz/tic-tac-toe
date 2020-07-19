from os import system
from tictactoe import create_board, game_status, print_board, get_position_index, position_taken
from minmax import minmax
from time import sleep

def game_loop_ai():
    GAME_OVER = 0
    GAME_RESULTS = 1

    board = create_board()
    while True:
        x, y = get_position_index(board, 'X') # Input from player

        board[y][x] = 'X'

        status = game_status(board) # Check game state
        if status[GAME_OVER]:
            system('cls')
            print_board(board)
            return status[GAME_RESULTS]

        # AI
        x, y = best_move(board)

        board[y][x] = 'O'

        status = game_status(board) # Check game state
        if status[GAME_OVER]:
            system('cls')
            print_board(board)
            return status[GAME_RESULTS]

def game_loop_pvp():
    GAME_OVER = 0
    GAME_RESULTS = 1

    players = ['X', 'O']
    board = create_board()
    while True:
        for player in players:
            x, y = get_position_index(board, player) # Input from player

            board[y][x] = player

            status = game_status(board) # Check game state
            if status[GAME_OVER]:
                system('cls')
                print_board(board)
                return status[GAME_RESULTS]

def best_move(board, players = ['X', 'O']):
    PLAYER = 0
    AI = 1
    bestScore = float('-inf')
    bestMove = ('','')
    for y in range(3):
        for x in range(3):
            if not position_taken(board, x, y):
                board[y][x] = players[AI]
                score = minmax(board, players, 0, False) # False since the next move is the  player's- AI maximizing, while player minimizing the score
                board[y][x] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = (x, y)
    return bestMove


def main():
    system('cls')
    print("Welcome to tictactoe! Choose one of the following options:")
    print("1. To play against an AI")
    print("2. To play pvp")
    choice = int(input())
    while choice not in [1, 2]:
        print("Invalid choice!")
        choice = int(input())
    if choice == 1:
        winner = game_loop_ai()
    if choice == 2:
        winner = game_loop_pvp()
    if winner:
        print('The winner of the game is {}!'.format(winner))
    else:
        print('Tie!')

if __name__ == '__main__':
    main()
