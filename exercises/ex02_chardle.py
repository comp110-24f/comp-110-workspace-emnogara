"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730670853"


def input_word() -> str:
    """Player enters in a word."""
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) == 5:  # if the length of the entry is 5
        print(user_word)
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        print(user_word)
    return user_word


def input_letter() -> str:
    """Players enter in a letter."""
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:  # if the length of the entry is a single character
        print("Error: Character must be a single character.")
        exit()
    print(user_letter)
    return user_letter


def contains_char(word: str, letter: str) -> None:
    """Looking for character in word."""
    print("Searching for " + letter + " in " + word)
    index: int = 0
    count: int = 0
    while index < len(word):  # while loop to determine if the letter is at any index
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count = count + 1
        index = index + 1
    if count == 0:  # the letter is not an element of the word
        print("No instances of " + letter + " found in " + word)
    elif count == 1:  # the letter was found once in the word
        print("1 instance of " + letter + " found in " + word)
    else:  # the letter was found more than once in the word
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
