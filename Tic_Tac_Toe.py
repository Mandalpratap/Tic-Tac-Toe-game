import math

# Initialize the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(3):
        print(board[3 * i], '|', board[3 * i + 1], '|', board[3 * i + 2])
        if i < 2:
            print('---------')

# Check for a win condition
def check_winner(board):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for (x, y, z) in win_combinations:
        if board[x] == board[y] == board[z] and board[x] != ' ':
            return board[x]
    return None

# Check if the game is a draw
def is_draw(board):
    return all([spot != ' ' for spot in board])

# Evaluate the board for Minimax
def evaluate(board):
    winner = check_winner(board)
    if winner == 'O':
        return 1  # AI wins
    elif winner == 'X':
        return -1  # Human wins
    else:
        return 0  # Draw or ongoing

# Minimax algorithm with optional alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    score = evaluate(board)
    
    # Terminal conditions (win/loss/draw)
    if score == 1 or score == -1 or is_draw(board):
        return score
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # AI move
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '  # Undo the move
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:  # Prune
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # Human move
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '  # Undo the move
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:  # Prune
                    break
        return best_score

# Function for the AI to make the best move
def ai_move():
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # AI's move
            score = minimax(board, 0, False)
            board[i] = ' '  # Undo the move
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Function for the human to make a move
def human_move():
    while True:
        move = int(input('Enter your move (1-9): ')) - 1
        if board[move] == ' ':
            board[move] = 'X'
            break
        else:
            print("Invalid move, try again.")

# Main game loop
def play_game():
    while True:
        print_board()
        if check_winner(board) or is_draw(board):
            break
        
        # Human's turn
        human_move()
        
        if check_winner(board) or is_draw(board):
            break
        
        # AI's turn
        ai_move()
    
    print_board()
    
    winner = check_winner(board)
    if winner:
        print(f"The winner is {winner}!")
    else:
        print("It's a draw!")

# Start the game
play_game()
