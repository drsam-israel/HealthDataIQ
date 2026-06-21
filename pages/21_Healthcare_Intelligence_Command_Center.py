import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🧠",
    "Healthcare Intelligence Command Center",
    "Executive mission control for healthcare informatics, governance, interoperability, AI, and digital transformation."
)

# =====================================================
# Executive Intelligence Scorecard
# =====================================================

st.markdown('<div class="section-title">Enterprise Healthcare Intelligence Scorecard</div>', unsafe_allow_html=True)

st.markdown("""
<style>
.intel-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 8px 22px rgba(15,23,42,0.06);
    min-height: 145px;
}
.intel-title {
    font-size: 15px;
    font-weight: 900;
    color: #0b1f3a;
}
.intel-value {
    font-size: 38px;
    font-weight: 900;
    margin-top: 10px;
}
.intel-note {
    font-size: 13px;
    color: #475569;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="intel-card">
        <div class="intel-title">🏆 HealthDataIQ Maturity Index</div>
        <div class="intel-value" style="color:#0066ff;">84</div>
        <div class="intel-note">Overall enterprise informatics maturity</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="intel-card" style="border-top-color:#16a34a;">
        <div class="intel-title">✅ Data Quality</div>
        <div class="intel-value" style="color:#16a34a;">92%</div>
        <div class="intel-note">Enterprise data trust readiness</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="intel-card" style="border-top-color:#9333ea;">
        <div class="intel-title">🤖 AI Readiness</div>
        <div class="intel-value" style="color:#9333ea;">91%</div>
        <div class="intel-note">Responsible AI and operational readiness</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)

with c4:
    st.markdown("""
    <div class="intel-card" style="border-top-color:#14b8a6;">
        <div class="intel-title">🔗 Interoperability</div>
        <div class="intel-value" style="color:#14b8a6;">88%</div>
        <div class="intel-note">FHIR and ecosystem connectivity readiness</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="intel-card" style="border-top-color:#f97316;">
        <div class="intel-title">📈 Transformation</div>
        <div class="intel-value" style="color:#f97316;">89%</div>
        <div class="intel-note">Digital health transformation maturity</div>
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="intel-card" style="border-top-color:#db2777;">
        <div class="intel-title">🛡 Governance</div>
        <div class="intel-value" style="color:#db2777;">90%</div>
        <div class="intel-note">Governance and stewardship readiness</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# Executive Heat Map
# =====================================================

st.markdown('<div class="section-title">Executive Capability Heat Map</div>', unsafe_allow_html=True)

heatmap_df = pd.DataFrame({
    "Capability":[
        "Governance",
        "Metadata",
        "Data Quality",
        "Interoperability",
        "AI Governance",
        "Transformation"
    ],
    "Score":[90,88,92,88,91,89],
    "Status":[
        "Strong",
        "Strong",
        "Excellent",
        "Strong",
        "Excellent",
        "Strong"
    ]
})

st.dataframe(
    heatmap_df,
    use_container_width=True,
    hide_index=True,
    height=260
)

# =====================================================
# Strategic Risks
# =====================================================

st.markdown('<div class="section-title">Strategic Risk Overview</div>', unsafe_allow_html=True)

risk_df = pd.DataFrame({
    "Risk":[
        "AI Governance Scaling",
        "Legacy Integration Dependencies",
        "Data Quality Variation",
        "Workforce Capability Gap",
        "Transformation Adoption Risk"
    ],
    "Severity":[
        "High",
        "High",
        "Medium",
        "Medium",
        "High"
    ],
    "Executive Impact":[
        "Potential AI risk growth",
        "Reduced interoperability agility",
        "Reduced analytical trust",
        "Delayed transformation execution",
        "Reduced organizational adoption"
    ]
})

st.dataframe(
    risk_df,
    use_container_width=True,
    hide_index=True,
    height=260
)

# =====================================================
# Strategic Priorities
# =====================================================

st.markdown('<div class="section-title">Strategic Priorities</div>', unsafe_allow_html=True)

priorities = [
    "Scale Responsible AI Governance",
    "Expand FHIR Interoperability",
    "Implement Metadata Lineage",
    "Operationalize Transformation Office",
    "Develop Healthcare Knowledge Graph",
    "Strengthen Workforce AI Capability"
]

for item in priorities:
    st.success(item)

# =====================================================
# Executive Recommendation
# =====================================================

st.markdown('<div class="section-title">Executive Recommendation</div>', unsafe_allow_html=True)

st.success("""
The organization is positioned for enterprise-scale AI adoption,
interoperability expansion, executive intelligence maturity,
and intelligent healthcare operations.

Leadership should prioritize Responsible AI governance,
FHIR ecosystem expansion, metadata lineage,
and transformation value realization over the next 12–24 months.
""")