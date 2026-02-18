"""
This is a number guessing game.
 You have to type a number from
1 to 100 and then guess.
"""
import random
def get_number(prompt:str) -> int:
   """
   Will ask for an integer, it will check if it's an integer and return it .
   """
   while True:
        try:
            value = int(input(prompt))

            return value
        except ValueError:
            print("please enter a valid integer.")
#INTRO 
print("Hello earthling! welcome to my game called the number guess of DOOM!")
name = input("What is you name, type name here ")
print(f"welcome {name}!")

# Import random module to generate a random number


# Function to get a valid 'y' or 'n' response from the user

# Function to play one round of the game
round_to_win = get_number("What do you want the range to be till?")
# Ask for number range

# Ensure low_number is less than high_number
def player_round() -> int:
   # Roll dice for both player and computer
    input("\nplease press ENTER to do next guess")
    player_guess = take_another_turn
    
    if player_guess > guessed_number:
        return print("To high try again!")
    elif player_roll < guessed_nuber:
        return print("To low try agian!")  
    else:
        return Print(" YAYA you guessed the number")
# Ask for number of attempts

# Generate random number

# Track number of attempts

# Loop for user guesses

# Check if guess is too low or too high

# Display success message if guessed correctly

# If max attempts are used up, reveal the correct number

# Main game loop

# Ask for user's name and greet them

# Ask if they want to play again, only accepting 'y' or 'n'

# Run the game

