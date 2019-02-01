import unittest
from solution4 import find_xor

example = find_xor("4.txt")

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(example, 'Now that the party is jumping\n')

if __name__ == '__main__':
    unittest.main()
