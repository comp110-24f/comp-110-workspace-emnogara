"""Mutating functions."""

__author__ = "730670853"


def manual_append(set1: list[int], number: int) -> None:
    """Mutating a list by adding a number to the end."""
    set1.append(number)
    return None


def double(set2: list[int]) -> None:
    """Multiplying every list element by 2."""
    index: int = 0
    while index < len(set2):
        set2[index] *= 2
        index += 1
    return None


list_1: list[int] = [1, 2, 3]

list_2: list[int] = list_1

double(list_2)

print(list_1)

print(list_2)
