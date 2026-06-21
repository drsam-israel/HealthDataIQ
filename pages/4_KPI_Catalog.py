import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "📊",
    "KPI Catalog",
    "Explore clinical, operational, financial, and AI governance KPIs."
)

df = pd.read_csv("./data/kpis.csv")

kpi_filter = st.selectbox(
    "Select KPI",
    ["All"] + sorted(df["kpi_name"].unique().tolist())
)

if kpi_filter != "All":
    df = df[df["kpi_name"] == kpi_filter]

c1, c2, c3 = st.columns(3)

c1.metric("KPIs", len(df))
c2.metric("Categories", df["category"].nunique())
c3.metric("Owners", df["owner"].nunique())

st.markdown('<div class="section-title">KPI Inventory</div>', unsafe_allow_html=True)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=500
)