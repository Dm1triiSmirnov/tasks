import pytest

from .task2 import sort_array


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 7, 8, 9], [8, 3, 9, 7]),
        ([9, 7, 8, 3], [8, 3, 9, 7]),
        ([], []),
        ("abc", "Function accepting only list"),
    ],
)
def test_sort_array(arr, expected):
    assert sort_array(arr) == expected
