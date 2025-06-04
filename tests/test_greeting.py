import unittest
from src.greeting import greet


class TestGreeting(unittest.TestCase):
    def test_greet_output(self):
        """Test greeting output matches expected format"""
        self.assertEqual(greet('World'), 'Hi, World')
        self.assertEqual(greet('Alice'), 'Hi, Alice')


if __name__ == '__main__':
    unittest.main()