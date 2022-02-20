from __future__ import annotations
from dataclasses import dataclass
from typing import List


class Wordle:
    MAX_ATTEMPTS: int = 6
    MAX_WORD_LENGTH: int = 5

    def __init__(self, word: str) -> None:

        # Word that is trying to be guessed
        self.word = word.upper()

        # List of attempts that have been made so far
        self.attempts: List[List[Letter]] = []

    @property
    def won(self) -> bool:
        """Checks if the game has been won"""

        # Can only win if a valid attempt has been made
        return len(self.attempts) > 0 and self.__correct_guess

    @property
    def __correct_guess(self) -> bool:
        """Checks if the most recent guess is correct"""
        guess_states = self.attempts[-1]
        guess = "".join([str(guess) for guess in guess_states])
        return guess == self.word

    @property
    def game_over(self) -> bool:
        """Returns a boolean value indicating whether the game is over"""
        return len(self.attempts) >= self.MAX_ATTEMPTS or self.won

    def add_attempt(self, attempt: str):
        """Adds the state of each letter for a guess to the attempts collection"""

        attempt_state = []
        for index, ch in enumerate(attempt):
            state = Letter(ch, ch in self.word, self.word[index] == attempt[index])
            attempt_state.append(state)

        self.attempts.append(attempt_state)


@dataclass
class Letter:
    character: str
    in_word: bool = False
    correct_position: bool = False

    def __repr__(self) -> str:
        return (
            f"{self.character}: in_word=[{self.in_word}] and "
            f"correct_position=[{self.correct_position}]"
        )

    def __str__(self) -> str:
        return self.character
