import unittest
from Challenge14 import is_armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_amstrong_number(self):
        self.assertTrue(is_armstrong_number(370))
        self.assertTrue(is_armstrong_number(371))
        self.assertTrue(is_armstrong_number(407))
        self.assertTrue(is_armstrong_number(8208))

        self.assertFalse(is_armstrong_number(10))
        self.assertFalse(is_armstrong_number(360))
        self.assertFalse(is_armstrong_number(1500))
        
    def test_amstrong_number_exception(self):
        with self.assertRaises(TypeError):
            is_armstrong_number("100")
            is_armstrong_number(True)
            is_armstrong_number(None)

if __name__ == '__main__':
    unittest.main()
