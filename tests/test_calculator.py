import pytest
from toolkit.calculator import evaluate


@pytest.mark.parametrize("expression, expected", [
    ("2 + 3 * 4", 14),
    ("(2 + 3) * 4", 20),
    ("-4 + 2", -2),
    ("7 - (-3)", 10),
    ("1.5 + 2.5", pytest.approx(4.0)),
])
def test_evaluate_positive(expression, expected):
    assert evaluate(expression) == expected


@pytest.mark.parametrize("expression", [
    "",
    "2 & 3",
    "2 + ",
    "2 + * 3",
    "5 / 0",
    "(2 + 3",
])

def test_evaluate_negative(expression):
    with pytest.raises(ValueError):
        evaluate(expression)
