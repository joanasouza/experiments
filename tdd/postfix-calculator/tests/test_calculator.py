import unittest 
from calculator import postfix_calc  

class CalculatorTest(unittest.TestCase):

    def test_simple_expression(self):
        self.assertEqual(1, postfix_calc('1'))
        self.assertEqual(2, postfix_calc('2'))
        self.assertEqual(3, postfix_calc('3'))
        self.assertEqual(4, postfix_calc('4'))


    def test_simple_sum(self):
        self.assertEqual(2, postfix_calc('1 1 +'))
        self.assertEqual(3, postfix_calc('1 2 +'))
        self.assertEqual(9, postfix_calc('2 2 5 + +'))
        self.assertEqual(9, postfix_calc('2 2 + 5 +'))

    def test_complex_sum(self):
        self.assertEqual(8, postfix_calc('1 1 1 + 2 3 + + +'))

       # 1 2 2
       # add more tests to complex sum
