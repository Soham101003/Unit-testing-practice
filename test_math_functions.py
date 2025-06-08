import unittest
from math_functions import add

class TestMathFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEquals(add(2,3), 5)
    def test_add_negative_numbers(self):
        self.assertEquals(add(-1,-2),-3)

    def test_add_mixed_numbers(self):
        self.assertEquals(add(-1,2), 1)
    #def test_intentionally_fail(self):
        #self.assertEquals(add(2,2), 6)


if __name__=='__main__':
    unittest.main()

