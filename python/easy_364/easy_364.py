
# Challenge 364 [Easy] Create a Dice Roller

# Description
# I love playing D&D with my friends, and my favorite part is creating character sheets (my DM is notorious for killing us all off by level 3 or so). One major part of making character sheets is rolling the character's stats. Sadly, I have lost all my dice, so I'm asking for your help to make a dice roller for me to use!

# Input - list of dice to roll, either as cmd input or a file. In the file, each set of dice rolls needs to be on a new line. 
# Output - list of roll results, either as cmd output or printed to a file. 


import argparse
import random

# Roll the dice
def rolldice(dice, n):
    result = 0
    for n in range(n):
        result = random.randrange(1, dice+1)

    print result

rolldice(6, 1)