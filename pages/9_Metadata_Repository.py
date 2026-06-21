import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🗄️",
    "Metadata Repository",
    "Explore enterprise metadata assets across data, glossary, FHIR, governance, and AI domains."
)

df = pd.read_csv("./data/metadata_assets.csv")

asset_filter = st.selectbox(
    "Select Asset Type",
    ["All"] + sorted(df["asset_type"].unique().tolist())
)

if asset_filter != "All":
    df = df[df["asset_type"] == asset_filter]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Metadata Assets", len(df))
c2.metric("Asset Types", df["asset_type"].nunique())
c3.metric("Owners", df["owner"].nunique())
c4.metric("Domains", df["domain"].nunique())

st.markdown('<div class="section-title">Metadata Inventory</div>', unsafe_allow_html=True)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=500
)