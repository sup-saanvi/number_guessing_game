"""
Dice battle Game
compete with the computer.
First to 3 points win!
"""
import random

# we will roll dice
def roll_dice() -> int:
    
    #this will generate a random number as a dice roll
    return  random.randint(1, 20)
    
def player_round() -> int:
   # Roll dice for both player and computer
    input("\nplease ENTER yo roll your dice ...")
    player_roll = roll_dice()
    computer_roll = roll_dice()

    if player_roll > computer_roll:
        return 1
    elif player_roll < computer_roll:
        return -1   
    else:
        return 0
    
def get_number(prompt:str) -> int:
   """
   Will ask for an integer, check if it is int and return it.
   """
   while True:
        try:
            value = int(input(prompt))

            return value
        except ValueError:
            print("please enter a valid integer.")



player_score = 0
computer_score = 0

round_to_win = get_number("How many points to win?")


while player_score < round_to_win and computer_score <round_to_win:
    result = player_round()

    if result == 1:
        player_score += 1
    elif result == -1:
        computer_score += 1

    print(f"Your score: {player_score}, computer score: {computer_score}")