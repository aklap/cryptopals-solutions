import unittest
from solution4 import decrypt

example = decrypt("4.txt")

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(example, (443.51, '5', 'Now that the party is jumping\n'))

if __name__ == '__main__':
    unittest.main()