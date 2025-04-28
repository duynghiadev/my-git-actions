def calculate_sum(x: int, y: int) -> int:
    result = x + y
    if result > 10:
        print(f"result is: {result}")
    return result


class Calculator:
    """A simple calculator class."""

    def __init__(self):
        """Initialize Calculator with default values."""
        """test commit"""
        self.x = 10
        self.y = 20


if __name__ == "__main__":
    calc = Calculator()
    calculate_sum(calc.x, calc.y)
