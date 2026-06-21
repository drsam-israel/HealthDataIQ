import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🏆",
    "Healthcare Informatics Maturity Index",
    "HealthDataIQ™ proprietary maturity scoring framework for assessing healthcare informatics, governance, interoperability, AI, and transformation readiness."
)

# =====================================================
# HealthDataIQ Maturity Index
# =====================================================

st.markdown('<div class="section-title">HealthDataIQ™ Maturity Index</div>', unsafe_allow_html=True)

domain_scores = {
    "Governance": 90,
    "Metadata": 88,
    "Data Quality": 92,
    "Interoperability": 88,
    "AI Governance": 91,
    "Transformation": 89
}

domain_weights = {
    "Governance": 0.20,
    "Metadata": 0.15,
    "Data Quality": 0.15,
    "Interoperability": 0.15,
    "AI Governance": 0.15,
    "Transformation": 0.20
}

hmi_score = round(
    sum(domain_scores[domain] * domain_weights[domain] for domain in domain_scores)
)

if hmi_score < 40:
    classification = "Level 1 — Fragmented"
    maturity_status = "Foundational"
elif hmi_score < 60:
    classification = "Level 2 — Governed"
    maturity_status = "Developing"
elif hmi_score < 75:
    classification = "Level 3 — Connected"
    maturity_status = "Managed"
elif hmi_score < 90:
    classification = "Level 4 — Intelligent"
    maturity_status = "Advanced"
else:
    classification = "Level 5 — Transformational"
    maturity_status = "Leading Practice"

# =====================================================
# Executive Scorecards
# =====================================================

st.markdown("""
<style>
.hmi-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 8px 22px rgba(15,23,42,0.06);
    min-height: 145px;
}
.hmi-title {
    font-size: 16px;
    font-weight: 900;
    color: #0b1f3a;
}
.hmi-value {
    font-size: 38px;
    font-weight: 900;
    margin-top: 10px;
}
.hmi-note {
    font-size: 14px;
    color: #475569;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="hmi-card">
        <div class="hmi-title">HealthDataIQ™ Maturity Index</div>
        <div class="hmi-value" style="color:#0066ff;">{hmi_score}/100</div>
        <div class="hmi-note">Weighted enterprise informatics maturity score</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="hmi-card" style="border-top-color:#16a34a;">
        <div class="hmi-title">Maturity Classification</div>
        <div class="hmi-value" style="color:#16a34a; font-size:28px;">{classification}</div>
        <div class="hmi-note">Current enterprise maturity level</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="hmi-card" style="border-top-color:#9333ea;">
        <div class="hmi-title">Maturity Status</div>
        <div class="hmi-value" style="color:#9333ea; font-size:32px;">{maturity_status}</div>
        <div class="hmi-note">Executive readiness interpretation</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# Domain Weighting Model
# =====================================================

st.markdown('<div class="section-title">Maturity Domain Weighting Model</div>', unsafe_allow_html=True)

weights_df = pd.DataFrame({
    "Domain": list(domain_scores.keys()),
    "Score": list(domain_scores.values()),
    "Weight": [
        "20%",
        "15%",
        "15%",
        "15%",
        "15%",
        "20%"
    ],
    "Weighted Contribution": [
        round(domain_scores[d] * domain_weights[d], 1) for d in domain_scores
    ],
    "Executive Meaning": [
        "Governance structure, accountability, stewardship, and policies",
        "Dictionary, glossary, lineage, and metadata repository maturity",
        "Completeness, accuracy, validity, timeliness, and trust readiness",
        "FHIR, terminology, APIs, HL7, and ecosystem connectivity readiness",
        "Responsible AI, model risk, explainability, fairness, and monitoring",
        "Roadmap, operating model, portfolio execution, and value realization"
    ]
})

st.dataframe(
    weights_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# HMI Maturity Levels
# =====================================================

st.markdown('<div class="section-title">HealthDataIQ™ Maturity Levels</div>', unsafe_allow_html=True)

levels_df = pd.DataFrame({
    "Level": [
        "Level 1",
        "Level 2",
        "Level 3",
        "Level 4",
        "Level 5"
    ],
    "Classification": [
        "Fragmented",
        "Governed",
        "Connected",
        "Intelligent",
        "Transformational"
    ],
    "Score Range": [
        "0–39",
        "40–59",
        "60–74",
        "75–89",
        "90–100"
    ],
    "Description": [
        "Siloed data, limited governance, manual reporting, weak interoperability.",
        "Governance foundations established with initial policies and stewardship.",
        "Connected systems, metadata management, FHIR readiness, and analytics maturity.",
        "Executive intelligence, responsible AI governance, and transformation capability.",
        "Learning health system capabilities, knowledge graph, AI scale, and continuous transformation."
    ]
})

st.dataframe(
    levels_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# Executive Interpretation
# =====================================================

st.markdown('<div class="section-title">Executive Interpretation</div>', unsafe_allow_html=True)

st.info(f"""
The organization currently scores **{hmi_score}/100**, corresponding to **{classification}**.

This indicates a strong healthcare informatics foundation with mature governance, data quality,
interoperability, responsible AI governance, and transformation readiness.

The organization is positioned to advance toward transformational maturity through healthcare
knowledge graph capabilities, AI governance at scale, learning health system adoption,
and executive value realization tracking.
""")

# =====================================================
# Strategic Recommendations
# =====================================================

st.markdown('<div class="section-title">Strategic Recommendations</div>', unsafe_allow_html=True)

recommendations = [
    "Advance from intelligent maturity toward transformational healthcare informatics capability.",
    "Scale responsible AI governance across all clinical, operational, and executive AI use cases.",
    "Implement healthcare knowledge graph to connect metadata, FHIR, terminology, KPIs, dashboards, and AI models.",
    "Expand transformation value tracking to link informatics investments with measurable outcomes.",
    "Benchmark maturity periodically using the HealthDataIQ™ Maturity Index.",
    "Position the organization for learning health system capabilities and continuous intelligence improvement."
]

for item in recommendations:
    st.success(item)