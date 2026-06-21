import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "📑",
    "Board & Executive Report",
    "Board-level summary of healthcare informatics maturity, transformation value, strategic risks, and executive priorities."
)

st.markdown('<div class="section-title">Executive Summary</div>', unsafe_allow_html=True)

st.info("""
HealthDataIQ™ indicates that the organization has established a strong healthcare informatics foundation,
with mature data quality, emerging responsible AI governance, expanding interoperability capability,
and clear digital health transformation priorities.
""")

st.markdown('<div class="section-title">Board-Level Scorecard</div>', unsafe_allow_html=True)

score_df = pd.DataFrame({
    "Domain": [
        "HealthDataIQ Maturity Index",
        "Data Quality",
        "Governance Readiness",
        "Interoperability",
        "AI Governance",
        "Transformation Readiness"
    ],
    "Score": [
        "82/100",
        "92%",
        "85%",
        "88%",
        "92%",
        "88%"
    ],
    "Status": [
        "Intelligent",
        "Strong",
        "Mature",
        "Connected",
        "Advanced",
        "Enterprise Enabled"
    ]
})

st.dataframe(
    score_df,
    use_container_width=True,
    hide_index=True,
    height=260
)

st.markdown('<div class="section-title">Strategic Risks</div>', unsafe_allow_html=True)

risk_df = pd.DataFrame({
    "Risk": [
        "Responsible AI Scaling Risk",
        "Legacy Interoperability Dependency",
        "Data Quality Variation",
        "Change Resistance",
        "Skills and Workforce Gap"
    ],
    "Severity": [
        "High",
        "High",
        "Medium",
        "High",
        "High"
    ],
    "Board Relevance": [
        "AI must scale safely with governance and clinical oversight",
        "Legacy integration may limit transformation speed",
        "Data quality gaps may affect analytics and AI reliability",
        "Transformation adoption may slow without change leadership",
        "Capability gaps may delay enterprise execution"
    ]
})

st.dataframe(
    risk_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

st.markdown('<div class="section-title">Value Realization Summary</div>', unsafe_allow_html=True)

value_df = pd.DataFrame({
    "Value Area": [
        "Data Governance",
        "Interoperability",
        "AI Enablement",
        "Executive Intelligence",
        "Workflow Automation"
    ],
    "Estimated Annual Value": [
        "$2.1M",
        "$3.4M",
        "$4.2M",
        "$1.5M",
        "$1.2M"
    ],
    "Executive Outcome": [
        "Trusted data and improved compliance",
        "Connected healthcare ecosystem",
        "Clinical and operational intelligence",
        "Faster leadership decisions",
        "Improved operational efficiency"
    ]
})

st.dataframe(
    value_df,
    use_container_width=True,
    hide_index=True,
    height=280
)

st.markdown('<div class="section-title">Board-Level Priorities</div>', unsafe_allow_html=True)

priorities = [
    "Scale Responsible AI Governance across all clinical and operational AI models.",
    "Expand FHIR interoperability and reduce dependency on legacy interfaces.",
    "Strengthen enterprise metadata lineage and data quality monitoring.",
    "Operationalize the Digital Health Transformation Office.",
    "Develop healthcare knowledge graph and semantic intelligence capabilities.",
    "Establish executive value tracking for healthcare informatics investments."
]

for item in priorities:
    st.success(item)

st.markdown('<div class="section-title">Executive Recommendation</div>', unsafe_allow_html=True)

st.success("""
HealthDataIQ™ recommends a 12-month executive transformation program focused on responsible AI governance,
FHIR interoperability expansion, metadata lineage, data quality automation, and transformation value tracking.

This will strengthen enterprise readiness for intelligent healthcare operations, clinical AI scale-up,
and learning health system capabilities.
""")