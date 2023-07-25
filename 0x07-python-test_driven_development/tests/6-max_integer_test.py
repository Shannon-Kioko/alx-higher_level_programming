#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_normal_list(self):
        """Test max_integer with a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element_list(self):
        """Test max_integer with a list containing a single element"""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-42]), -42)

    def test_max_integer_float_list(self):
        """Test max_integer with a list containing floating-point numbers"""
        self.assertEqual(max_integer([1.5, 2.8, 3.2, 4.7]), 4.7)
        self.assertEqual(max_integer([-1.5, -2.8, -3.2, -4.7]), -1.5)

    def test_max_integer_mixed_list(self):
        """Test max_integer with a list containing mixed data types"""
        self.assertEqual(max_integer([1, 2, 3, "4", 5]), 5)
        self.assertEqual(max_integer([1, 2, "3", 4, 5]), "5")

if __name__ == '__main__':
    unittest.main()
