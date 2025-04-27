# play_game.py

from tictactoe import create_board, print_board, make_move, undo_move, check_winner, is_full, get_available_moves, PLAYER_X, PLAYER_O
from alphabeta_ai import minimax_ab

def get_user_move(board):
    while True:
        try:
            move = input("Enter your move (row and column: 0 1): ").split()
            if len(move) != 2:
                print("Please enter two numbers (row and column).")
                continue
            row, col = map(int, move)
            if row not in range(3) or col not in range(3):
                print("Invalid input. Rows and columns are 0, 1, or 2.")
                continue
            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter numbers.")

def best_move(board):
    best_score = float('inf')
    move = None
    for (row, col) in get_available_moves(board):
        make_move(board, row, col, PLAYER_O)
        score = minimax_ab(board, True, -float('inf'), float('inf'))
        undo_move(board, row, col)
        if score < best_score:
            best_score = score
            move = (row, col)
    return move

def play_game():
    board = create_board()
    print("You are X, AI is O. You play first!")
    print_board(board)

    while True:
        # User move
        row, col = get_user_move(board)
        make_move(board, row, col, PLAYER_X)
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        ai_row, ai_col = best_move(board)
        make_move(board, ai_row, ai_col, PLAYER_O)
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
