"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730670853"


def input_word() -> str:
    """Player will input a word into the game."""
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")


input_word()
