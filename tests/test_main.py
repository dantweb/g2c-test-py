import unittest
from io import StringIO
import sys
from main import print_hi


class TestPrintHi(unittest.TestCase):
    def test_print_hi_output(self):
        """Test that print_hi outputs correct greeting."""
        captured_output = StringIO()
        sys.stdout = captured_output
        print_hi("TestName")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hi, TestName")


if __name__ == '__main__':
    unittest.main()
