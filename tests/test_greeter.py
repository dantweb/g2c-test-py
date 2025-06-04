import unittest
from src.greeter import get_greeting


class TestGreeter(unittest.TestCase):
    def test_greeting_output(self):
        """Test greeting message generation."""
        self.assertEqual(get_greeting('Alice'), 'Hi, Alice')
        self.assertEqual(get_greeting('Bob'), 'Hi, Bob')

    def test_input_types(self):
        """Test handling of non-string inputs."""
        with self.assertRaises(TypeError):
            get_greeting(123)
        with self.assertRaises(TypeError):
            get_greeting([])