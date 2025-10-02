import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
      

    def test_subtraction(self):
        """Test the subtract method"""
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(4, 6), -2)

    def test_multiply(self):
        """Test the multiply method"""
        self.assertEqual(self.calc.multiply(1, 0), 0)
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(-5, 5), -25)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

    def test_divide(self):
        """Test the divide method"""
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(4, -2), -2)
        self.assertEqual(self.calc.divide(-4, -2), 2)
        self.assertIsNone(self.calc.divide(4, 0))
        


if __name__ == "__main__":
    unittest.main()