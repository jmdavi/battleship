from random import randint
import sys

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print( " ".join(row) )

print( "Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row, ship_col #uncomment to cheat/see a win-condition

def guess_row():
    while True:
        try:
            user_row= int(input("Guess Row, 0-4:"))
            break #escape the while loop
        except ValueError:
            print('This is not an integer, try again 0-4')
    return user_row

def guess_col():
    while True:
        try:
            user_col= int(input("Guess Column, 0-4:"))
            break
        except ValueError:
            print('This is not an integer, try again 0-4')
    return user_col

def takeaturn(turn):
    print("Turn", turn+1) #Plus-one to avoid zero-based counting
    user_row = guess_row()
    user_col = guess_col()
    #print 'You guessed:',guess_rows,guess_cols

    if user_row == ship_row and user_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        exit() #if in a for loop, use break
    else:
        if (user_row < 0 or user_row > 4) or (user_col < 0 or user_col > 4):
            print("Oops, that's not even in the ocean.")
        elif(board[user_row][user_col] == "X"):
            print("You guessed that one already. Still losing a turn...")
        else:
            if turn==3:
                print('Game Over... You missed my battleship for the last time!')
                print('The ship was at row:'+str(ship_row)+' col: '+str(ship_col))
                board[ship_row][ship_col] = "@"
            else:
                print("You missed my battleship!")
                board[user_row][user_col] = "X"
        print_board(board)

for turn in range(4): #adjust for the number of tries before losing
    takeaturn(turn)
