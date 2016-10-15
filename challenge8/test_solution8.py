import unittest
from solution8 import find_plaintext

expected_bytes = [b'd880619740a8a19b', b'7840a8a31c810a3d', b'08649af70dc06f4f', b'd5d2d69c744cd283', b'e2dd052f6b641dbf', b'9d11b0348542bb57', b'08649af70dc06f4f', b'd5d2d69c744cd283', b'9475c9dfdbc1d465', b'97949d9c7e82bf5a', b'08649af70dc06f4f', b'd5d2d69c744cd283', b'97a93eab8d6aecd5', b'66489154789a6b03', b'08649af70dc06f4f', b'd5d2d69c744cd283', b'd403180c98c8f6db', b'1f2a3f9c4040deb0', b'ab51b29933f2c123', b'c58386b06fba186a']

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(find_plaintext('ciphertext.txt'), (132, expected_bytes))

if __name__ == '__main__':
    unittest.main()