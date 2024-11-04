"""File to define River class."""

__author__ = "730670853"


from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class for river simulation."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of animals to see who survives."""
        surviving_fish: list[Fish] = (
            []
        )  # creating two new lists to store the fish/bears
        surviving_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)  # adding fish to the new list
        for bears in self.bears:
            if bears.age <= 5:
                surviving_bears.append(bears)  # adding bears to the new list
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def remove_fish(self, amount: int):
        """Removing old fish."""
        if amount > len(
            self.fish
        ):  # adding a check in place to make sure there is enough fish
            amount = len(self.fish)
        for i in range(amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Bears eat fish in the simulation."""
        for bear in self.bears:
            if len(self.fish) >= 5:  # if there is enough fish, the bear will eat 3
                River.remove_fish(self, amount=3)
                bear.eat(num_fish=3)
        return None

    def check_hunger(self):
        """Checking the bears hunger levels."""
        satiated_bears: list[Bear] = []  # new list for all of the surviving bears
        for bears in self.bears:
            if bears.hunger_score >= 0:
                satiated_bears.append(bears)  # adding surviving bears to new list
        self.bears = satiated_bears
        return None

    def repopulate_fish(self):
        """Accounting for fish reproduction."""
        fish_offspring: int = (
            (len(self.fish) // 2)
        ) * 4  # creating a variable for the fish offspring
        for fish in range(fish_offspring):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Accounting for bear reproduction."""
        bear_offspring: int = (
            len(self.bears) // 2
        )  # creating a variable for the bear offspring
        for bears in range(bear_offspring):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Looking at the river for a given day."""
        x: int = self.day  # creating x, y, z to use in the printed statements
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of the river."""
        for idx in range(7):
            self.one_river_day()
        return None
