import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "✅",
    "Data Quality Center",
    "Assess enterprise healthcare data quality across completeness, accuracy, consistency, timeliness, validity, and trust readiness."
)

# =====================================================
# Executive Data Quality Scorecard
# =====================================================

quality_scores = {
    "Completeness": 92,
    "Accuracy": 89,
    "Consistency": 94,
    "Timeliness": 87,
    "Validity": 96,
}

overall_score = round(sum(quality_scores.values()) / len(quality_scores))
trust_readiness = "High" if overall_score >= 90 else "Moderate"

st.markdown(
    '<div class="section-title">Executive Data Quality Scorecard</div>',
    unsafe_allow_html=True
)

st.markdown("""
<style>
.dq-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 18px 22px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
    min-height: 130px;
}
.dq-title {
    font-size: 15px;
    font-weight: 800;
    color: #0b1f3a;
}
.dq-value {
    font-size: 34px;
    font-weight: 900;
    color: #0066ff;
    margin-top: 8px;
}
.dq-note {
    font-size: 13px;
    color: #475569;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="dq-card">
        <div class="dq-title">Overall DQ Score</div>
        <div class="dq-value">{overall_score}%</div>
        <div class="dq-note">Enterprise data trust score</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="dq-card" style="border-top-color:#9333ea;">
        <div class="dq-title">Quality Dimensions</div>
        <div class="dq-value" style="color:#9333ea;">5</div>
        <div class="dq-note">Completeness, accuracy, consistency, timeliness, validity</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="dq-card" style="border-top-color:#16a34a;">
        <div class="dq-title">Trust Readiness</div>
        <div class="dq-value" style="color:#16a34a;">{trust_readiness}</div>
        <div class="dq-note">Readiness for analytics and AI</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

c4, c5, c6, c7, c8 = st.columns(5)

dimension_cards = [
    ("Completeness", quality_scores["Completeness"], "#2563eb"),
    ("Accuracy", quality_scores["Accuracy"], "#16a34a"),
    ("Consistency", quality_scores["Consistency"], "#9333ea"),
    ("Timeliness", quality_scores["Timeliness"], "#f97316"),
    ("Validity", quality_scores["Validity"], "#db2777"),
]

for col, (label, value, color) in zip([c4, c5, c6, c7, c8], dimension_cards):
    with col:
        st.markdown(f"""
        <div class="dq-card" style="border-top-color:{color}; min-height:115px;">
            <div class="dq-title">{label}</div>
            <div class="dq-value" style="color:{color};">{value}%</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =====================================================
# Quality Dimensions
# =====================================================

st.markdown('<div class="section-title">Data Quality Dimensions</div>', unsafe_allow_html=True)

dimension_df = pd.DataFrame({
    "Dimension": [
        "Completeness",
        "Accuracy",
        "Consistency",
        "Timeliness",
        "Validity"
    ],
    "Definition": [
        "Degree to which required data values are present.",
        "Degree to which data correctly represents real-world clinical or operational facts.",
        "Degree to which data is consistent across systems and reporting layers.",
        "Degree to which data is available within expected timeframes.",
        "Degree to which data conforms to approved formats, rules, and standards."
    ],
    "Healthcare Example": [
        "Missing demographics, missing lab values, incomplete encounter records.",
        "Incorrect date of birth, incorrect diagnosis code, wrong patient attribution.",
        "Mismatch between EHR, data warehouse, and executive dashboards.",
        "Delayed lab results, late claims updates, outdated census data.",
        "Invalid ICD-10, LOINC, SNOMED CT, RxNorm, or FHIR values."
    ]
})

st.dataframe(
    dimension_df,
    use_container_width=True,
    hide_index=True,
    height=280
)

# =====================================================
# Domain Quality Scores
# =====================================================

st.markdown('<div class="section-title">Domain-Level Quality Assessment</div>', unsafe_allow_html=True)

domain_df = pd.DataFrame({
    "Data Domain": [
        "Demographics",
        "Clinical",
        "Laboratory",
        "Medication",
        "Operations",
        "Quality",
        "AI Features"
    ],
    "Completeness": [98, 91, 88, 90, 93, 92, 86],
    "Accuracy": [96, 89, 87, 88, 91, 90, 84],
    "Consistency": [95, 90, 89, 87, 94, 92, 85],
    "Timeliness": [94, 88, 85, 86, 90, 89, 83],
    "Validity": [97, 92, 91, 90, 95, 93, 88]
})

domain_df["Overall Score"] = domain_df[
    ["Completeness", "Accuracy", "Consistency", "Timeliness", "Validity"]
].mean(axis=1).round(1)

st.dataframe(
    domain_df,
    use_container_width=True,
    hide_index=True,
    height=320
)

# =====================================================
# Executive Interpretation
# =====================================================

st.markdown('<div class="section-title">Executive Interpretation</div>', unsafe_allow_html=True)

if overall_score >= 90:
    st.success("""
Enterprise data quality performance is strong and supports advanced analytics,
FHIR interoperability, responsible AI governance, and executive intelligence initiatives.
Priority improvement areas should focus on automation, observability, and continuous monitoring.
""")
elif overall_score >= 75:
    st.warning("""
Enterprise data quality performance is moderate. The organization has a usable data foundation,
but selected domains require improvement before scaling advanced AI, interoperability, and
executive intelligence programs.
""")
else:
    st.error("""
Enterprise data quality performance is weak. Significant improvement is required before
the organization can safely scale analytics, interoperability, executive dashboards, or AI models.
""")

# =====================================================
# Strategic Recommendations
# =====================================================

st.markdown('<div class="section-title">Strategic Data Quality Recommendations</div>', unsafe_allow_html=True)

recommendations = [
    "Implement enterprise data quality scorecards across priority clinical and operational domains.",
    "Define critical data elements and assign accountable data stewards.",
    "Automate validation rules for ICD-10, SNOMED CT, LOINC, RxNorm, and FHIR mappings.",
    "Strengthen laboratory and AI feature completeness monitoring.",
    "Establish recurring Data Quality Council review cycles.",
    "Connect data quality performance to executive intelligence and AI governance readiness."
]

for item in recommendations:
    st.success(item)