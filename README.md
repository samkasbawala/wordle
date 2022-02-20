# Wordle
Wordle is a game that is taking the world by storm. It is a simple word guessing game that was created by Josh Wardle. You can read more about the game and its rise in popularity [here](https://www.nytimes.com/2022/01/03/technology/wordle-word-game-creator.html). Used the word banks found on [this reddit](https://www.reddit.com/r/wordle/comments/s4tcw8/a_note_on_wordles_word_list/) thread to make this project.

## This Repo
This repo is a simple clone of it that has been built using Python and can be played in the terminal. It's not meant to rival the original game, nor is it supposed to be seen as a replacement. Instead, it is just a simple project that allows me to experiment with Python libraries and work on my programming skills.

## Installation
Only 3rd party package that is used for this project is `colorama`. So to install the dependencies, run:
```
pip install -r requirements.txt
```
This project requires Python 3.7+

## How to run
To run the program, run:
```
python play_wordle.py
```
That's it! Rules are the same as the original wordle game. Have fun!

## Possible Improvements
Use curses to make a terminal app instead of just writing to stdout.