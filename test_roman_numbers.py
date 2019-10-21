import unittest
from roman_numbers import roman_to_decimal


class TestRomanNumbers(unittest.TestCase):
    def test_I(self):
        decimal = roman_to_decimal("I")
        self.assertEqual(decimal, 1)


if __name__ == '__main__':
    unittest.main()
