import unittest
from Challenge13 import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(9), 362880)

        self.assertNotEqual(factorial(0), 0)
        self.assertNotEqual(factorial(3), 150)
        self.assertNotEqual(factorial(4), 250)
        
    def test_factorial_exception(self):
        with self.assertRaises(ValueError):
            factorial(-1)
            factorial(-10)
            factorial(-150)

if __name__ == '__main__':
    unittest.main()
