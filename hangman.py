"""
Task 1: Hangman Game
A simple text-based Hangman game.
Concepts used: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "hangman", "computer", "keyboard", "science"]
MAX_WRONG = 6


def choose_word():
    return random.choice(WORDS)


def display_progress(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_WRONG} wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG:
        print("Word:", display_progress(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG}")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"You win! The word was '{word}'.")
                return
        else:
            wrong_guesses += 1
            print("Wrong guess.\n")

    print(f"You lose! The word was '{word}'.")


if __name__ == "__main__":
    play_hangman()
