def sort_array(arr: list) -> list | str:
    """Function to sort array of numbers by
    amount of 1 in its binary representation.
    Numbers with identical amount of 1
    ordered by decimal representation."""

    if not isinstance(arr, list):
        return "Function accepting only list"

    result = sorted(arr, key=lambda num: (bin(num).count("1"), num))

    return result
