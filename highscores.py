#to check highscores

import fileinput

def hscores():
    with fileinput.input(files='C:/Users/Srikar/Desktop/Mastermind/User.txt') as f:
        for line in f:
            print(line)
