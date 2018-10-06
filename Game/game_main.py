#main module to play the game

import sys
from pattern_gen import *
from play_game import *


def main_game():
    rand_patt=pattern_generator()
    play_game(rand_patt)
    print("Enter 1 to play again.")
    print("Enter 2 to go back.")
    print("Enter anything else to quit.")
    inp=input("Enter your choice :")
    if(inp=='1'):
        main_game()
    elif(inp=='2'):pass
    else:pass#code to quit
