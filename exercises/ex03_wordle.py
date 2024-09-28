"""Creating a secret word guessing game."""

__author__: "730670853"


def input_guess(secret_word_len: int) -> str:
    """Entering in a word the same length as the secret word."""
    userword: str = input(f"Enter a {secret_word_len} character word: ")
    while (
        True
    ):  # while loop to ensure that the user's guess is the length of the secret word
        if len(userword) == secret_word_len:
            return userword
        else:
            userword: str = input(f"That wasn't {secret_word_len} chars! Try again: ")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searching for the user inputted character in the user inputted word."""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(
        secret_word
    ):  # while loop to determine if the char is at any index
        if secret_word[index] == char_guess:
            return True  # char was found in the word
        index += 1
    return False  # char was not found in the word


def emojified(user_guess: str, secret_phrase: str) -> str:
    """Emoji string to represent how close the guess is to the secret word."""
    assert len(user_guess) == len(secret_phrase)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    answer: str = ""
    while index < len(secret_phrase):
        if user_guess[index] == secret_phrase[index]:
            answer += GREEN_BOX  # letter at correct index
        elif contains_char(secret_word=secret_phrase, char_guess=user_guess[index]):
            answer += YELLOW_BOX  # letter in word but at wrong index
        else:
            answer += WHITE_BOX  # letter not in word
        index += 1
    return answer


def main(secret: str) -> None:
    """The point of entry for the program and main game loop."""
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        word_guess: str = input_guess(
            secret_word_len=len(secret)
        )  # using the input_guess function
        user_answer: str = emojified(word_guess, secret)  # using the emojified function
        print(user_answer)
        if word_guess == secret:
            print(f"You won in {turns} turns!")
            exit()  # stopping the function once the word has been guessed
        turns += 1
    if turns > 6:
        print("X/6 - Sorry, try again tomorrow!")
        exit()


if __name__ == "__main__":
    main(secret="codes")
