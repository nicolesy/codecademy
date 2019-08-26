# codecademy_project_cho_han.py

# Create a function that simulates playing the game Cho-Han. The function should simulate rolling two dice and adding the results together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.

# The function should have a parameter that allows for the player to guess whether the sum of the two dice is "Odd" or "Even". The function should also have a parameter that allows the player to bet an amount of money on the game.

# test

import random

def roll_dice(guess, comp):
    if guess == comp:
        result = "You win!"
    else:
        result = "You lose."
    return result

money = 100

while money > 0:
    user_guess = input("Is it even, or odd? ")
    user_bet = input("How much would you like to bet? ")
    user_bet = int(user_bet)
    calc_1 = random.randint(1,6)
    calc_2 = random.randint(1,6)
    computer_calc = calc_1 + calc_2
    print(f"The random number is {computer_calc}")
    if computer_calc % 2 == 0:
        computer_calc = "even"
    else:
        computer_calc = "odd"
    if roll_dice(user_guess, computer_calc) == "You win!":
        money += user_bet
    else:
        money -= user_bet
    print(f"{roll_dice(user_guess, computer_calc)} You have ${money} remaining.")
else:
    print("You are out of money.")