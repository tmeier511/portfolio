import unittest
from Deck import *

class TestDeck(unittest.TestCase):
    
    def setUp(self):
        pass

    
    def test_constructor(self):
        d1 = Deck()
        self.assertEqual(len(d1.cards), 52, True)
        

    def test_deal(self):
        d2 = Deck()
        print(d2.deal())
        
    
    def test__repr__(self):
        d3 = Deck()
        d4 = Deck()
        self.assertEqual(d3.__repr__(), d4.__repr__())
        


if __name__ == '__main__':
    unittest.main()