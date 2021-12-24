#---------Imports:---------#
from game_data import data
from art import logo
import random
import os


#-----------Functions:----------#
def chose_next():
    return random.choice(data)


def pick_A ():
    current_pick = chose_next()
    global likes_A
    likes_A = current_pick ['follower_count']
    return current_pick


def pick_B ():
    current_pick = chose_next()
    global likes_B
    likes_B = current_pick ['follower_count']
    return current_pick


def print_statement(A,B):
    global score
    print(f"Your score is {score}")
    print(f"Compare A: {A ['name']} is a {A ['description']} from {A ['country']}\n\n\n\nAgainst B: {B ['name']} is a {B ['description']} from {B['country']}\n")


#------------Definitions:------------#
continue_game = True
score = 0
current_pick_A = {}
current_pick_B = {}
likes_A = 0
likes_B = 0
current_pick_A = pick_A ()
current_pick_B = pick_B () #could add if current_pick_A == current_pick_B then run current_pick_B again

#------------Game:------------------#
while continue_game == True:
    print(logo)
    print_statement(current_pick_A, current_pick_B)
    choice_player = input("Who has more followers? Type 'A' or 'B'")

    if likes_A > likes_B:
        winner = "A"
        current_pick_B = pick_B () #generally in the solution much more functions with true statements and if will automatically check these statements without writing == True

    else:
        winner = "B"
        current_pick_A = current_pick_B
        current_pick_B = pick_B ()

    if choice_player == winner:
        score += 1


    else:
        continue_game = False


print("Loser")
