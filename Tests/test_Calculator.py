import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_access_difference_result(self):
        self.calculator.Difference(1, 2)
        self.assertEqual(-1, self.calculator.Result)

    def test_calculator_access_product_result(self):
        self.calculator.Product(1, 2)
        self.assertEqual(2, self.calculator.Result)

    def test_calculator_access_quotient_result(self):
        self.calculator.Quotient(4, 2)
        self.assertEqual(2, self.calculator.Result)

    def test_calculator_access_power_result(self):
        self.calculator.Power(4, 2)
        self.assertEqual(16, self.calculator.Result)

    def test_calculator_access_root_result(self):
        self.calculator.Root(9, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_access_log_result(self):
        self.calculator.Log(2, 8)
        self.assertEqual(3, self.calculator.Result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)


if __name__ == '__main__':
    unittest.main()
