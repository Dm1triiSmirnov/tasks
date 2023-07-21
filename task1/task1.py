import re
from functools import reduce


def find_digits(string: str) -> list:
    """Function that looks for combinations of exactly
    four digits and returns a list of combinations"""

    pattern = r"\d+"
    digits = re.findall(pattern, string)
    filtered_combinations = [comb for comb in digits if len(comb) == 4]

    return filtered_combinations


def max_multiplications(string: str) -> int | str:
    """Function that gives a combination of four digits
    in a string and returns the max multiplication.
    If object is not a string or there are no
    combinations found - return Nil."""

    if not isinstance(string, str):
        return "Nil"

    combinations = find_digits(string)

    if not combinations:
        return "Nil"

    result = max(
        [
            reduce(lambda x, y: int(x) * int(y), combination)
            for combination in combinations
        ]
    )

    return result
