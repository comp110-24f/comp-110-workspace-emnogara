"""Planning a Tea Party."""

__author__: str = "730670853"


def main_planner(guests: int) -> None:
    """Entry point of the program."""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # Spaces were added between letters
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # I converted tea bags to a string
    print("Treats: " + str(treats(people=guests)))  # I converted treats to a string
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # Tea count and treat count depend on tea bags and treats


def tea_bags(people: int) -> int:
    """Number of tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
