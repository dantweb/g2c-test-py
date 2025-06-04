import unittest
from src.gpt2code.greeting import get_greeting, get_formal_greeting, get_farewell


class TestGreeting(unittest.TestCase):
    def test_get_greeting(self):
        """Test that get_greeting returns correct greeting."""
        self.assertEqual(get_greeting("TestName"), "Hi, TestName")

    def test_get_formal_greeting(self):
        """Test that get_formal_greeting returns correct formal greeting."""
        self.assertEqual(get_formal_greeting("Smith", "Dr."), "Dear Dr. Smith")

    def test_get_farewell(self):
        """Test that get_farewell returns correct farewell."""
        self.assertEqual(get_farewell("Alice"), "Goodbye, Alice")


if __name__ == '__main__':
    unittest.main()