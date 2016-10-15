import unittest
from solution1 import toBase64

example = toBase64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
)

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(example, "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

# run test from command line
if __name__ == '__main__':
    unittest.main()