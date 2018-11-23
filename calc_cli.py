"""Simple functions to emulate basic operations of a calculator
with a CLI Interface
"""
import hug

# Types
@hug.type(extend=hug.types.number)
def not_zero(value):
    """Accept any value of number type except 0"""
    if value is 0:
        raise ValueError('Value cannot be 0')
    else:
        return value

# Operations
# simple example
@hug.cli()
def add(x: int, y: int) -> int:
    """Add two numbers"""
    return x + y


# Hug respects type hints
@hug.cli()
def subtract(x: int, y: int) -> float:
    """Subtract two numbers"""
    return x - y


# Hug's built-in types
@hug.cli()
def multiply(x: hug.types.number, y: hug.types.number) -> hug.types.number:
    """Multiply two numbers"""
    return x * y


# Custom type
@hug.cli()
def divide(x: hug.types.number, y: not_zero) -> hug.types.number:
    """Divide two numbers"""
    return x / y


if __name__ == '__main__':
    print(subtract(1, 2))
