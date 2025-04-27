TicTacToe AI 🎮🤖
This project implements a Tic-Tac-Toe game with an AI player using:

Minimax Algorithm (optimal decision-making)

Alpha-Beta Pruning (optimization to minimize the number of explored nodes)

📜 Project Structure

File	Description
tictactoe.py	Core logic for the Tic-Tac-Toe game (board setup, moves, win checking).
minimax_ai.py	AI player using standard Minimax algorithm.
alphabeta_ai.py	AI player using Alpha-Beta Pruning to optimize Minimax.
comparison.py	Compares performance (speed and node visits) between Minimax and Alpha-Beta.
play_game.py	Playable game where you play against the AI!
🧠 Algorithms Used
Minimax: Explores all possible moves to pick the best one.

Alpha-Beta Pruning: Skips unnecessary branches to speed up the decision-making.

🚀 How to Run
1. Play the Game
bash
Copy
Edit
python play_game.py
You play as X.

AI plays as O.

Enter your moves as row column (e.g., 0 1).

2. Compare AI Performance
bash
Copy
Edit
python comparison.py
Shows the number of nodes visited and time taken for both algorithms.

📋 Requirements
Python 3.x

No extra libraries needed (pure Python)

✨ Future Improvements
Add a GUI version (using tkinter or pygame)

Allow different AI difficulty levels (easy, medium, hard)

📌 Author
Shahzaib Ahmed

