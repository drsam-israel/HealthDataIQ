import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🧭",
    "Healthcare AI Governance Operating Model",
    "Board-level operating model for governing healthcare AI ownership, approval, monitoring, safety, risk, and value realization."
)

# =====================================================
# Executive AI Governance Scorecard
# =====================================================

st.markdown('<div class="section-title">Executive AI Governance Scorecard</div>', unsafe_allow_html=True)

st.markdown("""
<style>
.govai-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
    min-height: 145px;
}
.govai-title {
    font-size: 16px;
    font-weight: 900;
    color: #0b1f3a;
}
.govai-value {
    font-size: 38px;
    font-weight: 900;
    margin-top: 10px;
}
.govai-note {
    font-size: 14px;
    color: #475569;
    margin-top: 10px;
    line-height: 1.4;
}
</style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="govai-card">
        <div class="govai-title">🤖 Governed Models</div>
        <div class="govai-value" style="color:#0066ff;">5</div>
        <div class="govai-note">AI models registered under governance oversight</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="govai-card" style="border-top-color:#16a34a;">
        <div class="govai-title">✅ Approved Models</div>
        <div class="govai-value" style="color:#16a34a;">4</div>
        <div class="govai-note">Models approved for operational or clinical use</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="govai-card" style="border-top-color:#ef4444;">
        <div class="govai-title">⚠️ High-Risk Models</div>
        <div class="govai-value" style="color:#ef4444;">2</div>
        <div class="govai-note">Models requiring enhanced clinical safety oversight</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)

with c4:
    st.markdown("""
    <div class="govai-card" style="border-top-color:#9333ea;">
        <div class="govai-title">🛡️ Responsible AI Score</div>
        <div class="govai-value" style="color:#9333ea;">92%</div>
        <div class="govai-note">Fairness, explainability, transparency, and accountability readiness</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="govai-card" style="border-top-color:#f97316;">
        <div class="govai-title">📋 AI Compliance Score</div>
        <div class="govai-value" style="color:#f97316;">88%</div>
        <div class="govai-note">Policy, documentation, validation, and audit alignment</div>
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="govai-card" style="border-top-color:#14b8a6;">
        <div class="govai-title">🔍 AI Audit Readiness</div>
        <div class="govai-value" style="color:#14b8a6;">High</div>
        <div class="govai-note">Readiness for executive, compliance, and clinical safety review</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# Governance Structure
# =====================================================

st.markdown('<div class="section-title">AI Governance Structure</div>', unsafe_allow_html=True)

structure_df = pd.DataFrame({
    "Governance Layer": [
        "Board Oversight",
        "AI Steering Committee",
        "Responsible AI Council",
        "Model Risk Committee",
        "Clinical Review Board",
        "AI Operations Team"
    ],
    "Primary Role": [
        "Executive accountability and strategic risk oversight",
        "AI strategy, investment prioritization, and portfolio direction",
        "Fairness, transparency, explainability, privacy, and ethics review",
        "Technical validation, performance monitoring, and risk classification",
        "Clinical safety, patient impact, workflow fit, and escalation review",
        "Operational monitoring, incident response, drift alerts, and reporting"
    ],
    "Typical Members": [
        "CEO, Board, C-suite",
        "CIO, CDAO, CAIO, CMO, COO",
        "AI Governance Lead, Compliance, Legal, Privacy, Clinical Informatics",
        "Data Science, ML Engineering, Risk, Cybersecurity",
        "CMO, CMIO, Clinical Leads, Quality & Safety",
        "MLOps, Data Engineering, Analytics, AI Governance Office"
    ]
})

st.dataframe(
    structure_df,
    use_container_width=True,
    hide_index=True,
    height=320
)

# =====================================================
# AI Lifecycle Governance
# =====================================================

st.markdown('<div class="section-title">AI Lifecycle Governance</div>', unsafe_allow_html=True)

lifecycle_df = pd.DataFrame({
    "Lifecycle Stage": [
        "Ideation",
        "Design",
        "Development",
        "Validation",
        "Approval",
        "Deployment",
        "Monitoring",
        "Retirement"
    ],
    "Governance Control": [
        "Business case and clinical relevance review",
        "Data, privacy, workflow, and risk design assessment",
        "Development standards, documentation, and model traceability",
        "Technical validation, clinical validation, bias and explainability review",
        "Formal approval by governance and clinical safety bodies",
        "Controlled implementation with monitoring and escalation pathways",
        "Drift, bias, performance, safety, and value monitoring",
        "Model decommissioning, replacement, or retraining decision"
    ],
    "Executive Question Answered": [
        "Should we build or buy this AI capability?",
        "Is this AI designed safely and responsibly?",
        "Can we trust how the model was developed?",
        "Is the model safe, fair, and effective?",
        "Who approved this AI for use?",
        "How will this AI be safely deployed?",
        "Is the model still safe and valuable?",
        "When should the model be retired or replaced?"
    ]
})

st.dataframe(
    lifecycle_df,
    use_container_width=True,
    hide_index=True,
    height=360
)

# =====================================================
# AI Risk Classification
# =====================================================

st.markdown('<div class="section-title">AI Risk Classification Framework</div>', unsafe_allow_html=True)

risk_df = pd.DataFrame({
    "Risk Tier": [
        "Tier 1",
        "Tier 2",
        "Tier 3",
        "Tier 4"
    ],
    "Classification": [
        "Administrative AI",
        "Operational AI",
        "Clinical Decision Support AI",
        "Autonomous Clinical AI"
    ],
    "Healthcare Example": [
        "Appointment reminders, document routing, coding assistance",
        "Capacity forecasting, claims analytics, workflow optimization",
        "Sepsis prediction, readmission risk, mortality risk prediction",
        "Autonomous diagnosis, autonomous treatment recommendation"
    ],
    "Governance Requirement": [
        "Basic monitoring and documentation",
        "Model registry, performance review, and operational validation",
        "Clinical validation, explainability, bias review, and safety monitoring",
        "Restricted deployment, enhanced oversight, regulatory review, human supervision"
    ]
})

st.dataframe(
    risk_df,
    use_container_width=True,
    hide_index=True,
    height=260
)

# =====================================================
# Responsible AI Framework
# =====================================================

st.markdown('<div class="section-title">Responsible AI Framework</div>', unsafe_allow_html=True)

rai_df = pd.DataFrame({
    "Responsible AI Dimension": [
        "Fairness",
        "Transparency",
        "Explainability",
        "Accountability",
        "Privacy",
        "Clinical Safety"
    ],
    "Current Status": [
        "Managed",
        "Managed",
        "Advanced",
        "Managed",
        "Advanced",
        "Advanced"
    ],
    "Governance Meaning": [
        "AI performance is assessed across demographic and clinical subgroups",
        "Model purpose, assumptions, data use, and limitations are documented",
        "Model outputs can be interpreted through feature attribution and explanation methods",
        "Named owners and committees are responsible for AI approval and oversight",
        "Patient data protection, access controls, and privacy-by-design are enforced",
        "Clinical impact, escalation, and patient safety risks are reviewed continuously"
    ]
})

st.dataframe(
    rai_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# Strategic Recommendations
# =====================================================

st.markdown('<div class="section-title">Strategic AI Governance Recommendations</div>', unsafe_allow_html=True)

recommendations = [
    "Establish an Enterprise AI Steering Committee with executive-level accountability.",
    "Formalize AI approval workflow from ideation through retirement.",
    "Implement AI incident management and escalation pathways.",
    "Deploy continuous model monitoring for drift, bias, performance, and safety.",
    "Define clinical AI safety review procedures before production deployment.",
    "Establish an Enterprise AI Center of Excellence to coordinate strategy, governance, delivery, and value realization."
]

for item in recommendations:
    st.success(item)

st.divider()

# =====================================================
# Executive Interpretation
# =====================================================

st.markdown('<div class="section-title">Executive Interpretation</div>', unsafe_allow_html=True)

st.info("""
The Healthcare AI Governance Operating Model defines how healthcare AI should be owned,
approved, monitored, audited, escalated, and retired.

This page shifts HealthDataIQ™ from AI model tracking into enterprise AI leadership by
connecting governance structures, responsible AI principles, clinical safety oversight,
model risk classification, lifecycle controls, executive accountability, and value realization.
""")