from collections.abc import Sequence


def average(numbers: Sequence[float]) -> float:
    if not numbers:
        raise ValueError("numbers must not be empty")

    return sum(numbers) / len(numbers)