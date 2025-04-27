# alphabeta_ai.py

from tictactoe import make_move, undo_move, check_winner, is_full, get_available_moves, PLAYER_X, PLAYER_O

node_count_ab = 0

def minimax_ab(board, is_maximizing, alpha, beta):
    global node_count_ab
    node_count_ab += 1

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
            score = minimax_ab(board, False, alpha, beta)
            undo_move(board, row, col)
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for (row, col) in get_available_moves(board):
            make_move(board, row, col, PLAYER_O)
            score = minimax_ab(board, True, alpha, beta)
            undo_move(board, row, col)
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score
