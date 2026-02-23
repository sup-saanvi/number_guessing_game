"""
This is a number guessing game.
 You have to type a number from
1 to 100 and then guess.
"""
# Import random module to generate a random number
import random



# prompt means the message that will be displayed to the user when asking for input
def get_valid_integer(prompt):
    while True:  # Loop until a valid integer is entered
        try:  # Try to convert the input to an integer
            return int(input(prompt))  # If successful, return the integer
        except ValueError:  # If a ValueError occurs, it means the input was not a valid integer
            # Prompt the user to enter a valid integer again
            print("Please enter a valid integer.")

# Function to get a valid 'y' or 'n' response from the user


def get_yes_no(prompt):  # Loop until a valid response is entered
    while True:
        # Get the user's response and convert it to lowercase
        response = input(prompt).lower()
        if response in ['y', 'n']:  # Check if the response is either 'y' or 'n'
            return response  # If valid, return the response
        else:
            # Prompt the user to enter a valid response again
            print("Please enter 'y' for yes or 'n' for no.")

# Function to play one round of the game


def play_game():

    # Ask for number range
    while True:  # Loop until a valid number range is entered
        low_number = get_valid_integer(
            # Get the lower bound of the number range from the user
            "Enter the lower bound of the number range: ")
        high_number = get_valid_integer(
            # Get the upper bound of the number range from the user
            "Enter the upper bound of the number range: ")
        if low_number < high_number:  # Check if the lower bound is less than the upper bound
            break
        else:  # If the lower bound is not less than the upper bound, prompt the user to enter a valid range again
            print("The lower bound must be less than the upper bound.")
# Ask for number of attempts
    # Get the number of attempts from the user
    max_attempts = get_valid_integer("Enter the number of attempts you want: ")
    while max_attempts <= 0:  # Check if the number of attempts is a positive integer
        print("Please enter a positive integer for attempts.")
        max_attempts = get_valid_integer(
            # If the number of attempts is not a positive integer, prompt the user to enter a valid number of attempts again
            "Enter the number of attempts you want: ")

# Generate random number
    target_number = random.randint(low_number, high_number)

# Track number of attempts
    attempts = 0

# Loop for user guesses
    while attempts < max_attempts:  # Loop until the user has used up all attempts
        guess = get_valid_integer(
            # Get the user's guess and display the current attempt number and total attempts
            f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ")
        attempts += 1

# Check if guess is too low or too high
        if guess < target_number:  # If the guess is less than the target number, inform the user that their guess is too low
            print("TOO LOW YOUR FREEZING! Try again.")
        elif guess > target_number:  # If the guess is greater than the target number, inform the user that their guess is too high
            print("TOO HIGH YOUR BURNING! Try again.")
        else:  # If the guess is equal to the target number, break out of the loop as the user has guessed correctly
            break
# Display success message if guessed correctly
    if guess == target_number:  # If the user's guess is correct, congratulate them and display the number of attempts it took
        print(
            f"Congrats I guess.... you've guessed the number {target_number} in {attempts} attempts.")
# If max attempts are used up, reveal the correct number
    else:  # If the user has used up all attempts without guessing correctly, reveal the correct number
        print(
            f"HAHAHA, you've used all {max_attempts} attempts. The DOOM number was {target_number}.")
# Main game loop


def main():
    print("Welcome to the Number Guessing Game!")
# Ask for user's name and greet them
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Let's start the game game of DOOM if you dare.")
    while True:  # Loop to allow the user to play multiple rounds
        play_game()  # Play one round of the game
# Ask if they want to play again, only accepting 'y' or 'n'
        play_again = get_yes_no("Do you want to play in the doom again? (y/n): ")
        if play_again == 'n':  # If the user doesn't want to play again, break out of the loop
            print(" Not Thanks for playing!")
            break


# Run the game
if __name__ == "__main__":  # run the main function if this script is executed directly
    # This line checks if the script is being run directly (as the main program) and if so, it calls the main() function to start the game.
    main()



#INTRO 
print("Hello earthling! welcome to my game called the number guess of DOOM!")
name = input("What is you name? Type your name here. ")
print(f"welcome {name}!")

 