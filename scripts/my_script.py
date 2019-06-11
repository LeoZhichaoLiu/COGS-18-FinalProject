"""
Script to run my project. 

The detailed description is in the Notebook.
While I also put instructions in the game process, so I think you can understand
how to play it when you execute this script.
Note that you can also play this project in Notebook, where I also write the
following codes.

Thanks for you all for this wonderful quarter!
"""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.functions import check_which_game
from my_module.functions import set_goal
from my_module.functions import check_1_win
from my_module.functions import game_1_communicate 
from my_module.functions import play_game_1 
from my_module.functions import set_vocabulary 
from my_module.functions import set_hiding_vocabulary
from my_module.functions import check_2_win 
from my_module.functions import game_2_communicate 
from my_module.functions import play_game_2

# To play the game, we first check which game the user wants to play (1 or 2)
game_to_play = check_which_game ()

# If that number is 1, just call play_game_1 to play that game 1
if (game_to_play == 1) :
    play_game_1 ()

# If that number is 2, call play_game_2 to play game 2
elif (game_to_play == 2) :
    play_game_2 ()

