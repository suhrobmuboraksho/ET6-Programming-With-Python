def mystery_8(a, b):
    """Filters a list of strings to include only those, that contain a specific substring.

    Parameters:
        a (list of strings): A list to search through
        b (string): The substring to search for

    Returns:
        list of strings: A list of strings from "a", that contain the substring "b".
        
        >>> mystery_8(["dog", "cat", "bird", "fish"], "i")
        ['bird', 'fish']

        >>> mystery_8(["tree", "bush", "flower"], "ee")
        ['tree']

        >>> mystery_8(["car", "cart", "cartoon"], "car")
        ['car', 'cart', 'cartoon']

        >>> mystery_8(["single"], "s")
        ['single']
    
        >>> mystery_8(["red", "green", "blue"], "yellow")
        []

        >>> mystery_8([], "any")
        []
    """
    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c
