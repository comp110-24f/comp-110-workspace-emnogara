"""Working with Utility Functions."""

__author__ = "730670853"


def all(list1: list[int], number: int) -> bool:
    """Seeing if all list entries equal a certain number."""
    if len(list1) == 0:
        return False
    index: int = 0
    while index < len(list1):
        if list1[index] != number:
            return False
        index += 1
    return True  # If every list entry is equal to the number


def max(input: list[int]) -> int:
    """Finding the largest number of the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    maxnumb: int = input[0]
    while idx < len(input):
        if input[idx] > maxnumb:
            maxnumb = input[idx]  # Letting the next number in the list be the new max
        idx += 1
    return maxnumb


def is_equal(intlist1: list[int], intlist2: list[int]) -> bool:
    """If the 2 list entries are exactly the same at every index."""
    indx: int = 0
    while indx < len(intlist1) and indx < len(
        intlist2
    ):  # Both list lengths need to be > indx
        if intlist1[indx] != intlist2[indx]:
            return False
        indx += 1
    if indx < len(intlist1) or indx < len(intlist2):  # To account for index errors
        return False
    return True


def extend(listint1: list[int], listint2: list[int]) -> None:
    """Adding listint2 to the end of listint1."""
    i: int = 0
    while i < len(listint2):  # Making sure every index of the second list is hit
        listint1.append(listint2[i])
        i += 1
