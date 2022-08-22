import unittest
from Player import *

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        pass
    
    
    def test_constructor(self):
        p1 = Player()
        self.assertEqual(p1.wins, 0)
        self.assertEqual(p1.name, '')
        
        
    def test_constructor_valid(self):
        p2 = Player('Tim')
        self.assertEqual(p2.name, 'Tim')
        p2.wins = p2.wins + 1
        self.assertEqual(p2.wins, 1)
        
        
    def test_constructor_invalid(self):
        p3 = Player()
        name = 3
        with self.assertRaises(TypeError):
            p3.name = name
            
            
    def test__str__(self):
        p4 = Player()
        self.assertEqual(str(p4.wins), str(p4))
        
    
if __name__ == '__main__':
    unittest.main()