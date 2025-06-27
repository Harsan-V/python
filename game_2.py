

import random

def game():
    target_number = random.randint(1, 1000)
    guess = 0
    number_of_tries = 0
    max_tries = 10

    print("Welcome to Guess Game!")
    print("I'm thinking of a number between 1 and 1000. Guess the number:")

    while number_of_tries < max_tries:
        try:
            guess = int(input(f"Attempt {number_of_tries + 1} - Enter your guess: "))
            number_of_tries += 1

            if guess < target_number:
                print("Your guess is too low.")
            elif guess > target_number:
                print("Your guess is too high.")
            else:
                print(f"🎉 You guessed it in {number_of_tries} tries!")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

    if guess != target_number:
        print(f"😢 Sorry! You've used all {max_tries} tries. The number was {target_number}.")

# Run the game
game()

"""
# snake and ladder game :

def dice():
    number_of_dice = random.randint(1, 6)
    guess = 0
    number_of_tries = 0
    max_tries = 10

print("Welcome to Snake Game!")
"""





