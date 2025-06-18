import pandas as pd
from typing import Dict

def read_excel_sheets(file_path: str) -> Dict[str, pd.DataFrame]:
    """Read all sheets from an Excel file into a dictionary."""
    try:
        sheets = pd.read_excel(file_path, sheet_name=None)
        return sheets
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return{}