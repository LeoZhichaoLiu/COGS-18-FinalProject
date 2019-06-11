"""Test for my functions: check_1_win, set_hiding_vocabulary, check_2_win
"""

from functions import check_1_win
from functions import set_hiding_vocabulary 
from functions import check_2_win

def test_check_1_win():
    """ test function for check_1_win"""
    
    # First we check for the conditions that different player input return not
    # win
    assert check_1_win(20, 10, "computer") == False

    assert check_1_win(20, 10, "you") == False

    # Then we check for the conditions that when goal = accmulation with win
    assert check_1_win(20, 20, "computer") == True

    assert check_1_win(20, 20, "you") == True

    # We finally check for the conditions that when goal < accumulation
    assert check_1_win(20, 21, "you") == True


def test_set_hiding_vocabulary():
    """ test function for set_hiding_vocabulary"""

    # We first check for word "Cat" with capital C.
    assert set_hiding_vocabulary("Cat") == "***"

    # Then we check for word with all lower case.
    assert set_hiding_vocabulary("python") == "******"
 
    # We finally check for word with a space.
    assert set_hiding_vocabulary("COGS 18") == "*******"


def test_check_2_win() :
    """ test function for check_2_win"""

    # We check for word without any *, which is win
    assert check_2_win ("cat") == True

    # We check for word with one *, which is false
    assert check_2_win ("c*t") == False

    # We cehck for word with space, but several *, which is false
    assert check_2_win ("**** **") == False

    # We check for word wit hall *, which is false.
    assert check_2_win ("*******") == False

