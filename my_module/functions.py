"""A collection of functions for doing my project."""

# Import random and string pakage used in below functions
import random 
import string


def check_which_game () :
    """
    Let user enter a loop to select which game they want to play (1 or 2).
    
    Returns
    -------
    output : String
        String indicating the choice that user make (1 or 2).
    """
    
    # Print the introducation sentences to welcome the players!
    print ("Start to play game! There are two games you can select:" )     
    print ("  1）Accumulate Number to goal            2）Guess vocabulary")
    
    # Use while loop to ask user the input command
    while (1) :
        
        # Print the instruction asking user to input command 1 or 2, and record user's input as command
        print ()
        command = input ("Please enter number 1 as first game, or 2 as second game:    ")
        
        # If command is 1, return 1 as user choose to play the first game
        if (command == "1") :    
            return 1
        
        # If command is 2, return 2 as user choose to play the second game
        elif (command == "2") :
            return 2
        
        # If command is not 1 or 2, the instruction will be prompted again until you enter 1 or 2
        else :
            continue


def set_goal () :
    """
    Let user enter a loop to set the goal number that want to reach in game. It should be in range [10,100].
    
    Returns
    -------
    output : String
        String indicates that the goal number the user sets.
    """
    
    # Use while loop to set the goal
    while (1) :
        
            # Print instruction that which number you want to set as goal, and record that number as goal
            goal_string = input (" READY TO START? First set up the GOAL, positive integer from 10 to 100   ")
            goal = int (goal_string, 10)
            
            # If goal is not in range [10,100], continue to loop until the user enter valid goal
            if (goal < 10 or goal > 100) :         
                continue
              
            # If goal is in the range, break the loop
            else :
                break
                
    # Finally return the goal number            
    return goal


def check_1_win (goal, accumulation, player) :
    """
    Check whether the player (human or computer) win this game.
    
    Parameters
    ----------
    input: goal             An int indicating the goal number the player want to reach.
           accumulation     The int current number the palyer reaches.
           player           The string indicating the name of the user (computer or human).
           
    Returns
    -------
    output : bol
        bol indicating whether the user win the game.
    """
    
    # If accumulation is bigger or equal to goal, meaning that player win the game
    if (accumulation >= goal) :
        
        # If that player is you, print the congradulation sentence and return true
        if (player == "you") :     
            
            print ("CONGRADULATION! YOU WIN!")
            return True
        
        # If that player is computer, print the congradulation sentence and return true
        elif (player == "computer") :  
            
            print ("UNFORTUNELY, YOU LOSE! COMPUTER WIN!")
            return True
    
    # If accumulation is smaller than goal, just return false as the player is not win now.
    else :
        return False


def game_1_communicate (goal, accumulation, turn) :
    """
    Let user enter a interactive loop to play the game.
    
    Parameters
    ----------
    input: goal             An int indicating the goal number the player want to reach.
           accumulation     The int current number the palyer reaches.
           turn             The round that players play now.
           
    Returns
    -------
    output : None
    """
    
    while (1) :
        
        # In each loop, increment of turn showing which turn we are in
        turn = turn + 1
        
        # Print the current turn's information, with turn number and accumulation number and goal number
        print ()
        print ("TURN " + str (turn) +") accumulation: " + str (accumulation) + "    goal: " + str (goal) )
        print ()
        
        # Then, print the prompt to ask user input the number in this turn
        you_input_string = input (" Please enter a number from range [1,3]  ")
        you_input = int (you_input_string, 10)
        
        # Print your input to the display
        print ()
        print ("your input: " + str (you_input))
        
        # If your input is not in the rangle [1,3], you will continue the loop, but turn will remain the same
        if ( you_input < 1 or you_input > 3) :
            turn = turn - 1
            continue
        
        # Then, after you input the number, calculate the accmulation and check whether you win.
        accumulation = accumulation + you_input
        
        if (check_1_win (goal, accumulation, "you")) :
            break
        
        # Then, computer will randomly select the input number, and we calculate accumulation.
        computer_input = random.choice ([1,2,3])
        print ("computer input: " + str (computer_input))
        accumulation = accumulation + computer_input
        
        # We check whether computer win this game. If not, continue to the next turn.
        if (check_1_win (goal, accumulation, "computer")) :
            break
            

def play_game_1 () :
    """
    Print the instructions and implement the above functions to play the game.
    
    Returns
    -------
    output : None
    """
    
    # First, we print the game 1 instruction.
    print ()
    print ("You choose game 1: Accumulate Number to Goal!")
    print ()
    print ("In this game, you will play with the computer each turn to complete a goal.")
    print ()
    print ("1) You need to set up the goal (a positive number in range [10,100]. ")
    print ("2) Then in each turn, you can enter a number from range [1,3], invalid input causes prompt again")
    print ("   The computer will randomly pick the number in each turn.")
    print ("   the sum of your input and computer input will be accmulated")
    print ("3) Finally, if you enter a number and the accumulation reach the goal you set, YOU WIN!")
    print ("   If computer reach the goal, COMPUTER WIN!")
    print ()
    
    # We set the initial value of goal to 0, and then call function set_goal to set goal number
    goal = 0
    goal = set_goal ()
    
    # We also set accumulation and turn to 0.
    accumulation = 0
    turn = 0  
    
    # We call function game_1_communicate to enter the game process
    game_1_communicate (goal, accumulation, turn)


