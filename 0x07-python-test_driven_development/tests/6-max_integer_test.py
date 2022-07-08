#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """max_integer test cases class"""

    def test_empty_list(self):
        """check that max_integer return's None when list is empty"""
        self.assertIsNone(max_integer([]), None)

    def test_asc_ordered_list(self):
        """Check if return's correct on ascending ordreded list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_desc_ordered_list(self):
        """Check that max_integer return's correct on descending ordred list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unordered_list(self):
        """Check that max_intger return's correct on unordred list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_item_list(self):
        """Check if return's correct when list content a single item"""
        self.assertEqual(max_integer([1]), 1)

    def test_one_negative_number_in_list(self):
        """One negative number in the list"""
        self.assertEqual(max_integer([1,2,3,-3]), 3)

    def test_only_negative_numbers_in_list(self):
        """Only negative numbers in the list"""
        self.assertEqual(max_integer([-2, -1, -5, -4]), -1)

if __name__ == "__main__":
    unittest.main()
