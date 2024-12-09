#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 12 07 24

@author: Sukhrob Muborakshoev

This module contains utility function for working with string.

- `mystery_2`: A function to calculate length of a string if it's not empty and None if empty.
"""

def mystery_2(a: str) -> int | None :
    """Returns the length of the string if it is non-empty and returns None if empty.

    Parameters:
        a (string): The input string

    Returns:
        int: The length of the string.
        None: If the string is empty.
        
    >>> mystery_2("hello")
    5
    
    >>> mystery_2("Python")
    6
    
    >>> mystery_2("MIT")
    3
    
    >>> mystery_2("")
    
    """ 
    if len(a) == 0:
        return None

    return len(a)
