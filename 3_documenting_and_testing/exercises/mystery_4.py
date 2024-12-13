#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 12 12 24
@author: Sukhrob Muborakshoev

This module contains utility function, for generating sequential list up to a specified number.

- `mystery_4(a)`: Returns a list starting from 0 up to provided integer as an input.
"""
def mystery_4(a: int) -> list:
    """
    Returns a list of integers starting from 0 up to a specified length.

    Parameters:
        a (int): The length of the list. Must be a non-negative integer.

    Returns:
        list: A list of integers starting from 0 up to (a-1), with a total length of `a`.

        >>> mystery_4(0)
        []

        >>> mystery_4(5)
        [0, 1, 2, 3, 4]

        >>> mystery_4(10)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
