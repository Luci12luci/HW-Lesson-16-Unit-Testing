import unittest
from main import IntegerSet


class TestIntegerSet(unittest.TestCase):
        def test_add_sum_elements(self):
         s = IntegerSet()
         self.assertEqual(s.sum_elements(1, 2), 3)


        def test_add_arithmetic_mean(self):
         s = IntegerSet()
         self.assertAlmostEqual(s.arithmetic_mean(), 3.0)


        def test_add_minimum_element(self):
         s = IntegerSet()
         self.assertEqual(s.minimum_element(), 3)


if __name__ == '__main__':
    unittest.main()


