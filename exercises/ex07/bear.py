"""File to define Bear class."""

__author__ = "730670853"


class Bear:
    """Class bear for river simulation."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializer for bear."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """One day function for bear."""
        self.age += 1  # age increases by 1 and hunger decreases by 1 every day
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bear is eating to decrease hunger score."""
        self.hunger_score += num_fish
        return None
