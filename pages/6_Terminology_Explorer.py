import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🧬",
    "Terminology Explorer",
    "Explore clinical terminology mappings across SNOMED CT, ICD, LOINC, and RxNorm."
)

df = pd.read_csv("./data/terminology_crosswalks.csv")

concept_filter = st.selectbox(
    "Select Clinical Concept",
    ["All"] + sorted(df["clinical_concept"].dropna().unique().tolist())
)

if concept_filter != "All":
    df = df[df["clinical_concept"] == concept_filter]

c1, c2, c3 = st.columns(3)

c1.metric("Concepts", len(df))
c2.metric("SNOMED Concepts", df["snomed_ct"].notna().sum())
c3.metric("LOINC Concepts", df["loinc"].notna().sum())

st.markdown('<div class="section-title">Terminology Crosswalks</div>', unsafe_allow_html=True)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=500
)