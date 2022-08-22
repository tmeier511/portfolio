import unittest
from Suit import *

class TestSuit(unittest.TestCase):
    
    def setUp(self):
        pass
    
    
    def test_constructor(self):
        s1 = Suit("spades")
        
    
    def test_constructor_invalid(self):
        with self.assertRaises(ValueError):
            s2 = Suit("Clover")


    def test__str__(self):
        s3 = Suit("clubs")
        print(s3._suit)
        

if __name__ == '__main__':
    unittest.main()