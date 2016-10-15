import unittest
from solution6 import *

class MyTest(unittest.TestCase):
    def test_hamming(self):
        # per the instructions, result is 37
        self.assertEqual(hamming('this is a test', 'wokka wokka!!!'), 37)

    def test_chunking_express(self):
        test_str = 'this is a test'
        self.assertEqual(len(to_chunks(test_str, 2)), 7)
        # can split into n-sized list with enough elements
        self.assertEqual(to_chunks(test_str, 2), ['th', 'is', ' i', 's ', 'a ', 'te', 'st'])
        # can handle splitting n-size lists even if there aren't enough elements left over
        self.assertEqual(to_chunks(test_str, 3), ['thi', 's i', 's a', ' te', 'st'])

if __name__ == '__main__':
    unittest.main()