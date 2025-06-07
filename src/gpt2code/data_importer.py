import csv
import os
from typing import List, Dict, Type


class CSVImporter:
    """Imports data from CSV files into structured dictionaries with automatic delimiter and quote detection."""

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
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found at {file_path}")
            
        try:
            with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
                # Read sample for dialect detection
                sample = csvfile.read(1024)
                csvfile.seek(0)
                
                # Detect dialect parameters
                dialect = CSVImporter.detect_dialect(sample)
                
                reader = csv.reader(csvfile, dialect)
                headers = next(reader)
                cleaned_headers = [h.strip().replace(" ", "_") for h in headers]
                
                data = []
                for row_num, row in enumerate(reader, start=2):
                    if len(row) != len(cleaned_headers):
                        raise ValueError(
                            f"Row {row_num} has {len(row)} fields, "
                            f"expected {len(cleaned_headers)}"
                        )
                    data.append(dict(zip(cleaned_headers, row)))
                
                return data
        except csv.Error as e:
            raise ValueError(f"CSV parsing error: {str(e)}") from e

    @staticmethod
    def detect_dialect(sample: str) -> Type[csv.Dialect]:
        """Detect CSV dialect from sample content.
        
        Args:
            sample: First 1024 bytes of CSV content
            
        Returns:
            Detected CSV dialect class (subclass of csv.Dialect)
            
        Raises:
            ValueError: If unable to detect dialect
        """
        try:
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            
            # Validate quote character
            if dialect.quotechar not in ['"', "'"]:
                dialect.quotechar = '"'
                
            return dialect
        except csv.Error as e:
            raise ValueError(f"CSV dialect detection failed: {str(e)}") from e
