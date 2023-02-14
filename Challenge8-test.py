import unittest
from Challenge8 import to_binary

class TestIsAnagram(unittest.TestCase):

    def test_isAnagram(self):
        self.assertEqual(to_binary(0),"0")
        self.assertEqual(to_binary(1),"1")
        self.assertEqual(to_binary(20),"10100")
        self.assertEqual(to_binary(203),"11001011")
        self.assertEqual(to_binary(51),"110011")
        
        with self.assertRaises(ValueError):
            to_binary(-10)

if __name__ == '__main__':
    unittest.main()
