import unittest
from solution3 import freq_decode

example = freq_decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(example, (345.46000000000015, 'X', 'Cooking MC\'s like a pound of bacon'))

if __name__ == '__main__':
    unittest.main()