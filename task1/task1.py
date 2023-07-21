import re
from functools import reduce


def find_digits(string: str) -> list:
    """Function that looks for combinations of
    four or more digits and returns a list of combinations"""

    pattern = r"\d+"
    digits = re.findall(pattern, string)
    digits_combinations = [comb for comb in digits if len(comb) >= 4]

    return digits_combinations


def find_combinations_of_four_digits(digits_combinations: list) -> list:
    """Function that looks for combinations of exactly
    four digits in given list and returns a list of combinations"""

    combinations_of_four_digits = []

    for item in digits_combinations:
        for i in range(len(item)):
            comb = item[i:i + 4]
            if len(comb) == 4:
                combinations_of_four_digits.append(comb)

    return combinations_of_four_digits


def find_max_multiplications(filtered_combinations: list) -> int:
    """Function that multiply all digit in each
    4-digits combination and find the maximum"""

    max_mul = max(
        [
            reduce(lambda x, y: int(x) * int(y), combination)
            for combination in filtered_combinations
        ]
    )
    return max_mul


def max_multiplications(string: str) -> int | str:
    """Function that look for combination of four digits
    in a string and returns the max multiplication.
    If object is not a string or there are no
    combinations found - return Nil."""

    if not isinstance(string, str):
        return "Nil"

    digits_combinations = find_digits(string)

    if not digits_combinations:
        return "Nil"

    filtered_combinations = find_combinations_of_four_digits(digits_combinations)  # noqa E203

    result = find_max_multiplications(filtered_combinations)

    return result
