import unittest
from Challenge3 import isPrime

class TestIsAnagram(unittest.TestCase):

    def test_isAnagram(self):
        self.assertFalse(isPrime(0))
        self.assertFalse(isPrime(1))
        self.assertFalse(isPrime(4))
        self.assertFalse(isPrime(6))
        self.assertFalse(isPrime(100))
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(5))
        self.assertTrue(isPrime(7))
        self.assertTrue(isPrime(17))
        self.assertTrue(isPrime(67))
        self.assertTrue(isPrime(97))

if __name__ == '__main__':
    unittest.main()
