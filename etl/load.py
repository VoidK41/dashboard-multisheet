import pandas as pd
import sqlite3

def save_to_database(df: pd.DataFrame, db_path: str = "data/sales.db"):
    """Save DataFrame to SQLite database."""
    conn = sqlite3.connect(db_path)
    df.to_sql("sales_data", conn, if_exists="replace", index=False)
    conn.close()