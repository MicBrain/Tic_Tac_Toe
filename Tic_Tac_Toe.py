###################
### DESCRIPTION ###
###################

"""
    Tic-tac-toe (or Noughts and crosses, Xs and Os) is a game for two players, X and O, who take
turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks
in a horizontal, vertical, or diagonal row wins the game.
    The simplicity of Tic-tac-toe makes it ideal as a pedagogical tool for teaching the concepts
of good sportsmanship and the branch of artificial intelligence that deals with the searching of 
game trees. It is straightforward to write a computer program to play Tic-tac-toe perfectly.
    The game can be generalized to an m,n,k-game in which two players alternate placing stones of 
their own color on an m×n board, with the goal of getting k of their own color in a row. Tic-tac-toe 
is the (3,3,3)-game.
    Despite its apparent simplicity, Tic-tac-toe requires detailed analysis to determine even some 
elementary combinatory facts, the most interesting of which are the number of possible games and the 
number of possible positions. A position is merely a state of the board, while a game usually refers 
to the way a terminal position is obtained.
"""

from string import *
from random import *
import itertools
import math

####################
## MAIN VARIABLES ##
####################

Player_1 = 'x'      # player 1's mark
Player_2 = 'o'      # player 2's mark

A = 'A'     # these just make it easier to keep referring to 'A', 'B' and 'C'
B = 'B'
C = 'C'

#####################
## State variables ##
#####################
EMPTY = ' '     # the value of an empty square
Table = [[EMPTY, EMPTY, EMPTY],     # board is initially all empty squares,
         [EMPTY, EMPTY, EMPTY],     # implemented as a list of rows,
         [EMPTY, EMPTY, EMPTY]]     # three rows with three squares each

current = randint(1, 2)      # randomly choose starting player

#########################
### Coordinate system ###
#########################

def square(row, col):       # squares are represented as tuples of (row, col).
    return (row, col)       # rows are numbered 1 thru 3, cols 'A' thru 'C'.

def square_row(square):     # these two functions save us the hassle of using
    return square[0]        # index values in our code, e.g. square[0]...

def square_col(square):     # from this point on, i should never directly use
    return square[1]        # tuples when working with squares.

def get_square(square):
    row_i = square_row(square) - 1      
    col_i = ord(square_col(square)) - ord(A)    
    return Table[row_i][col_i]  # note how this and set_square are the ONLY
                                # functions which directly use board!

def set_square(square, mark):
    row_i = square_row(square) - 1
    col_i = ord(square_col(square)) - ord(A)
    Table[row_i][col_i] = mark  # note how this and get_square are the ONLY
                            
def get_row(row):
    return [get_square((row, A)), get_square((row, B)), get_square((row, C))]

def get_column(col):
    return [get_square((1, col)), get_square((2, col)), get_square((3, col))]

def get_diagonal(corner_square):
    if corner_square == (1, A) or corner_square == (3, C):
        return [get_square((1, A)), get_square((2, B)), get_square((3, C))]
    else:
        return [get_square((1, C)), get_square((2, B)), get_square((3, A))]

def get_mark(player):
    if player == 1:
        return Player_1
    else:
        return Player_2

def all_squares_filled():
    for row in range(1, 4):     # range(1, 4) returns the list [1, 2, 3]
        if EMPTY in get_row(row):
            return False    # this row contains an empty square, we know enough
    return True     # no empty squares found, all squares are filled

def player_has_won(player):
    MARK = get_mark(player)
    win = [MARK, MARK, MARK]
    if get_row(1) == win or get_row(2) == win or get_row(3) == win:
        return True
    if get_column(A) == win or get_column(B) == win or get_column(C) == win:
        return True
    if get_diagonal((1, A)) == win or get_diagonal((1, C)) == win:
        return True
    return False    

