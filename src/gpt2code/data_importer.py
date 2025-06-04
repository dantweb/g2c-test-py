import csv
from collections import namedtuple
from typing import List


class CSVImporter:
    """Imports data from CSV files into structured objects.
    
    Attributes:
        None
    """
    
    @staticmethod
    def import_data(file_path: str) -> List[namedtuple]:
        """Read CSV file and return objects matching header structure.
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            List of objects where attributes match CSV headers
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If CSV formatting is invalid
        """
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)
                cleaned_headers = [h.strip().replace(' ', '_') for h in headers]
                Row = namedtuple('Row', cleaned_headers)
                
                return [Row(*row) for row in reader]
                
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found at {file_path}")
        except Exception as e:
            raise ValueError(f"Error processing CSV: {str(e)}")