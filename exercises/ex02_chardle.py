"""EX02 - Chardle - A Word Guessing Game."""

__author__ = "730670853"


def input_word() -> str:
    """Determining the length of the word and if the guess is close to the truth."""
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
    return user_word


def input_letter() -> str:
    """Looking at a single letter in a word."""
    sing_char: str = input("Enter a single character: ")
    if len(sing_char) != 1:
        print("Error: Character must be a single character.")
    return sing_char


def contains_char(word: str, letter: str) -> None:
    "Seeing if the character is in the word."
    print("Searching for " + letter + " in " + word)
