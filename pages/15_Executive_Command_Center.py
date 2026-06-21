import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🏆",
    "Executive Command Center",
    "Board-level view of HealthDataIQ™ healthcare informatics maturity, governance readiness, data quality, AI governance, and transformation priorities."
)

# =====================================================
# Executive HealthDataIQ Scorecard
# =====================================================

hmi_score = 82
dq_score = 92
governance_score = 85
interop_score = 78
ai_score = 76
transformation_score = 83

st.markdown('<div class="section-title">Enterprise HealthDataIQ™ Scorecard</div>', unsafe_allow_html=True)

st.markdown("""
<style>
.exec-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 18px 22px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
    min-height: 135px;
}
.exec-title {
    font-size: 15px;
    font-weight: 900;
    color: #0b1f3a;
}
.exec-value {
    font-size: 36px;
    font-weight: 900;
    color: #0066ff;
    margin-top: 8px;
}
.exec-note {
    font-size: 13px;
    color: #475569;
    margin-top: 8px;
    line-height: 1.4;
}
</style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="exec-card">
        <div class="exec-title">HealthDataIQ Maturity Index</div>
        <div class="exec-value">{hmi_score}/100</div>
        <div class="exec-note">Overall healthcare informatics maturity</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="exec-card" style="border-top-color:#16a34a;">
        <div class="exec-title">Data Quality Score</div>
        <div class="exec-value" style="color:#16a34a;">{dq_score}%</div>
        <div class="exec-note">Enterprise data trust readiness</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="exec-card" style="border-top-color:#9333ea;">
        <div class="exec-title">Governance Readiness</div>
        <div class="exec-value" style="color:#9333ea;">{governance_score}%</div>
        <div class="exec-note">Policy, stewardship, and accountability maturity</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)

with c4:
    st.markdown(f"""
    <div class="exec-card" style="border-top-color:#14b8a6;">
        <div class="exec-title">Interoperability Readiness</div>
        <div class="exec-value" style="color:#14b8a6;">{interop_score}%</div>
        <div class="exec-note">FHIR, terminology, and integration maturity</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class="exec-card" style="border-top-color:#f97316;">
        <div class="exec-title">AI Governance Readiness</div>
        <div class="exec-value" style="color:#f97316;">{ai_score}%</div>
        <div class="exec-note">Bias, drift, explainability, and model oversight</div>
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown(f"""
    <div class="exec-card" style="border-top-color:#db2777;">
        <div class="exec-title">Transformation Readiness</div>
        <div class="exec-value" style="color:#db2777;">{transformation_score}%</div>
        <div class="exec-note">Digital health transformation execution capability</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# Executive Interpretation
# =====================================================

st.markdown('<div class="section-title">Executive Interpretation</div>', unsafe_allow_html=True)

st.info("""
HealthDataIQ™ indicates a strong healthcare informatics foundation with mature data quality,
established governance structures, emerging responsible AI governance, and expanding
interoperability capability.

The organization is positioned to move from connected healthcare informatics capability
toward intelligent and transformational digital health maturity.
""")

# =====================================================
# Strategic Priorities
# =====================================================

st.markdown('<div class="section-title">Strategic Priorities</div>', unsafe_allow_html=True)

priority_df = pd.DataFrame({
    "Priority": [
        "Strengthen Responsible AI Governance",
        "Scale FHIR Interoperability",
        "Expand Metadata Lineage",
        "Develop Healthcare Knowledge Graph",
        "Operationalize Transformation Value Tracking"
    ],
    "Executive Owner": [
        "Chief AI Officer",
        "CIO / Integration Office",
        "Chief Data Officer",
        "Chief Data & AI Officer",
        "Chief Transformation Officer"
    ],
    "Strategic Value": [
        "Improves trust, safety, explainability, and compliance of AI systems",
        "Enables modern healthcare data exchange and ecosystem integration",
        "Improves transparency, traceability, and governed use of data assets",
        "Connects data, terminology, FHIR, KPIs, AI models, and dashboards",
        "Links transformation initiatives to measurable business outcomes"
    ],
    "Priority Level": [
        "High",
        "High",
        "Medium",
        "Medium",
        "High"
    ]
})

st.dataframe(
    priority_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# Board-Level Recommendation
# =====================================================

st.markdown('<div class="section-title">Board-Level Recommendation</div>', unsafe_allow_html=True)

st.success("""
HealthDataIQ™ recommends prioritizing Responsible AI Governance, FHIR interoperability scaling,
metadata lineage expansion, and transformation value tracking over the next 12 months.

These initiatives will strengthen trust, improve executive visibility, reduce informatics risk,
and prepare the organization for advanced healthcare AI and learning health system capabilities.
""")