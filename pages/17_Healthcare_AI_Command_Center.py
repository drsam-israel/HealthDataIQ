import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🤖",
    "Healthcare AI Command Center",
    "Executive view of healthcare AI portfolio, responsible AI readiness, model risk, business value, and AI transformation priorities."
)

# =====================================================
# Executive AI Scorecard
# =====================================================

st.markdown('<div class="section-title">Executive AI Scorecard</div>', unsafe_allow_html=True)

st.markdown("""
<style>
.ai-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
    min-height: 145px;
}
.ai-title {
    font-size: 16px;
    font-weight: 900;
    color: #0b1f3a;
}
.ai-value {
    font-size: 38px;
    font-weight: 900;
    margin-top: 10px;
}
.ai-note {
    font-size: 14px;
    color: #475569;
    margin-top: 10px;
    line-height: 1.4;
}
</style>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="ai-card">
        <div class="ai-title">🤖 AI Models</div>
        <div class="ai-value" style="color:#0066ff;">5</div>
        <div class="ai-note">Enterprise AI portfolio assets</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="ai-card" style="border-top-color:#16a34a;">
        <div class="ai-title">✅ Approved Models</div>
        <div class="ai-value" style="color:#16a34a;">4</div>
        <div class="ai-note">Models approved for operational use</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="ai-card" style="border-top-color:#9333ea;">
        <div class="ai-title">🛡️ Responsible AI Score</div>
        <div class="ai-value" style="color:#9333ea;">92%</div>
        <div class="ai-note">Governance, fairness, transparency, and monitoring readiness</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="ai-card" style="border-top-color:#f97316;">
        <div class="ai-title">💰 Annual AI Value</div>
        <div class="ai-value" style="color:#f97316;">$5.2M</div>
        <div class="ai-note">Estimated annual value realization</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# AI Portfolio Registry
# =====================================================

st.markdown('<div class="section-title">AI Portfolio Registry</div>', unsafe_allow_html=True)

portfolio_df = pd.DataFrame({
    "AI Model": [
        "SepsisIntel AI",
        "Readmission AI",
        "Mortality Risk AI",
        "Capacity Forecast AI",
        "Claims Fraud AI"
    ],
    "Domain": [
        "Clinical",
        "Quality",
        "Clinical",
        "Operations",
        "Revenue Cycle"
    ],
    "Status": [
        "Production",
        "Production",
        "Production",
        "Pilot",
        "Pilot"
    ],
    "Accuracy": [
        "90.2%",
        "88.7%",
        "91.4%",
        "86.5%",
        "89.2%"
    ],
    "Risk Tier": [
        "High",
        "Medium",
        "High",
        "Medium",
        "Medium"
    ],
    "Executive Owner": [
        "CMO",
        "Chief Quality Officer",
        "CMO",
        "COO",
        "CFO"
    ]
})

st.dataframe(
    portfolio_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# Responsible AI Governance Scorecard
# =====================================================

st.markdown('<div class="section-title">Responsible AI Governance Scorecard</div>', unsafe_allow_html=True)

rai_df = pd.DataFrame({
    "Governance Dimension": [
        "Fairness",
        "Explainability",
        "Transparency",
        "Monitoring",
        "Accountability"
    ],
    "Score": [
        91,
        95,
        94,
        89,
        92
    ],
    "Executive Meaning": [
        "Bias and equity risks are actively assessed",
        "Model decisions can be interpreted by stakeholders",
        "Documentation and intended use are clearly defined",
        "Performance, drift, and risk are monitored",
        "Ownership, review, and escalation responsibilities are assigned"
    ]
})

st.dataframe(
    rai_df,
    use_container_width=True,
    hide_index=True,
    height=280
)

rai_score = round(rai_df["Score"].mean())
st.success(f"Overall Responsible AI Readiness: {rai_score}%")

# =====================================================
# AI Value Realization
# =====================================================

st.markdown('<div class="section-title">AI Value Realization</div>', unsafe_allow_html=True)

value_df = pd.DataFrame({
    "AI Capability": [
        "Sepsis Detection",
        "Readmission Reduction",
        "Capacity Optimization",
        "Fraud Detection",
        "Workflow Automation"
    ],
    "Estimated Annual Value": [
        "$1.8M",
        "$1.2M",
        "$900K",
        "$800K",
        "$500K"
    ],
    "Value Driver": [
        "Earlier detection and improved clinical outcomes",
        "Reduced avoidable readmissions and penalties",
        "Improved bed utilization and operational efficiency",
        "Reduced claims leakage and financial loss",
        "Reduced administrative burden and cycle time"
    ]
})

st.dataframe(
    value_df,
    use_container_width=True,
    hide_index=True,
    height=280
)

# =====================================================
# AI Risk Register
# =====================================================

st.markdown('<div class="section-title">Executive AI Risk Register</div>', unsafe_allow_html=True)

risk_df = pd.DataFrame({
    "AI Risk": [
        "Model Drift",
        "Data Bias",
        "Explainability Gaps",
        "Regulatory Exposure",
        "Third-Party AI Dependency"
    ],
    "Severity": [
        "Medium",
        "Medium",
        "Low",
        "Medium",
        "High"
    ],
    "Executive Impact": [
        "Declining performance over time may affect reliability",
        "Unequal model performance may increase equity and safety risks",
        "Limited interpretability may reduce clinician trust",
        "AI use may create compliance and liability exposure",
        "External vendors may introduce operational, security, and governance risks"
    ],
    "Recommended Control": [
        "Continuous performance and drift monitoring",
        "Bias assessment across demographic and clinical subgroups",
        "SHAP, feature attribution, and model documentation",
        "Formal AI governance review and audit process",
        "Vendor risk assessment and contractual AI governance controls"
    ]
})

st.dataframe(
    risk_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# AI Maturity
# =====================================================

st.markdown('<div class="section-title">Healthcare AI Maturity</div>', unsafe_allow_html=True)

st.success("Current AI Maturity: Level 4 — Enterprise AI Enabled")
st.progress(0.82)

st.write("""
**Interpretation:** The organization demonstrates strong healthcare AI capability with a defined model portfolio,
emerging responsible AI governance, production clinical AI use cases, and measurable business value.
Remaining priorities include continuous monitoring, enterprise AI governance scaling, and healthcare LLM readiness.
""")

# =====================================================
# Strategic AI Roadmap
# =====================================================

st.markdown('<div class="section-title">Strategic Healthcare AI Roadmap</div>', unsafe_allow_html=True)

recommendations = [
    "Scale clinical AI across priority service lines.",
    "Establish enterprise model monitoring for drift, bias, and performance degradation.",
    "Expand responsible AI governance with formal review, approval, and escalation pathways.",
    "Deploy healthcare LLM governance before introducing generative AI into clinical workflows.",
    "Enable AI-assisted clinical decision support with human oversight and safety controls.",
    "Implement an Enterprise AI Center of Excellence for healthcare AI strategy, governance, and value realization."
]

for item in recommendations:
    st.success(item)

st.divider()

# =====================================================
# Executive Interpretation
# =====================================================

st.markdown('<div class="section-title">Executive Interpretation</div>', unsafe_allow_html=True)

st.info("""
The Healthcare AI Command Center positions HealthDataIQ™ as an executive platform for monitoring
AI portfolio maturity, responsible AI readiness, clinical AI risk, and business value realization.

This capability supports healthcare AI strategy, responsible AI governance, clinical safety,
executive oversight, and enterprise digital health transformation.
""")