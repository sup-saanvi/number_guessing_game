# TASK: Write a function that returns a random encouragement message.

import random

def get_encouragement() -> str:
    """Returns a random encouragement message."""
    message1 = "You can do it!"
    message2 = "Keep going, you're doing great!"
    message3 = "Believe in yourself!"
    message4 = "Every small step counts!"

    random_number = random.randint(1, 4)

    if random_number == 1:
        return message1
    elif random_number == 2:
        return message2
    elif random_number == 3:
        return message3
    else:
        return message4

# Call the function and print the result
print(get_encouragement())