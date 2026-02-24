"""
Number Guessing Game - DOOM Edition
Guess the randomly generated number within your chosen range
and limited attempts.
"""

import random


# ==========================
# Input Helper Functions
# ==========================

def get_valid_integer(prompt):
    """Prompt user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def get_yes_no(prompt):
    """Prompt user until 'y' or 'n' is entered."""
    while True:
        response = input(prompt).lower()
        if response in ('y', 'n'):
            return response
        print("Please enter 'y' for yes or 'n' for no.")


# ==========================
# Game Logic Functions
# ==========================

def get_number_range():
    """Get a valid number range from the user."""
    while True:
        low = get_valid_integer("Enter the lower bound: ")
        high = get_valid_integer("Enter the upper bound: ")

        if low < high:
            return low, high
        print("Lower bound must be less than upper bound.")


def get_attempt_limit():
    """Get a positive number of attempts from the user."""
    while True:
        attempts = get_valid_integer("Enter number of attempts: ")
        if attempts > 0:
            return attempts
        print("Please enter a positive number.")


def play_game():
    """Play one round of the guessing game."""
    low, high = get_number_range()
    max_attempts = get_attempt_limit()

    target_number = random.randint(low, high)
    attempts = 0

    while attempts < max_attempts:
        guess = get_valid_integer(
            f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "
        )
        attempts += 1

        if guess < target_number:
            print("TOO LOW... YOU'RE FREEZING!")
        elif guess > target_number:
            print("TOO HIGH... YOU'RE BURNING!")
        else:
            print(
                f"Congrats! You guessed the number {target_number} "
                f"in {attempts} attempts."
            )
            return

    print(
        f"HAHAHA! You've used all {max_attempts} attempts.\n"
        f"The DOOM number was {target_number}."
    )


# ==========================
# Main Program
# ==========================

def main():
    print("Welcome to the NUMBER GUESS OF DOOM!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let the guessing of DOOM begin...\n")

    while True:
        play_game()
        if get_yes_no("Play again? (y/n): ") == 'n':
            print("Thanks for playing I guess ........")
            break


if __name__ == "__main__":
    main()
