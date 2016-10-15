import unittest
from solution6 import *

class MyTest(unittest.TestCase):
    def test_hamming(self):
        self.assertEqual(hamming('this is a test', 'wokka wokka!!!'), 37)

        

if __name__ == '__main__':
    unittest.main()