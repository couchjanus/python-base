# test_sum_fr_rais.py
import unittest
# from my_sum import sum
from fractions import Fraction

target = __import__("my_sum")
# sum = target.sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
            Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        # result = sum(data)
        result = target.sum(data)
        self.assertEqual(result, 6)

    # def test_list_fraction(self):
    #     """
    #         Test that it can sum a list of fractions
    #     """
    #     data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
    #     result = target.sum(data)
    #     self.assertEqual(result, 1)

    def test_bad_type(self):
        data = "ababahalamaha"
        with self.assertRaises(TypeError):
            result = target.sum(data)

if __name__ == '__main__':
    unittest.main()