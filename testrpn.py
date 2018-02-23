import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_add2(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)
    def test_mult(self):
        result = rpn.calculate('4 3 *')
        self.assertEqual(12, result)
    def test_div(self):
        result = rpn.calculate('21 7 /')
        self.assertEqual(3, result)
    def test_toomany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 2 3 +')

