'''
Sample test
'''

from django.test import SimpleTestCase

from . import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """test adding num togeter"""
        res = calc.add(5,6)

        self.assertEqual(res,11)

    def test_subtract_numbers(self):
        """test substracting number"""

        res = calc.subtract(6,2)

        self.assertEqual(res,4)