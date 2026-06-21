import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "📖",
    "Data Dictionary",
    "Explore standardized enterprise healthcare data elements."
)

df = pd.read_csv("./data/data_elements.csv")

selected_element = st.selectbox(
    "Select Data Element",
    ["All"] + sorted(df["element_name"].unique().tolist())
)

if selected_element != "All":
    filtered_df = df[df["element_name"] == selected_element]
else:
    filtered_df = df

c1, c2, c3 = st.columns(3)

c1.metric("Data Elements", len(filtered_df))
c2.metric("Domains", filtered_df["domain"].nunique())
c3.metric("Owners", filtered_df["owner"].nunique())

st.markdown(
    '<div class="section-title">Data Element Inventory</div>',
    unsafe_allow_html=True
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True,
    height=500
)