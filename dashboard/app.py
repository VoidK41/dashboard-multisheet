import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import format_currency

def run_dashboard(df: pd.DataFrame):
    st.title("📊 Multisheet Sales Dashboard")

    st.sidebar.header("Filter")
    products = st.sidebar.multiselect("Select Product", options=df["Product"].unique())
    if products:
        df = df[df["Product"].isin(products)]
        
    st.markdown("## 💰 Total Sales")
    total_sales = df["Sales"].sum()
    st.metric("Total Sales", format_currency(total_sales))

    st.markdown("## 📈 Sales Overtime")
    fig = px.line(df, x="Date", y="Sales", color="Product", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("## 📊 Top Products")
    top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
    st.bar_chart(top_products)