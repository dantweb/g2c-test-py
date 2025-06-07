import unittest
import os
import tempfile
from typing import List, Dict
from src.gpt2code.data_importer import CSVImporter


class TestCSVImporter(unittest.TestCase):
    """Test suite for CSV data importer functionality."""
    
    def test_imports_valid_csv_correctly(self) -> None:
        """Test proper import of well-formatted CSV data."""
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
            tmp.write("name,age,occupation\n")
            tmp.write("Alice,30,Engineer\n")
            tmp.write("Bob,25,Designer\n")
            tmp_path = tmp.name
        try:
            data: List[Dict[str, str]] = CSVImporter.import_data(tmp_path)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["name"], "Alice")
            self.assertEqual(data[0]["age"], "30")
            self.assertEqual(data[0]["occupation"], "Engineer")
            self.assertEqual(data[1]["name"], "Bob")
            self.assertEqual(data[1]["age"], "25")
            self.assertEqual(data[1]["occupation"], "Designer")
        finally:
            os.unlink(tmp_path)

    def test_header_whitespace_handling(self) -> None:
        """Test headers with whitespace are properly sanitized."""
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
            tmp.write("First Name, Last Name \n")
            tmp.write("John,Doe\n")
            tmp_path = tmp.name
        try:
            data: List[Dict[str, str]] = CSVImporter.import_data(tmp_path)
            self.assertIn("First_Name", data[0])
            self.assertIn("Last_Name", data[0])
            self.assertEqual(data[0]["First_Name"], "John")
            self.assertEqual(data[0]["Last_Name"], "Doe")
        finally:
            os.unlink(tmp_path)

    def test_missing_file_handling(self) -> None:
        """Test proper error when file doesn't exist."""
        with self.assertRaises(FileNotFoundError):
            CSVImporter.import_data("non_existent_file.csv")

    def test_invalid_csv_handling(self) -> None:
        """Test error handling for malformed CSV."""
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
            tmp.write("header1,header2\n")
            tmp.write("value1\n")  # Missing second value
            tmp_path = tmp.name
        try:
            with self.assertRaises(ValueError):
                CSVImporter.import_data(tmp_path)
        finally:
            os.unlink(tmp_path)
            
    def test_demo_data_import(self) -> None:
        """Test reading demo CSV file from tests/demo directory."""
        demo_file = os.path.join(os.path.dirname(__file__), 'demo', 'demo_data.csv')
        data = CSVImporter.import_data(demo_file)
        self.assertEqual(len(data), 10)
        self.assertEqual(data[0]["id"], "1")
        self.assertEqual(data[0]["name"], "Alice")
        self.assertEqual(data[0]["value"], "100")
        self.assertEqual(data[9]["id"], "10")
        self.assertEqual(data[9]["name"], "Jack")
        self.assertEqual(data[9]["value"], "1000")


if __name__ == "__main__":
    unittest.main()