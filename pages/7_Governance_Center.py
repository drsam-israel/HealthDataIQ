import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🛡️",
    "Governance Center",
    "Explore enterprise governance policies, ownership, review cycles, and status."
)

df = pd.read_csv("./data/governance_policies.csv")

policy_filter = st.selectbox(
    "Select Governance Policy",
    ["All"] + sorted(df["policy_name"].unique().tolist())
)

if policy_filter != "All":
    df = df[df["policy_name"] == policy_filter]

c1, c2, c3 = st.columns(3)

c1.metric("Policies", len(df))
c2.metric("Active Policies", len(df[df["status"] == "Active"]))
c3.metric("Owners", df["owner"].nunique())

st.markdown('<div class="section-title">Governance Policy Inventory</div>', unsafe_allow_html=True)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=500
)