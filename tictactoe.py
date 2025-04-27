# tictactoe.py

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def get_available_moves(board):
    moves = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                moves.append((r, c))
    return moves

def make_move(board, row, col, player):
    board[row][col] = player

def undo_move(board, row, col):
    board[row][col] = EMPTY
