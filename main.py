from game_logic import initialize_game, checkIfWin, checkIfTie
from board_display import printBoard, gameIntro
from player_moves import playerInput, computerMove

# Initialize game variables
board, currentPlayer, gameRunning, winner = initialize_game()

if __name__ == "__main__":
    gameIntro()
    while True:
        while gameRunning:
            printBoard(board)
            if currentPlayer == "X":
                playerInput(board, currentPlayer)
            else:
                computerMove(board, currentPlayer)
            # Check for win or tie
            winner = checkIfWin(board)
            if winner:
                print(f"The winner is {winner}!")
                printBoard(board)
                gameRunning = False
            elif checkIfTie(board):
                print("It's a tie!")
                printBoard(board)
                gameRunning = False

            # Switch player if game is still running
            if gameRunning:
                currentPlayer = "O" if currentPlayer == "X" else "X"

        # Restart or exit
        board, currentPlayer, gameRunning, winner = initialize_game(restart=True, winner=winner)
        if not gameRunning:
            break
        
    
