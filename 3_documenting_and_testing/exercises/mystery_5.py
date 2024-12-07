def mystery_5(a, b=None):
    """Sorts a list in an ascending order and appends the sorted elements to a new list.

    Parameters:
        a (list): List of values for sorting.
        b (list, optional): Optional list to accumulate sorted elements. Empty list by default.

    Returns:
        list: A list containing the elements of "a" list in an ascending order.
        
        >>> mystery_5([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
        
        >>> mystery_5([8, 12, 6, 11, 14])
        [6, 8, 11, 12, 14]

        >>> mystery_5([7, 3, 9], [2])
        [2, 3, 7, 9]

        >>> mystery_5([])
        []
    """
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
