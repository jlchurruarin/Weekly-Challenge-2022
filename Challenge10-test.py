import unittest
from Challenge10 import is_expresion_balanced

class TestBalancedExpresion(unittest.TestCase):

    def test_balanced_true(self):
        self.assertTrue(is_expresion_balanced("{ [ a * ( c + d ) ] - 5 }"))
        self.assertTrue(is_expresion_balanced("5 + (2 + a) / 3"))
        self.assertTrue(is_expresion_balanced("{[[1+1] / 2 ] / 2} / [18 * (4 + 5)]"))
        

    def test_balanced_false(self):
        self.assertFalse(is_expresion_balanced("{a + b [c] * (2x2)}}}}"))
        self.assertFalse(is_expresion_balanced("{a^4 + (((ax4)}"))
        self.assertFalse(is_expresion_balanced("{ a * ( c + d ) ] - 5 }"))
        self.assertFalse(is_expresion_balanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))
        self.assertFalse(is_expresion_balanced("{{{{{{(}}}}}}"))
        self.assertFalse(is_expresion_balanced("(a"))


if __name__ == '__main__':
    unittest.main()
