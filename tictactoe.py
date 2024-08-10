import random

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a win or a tie
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    if all(board[row][col] != " " for row in range(3) for col in range(3)):
        return "Tie"
    return None

# Function to get all available moves
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    elif winner == "O":
        return 10 - depth
    elif winner == "Tie":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "O"
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "X"
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            best_score = min(score, best_score)
        return best_score

# AI move function
def ai_move(board):
    best_score = -float("inf")
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = "O"
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = " "
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move[0]][best_move[1]] = "O"

# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"The winner is {winner}!")
            break

        if current_player == "X":
            move = input("Enter your move (row and column): ").split()
            row, col = int(move[0]), int(move[1])
            if board[row][col] == " ":
                board[row][col] = "X"
                current_player = "O"
            else:
                print("Invalid move! Try again.")
        else:
            ai_move(board)
            current_player = "X"

if _name_ == "_main_":
    play_game()
