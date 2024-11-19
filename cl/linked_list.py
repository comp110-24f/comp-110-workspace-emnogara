"""Creating a Node Class and Sum Function."""

__author__ = "730670853"


class Node:
    """Creating the Node Class."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next
