import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Checks to make sure that max_list_iter is functioning correctly"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(max_list_iter([8, 3, 6, 5, 1, 9, 10, 2, 4, 7]), 10)

    def test_reverse_rec(self):
        """Checks to make sure that reverse_rec is functioning correctly"""
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([2, 5, 8, 11]), [11, 8, 5, 2])

    def test_bin_search(self):
        """Checks to make sure that bin_search is functioning correctly"""
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, tlist)
        self.assertEqual(bin_search(6, 0, 0, []), None)
        list_val =[0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4 )
        self.assertEqual(bin_search(6, 0, len(list_val) - 1, list_val), None)

if __name__ == "__main__":
        unittest.main()

    
