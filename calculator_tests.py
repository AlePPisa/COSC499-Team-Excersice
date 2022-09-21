import unittest
from calculator import *

class CalculatorTests(unittest.TestCase):
    # This is a default method
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
    
    def test_addcase(self):
        test = addition(1, 2)
        expected = 3
        self.assertEqual(test, expected)

if __name__ == '__main__':
    unittest.main()
