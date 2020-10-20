#global variables
#Create the game board through a list
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

#initilize to True because thta while loop will run until it's False
game_still_going = True
winner = None
current_player = 'X'
def display_game_board():
    """ This function displays the game board by accessing the indices
    from the game board list.
    """
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])

def play_game():

    #Calls game board function to display the game board
    display_game_board()

    #loop until someone wins or a tie occurs
    while game_still_going:
        #creates a single turn for each player
        handle_turn(current_player)
        #Checks if the game is over
        check_if_game_over()
        #Flips turns to the other player
        flip_player()
        #the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

def handle_turn(player):
    """Handles a turn for a player"""
    print(player + "'s turn")
    position_question = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position_question not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position_question = input("Invalid input. Choose a position from 1-9: ")
        position_question = int(position_question) - 1
        if game_board[position_question] == "-":
            valid = True
        else:
            print("You can't go there. Go again")
    #player will be either X or O
    game_board[position_question] = player
    display_game_board()

def check_if_game_over():
    """ This function checks if the game over by checking if there is
    a win or a tie present on the game board"""
    check_if_win()
    check_if_tie()

def check_if_win():
    """There are three different way to win including 3 in a row, in a column or diagonally"""
    #sets up the global variables
    global winner
    #checks rows
    row_winner = check_rows()
    #checks columns
    column_winner = check_columns()
    #check diagnals
    diagnal_winner = check_diagnol()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagnal_winner:
        winner = diagnal_winner
    else:
        winner = None
    return

def check_rows():
    """Checks if the 3 of the same letters are present in a row"""

    #sets up global variables
    global game_still_going
    row_1 = game_board[0] == game_board[1] == game_board[2] != '-'
    row_2 = game_board[3] == game_board[4] == game_board[5] != '-'
    row_3 = game_board[6] == game_board[7] == game_board[8] != '-'
    #if any row has a match, the game is stopped
    if row_1 or row_2 or row_3:
        game_still_going = False

    #return's the winner if its X or O
    if row_1:
        return game_board[0]
    elif row_2:
        return game_board[3]
    elif row_3:
        return game_board[6]
    return

def check_columns():
    """Checks to see if there are 3 letters in a column"""
    #sets up global variables
    global game_still_going
    column_1 = game_board[0] == game_board[3] == game_board[6] != '-'
    column_2 = game_board[1] == game_board[4] == game_board[7] != '-'
    column_3 = game_board[2] == game_board[5] == game_board[8] != '-'
    #if any column has a match, the game is stopped
    if column_1 or column_2 or column_3:
        game_still_going = False

    #return's the winner if its X or O
    if column_1:
        return game_board[0]
    elif column_2:
        return game_board[1]
    elif column_3:
        return game_board[2]
    return

def check_diagnol():
    """ Checks if three of the same letters are present diagnolly to determine a winner"""
    #sets up global variables
    global game_still_going
    diagnol_1 = game_board[0] == game_board[4] == game_board[8] != '-'
    diagnol_2 = game_board[6] == game_board[4] == game_board[2] != '-'
    #if any column has a match, the game is stopped
    if diagnol_1 or diagnol_2:
        game_still_going = False

    #return's the winner if its X or O
    if diagnol_1:
        return game_board[8]
    elif diagnol_2:
        return game_board[6]
    return

def check_if_tie():
    """Checks if a tie is present among the two players"""
    global game_still_going
    if '-' not in game_board:
        game_still_going = False
    return

def flip_player():
    """This function will flip between the two players ie X and O"""
    #global variables that we need
    global current_player
    #if the current player is X, then switch to player O
    if current_player == 'X':
        current_player = 'O'
    #if the current player is O, then switch to player X
    elif current_player == 'O':
        current_player = 'X'
    return
play_game()