import unittest
import calculator
from calculator import *


class CalculatorTests(unittest.TestCase):
    # Tests for addition functionality
    def test_division(self):
        # Two positives
        self.assertEqual(1, calculator.division(1, 1))

        # Two negatives
        self.assertEqual(2, calculator.division(-4, -2))

        # One of each
        self.assertEqual(-2, calculator.division(-4, 2))

        # Float number
        self.assertEqual(0.5, calculator.division(1, 2))

        # Exceptions
        with self.assertRaises(Exception):
            calculator.division("a", 9)

        with self.assertRaises(Exception):
            calculator.division(4, 0)
            
            
    def test_addcase(self):
        test = calculator.addition(1, 2)
        expected = 3
        self.assertEqual(test, expected)


if __name__ == '__main__':
    unittest.main()
