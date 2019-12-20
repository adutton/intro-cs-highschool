import random

# Board spots:
#
# 1 | 2 | 3 
#---+---+---
# 4 | 5 | 6 
#---+---+---
# 7 | 8 | 9 
#
# "-" indicates an open spot

b1 = "-"
b2 = "-"
b3 = "-"
b4 = "-"
b5 = "-"
b6 = "-"
b7 = "-"
b8 = "-"
b9 = "-"
r1 = "---" # Row 1, spots 1, 2, 3
r2 = "---" # Row 2, spots 4, 5, 6
r3 = "---" # Row 3, spots 7, 8, 9
c1 = "---" # Column 1, spots 1, 4, 7
c2 = "---" # Column 2, spots 2, 5, 8
c3 = "---" # Column 3, spots 3, 6, 9
x1 = "---" # Cross 1, spots 1, 5, 9
x2 = "---" # Cross 2, spots 3, 5, 7

def initialize_board():
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9

    b1 = "-"
    b2 = "-"
    b3 = "-"
    b4 = "-"
    b5 = "-"
    b6 = "-"
    b7 = "-"
    b8 = "-"
    b9 = "-"
    
    calculate_row_col_cross()
    
def calculate_row_col_cross():
    global r1
    global r2
    global r3
    global c1
    global c2
    global c3
    global x1
    global x2
    
    r1 = b1 + b2 + b3
    r2 = b4 + b5 + b6
    r3 = b7 + b8 + b9
    c1 = b1 + b4 + b7
    c2 = b2 + b5 + b8
    c3 = b3 + b6 + b9
    x1 = b1 + b5 + b9
    x2 = b3 + b5 + b7

def calculate_winner():
    # Four possible returns from this function
    # "X" - The X player wins
    # "Y" - The Y player wins
    # "T" - There is a TIE
    # "-" - There is no winner
    
    if r1 == "XXX" or r2 == "XXX" or r3 == "XXX":
        return "X"
    if c1 == "XXX" or c2 == "XXX" or c3 == "XXX":
        return "X"
    if x1 == "XXX" or x2 == "XXX":
        return "X"

    if r1 == "OOO" or r2 == "OOO" or r3 == "OOO":
        return "O"
    if c1 == "OOO" or c2 == "OOO" or c3 == "OOO":
        return "O"
    if x1 == "OOO" or x2 == "OOO":
        return "O"

    # Look for ties if there are no more spots available
    if "-" not in (r1 + r2 + r3):
        return "T"
    
    return "-"

def get_spot_marker(spot):
    if spot == 1:
        return b1
    elif spot == 2:
        return b2
    elif spot == 3:
        return b3
    elif spot == 4:
        return b4
    elif spot == 5:
        return b5
    elif spot == 6:
        return b6
    elif spot == 7:
        return b7
    elif spot == 8:
        return b8
    elif spot == 9:
        return b9

def is_spot_open(spot):
    # Returns True if the spot is empty (and a marker can be placed on the spot)
    # Returns False if the spot is used
    
    if get_spot_marker(spot) == "-":
        return True
    else:
        return False

def set_marker_in_spot(marker, spot):
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9

    if spot == 1:
        b1 = marker
    elif spot == 2:
        b2 = marker
    elif spot == 3:
        b3 = marker
    elif spot == 4:
        b4 = marker
    elif spot == 5:
        b5 = marker
    elif spot == 6:
        b6 = marker
    elif spot == 7:
        b7 = marker
    elif spot == 8:
        b8 = marker
    elif spot == 9:
        b9 = marker

    calculate_row_col_cross()    

def opposite_marker(marker):
    if marker == "X":
        return "O"
    else:
        return "X"

def can_win(marker, row_col_cross):
    # Returns True if putting the given marker into the given row, column, or cross would win
    # Returns False if that is not going to trigger a win
    
    if row_col_cross == marker + marker + "-":
        return True
    if row_col_cross == marker + "-" + marker:
        return True
    if row_col_cross == "-" + marker + marker:
        return True
        
    return False

def find_winning_spot(marker):
    # Returns the winning spot if possible
    # Returns 0 if no winning spot exists
    
    if can_win(marker, r1):
        if b1 == "-":
            return 1
        elif b2 == "-":
            return 2
        return 3
    if can_win(marker, r2):
        if b4 == "-":
            return 4
        elif b5 == "-":
            return 5
        return 6
    if can_win(marker, r3):
        if b7 == "-":
            return 7
        elif b8 == "-":
            return 8
        return 9
    if can_win(marker, c1):
        if b1 == "-":
            return 1
        elif b4 == "-":
            return 4
        return 7
    if can_win(marker, c2):
        if b2 == "-":
            return 2
        elif b5 == "-":
            return 5
        return 8
    if can_win(marker, c3):
        if b3 == "-":
            return 3
        elif b6 == "-":
            return 6
        return 9
    if can_win(marker, x1):
        if b1 == "-":
            return 1
        elif b5 == "-":
            return 5
        return 9
    if can_win(marker, x2):
        if b3 == "-":
            return 3
        elif b5 == "-":
            return 5
        return 7
    return 0

