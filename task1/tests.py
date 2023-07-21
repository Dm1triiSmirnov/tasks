import pytest

from .task1 import max_multiplications


@pytest.mark.parametrize(
    "string, expected",
    [
        ("2345sdlfsnf765765767skn123,jbkjb9999", 6561),
        ("asjhda12 sdjk788kk*^%%090", "Nil"),
        ("", "Nil"),
        ("123kjbkj  987987msnxb7457", 980),
        ([], "Nil"),
        (None, "Nil"),
    ],
)
def test_max_multiplications(string, expected):
    assert max_multiplications(string) == expected
