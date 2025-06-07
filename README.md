# GPT2Code Project

This project demonstrates a simple Python application with data import capabilities.

## Features
- CSV data import with validation
- Greeting message generation
- Unit testing

## Requirements
- Python 3.8+

## Installation
```bash
pip install -e .
```

## Running Tests
```bash
python -m unittest discover tests
```

## Project Structure
```
src/
├── gpt2code/
│   ├── data_importer.py
│   ├── greeting.py
│   ├── main.py
│   └── __init__.py
tests/
├── test_data_importer.py
├── test_main.py
└── demo/
    └── demo_data.csv
```