# ------------------------------------------
# Display customization
# ------------------------------------------

# Idea - allow players to enter names instead of just X's and O's
# Idea - customize the game board and dialogue.  Some ideas: https://www.asciiart.eu/art-and-design/borders
# Idea - give the human player hints about winning moves or blocking their opponent

def print_board():
    print()
    print(" " + b1 + " ║ " + b2 + " ║ " + b3 + " ")
    print("═══╬═══╬═══")
    print(" " + b4 + " ║ " + b5 + " ║ " + b6 + " ")
    print("═══╬═══╬═══")
    print(" " + b7 + " ║ " + b8 + " ║ " + b9 + " ")
    print()

def print_game_start(marker_goes_first):
    print("Let's begin the game!  " + marker_goes_first + " goes first")

def print_winner(winning_marker):
    if winning_marker == "T":
        print("TIE!")
    else:
        print(winning_marker + " wins the game!")
        
def print_place_marker(marker, spot):
    print(marker + " plays on spot " + str(spot))

def print_player_gives_up(marker):
    print(marker + " gives up!")
    
def ask_human_for_spot(marker):
    return int(input("Where spot do you want " + marker + " to play? 0 to give up"))

# ------------------------------------------
# Computer algorithms
# ------------------------------------------

# Idea - create a computer algorithm that plays to win
# Idea - create a computer algorithm that plays to tie

def ask_defeated_computer_for_spot(marker):
    # This computer opponent always gives up
    
    return 0

def ask_random_computer_for_spot(marker):
    # This computer opponent picks a spot at random
    
    return random.randint(1, 9)

def ask_sequential_computer_for_spot(marker):
    # This computer opponent just picks the first available spot sequentially
    
    spot = 1
    
    while not is_spot_open(spot):
        spot = spot + 1
        
    return spot

def ask_fixed_optimal_computer_for_spot(marker):
    # This computer opponent picks an optimal spot based on a pre-programmed order
    # without regarding what the opponent is doing
    
    if is_spot_open(5):
        return 5
    if is_spot_open(1):
        return 1
    if is_spot_open(3):
        return 3
    if is_spot_open(7):
        return 7
    if is_spot_open(9):
        return 9
    if is_spot_open(2):
        return 2
    if is_spot_open(4):
        return 4
    if is_spot_open(6):
        return 6
    if is_spot_open(8):
        return 8

def ask_computer_for_spot(marker):
    # This computer opponent tries to go for the win if available
    # If not available, it just picks a random spot
    
    winning_spot = find_winning_spot(marker)
    
    if winning_spot != 0:
        return winning_spot
    else:
        return ask_random_computer_for_spot(marker)

# ------------------------------------------
# Customize the player settings
# ------------------------------------------

# Idea - Pick starting marker via a different mechanism.  A random roll? A guessing game?
# Idea - Allow the players to pick what type of game - human vs computer, human vs human, computer vs computer
# Idea - Allow the players to pick which computer algorithm they want to play against
# Idea - Add another modification.  Flip every spot?

def pick_starting_marker():
    return "X"

def pick_spot_for_player(marker):
    # This determines what algorithm will be used to play
    
    if marker == "X":
        return ask_human_for_spot(marker)
    else:
        return ask_computer_for_spot(marker)

def modify_game():
    global current_marker

    # Re-run the calculations before changing things
    calculate_winner()
    
    roll = random.randint(1, 6)
    
    if roll == 7:
        current_marker = opposite_marker(current_marker)
        print("Surprise, another turn for " + current_marker + "!")
        
    elif roll == 8:
        # Find a spot that is already filled
        spot = random.randint(1, 9)
        while is_spot_open(spot):
            spot = random.randint(1, 9)
       
        # Reverse the marker on that spot
        place_marker(opposite_marker(get_spot_marker(spot)), spot)
        
        print("Randomly reversed spot " + str(spot) + " to " + get_spot_marker(spot) + "!")
        
# ------------------------------------------
# Play the game
# ------------------------------------------

initialize_board()
current_marker = pick_starting_marker()
winner = "-"
turn_number = 0

print_game_start(current_marker)

while winner == "-":
    turn_number = turn_number + 1
    
    print_board()
    
    spot = pick_spot_for_player(current_marker)
    
    while not is_spot_open(spot) and spot != 0:
        spot = pick_spot_for_player(current_marker)

    if (spot == 0):
        print_player_gives_up(current_marker)
        
        winner = opposite_marker(current_marker)
    else:        
        set_marker_in_spot(current_marker, spot)

        print_place_marker(current_marker, spot)

        current_marker = opposite_marker(current_marker)
        
        modify_game()

        winner = calculate_winner()

# The game has ended
print_board()

print_winner(winner)
