# codecademy_project_game_of_chance.py

import random

#Write your game of chance functions here


def winner(call):
    call = str.lower(call)
    if call == "heads":
        call = 1
    elif call == "tails":
        call = 2
    return call

#Call your game of chance functions here

money = 100

while money > 0:
    print("\n")
    print("* " * 10)
    user_call = input("\nChoose one — heads or tails: ")
    user_bet = input("\nHow much money would you like to bet? ")
    user_bet = int(user_bet)
    computer_call = random.randint(1,2)
    if computer_call == 1:
        print(f"\nThe computer picked heads")
    else:
        print(f"\nThe computer picked tails")
    if winner(user_call) == computer_call:
        money += user_bet
        print(f"\nYou win! Your balance is now {money}")
    else:
        money -= user_bet
        print(f"\nYou lose! Your balance is now {money}")
else:
    print("You are out of money.")