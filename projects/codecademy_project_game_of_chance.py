# codecademy_project_game_of_chance.py

import random

#Write your game of chance functions here


def winner(call, computer):
    if call == "heads":
        call = 1
    elif call == "tails":
        call = 2
    if call == computer:
        result = "You win!"
    elif call != computer:
        result = "You lose."
    return result

#Call your game of chance functions here

money = 100

while money > 0:
    user_call = input("Choose one — heads or tails: ").lower
    user_bet = input("How much money would you like to bet? ")
    user_bet = int(user_bet)
    computer_call = random.randint(1,2)
    print(f"The computer picked {computer_call}")
    if winner(user_call, computer_call) == "You win!":
        money += user_bet
    else:
        money -= user_bet
    print(f"{winner(user_call, computer_call)} Your balance is now {money}")
else:
    print("You are out of money.")