def draw_board_straight():
    A1, A2, A3 = get_square((1, A)), get_square((2, A)), get_square((3, A))
    B1, B2, B3 = get_square((1, B)), get_square((2, B)), get_square((3, B))
    C1, C2, C3 = get_square((1, C)), get_square((2, C)), get_square((3, C))
    lines = []
    lines.append("")
    lines.append("     " + A + "   " + B + "   " + C + " ")
    lines.append("              ")
    lines.append("1    " + A1 + " | " + B1 + " | " + C1 + " ")
    lines.append("    ---+---+---")
    lines.append("2    " + A2 + " | " + B2 + " | " + C2 + " ")
    lines.append("    ---+---+---")
    lines.append("3    " + A3 + " | " + B3 + " | " + C3 + " ")
    lines.append("")
    return str.join(str(lines), '\n')    # the '\n' represents a newline

def draw_board_slanted():
    A1, A2, A3 = get_square((1, A)), get_square((2, A)), get_square((3, A))
    B1, B2, B3 = get_square((1, B)), get_square((2, B)), get_square((3, B))
    C1, C2, C3 = get_square((1, C)), get_square((2, C)), get_square((3, C))
    lines = []
    lines.append("")
    lines.append("           " + A + "   " + B + "   " + C + " ")
    lines.append("                     ")
    lines.append("    1    " + A1 + " / " + B1 + " / " + C1 + "  ")
    lines.append("       ---/---/---  ")
    lines.append("  2    " + A2 + " / " + B2 + " / " + C2 + "    ")
    lines.append("     ---/---/---    ")
    lines.append("3    " + A3 + " / " + B3 + " / " + C3 + "      ")
    lines.append("")
    return str.join(str(lines), '\n')   

def draw_board():
    return draw_board_slanted()     

def reset_main_board():
    for row in (1, 2, 3):
        for col in (A, B, C):
            set_square(square(row, col), EMPTY)

def play():
    global current  
    reset_main_board()
    current = randint(1, 2)
    print ("Tic-Tac-Toe!")
    print
    player1_name = input("Player 1, what is your name? ")
    player2_name = input("Player 2, what is your name? ")
    def get_name(player):
        if player == 1:
            return player1_name
        else:
            return player2_name
    print
    print ("Welcome,", player1_name, "and", player2_name + "!")
    print (player1_name, "will be", Player_1 + ", and", player2_name, "will be", Player_2 + ".")
    print ("By random decision,", get_name(current), "will go first.")
    print
    input("[Press enter when ready to play.] ")     # just waiting for them to press enter
    print (draw_board())
    while not all_squares_filled():
        choice = input(get_name(current) + ", which square? (e.g. 2B, 2b, B2 or b2) ")
        if len(choice) != 2:
            print ("That's not a square. You must enter a square like b2, or 3C.")
            print
            continue
        if choice[0] not in ["1", "2", "3"] and str.upper(choice[0]) not in [A, B, C]:
            print ("The first character must be a row (1, 2 or 3) or column (A, B or C).")
            print
            continue
        if choice[1] not in ["1", "2", "3"] and str.upper(choice[1]) not in [A, B, C]:
            print ("The second character must be a row (1, 2 or 3) or column (A, B or C).")
            print
            continue
        if choice[0] in ["1", "2", "3"] and choice[1] in ["1", "2", "3"]:
            print ("You entered two rows! You must enter one row and one column (A, B or C).")
            print
            continue
        if str.upper(choice[0]) in [A, B, C] and str.upper(choice[1]) in [A, B, C]:
            print ("You entered two columns! You must enter one row (1, 2 or 3) and one column.")
            print
            continue
        if choice[0] in ["1", "2", "3"]:
            row = int(choice[0])
            col = str.upper(choice[1])
        else:
            row = int(choice[1])
            col = str.upper(choice[0])
        choice = square(row, col)   # make this into a (row, col) tuple
        if get_square(choice) != EMPTY:
            print ("Sorry, that square is already marked.")
            print
            continue
        set_square(choice, get_mark(current))
        print (draw_board())
        if player_has_won(current):
            print ("Congratulations", get_name(current), "-- you win!")
            print
            break
        if all_squares_filled():
            print ("Cats game!", player1_name, "and", player2_name, "draw.")
            print
            break
        current = 3 - current     # sets 1 to 2 and 2 to 1
    print ("GAME IS OVER")
    print
if __name__ == "__main__":
    continue_playing = True
    while continue_playing:
        play()
        again = str.lower(input("Play again? (y/n) "))
        print
        print
        print
        if again != "y":
            continue_playing = False
    print ("Thanks for playing!")
    print