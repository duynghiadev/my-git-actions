"""
Module for demonstrating basic arithmetic operations and class implementation.
"""

def calculate_sum(x: int, y: int) -> int:
    """
    Calculate the sum of two numbers and print if result exceeds 10.

    Args:
        x (int): First number
        y (int): Second number

    Returns:
        int: Sum of x and y
    """
    result = x + y
    if result > 10:
        print(f'result is: {result}')
    return result


class Calculator:
    """A simple calculator class."""

    def __init__(self):
        """Initialize Calculator with default values."""
        self.x = 10
        self.y = 20


# Remove unused imports and undefined variable reference
if __name__ == "__main__":
    calc = Calculator()
    calculate_sum(calc.x, calc.y)