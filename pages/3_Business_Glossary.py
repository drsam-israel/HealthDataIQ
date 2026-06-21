import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "📚",
    "Business Glossary",
    "Explore standardized healthcare business terms and definitions."
)

df = pd.read_csv("./data/glossary_terms.csv")

selected_term = st.selectbox(
    "Select Business Term",
    ["All"] + sorted(df["term_name"].unique().tolist())
)

if selected_term != "All":
    filtered_df = df[df["term_name"] == selected_term]
else:
    filtered_df = df

c1, c2, c3 = st.columns(3)

c1.metric("Business Terms", len(filtered_df))
c2.metric("Categories", filtered_df["category"].nunique())
c3.metric("Owners", filtered_df["owner"].nunique())

st.markdown(
    '<div class="section-title">Glossary Inventory</div>',
    unsafe_allow_html=True
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True,
    height=500
)