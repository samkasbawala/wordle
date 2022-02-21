from __future__ import annotations
from typing import Dict
from .wordle import Wordle, Letter

from colorama import Fore
import os
import random


class Interface:
    def __init__(self) -> None:

        # Path for possible guesses
        file_dir = os.path.dirname(__file__)
        g_path = os.path.join(file_dir, "../data/wordle-allowed-guesses.txt")

        # Path for possible answers
        a_path = os.path.join(file_dir, "../data/wordle-answers-alphabetical.txt")

        with open(a_path, "r") as file:
            lines = file.readlines()
            self.answers = [word.strip().upper() for word in lines]

        with open(g_path, "r") as file:
            lines = file.readlines()
            self.guesses = set([word.strip().upper() for word in lines])
            self.guesses = self.guesses.union(self.answers)

        # Instantiate a game of wordle
        self.wordle = Wordle(random.choice(self.answers))

    def main(self) -> None:
        print("Welcome to Wordle!")

        self.display_game()

        # Loop until the game is over
        while not self.wordle.game_over:
            inp = self.get_user_input()

            # Guess must be the correct length and must be a word
            if len(inp) != self.wordle.MAX_WORD_LENGTH or inp not in self.guesses:
                print(
                    Fore.RED
                    + "You must enter a valid word that is of length "
                    + str(self.wordle.MAX_WORD_LENGTH)
                    + Fore.RESET
                )
                continue

            # Add the attempt to out game
            self.wordle.add_attempt(inp)
            self.display_game()

        if self.wordle.won:
            print("\nYou won! :)")
        else:
            print("\nYou lost! :(")
            print(f"The correct word was {self.wordle.word}")

    def get_user_input(self) -> str:
        """Gets user input"""
        input_str = input("\nEnter your guess: ")
        return input_str.upper()

    def display_game(self) -> None:
        """Function to display the guesses"""

        # Print an empty line
        print()

        # Display guesses so far
        for attempt_states in self.wordle.attempts:
            colored_guess = self.add_color(attempt_states)
            print(colored_guess)

        # Add underscores for attempts that haven't been made yet
        for _ in range(self.wordle.MAX_ATTEMPTS - len(self.wordle.attempts)):
            print(" ".join(["_"] * self.wordle.MAX_WORD_LENGTH))

    def add_color(self, attempt: Dict[int, Letter]) -> str:
        """Function to add color to an attempt"""

        # Colored characters
        colored_guess = []

        # Color each character in the guess and append it to the list
        for _, letter in sorted(attempt.items(), key=lambda x: x[0]):
            if letter.correct_position:
                color = Fore.GREEN
            elif letter.in_word:
                color = Fore.YELLOW
            else:
                color = Fore.LIGHTRED_EX

            colored_guess.append(color + str(letter) + Fore.RESET)

        # Join the colored characters with a space in between
        return " ".join(colored_guess)
