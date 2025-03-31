import unittest
from roman_to_decimal import roman_to_decimal

class TestRomanToDecimal(unittest.TestCase):

    def test_single_characters(self):
        self.assertEqual(roman_to_decimal('I'), 1)
        self.assertEqual(roman_to_decimal('V'), 5)
        self.assertEqual(roman_to_decimal('X'), 10)
        self.assertEqual(roman_to_decimal('L'), 50)
        self.assertEqual(roman_to_decimal('C'), 100)
        self.assertEqual(roman_to_decimal('D'), 500)
        self.assertEqual(roman_to_decimal('M'), 1000)

    def test_basic_combinations(self):
        self.assertEqual(roman_to_decimal('III'), 3)
        self.assertEqual(roman_to_decimal('IV'), 4)
        self.assertEqual(roman_to_decimal('IX'), 9)
        self.assertEqual(roman_to_decimal('LVIII'), 58)
        self.assertEqual(roman_to_decimal('XC'), 90)

    def test_large_numbers(self):
        self.assertEqual(roman_to_decimal('MCMXCIV'), 1994)
        self.assertEqual(roman_to_decimal('MMXXIV'), 2024)
        self.assertEqual(roman_to_decimal('MMMCMXCIX'), 3999)

    def test_case_insensitivity(self):
        self.assertEqual(roman_to_decimal('mcmxciv'), 1994)
        self.assertEqual(roman_to_decimal('MmXxIi'), 2022)

    def test_invalid_characters(self):
        self.assertEqual(roman_to_decimal('ABCD'), 600)  # Only D has a valid value

    def test_empty_string(self):
        self.assertEqual(roman_to_decimal(''), 0)

if __name__ == '__main__':
    unittest.main()

