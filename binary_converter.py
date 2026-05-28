"""Utilities for converting natural numbers to binary notation."""


def natural_to_binary(number: int) -> str:
    """Convert a natural number from the range 0-100 to binary notation.
    """
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Number must be a natural integer.")

    if number < 0 or number > 100:
        raise ValueError("Number must be in range from 0 to 100.")

    return bin(number)[2:]
