from random import randint #use to generate random ship/target coordinates
import sys
from itertools import cycle #use to cycle between players
import os #use to clear screen in WHILE TRUE clause

print "Let's play Battleship!"

#board that player1 uses to sink player2 ships
board1 = []
#board that player2 users to sink player1 ships
board2 = []

#set who goes first
active_player=cycle(i for i in range(1,3,1)) #cycle between [1] and [2]
#print 'Starting player',active_player.next()
a_player=0

#create boards to play on
for x in range(5):
    board1.append(["O"] * 5)
    board2.append(["O"] * 5)

def print_board():
    if a_player==1:
        for row in board1:
            print " ".join(row)
    if a_player==2:
        for row in board2:
            print "-".join(row) #differentiation from board1 display

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board1[0]) - 1)

#pick random location for ship in board
ship_row1 = random_row(board1)
ship_col1 = random_col(board1)
#print ship_row1, ship_col1 #uncomment to cheat/see a win-condition

#pick random location for ship in board2
ship_row2 = random_row(board2)
ship_col2 = random_col(board2)


def guess_row():
    while True:
        try:
            #allows input to not be zero-based
            user_row= int(raw_input("Guess Row, 1-5: "))-1
            if user_row>=0 and user_row<=4: #remember: converted to zero-based
                break #escape the while loop
        except ValueError:
            print 'This is not an integer, try again 1-5'
    return user_row

def guess_col():
    while True:
        try:
            #allows input to not be zero-based
            user_col= int(raw_input("Guess Column, 1-5: "))-1
            if user_col>=0 and user_col<=4:
                break #escape the while loop
        except ValueError:
            print 'This is not an integer, try again 1-5'
    return user_col

def checkhit1(user_row,user_col,player):
    if user_row == ship_row1 and user_col == ship_col1:
        print "Congratulations! Player",player,'won!'
        exit() #if in a for loop, use break
    else:
        if (user_row < 0 or user_row > 4) or (user_col < 0 or user_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board1[user_row][user_col] == "X"):
            print "You guessed that one already. Still losing a turn..."
        else:
            print "You missed my battleship!"
            board1[user_row][user_col] = "X"

def checkhit2(user_row,user_col,player):
    if user_row == ship_row2 and user_col == ship_col2:
        print "Congratulations! Player",player,'won!'
        exit() #end the program. if in a for loop, use break
    else:
        if (user_row < 0 or user_row > 4) or (user_col < 0 or user_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board2[user_row][user_col] == "X"):
            print "You guessed that one already. Still losing a turn..."
        else:
            print "You missed my battleship!"
            board2[user_row][user_col] = "X"
        #print_board()

def takeaturn(player):
    print "Turn of player", player #displays active_player
    print_board()
    user_row = guess_row()
    user_col = guess_col()
    #print 'You guessed:',user_row,user_col
    if player==1:
        checkhit1(user_row,user_col,player)
    #    print 'local player:',player
    elif player==2:
        checkhit2(user_row,user_col,player)
    #    print 'local player:',player
    print_board()
    raw_input("Press enter to pass to other player\n")


while True:
    os.system('clear')
    a_player=active_player.next()
    #print 'global var active_player:',a_player
    takeaturn(a_player) #cycle player turns
