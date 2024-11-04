"""File to define Fish class."""

__author__ = "730670853"


class Fish:
    """Fish class for river simulation."""

    age: int

    def __init__(self):
        """Initizalizer for fish."""
        self.age = 0

    def one_day(self):
        """Function of one day for fish."""
        self.age += 1
        return None
