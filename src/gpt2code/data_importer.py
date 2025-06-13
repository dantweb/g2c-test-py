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
<<<<<<< Updated upstream
                # Read sample for dialect detection
                sample = csvfile.read(1024)
                csvfile.seek(0)
                
                # Detect dialect parameters
                dialect = CSVImporter.detect_dialect(sample)
                
=======
                # Read a sample for dialect detection
                sample: str = csvfile.read(1024)
                csvfile.seek(0)

                # Detect dialect parameters with fallback for delimiter and quote character
                dialect: csv.Dialect = CSVImporter._detect_dialect(sample)

>>>>>>> Stashed changes
                reader = csv.reader(csvfile, dialect)
                headers = next(reader)
                cleaned_headers = CSVImporter._sanitize_headers(headers)

                data: List[Dict[str, str]] = []
                for row_num, row in enumerate(reader, start=2):
                    # Skip empty rows
                    if not row:
                        continue
                        
                    if len(row) != len(cleaned_headers):
                        raise ValueError(
                            f"Row {row_num} has {len(row)} fields, expected {len(cleaned_headers)}"
                        )
                    data.append(dict(zip(cleaned_headers, row)))

                return data
        except (csv.Error, UnicodeDecodeError) as e:
            raise ValueError(f"CSV parsing error: {str(e)}") from e

    @staticmethod
<<<<<<< Updated upstream
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
            
            # Skip dialect detection for small samples
            if not sample.strip() or '\n' not in sample:
                return csv.excel  # Default dialect
                
            # Provide common delimiters to try
            dialect = sniffer.sniff(sample, delimiters=",;\t")
            
            # Validate quote character
            if dialect.quotechar not in ['"', "'"]:
                dialect.quotechar = '"'
                
            return dialect
        except Exception:
            # Return default dialect if any detection error occurs
            return csv.excel
=======
    def _sanitize_headers(headers: List[str]) -> List[str]:
        """Sanitize CSV headers by stripping whitespace and replacing spaces with underscores.
        
        Args:
            headers: List of header strings as read from the CSV file
        
        Returns:
            Cleaned list of header strings
        """
        return [header.strip().replace(" ", "_") for header in headers]

    @staticmethod
    def _detect_dialect(sample: str) -> csv.Dialect:
        """Detect CSV dialect from a sample of CSV content.
        
        This method uses csv.Sniffer to detect the CSV dialect. If detection fails,
        it falls back to determining the delimiter based on occurrence counts and
        then sets a default quote character. Additionally, if the sample starts with a
        quote character (single or double), that character is enforced as the quotechar.
        
        Args:
            sample: A string sample from the CSV file
        
        Returns:
            A csv.Dialect object with ensured delimiter and quote character
        
        Raises:
            ValueError: If the sample is empty
        """
        if not sample:
            raise ValueError("Empty CSV sample, unable to detect dialect")

        try:
            sniffer = csv.Sniffer()
            dialect: csv.Dialect = sniffer.sniff(sample)
        except csv.Error:
            # Fallback: determine delimiter based on occurrence count
            delimiter: str = "," if sample.count(",") >= sample.count(";") else ";"
            FallbackDialect = type(
                'FallbackDialect',
                (csv.Dialect,),
                {
                    'delimiter': delimiter,
                    'quotechar': '"',
                    'escapechar': None,
                    'doublequote': True,
                    'skipinitialspace': False,
                    'lineterminator': "\n",
                    'quoting': csv.QUOTE_MINIMAL
                }
            )
            dialect = FallbackDialect()

        # Ensure the delimiter is either a comma or semicolon
        if dialect.delimiter not in [",", ";"]:
            dialect.delimiter = "," if sample.count(",") > sample.count(";") else ";"

        # Adjust quotechar if it is not a standard single or double quote
        if dialect.quotechar not in ("'", '"'):
            if '"' in sample:
                dialect.quotechar = '"'
            elif "'" in sample:
                dialect.quotechar = "'"
            else:
                dialect.quotechar = '"'

        # Enforce quote character based on the first non-whitespace character in the sample
        sample_stripped = sample.lstrip()
        if sample_stripped and sample_stripped[0] in ("'", '"'):
            dialect.quotechar = sample_stripped[0]

        return dialect
>>>>>>> Stashed changes
