"""Unit tests for natural number to binary converter."""

import pytest

from binary_converter import natural_to_binary


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (5, "101"),
        (10, "1010"),
        (64, "1000000"),
        (100, "1100100"),
    ],
)
def test_natural_to_binary_returns_correct_binary_number(number, expected):
    """Check correct conversion for numbers from the allowed range."""
    assert natural_to_binary(number) == expected


@pytest.mark.parametrize("number", [-1, 101, 150])
def test_natural_to_binary_raises_value_error_for_number_outside_range(number):
    """Check that numbers outside 0-100 are rejected."""
    with pytest.raises(ValueError):
        natural_to_binary(number)


@pytest.mark.parametrize("number", [1.5, 2.0, "5", None, True])
def test_natural_to_binary_raises_type_error_for_non_natural_number(number):
    """Check that values with decimal part or non-integers are rejected."""
    with pytest.raises(TypeError):
        natural_to_binary(number)
