# Importing the unittest module to write test cases for the StringCalculator class.
import unittest

# Importing the StringCalculator class from the module.
from StringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    # Test for an empty string input, expecting a sum of 0.
    def test_empty_string(self):
        self.assertEqual(StringCalculator.add(""), 0)

    # Test for a single number as input, expecting the number itself as the sum.
    def test_single_number(self):
        self.assertEqual(StringCalculator.add("1"), 1)

    # Test for two comma-separated numbers, expecting their sum.
    def test_two_numbers(self):
        self.assertEqual(StringCalculator.add("1,5"), 6)
        
    # Test for multiple comma-separated numbers, expecting their sum.
    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator.add("1,2,3,4"), 10)
        
    # Test for numbers separated by new lines and commas, expecting their sum.
    def test_new_lines_between_numbers(self):
        self.assertEqual(StringCalculator.add("1\n2,3"), 6)

# Entry point for running the tests.
if __name__ == "__main__":
    unittest.main()
