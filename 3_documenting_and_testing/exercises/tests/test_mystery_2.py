#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created on 12 09 24
    
    @author: Sukhrob Muborakshoev
"""
import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """Test the mystery_2 function"""
    
    def test_0(self):
        """It should evaluate to 5"""
        actual = mystery_2("hello")
        expected = 5
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should evaluate to 6"""
        actual = mystery_2("Python")
        expected = 6
        self.assertEqual(actual, expected)
        
    def test_2(self):
        """It should evaluate to 3"""
        actual = mystery_2("MIT")
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_3(self):
        """It should evaluate to None"""
        actual = mystery_2("")
        expected = None
        self.assertEqual(actual, expected)
