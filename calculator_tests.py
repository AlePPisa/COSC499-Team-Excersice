import unittest
import numpy as np
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

    # Tests for subtraction functionality
    def test_subtraction(self):
        # Two positives
        self.assertEqual(0, calculator.subtraction(1, 1))

        # Two negatives
        self.assertEqual(-2, calculator.subtraction(-4, -2))

        # One of each
        self.assertEqual(-6, calculator.subtraction(-4, 2))

        # The Other Way
        self.assertEqual(6, calculator.subtraction(4, -2))

        # Exceptions
        with self.assertRaises(Exception):
            calculator.division("a", 9)

    def test_multiply(self):
        nums = np.array([[1, 1], [2, 2], [10, 10], [50, 50], [
                        1000, 1000], [-365, 256], [-420, -69], [99, -1], [17, 38], [600, 66]])
        ans = [1*1, 2*2, 10*10, 50*50, 1000*1000, -
               365*256, -420*-69, 99*-1, 17*38, 600*66]

        testAns = []
        for i in range(0, len(nums)):
            num1 = nums[i][0]
            num2 = nums[i][1]
            testAns.append(calculator.multiply(num1, num2))
        self.assertEqual(ans, testAns)


if __name__ == '__main__':
    unittest.main()
