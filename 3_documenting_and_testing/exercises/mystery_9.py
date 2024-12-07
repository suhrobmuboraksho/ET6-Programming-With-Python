def mystery_9(a):
    """Sorts a list of numbers in ascending order using the Bubble Sort algorithm.

    Parameters:
        a (list of int or float): The list of numbers to be sorted.

    Returns:
        list of int or float: The sorted list in ascending order.
        
        >>> mystery_9([5, 3, 8, 4, 2])
        [2, 3, 4, 5, 8]

        >>> mystery_9([10, -1, 0, 3, 2])
        [-1, 0, 2, 3, 10]

        >>> mystery_9([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]

        >>> mystery_9([3])
        [3]
        >>> mystery_9([])
        []
    """
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
