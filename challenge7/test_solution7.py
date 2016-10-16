import unittest
from solution7 import decrypt_AES
from lyrics import song
import string

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(decrypt_AES(), song.decode())

if __name__ == '__main__':
    unittest.main()