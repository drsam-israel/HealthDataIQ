import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🔄",
    "FHIR Explorer",
    "Explore healthcare data element mappings to FHIR resources."
)

df = pd.read_csv("./data/fhir_mappings.csv")

resource = st.selectbox(
    "Select FHIR Resource",
    ["All"] + sorted(df["fhir_resource"].unique().tolist())
)

if resource != "All":
    df = df[df["fhir_resource"] == resource]

c1, c2, c3 = st.columns(3)

c1.metric("FHIR Mappings", len(df))
c2.metric("FHIR Resources", df["fhir_resource"].nunique())
c3.metric("Mapping Types", df["mapping_type"].nunique())

st.markdown('<div class="section-title">FHIR Mapping Inventory</div>', unsafe_allow_html=True)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=500
)