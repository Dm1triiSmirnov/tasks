import pytest

from .task1 import max_multiplications


@pytest.mark.parametrize(
    "string, expected",
    [
        ("abc12345def", 120),
        ("2345sdlfsnf765765767skn123,jbkjb999", 1470),
        ("asjhda12 sdjk788kk*^%%090", "Nil"),
        ("", "Nil"),
        ([], "Nil"),
        (None, "Nil"),
    ],
)
def test_max_multiplications(string, expected):
    assert max_multiplications(string) == expected
