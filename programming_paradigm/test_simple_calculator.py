# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """ Unit tests for the SimpleCalculator class. """

    def setUp(self):
        """ Create a SimpleCalculator instance before each test. """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """ Test the add() method. """
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-5, 5), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """ Test the subtract() method. """
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-2, -2), 0)

    def test_multiply(self):
        """ Test the multiply() method. """
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 99), 0)

    def test_divide(self):
        """ Test the divide() method. """
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        # Edge case: dividing by zero
        self.assertIsNone(self.calc.divide(10, 0))


if __name__ == "__main__":
    unittest.main()
