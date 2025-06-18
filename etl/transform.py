import pandas as pd
from typing import Dict

def merge_sheets(sheets: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Combine multiple sheets into a single DataFrame."""
    df_combined = pd.concat(sheets.values(), ignore_index=True)
    return df_combined

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare the DataFrame for visualization."""
    df = df.dropna(subset=["Product", "Sales", "Date"])
    df["Date"] = pd.to_datetime(df["Date"])
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)
    return df