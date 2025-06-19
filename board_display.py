def gameIntro():
    print("""
    *****************************
    *       TIC-TAC-TOE         *
    *                           *
    *****************************
    """)

def printBoard(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")
