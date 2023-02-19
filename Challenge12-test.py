import unittest
from Challenge12 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("Sometamos o matemos"))
        self.assertTrue(is_palindrome("Isaac no ronca así"))
        self.assertTrue(is_palindrome("Yo dono rosas, oro no doy"))
        

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("Lorem ipsum dolor sit amet"))
        self.assertFalse(is_palindrome("Delfina fue al parque"))
        self.assertFalse(is_palindrome("El cabello bonito de la niñita estaba peinado muy bien"))
        self.assertFalse(is_palindrome("Un bebé muy pequeño estaba llorando"))
        self.assertFalse(is_palindrome("Lavó el vestido bien"))
        self.assertFalse(is_palindrome("El estudiante puede utilizar frases pequeñas y comunicar ideas esenciales"))


if __name__ == '__main__':
    unittest.main()
