def initialize_game(restart=False, winner=None):
    if not restart:
        board = ["-" for _ in range(9)]
        currentPlayer = "X"
        gameRunning = True
        winner = None
    else:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            board = ["-" for _ in range(9)]
            gameRunning = True
            currentPlayer = "X" if not winner else winner
            winner = None
        elif choice == "no":
            print("Thanks for playing! Goodbye!")
            board = []
            currentPlayer = None
            gameRunning = False
        else:
            print("Invalid input! Exiting.")
            board = []
            currentPlayer = None
            gameRunning = False
    return board, currentPlayer, gameRunning, winner

def checkHorizontle(board):
    for row_start in [0, 3, 6]:
        if board[row_start] == board[row_start + 1] == board[row_start + 2] and board[row_start] != "-":
            return board[row_start]  # Return winner
    return None

def checkRow(board):
    for col_start in range(3):
        if board[col_start] == board[col_start + 3] == board[col_start + 6] and board[col_start] != "-":
            return board[col_start]  # Return winner
    return None

def checkDiag(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        return board[0]  # Return winner
    if board[2] == board[4] == board[6] and board[2] != "-":
        return board[2]  # Return winner
    return None

def checkIfWin(board):
    winner = checkHorizontle(board) or checkRow(board) or checkDiag(board)
    return winner

def checkIfTie(board):
    return "-" not in board
