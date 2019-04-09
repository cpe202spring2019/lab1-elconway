import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!

    def test_equality(self):
        loc1 = location.Location("SLO", 35.3, -120.7)
        loc2 = location.Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1, loc2)

    def test_lat_diff(self):
        loc1 = location.Location("SLO", 35.3, -120.7)
        loc3 = location.Location("SLO", 35.4, -120.7)
        self.assertNotEqual(loc1, loc3)
    
    def test_lon_diff(self):
        loc1 = location.Location("SLO", 35.3, -120.7)
        loc4 = location.Location("SLO", 35.3, -120.8)
        self.assertNotEqual(loc1, loc4)

    def test_name_diff(self):
        loc1 = location.Location("SLO", 35.3, -120.7)
        loc5 = location.Location("SLOB", 35.3, -120.7)
        self.assertNotEqual(loc1, loc5)

if __name__ == "__main__":
        unittest.main()
