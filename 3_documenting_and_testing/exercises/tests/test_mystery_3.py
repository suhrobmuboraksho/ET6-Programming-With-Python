import unittest

from ..mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    """Test the mystery_3 function"""

    def test_minimal_input(self):
        """It should return 0"""
        self.assertEqual(mystery_3(0, 0), 0)

    def test_0(self):
        """It should return 3"""
        actual = mystery_3(3, 5)
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should return 31"""
        actual = mystery_3(44, 31)
        expected = 31
        self.assertEqual(actual, expected)
    
    def test_2(self):
        actual = mystery_3(15, 15)
        expected = 30
        self.assertEqual(actual, expected)
