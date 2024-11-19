"""Creating a node class and related functions."""

from __future__ import annotations

__author__ = "730670853"


class Node:
    """Creating the Node class."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initializing the Node class."""
        self.value = val
        if next is None:
            self.next = None
        else:
            self.next = next


def value_at(head: Node | None, index: int) -> int:
    """Returns value of node at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:  # Node Value at First Index.
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Finds the maximum of a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:  # If there are no other values left in the list.
        return head.value
    return max(head.next)


def linkify(items: list[int]) -> Node | None:
    """Creates a linked list from a list of integers."""
    if len(items) == 0:
        return None
    head = Node(items[0], None)  # Creating a new node for the linked list.
    head.next = linkify(items[1:])
    return head


def scale(head: Node | None, factor: int) -> None:
    """Scalar multiplication for a linked list."""
    if head is None:
        return None
    head.value *= factor  # Multiplying each node value by a scalar.
    scale(head.next, factor)
    return None
