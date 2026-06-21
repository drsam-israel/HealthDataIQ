import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "💰",
    "Value Realization Office",
    "Track healthcare informatics investment performance, business outcomes, ROI, and transformation value realization."
)

st.markdown("""
<style>

.value-card{
    background:white;
    border-radius:16px;
    padding:28px;
    border:1px solid #E5E7EB;
    box-shadow:0px 8px 20px rgba(15,23,42,0.06);
    text-align:center;
    min-height:180px;
}

.value-title{
    font-size:18px;
    font-weight:700;
    color:#475569;
}

.value-number{
    font-size:52px;
    font-weight:900;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="value-card">
        <div class="value-title">Value Realized</div>
        <div class="value-number" style="color:#16A34A;">$52M</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="value-card">
        <div class="value-title">Transformation ROI</div>
        <div class="value-number" style="color:#1E66F5;">247%</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="value-card">
        <div class="value-title">Cost Avoidance</div>
        <div class="value-number" style="color:#9333EA;">$18M</div>
    </div>
    """, unsafe_allow_html=True)

    

portfolio_df = pd.DataFrame({
    "Initiative":[
        "Data Governance",
        "Metadata Management",
        "Interoperability",
        "AI Governance",
        "Digital Transformation"
    ],
    "Investment":[
        "$2M",
        "$1.5M",
        "$3M",
        "$1M",
        "$4M"
    ],
    "Benefit":[
        "$8M",
        "$6M",
        "$12M",
        "$4M",
        "$15M"
    ],
    "ROI":[
        "300%",
        "300%",
        "300%",
        "300%",
        "275%"
    ],
    "Status":[
        "Complete",
        "Complete",
        "Complete",
        "Complete",
        "In Progress"
    ]
})

st.dataframe(
    portfolio_df,
    use_container_width=True,
    hide_index=True
)

st.success("""
HealthDataIQ™ estimates that the Healthcare Informatics
Transformation Program generated approximately $52M
in enterprise value through improvements in data quality,
governance, interoperability, AI readiness, operational
efficiency, and executive decision support.

Current portfolio ROI is estimated at 247%, demonstrating
strong value realization and strategic alignment.
""")