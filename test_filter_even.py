import unittest
from filter_even_numbers import filter_even_numbers_fn

class TestFilterEvenNumbersWorking(unittest.TestCase):

    def test_case_all_even(self):
        self.assertEqual(filter_even_numbers_fn([2, 4, 6]), [2, 4, 6])
    def test_case_all_odd(self):
        self.assertEquals(filter_even_numbers_fn([1,3,5,7]), [])
    def test_case_mixed(self):
        self.assertEquals(filter_even_numbers_fn([1,2,3,4,5,6]), [2,4,6])

if __name__=="__main__":
    unittest.main()