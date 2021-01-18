import unittest
from q2 import pricing


class TestAlphabetRange(unittest.TestCase):
    def test_one(self):
        output = pricing('Trolly', 2, 'Hourly', 3.0)
        expected = 720.0
        self.assertEqual(output, expected)

    def test_two(self):
        output = pricing('Limousine', 3, 'Daily', 3.0)
        expected = 4950.0
        self.assertEqual(output, expected)

    def test_three(self):
        output = pricing('SUV', 3, 'Distance', 4.2)
        expected = 28.35
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()

