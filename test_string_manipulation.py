import unittest

from string_manipulation import string_cap

class TestStringManipulation(unittest.TestCase):
    
    def test_regular_name(self):
        self.assertEquals(string_cap("soham"), "Soham")

    def test_whitespace_separated(self):
        self.assertEquals(string_cap(" soham"), "Soham")

    def test_already_capitalized(self):
        self.assertEquals(string_cap("Soham"), "Soham")


if __name__=='__main__':
    unittest.main()