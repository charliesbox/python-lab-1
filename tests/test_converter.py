import pytest
from toolkit.converter import convert


@pytest.mark.parametrize("value, unit_from, unit_to, expected", [
    ("1", "km", "cm", "100000.0"),
    ("1000", "g", "kg", "1.0"),
    ("100", "c", "f", "212.0"),
    ("1", "KM", "M", "1000.0"),  # регистр не важен
])
def test_convert_positive(value, unit_from, unit_to, expected):
    assert convert(value, unit_from, unit_to) == expected


@pytest.mark.parametrize("value, unit_from, unit_to", [
    ("1", "xyz", "cm"),
    ("1", "km", "kg"),
    ("abc", "km", "m"),
    ("-300", "c", "k"),
])

def test_convert_negative(value, unit_from, unit_to):
    with pytest.raises(ValueError):
        convert(value, unit_from, unit_to)
