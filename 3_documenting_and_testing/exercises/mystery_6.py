def mystery_6(a, b):
    """Generates and returns a list of sequential integers starting from a given number.

    Parameters:
        a (int): The number of elements to generate. Must not be negative.
        b (int): The starting number for the sequence.

    Returns:
        list: A list of "a" integers starting from "b"
        
        >>> mystery_6(3, 10)
        [10, 11, 12]

        >>> mystery_6(5, 0)
        [0, 1, 2, 3, 4]
        
        >>> mystery_6(0, 5)
        []
    """
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
