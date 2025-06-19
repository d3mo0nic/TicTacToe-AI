import random
from game_logic import checkIfWin, checkIfTie

def playerInput(board, currentPlayer):
    while True:
        try:
            inp = int(input(f"Player {currentPlayer}, select a spot (1-9): "))
            if inp < 1 or inp > 9:
                print("Invalid input! Please choose a number between 1 and 9.")
            elif board[inp - 1] != "-":
                print("Spot already taken! Choose another.")
            else:
                board[inp - 1] = currentPlayer
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

def computerMove(board, currentPlayer):
    def checkWinningMove(board, player):
        for i in range(9):
            if board[i] == "-":
                board[i] = player
                if checkIfWin(board):
                    board[i] = "-"
                    return i
                board[i] = "-"
        return None

    # Priority: Win > Block > Random
    winning_move = checkWinningMove(board, currentPlayer)
    if winning_move is not None:
        board[winning_move] = currentPlayer
        print(f"Computer chose spot {winning_move + 1} to win!")
        return

    opponent = "X" if currentPlayer == "O" else "O"
    blocking_move = checkWinningMove(board, opponent)
    if blocking_move is not None:
        board[blocking_move] = currentPlayer
        print(f"Computer chose spot {blocking_move + 1} to block!")
        return

    available_spots = [i for i, spot in enumerate(board) if spot == "-"]
    if available_spots:
        move = random.choice(available_spots)
        board[move] = currentPlayer
        print(f"Computer chose spot {move + 1}.")
