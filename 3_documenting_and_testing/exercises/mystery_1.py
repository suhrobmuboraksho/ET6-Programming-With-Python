#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 12 07 24

@author: Sukhrob Muborakshoev

This module contains utility function for basic mathematical operations.

Currently, it includes:
- `mystery_1`: A function to calculate the sum of two non-negative integers.
"""

def mystery_1(a: int, b: int) -> int:
    """Returns the sum of two numbers.

    Parameters:
        a (int): greater than or equal to 0
        b (int): greater than or equal to 0

    Returns:
        int: returns the sum of integers a and b
        
        >>> mystery_1(0,0)
        0
        
        >>> mystery_1(5,5)
        10
        
        >>> mystery_1(200,1)
        201
        
        >>> mystery_1(35,55)
        90
    """
    return a + b
