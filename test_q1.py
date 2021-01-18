import unittest
from q1 import formatString


class TestAlphabetRange(unittest.TestCase):
    def test_one(self):
        output = formatString("xxxxyyyyxx", 1)
        expected = 'xyx'
        self.assertEqual(output, expected)

    def test_two(self):
        output = formatString("xxxy", 2)
        expected = 'xxy'
        self.assertEqual(output, expected)

    def test_three(self):
        output = formatString("xxyy", 1)
        expected = 'xy'
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()

