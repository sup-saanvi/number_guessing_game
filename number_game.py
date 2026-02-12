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
