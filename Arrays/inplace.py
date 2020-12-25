"""pretty standard. instead of importing floor to calculate each one
use a double pointer method and exit when left points exceeds the right"""
""" o(1) space. o(n/2)=o(n) time"""


import math
import unittest
#listof Char -> listof Char
def reverse(lst):
    for i in range (0, math.floor((len(lst)/2))):
        char1 = lst[i]
        lst[i]=lst[-i-1]
        lst[-i-1]=char1

    return lst


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)