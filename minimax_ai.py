# minimax_ai.py

from tictactoe import make_move, undo_move, check_winner, is_full, get_available_moves, PLAYER_X, PLAYER_O

node_count = 0

def minimax(board, is_maximizing):
    global node_count
    node_count += 1

    winner = check_winner(board)
    if winner == PLAYER_X:
        return 1
    if winner == PLAYER_O:
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for (row, col) in get_available_moves(board):
            make_move(board, row, col, PLAYER_X)
            score = minimax(board, False)
            undo_move(board, row, col)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for (row, col) in get_available_moves(board):
            make_move(board, row, col, PLAYER_O)
            score = minimax(board, True)
            undo_move(board, row, col)
            best_score = min(score, best_score)
        return best_score
