"""Functions Challenge Question"""

__author__ = "730670853"


def mimic(message: str) -> str:
    """Write a message back to me."""
    return message


def main() -> None:
    """Pulling together all the functions into one."""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
