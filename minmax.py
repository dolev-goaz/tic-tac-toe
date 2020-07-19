from tictactoe import game_status, position_taken


def minmax(board, players, depth, maximizing):
    # For the status
    GAME_OVER = 0
    GAME_RESULTS = 1

    # For player signs
    PLAYER = 0
    AI = 1

    status = game_status(board)

    if status[GAME_OVER]:
        if not status[GAME_RESULTS]:
            return 0
        # Adding depth so it will prioritize finishing faster/losing slower
        elif status[GAME_RESULTS] == players[AI]:
            return 100 - depth
        else:
            return -100 + depth

    bestScore = float('-inf') if maximizing else float('inf')
    for y in range(3):
        for x in range(3):
            if not position_taken(board, x, y):
                board[y][x] = players[AI if maximizing else PLAYER]
                score = minmax(board, players, depth + 1, not maximizing)
                board[y][x] = ' '
                if maximizing:
                    bestScore = max(score, bestScore)
                else:
                    bestScore = min(score, bestScore)

    return bestScore
