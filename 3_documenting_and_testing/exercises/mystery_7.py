def mystery_7(a, b):
    """Filters through a list of strings, to return only those that contain a specific substring.

    Parameters:
        a (list of strings): A list of strings to search through
        b (string): The substring to look for within each string in "a".

    Returns:
        list of strings: A list of strings from "a", that contain the substring "b".
        
        >>> mystery_7(["apple", "banana", "cherry"], "a")
        ['apple', 'banana']

        >>> mystery_7(["hello", "world", "python"], "o")
        ['hello', 'world', 'python']

        >>> mystery_7(["test", "case", "example"], "z")
        []

        >>> mystery_7(["cat", "bat", "rat"], "at")
        ['cat', 'bat', 'rat']
    """
    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c
