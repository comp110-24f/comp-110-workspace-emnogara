"""While Loops Challenge Question."""

__author__ = "730670853"


def num_instances(phrase: str, search_char: str) -> int:
    "Find the instances of character in phrase."
    if len(search_char) != 1:
        exit()
    index: int = 0
    count: int = 0
    while (
        len(phrase) > index
    ):  # the position of the character itself is less than the phrase length
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count
