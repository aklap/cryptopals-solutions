import unittest
from solution2 import get_XOR

example = get_XOR("./buffer1.txt", "./buffer2.txt")

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(example, '746865206b696420646f6e277420706c6179')


if __name__ == '__main__':
    unittest.main()
