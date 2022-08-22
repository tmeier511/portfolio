import unittest
from Card import *


class TestCard(unittest.TestCase):
    
    def setUp(self):
        pass
     
    def test_constructor_card(self):
        a1 = Card("4", "diamonds")
        self.assertEqual(a1.value, Rank("4"))
        
    def test_constructor_invalid(self):
        with self.assertRaises(ValueError):
            b1 = Card("0", "hearts")
        with self.assertRaises(ValueError):
            b2= Card("4", "joker")
            
    def test__str__(self):
        c1 = Card("5", "hearts")
        self.assertEqual(str(c1), "5 of hearts")
            
        
    
        
if __name__ == '__main__':
    unittest.main()