def set_vocabulary () :
    """
    Let user 1 enter a loop to set the vocabulary that want the player 2 to guess.
    
    Returns
    -------
    output : String
        String indicates that the vocabulary the user 1 sets.
    """
    
    # We set the prompt instruction and record user's input as the vocabulary
    vocabulary = input ("READY TO START? Now let Player 1 enter the vocabulary:   ")
    print ()
    
    # Return that vocabulary
    return vocabulary


def set_hiding_vocabulary (vocabulary) :
    """
    Set the vocabulary provided by player 1 to a hiding string in format of ****.
    
    Parameters
    ----------
    input: vocabulary    The vocabulary that player 1 set to let player 2 to guess.
           
    Returns
    -------
    output : String
        String indicating the hiding vocabulary shown to player 2 to guess.
    """
    
    # Print the instruction to welcome the player 2
    print ("Now, invite Player 2!!")
    print()
    
    # We set the vocabulary_display as the hiding vocabulary with all *.
    vocabulary_display = "*" * len (vocabulary)
    
    # We print that hiding vocabulary and return hiding vocabulary
    print ("The vocabulary is looked like:   " + vocabulary_display)
    
    return vocabulary_display


def check_2_win (vocabulary_display) :
    """
    Check whether the player 2 win this game (guess the vocabulary).
    
    Parameters
    ----------
    input: vocabulary            The vocabulary that player 1 set to let player 2 to guess.
           vocabulary_display    The hiding string that give hint to player 2.
           
    Returns
    -------
    output : bol
        bol indicating whether the user win the game.
    """
    
    # If * is not in vocabulary_display, meaning you guess what is that word is. Congradulate to you!
    if ("*" not in vocabulary_display) :
        print ("CONGRADULATION! YOU WIN!!")
        return True
    
    # Else, you don't win now, return false
    else :
        return False


def game_2_communicate (vocabulary, vocabulary_display) :
    """
    Let user enter a interactive loop to play the game (guess what is the vocabulary).
    
    Parameters
    ----------
    input: vocabulary            The vocabulary that player 1 set to let player 2 to guess.
           vocabulary_display    The hiding string that give hint to player 2.
           
    Returns
    -------
    output : None
    """
    
    while (1) :
        
            # In while loop, ask player 2 to enter the letter.
            while (1) : 
                
                # Record that input as letter
                letter = input ("Now, please Player 2 enter the letter you think this vocabulary should contain:  ")
                
                # If letter's length is larger than 1, meaning it's not single letter, print error and continue
                if (len(letter) > 1) :
                    print ("Please enter SINGLE letter!!!")
                    print ()
                 
                # If letter is a single letter, break the while loop.
                else :
                    break
        
            # Then, we use for loop check each index of vocabulary
            for index in range (len (vocabulary)) :
                
                # If that index of vocabulary is letter user input, just replace that * with letter
                if (vocabulary[index] == letter) :
                    vocabulary_display = vocabulary_display[:index] + letter + vocabulary_display[index + 1:]
        
            # Print the current display hiding vocabulary, it should contain * and letter user input
            print ()
            print ("The new vocabulary is : " + vocabulary_display)
            
            # We call function check_2_win to see whether we finish guessing
            if (check_2_win (vocabulary_display)) :
                break


def play_game_2 () :
    """
    Print the instructions and implement the above functions to play the game.
    
    Returns
    -------
    output : None
    """

    # First we print the instruction guide to play the game 2
    print ()
    print ("You choose game 2: Guess vocabulary!")
    print ()
    print ("The goal of this game is to guess a vocabulary. It should involve two players to play")
    print ()
    print ("1) Player 1 sould enter any vocabulary that wish player 2 to guess, case matter.")
    print ("2) The system will output form like ***** to show the number of the correct vocabulary.")
    print ("3) Player 2 can guess the vocabulary by entering specific letter.")
    print ("4) The system will give hint to tell you whether the vocabulary contains your guessing letter")
    print ("   Symbol * indicate that your guessing letter doesn't exist in that position")
    print ("   If that position is your guessing letter, * will change to the letter you guess")
    print ("5) If you guess all the letter the vocabury contains, YOU WIN")
    print ()
    
    # Then we set the vocabulary and vocabulary_display according to vovabulary input
    vocabulary = set_vocabulary ()
    vocabulary_display = set_hiding_vocabulary (vocabulary)
    
    # Finally we call game_2_communicate to enter the game playing
    game_2_communicate (vocabulary, vocabulary_display)

