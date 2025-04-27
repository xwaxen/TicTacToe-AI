# comparison.py

import time
from tictactoe import create_board
import minimax_ai
import alphabeta_ai

def compare():
    board = create_board()

    # Standard Minimax
    minimax_ai.node_count = 0
    start = time.time()
    minimax_ai.minimax(board, True)
    end = time.time()
    print(f"Minimax: {minimax_ai.node_count} nodes, {end - start:.6f} seconds")

    # Alpha-Beta Pruning
    alphabeta_ai.node_count_ab = 0
    start = time.time()
    alphabeta_ai.minimax_ab(board, True, -float('inf'), float('inf'))
    end = time.time()
    print(f"Alpha-Beta: {alphabeta_ai.node_count_ab} nodes, {end - start:.6f} seconds")

if __name__ == "__main__":
    compare()
