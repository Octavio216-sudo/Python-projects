from random import randrange


row_rep = "+-------+-------+-------+"
column_rep = "|       |       |       |"
rows = int(input("how many rows do you want: " ))
board = [[" " for _ in range(3)] for _ in range(rows)]

def select_letter():
    global letter
    letter = input("what letter do you want to use: ")
    if letter != "X" and letter != "O" and letter != "x" and letter != "o":
        print("Invalid letter. Please enter 'X' or 'O'.")
        return select_letter()
    return letter

def victory_for(board, letter):
    # The function checks if the player with the given sign has won the game.
    sign = letter.upper()
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(rows):
        if all(board[row][col] == sign for row in range(len(board))):
            return True
    if all(board[i][i] == sign for i in range(rows)):
        return True
    if all(board[i][rows - 1 - i] == sign for i in range(rows)):
        return True
    return False

def display_board(row_count):
    numbers = 1
    # this function will display the board with the given number of rows and columns as well as the numbers in the board
    print(row_rep)
    for i in range(row_count):
        print(column_rep)
        print(f"|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |")
        print(column_rep)
        print(row_rep)
        numbers += 3

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move = int(input("Enter your move (1-9): "))
    if move < 1 or move > 9:
        print("Invalid move. Please enter a number between 1 and 9.")
        return enter_move(board)
    else:
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] != " ":
            print("That square is already taken. Please choose another one.")
            return enter_move(board)
        else:
            board[row][col] = letter.upper()
            display_board(rows)
            return victory_for(board, letter.upper())

def cpu_move(board):
    # The function draws the computer's random move and updates the board.
    import random
    move = randrange(1, 10)
    if board[(move - 1) // 3][(move - 1) % 3] != " ":
        return cpu_move(board)
    board[(move - 1) // 3][(move - 1) % 3] = "O" if letter.upper() == "X" else "X"
    display_board(rows)
    return victory_for(board, "O" if letter.upper() == "X" else "X")


def main():
    select_letter()
    display_board(rows)
    while True:
        if enter_move(board):
            print(f"Player {letter.upper()} wins!")
            break
        if cpu_move(board):
            print(f"Player {'O' if letter.upper() == 'X' else 'X'} wins!")
            break
main()


#notes: The last 2 flaws in the code is if the board is full and no one has won, the game will continue indefinitely. 
#You may want to add a check for a draw condition to handle that scenario. The code also wont allow the user to choose a number greater than 9 or less than 1. 
#even when the board has more than 3 rows. You may want to adjust the input validation to account for the actual size of the board.