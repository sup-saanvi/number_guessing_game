"""
This is a number guessing game.
 You have to type a number from
1 to 100 and then guess.
"""
import random

#INTRO 
print("Hello earthling! welcome to my game called the number guess of DOOM!")
name = input("What is you name, type name here ")
print(f"welcome {name}!")

# Import random module to generate a random number
import random
# Function to get a valid integer input with error handling
def number_guessing_game()
            print")
# Function to get a valid 'y' or 'n' response from the user

# Function to play one round of the game

# Ask for number range

# Ensure low_number is less than high_number

# Ask for number of attempts

# Generate random number

# Track number of attempts

# Loop for user guesses

# Check if guess is too low or too high

# Display success message if guessed correctly
=
# If max attempts are used up, reveal the correct number

# Main game loop

# Ask for user's name and greet them

# Ask if they want to play again, only accepting 'y' or 'n'

# Run the game

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please guess a number between 1 and 100.")
                continue

            if guess < number:
                print("Too low! 📉 Try again.")
            elif guess > number:
                print("Too high! 📈 Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Please enter a valid number.")

  
            

if __name__ == "__main__":
    number_guessing_game()
