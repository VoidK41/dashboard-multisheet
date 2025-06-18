import pandas as pd

def format_currency(value: float) -> str:
    """Format number as currency string."""
    return f"Rp {value:,.0f}".replace(",", ".")