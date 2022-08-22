import unittest
from Rank import *


class TestRank(unittest.TestCase):

    def setUp(self):
        pass
    
    
    def test_constructor(self):
        r1 = Rank("4")
        self.assertEqual(r1._rank, "4")
            
        
    def test_contrsuctor_invalid(self):
        with self.assertRaises(ValueError):
            p1 = Rank('R')
            
    def test_valid_rank(self):
        p2 = Rank('Q')
        if p2._rank not in ranks:
            self.assertRaise(ValueError)
            
#     def test_invalid_rank(self):
#         p3 = Rank('T')
#         if p3._rank not in ranks:
#             self.assertRaises(ValueError)
            
            
    def test__gt__true(self):
        r2 = Rank("K")
        r3 = Rank("8")
        self.assertTrue(r2 > r3)
        
        
    def test__lt__true(self):
        r4 = Rank("4")
        r5 = Rank("Q")
        self.assertTrue(r4.__lt__(r5))
        
        
    def test__eq__true(self):
        r6 = Rank("10")
        r7 = Rank("10")
        self.assertEqual(r6, r7)
        
        
    def test__gt__false(self):
        r8 = Rank("K")
        r9 = Rank("8")
        self.assertFalse(r9 > r8)
        
    def test__lt__false(self):
        r10 = Rank("4")
        r11 = Rank("Q")
        self.assertFalse(r11 < r10)
        
    def test__eq__false(self):
        r12 = Rank("6")
        r13 = Rank("A")
        self.assertFalse(r12 == r13)
    

if __name__ == '__main__':
    unittest.main()