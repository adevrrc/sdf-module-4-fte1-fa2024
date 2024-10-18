"""
Description: A simple guessing game.
Author: Damien Altenburg
Date: 2023-10-1
Usage: python guessing_game.py
"""

from random import randint

title_text: str = "** JELLYBEAN GUESSING GAME **"

LOW_RANGE: int = 1
HIGH_RANGE: int = 10
NUMBER_OF_JELLYBEANS: int = randint(LOW_RANGE, HIGH_RANGE)

guess_count: int = 0

print(title_text)
print("=" * len(title_text))

prompt_text: str = "Enter your guess: "

jellybeans_guessed: bool = False

while not jellybeans_guessed:
    guess_is_out_of_range: bool = True

    if guess_count > 0:
        print("That guess is incorrect.")

        prompt_text = "Guess again: "

    while guess_is_out_of_range:
        try:
            guess = input(prompt_text)
            guess = int(guess)

            guess_is_out_of_range = guess < LOW_RANGE or guess > HIGH_RANGE

            if guess_is_out_of_range:
                print(f"Your guess must be between {LOW_RANGE}-{HIGH_RANGE}.")
                prompt_text = f"Guess ({LOW_RANGE}-{HIGH_RANGE}): "
        except ValueError as exception:
            print("You must enter a whole number.")
            
            prompt_text = "Re-enter guess: "

    guess_count += 1

    jellybeans_guessed = guess == NUMBER_OF_JELLYBEANS

print(f"It took you {guess_count} guess{'' if guess_count == 1 else 'es'}.")
