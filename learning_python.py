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
    


player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    
# compare the two rolls
    player_roll = roll_dice()
    computer_roll = roll_dice()

    print(f"you rolled: {player_roll}")
    print(f"computer rolled: {computer_roll}")

    if player_roll > computer_roll :
        print("you won!")
        player_score += 1
    elif player_roll < computer_roll:
        print("you lose! hahah loser!")
        computer_score += 1
    else:
        print("you tied!")

    print(f"You score: {player_score}, Computer score: {computer_score}")

    pausing = input("\n")

# Put all the dice rolling in a seperate function that 
# returns 1 if player wins and returns -1 if computer wins or rturns 0 if 
# tied.Then decide whether to add points to user or computer based on the return value.
# validation for user input using try... except and allow user to decide how many rounds to play.z gyi  n k j b  ft fyt yt    

