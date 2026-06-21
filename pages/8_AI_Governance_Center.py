import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🧠",
    "AI Governance Center",
    "Monitor AI model registry, risk tiering, bias, drift, and explainability."
)

df = pd.read_csv("./data/ai_models.csv")

model_filter = st.selectbox(
    "Select AI Model",
    ["All"] + sorted(df["model_name"].unique().tolist())
)

if model_filter != "All":
    df = df[df["model_name"] == model_filter]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Models", len(df))
c2.metric("Avg Accuracy", f"{df['accuracy'].mean():.1f}%")
c3.metric("Avg Bias Score", f"{df['bias_score'].mean():.2f}")
c4.metric("Avg Explainability", f"{df['explainability_score'].mean():.2f}")

st.markdown('<div class="section-title">AI Model Registry</div>', unsafe_allow_html=True)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=500
)