from etl.extract import read_excel_sheets
from etl.transform import merge_sheets, clean_data
from dashboard.app import run_dashboard

import streamlit as st

def main():
    st.sidebar.title("📁 Upload Excel File")
    file = st.sidebar.file_uploader("Choose Excel File", type=["xlsx"])

    if file:
        sheets = read_excel_sheets(file)
        df_raw = merge_sheets(sheets)
        df_clean = clean_data(df_raw)
        run_dashboard(df_clean)
    else:
        st.write("Upload an Excel file with multiple sheets to begin.")

if __name__ == "__main__":
    main()