import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Tests for add method
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 6), 9)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -5), -7)

    # Tests for subtract method
    def test_subtract_positive_numbers(self):
        # Expected result: -5, because 5 - 10 is -5
        self.assertEqual(self.calc.subtract(5, 9), -4)


    def test_subtract_with_negative_result(self):
    # Expected result: 5, because 10 - 5 = 5
        self.assertEqual(self.calc.subtract(10, 4), 6)


    # Tests for multiply method
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_multiply_negative_number(self):
        self.assertEqual(self.calc.multiply(-2, 4), -8)

    # Tests for divide method
    def test_divide_whole_number(self):
        self.assertEqual(self.calc.divide(12, 2), 6)

    def test_divide_with_remainder(self):
        self.assertEqual(self.calc.divide(10, 3), 3)  # Integer division expected

    def test_divide_by_larger_number(self):
        self.assertEqual(self.calc.divide(2, 10), 0)

    # Tests for modulo method
    def test_modulo_when_a_is_greater(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_when_a_is_equal(self):
        self.assertEqual(self.calc.modulo(5, 5), 0)

    def test_modulo_when_a_is_smaller(self):
        self.assertEqual(self.calc.modulo(2, 3), 2)

if __name__ == '__main__':
    unittest.main()