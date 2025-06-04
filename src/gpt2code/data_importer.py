import csv
from typing import List, Dict


class CSVImporter:
    """Imports data from CSV files into structured dictionaries."""

    @staticmethod
    def import_data(file_path: str) -> List[Dict[str, str]]:
        """Read CSV file and return dictionaries matching header structure.
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            List of dictionaries where keys match sanitized CSV headers
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If CSV formatting is invalid
        """
        try:
            with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)
                cleaned_headers = [h.strip().replace(" ", "_") for h in headers]
                
                data = []
                for row in reader:
                    if len(row) != len(cleaned_headers):
                        raise ValueError("Row has incorrect number of fields")
                    data.append(dict(zip(cleaned_headers, row)))
                
                return data
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found at {file_path}")
        except Exception as e:
            raise ValueError(f"Error processing CSV: {str(e)}")
