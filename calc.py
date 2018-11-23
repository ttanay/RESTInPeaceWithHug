"""Simple functions to emulate basic operations of a calculator"""


def add(x: int, y: int) -> int:
    """Add two numbers"""
    return x + y


def subtract(x: int, y: int) -> int:
    """Subtract two numbers"""
    return x - y


def multiply(x: int, y: int) -> int:
    """Multiply two numbers"""
    return x * y


def divide(x: int, y: int) -> int:
    """Divide two numbers"""
    return x / y


if __name__ == '__main__':
    print(add(1, 2))