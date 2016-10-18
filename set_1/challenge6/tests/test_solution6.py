import unittest
import sys
sys.path.append('../challenge6')
from solution6 import *
sys.path.append('../helper_functions')
from helper_functions import *
from song import lyrics

class MyTest(unittest.TestCase):
    # test hamming function
    def test_hamming(self):
        # per the instructions, result is 37
        self.assertEqual(hamming('this is a test', 'wokka wokka!!!'), 37)

    # test to_chunks function
    def test_chunking_express(self):
        test_str = 'this is a test'
        self.assertEqual(len(to_chunks(test_str, 2)), 7)
        # can split into n-sized list with enough elements
        self.assertEqual(to_chunks(test_str, 2), ['th', 'is', ' i', 's ', 'a ', 'te', 'st'])
        # can handle splitting n-size lists even if there aren't enough elements left over
        self.assertEqual(to_chunks(test_str, 3), ['thi', 's i', 's a', ' te', 'st'])
    
    # test found key
    def test_key_result(self):
        self.assertEqual(break_repeating('ciphertext.txt')[0], 'Terminator X: Bring the noise')
   
    # test decrypted plaintext
    def test_plaintext(self):
        self.assertEqual(break_repeating('ciphertext.txt')[1], ''.join(lyrics))

if __name__ == '__main__':
    unittest.main()