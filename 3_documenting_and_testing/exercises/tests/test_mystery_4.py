import unittest

from ..mystery_4 import mystery_4

class TestMystery4(unittest.TestCase):
    """Test the mystery_4 function"""

    def test_minimal_input(self):
        """It should return empty list"""
        self.assertEqual(mystery_4(0), [])
    
    def test_0(self):
        """It should return [0, 1]"""
        actual = mystery_4(2)
        expected = [0, 1]
        self.assertEqual(actual, expected)
    
    def test_1(self):
        """It should evaluate to [0, 1, 2, 3, 4]"""
        actual = mystery_4(5)
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
        actual = mystery_4(10)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(actual, expected)
