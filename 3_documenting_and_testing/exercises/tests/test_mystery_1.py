#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created on 12 09 24
    
    @author: Sukhrob Muborakshoev
"""

import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """Test the mystery_1 function"""
    def test_0(self):
        """It should evaluate to 0"""
        actual = mystery_1(0, 0)
        expected = 0
        self.assertEqual(actual,expected)
        
    def test_1(self):
        """It should evaluate to 10"""
        actual = mystery_1(5,5)
        expected = 10
        self.assertEqual(actual, expected)
    
    def test_2(self):
        """It should evaluate to 201"""
        actual = mystery_1(200, 1)
        expected = 201
        self.assertEqual(actual, expected)
    
    def test_3(self):
        """It should evaluate to 90"""
        actual = mystery_1(35, 55)
        expected = 90
        self.assertEqual(actual, expected)
