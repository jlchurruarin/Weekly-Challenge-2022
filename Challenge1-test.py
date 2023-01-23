import unittest
from Challenge1 import isAnagram

class TestIsAnagram(unittest.TestCase):


    def test_isAnagram(self):
        self.assertTrue(isAnagram("Raza", "Zara"))
        self.assertTrue(isAnagram("Acuerdo", "Ecuador"))
        self.assertTrue(isAnagram("Brasil", "Silbar"))
        self.assertTrue(isAnagram("Tinieblas", "Sibilante"))
        self.assertFalse(isAnagram("Prueba", "Prueba"))
        self.assertFalse(isAnagram("Planeta", "Animal"))
        self.assertFalse(isAnagram("a", "b"))

if __name__ == '__main__':
    unittest.main()
