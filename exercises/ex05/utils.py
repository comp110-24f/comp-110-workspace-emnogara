"""Creating list utility functions."""

__author__ = "730670853"


def only_evens(input: list[int]) -> list[int]:
    """Finding only the even numbers in a list"""
    even: list[int] = []
    for elem in input:
        if elem % 2 == 0:  # Akin to saying k(mod2) == 0, where k = even
            even.append(elem)
    return even


def sub(input2: list[int], start: int, end: int) -> list[int]:
    """Returning a subset of a set, denoted input2."""
    if len(input2) == 0 or start >= len(input2):  # Considering two edge cases
        return []
    if start < 0:  # Considering the edge case of negative starting int
        start = 0
    if end > len(input2):  # Considering the edge case of a list exceeding the range
        end = len(input2)
    subset = [input2[numb] for numb in range(start, end)]
    return subset


def add_at_index(input3: list[int], nterm: int, idx: int) -> None:
    """Adding an int to a list at a given index."""
    if idx < 0 or idx > len(input3):
        raise IndexError("Index is out of bounds for the input list.")
    input3.append(0)  # This variable is random and is only meant to increase list size
    for no in range(
        len(input3) - 1, idx, -1
    ):  # Elements (numbers, denoted no) in initial list range remain the same
        input3[no] = input3[no - 1]
    input3[idx] = nterm  # Letting the term at the index equal nterm
