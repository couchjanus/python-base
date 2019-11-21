import unittest
import mathc.mathc as m

class MathcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(m.add(1, 2), 3)
        
    def test_sub(self):
        self.assertEqual(m.sub(4, 2), 2)
        
    def test_mul(self):
        self.assertEqual(m.mul(2, 5), 10)
        
    def test_div(self):
        self.assertEqual(m.div(8, 4), 2)
        
if __name__ == '__main__':
    unittest.main()
