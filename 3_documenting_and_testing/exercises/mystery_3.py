"""
This module contains utility function, that compares two numbers and handles equality with specific behavior.

- `mystery_3(a,b)`: Compares two numbers and returns the smaller number. If the numbers are equal, it returns their sum.
"""

def mystery_3(a: int, b: int) -> int :
    """Compares two numbers and returns the smaller number, or sums them if equal.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The smaller of the two numbers, if they are not equal.
        int or float: The sum of two numbers, if they are equal.
        
        >>> mystery_3(3,5)
        3
        
        >>> mystery_3(44, 31)
        31
        
        >>> mystery_3(15, 15)
        30
    """
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
