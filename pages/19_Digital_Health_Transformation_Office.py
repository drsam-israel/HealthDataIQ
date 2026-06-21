import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🚀",
    "Digital Health Transformation Office",
    "Executive oversight of transformation programs, value realization, strategic execution, and organizational readiness."
)

# =====================================================
# Executive Transformation Dashboard
# =====================================================

st.markdown('<div class="section-title">Executive Transformation Dashboard</div>', unsafe_allow_html=True)

st.markdown("""
<style>
.transform-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 8px 22px rgba(15,23,42,0.06);
    min-height: 145px;
}
.transform-title {
    font-size: 16px;
    font-weight: 900;
    color: #0b1f3a;
}
.transform-value {
    font-size: 38px;
    font-weight: 900;
    margin-top: 10px;
}
.transform-note {
    font-size: 14px;
    color: #475569;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="transform-card">
        <div class="transform-title">📂 Programs</div>
        <div class="transform-value" style="color:#0066ff;">12</div>
        <div class="transform-note">Active transformation initiatives</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="transform-card" style="border-top-color:#16a34a;">
        <div class="transform-title">✅ Completed</div>
        <div class="transform-value" style="color:#16a34a;">8</div>
        <div class="transform-note">Programs successfully delivered</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="transform-card" style="border-top-color:#f97316;">
        <div class="transform-title">💰 Benefits Realized</div>
        <div class="transform-value" style="color:#f97316;">$12.4M</div>
        <div class="transform-note">Annual transformation value</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="transform-card" style="border-top-color:#9333ea;">
        <div class="transform-title">📈 Readiness</div>
        <div class="transform-value" style="color:#9333ea;">88%</div>
        <div class="transform-note">Transformation execution readiness</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# Transformation Portfolio
# =====================================================

st.markdown('<div class="section-title">Transformation Portfolio</div>', unsafe_allow_html=True)

portfolio_df = pd.DataFrame({
    "Program":[
        "Enterprise Data Governance",
        "FHIR Modernization",
        "AI Governance Program",
        "Executive Intelligence Platform",
        "Digital Front Door"
    ],
    "Status":[
        "Active",
        "Active",
        "Active",
        "Active",
        "Planned"
    ],
    "Executive Sponsor":[
        "CIO",
        "Chief Data Officer",
        "CDAIO",
        "COO",
        "CEO"
    ],
    "Strategic Outcome":[
        "Trusted enterprise data",
        "Connected healthcare ecosystem",
        "Responsible AI adoption",
        "Executive decision intelligence",
        "Patient digital engagement"
    ]
})

st.dataframe(
    portfolio_df,
    use_container_width=True,
    hide_index=True,
    height=260
)

# =====================================================
# Transformation Value Realization
# =====================================================

st.markdown('<div class="section-title">Transformation Value Realization</div>', unsafe_allow_html=True)

value_df = pd.DataFrame({
    "Initiative":[
        "Data Governance",
        "Interoperability",
        "AI Enablement",
        "Executive Intelligence",
        "Workflow Automation"
    ],
    "Annual Value":[
        "$2.1M",
        "$3.4M",
        "$4.2M",
        "$1.5M",
        "$1.2M"
    ],
    "Business Outcome":[
        "Improved trust and compliance",
        "Improved data exchange",
        "Clinical and operational intelligence",
        "Faster executive decision making",
        "Operational efficiency"
    ]
})

st.dataframe(
    value_df,
    use_container_width=True,
    hide_index=True,
    height=260
)

# =====================================================
# Transformation Maturity
# =====================================================

st.markdown('<div class="section-title">Transformation Maturity</div>', unsafe_allow_html=True)

st.success("Current Transformation Maturity: Level 4 — Enterprise Transformation Enabled")

st.progress(0.88)

st.info("""
The organization demonstrates strong transformation capability supported by governance,
enterprise architecture, interoperability, AI governance, executive intelligence,
and measurable value realization.
""")

# =====================================================
# Transformation Risk Register
# =====================================================

st.markdown('<div class="section-title">Transformation Risk Register</div>', unsafe_allow_html=True)

risk_df = pd.DataFrame({
    "Risk":[
        "Change Resistance",
        "Skills Shortage",
        "Data Quality Gaps",
        "Funding Constraints",
        "Governance Fragmentation"
    ],
    "Severity":[
        "High",
        "High",
        "Medium",
        "Medium",
        "Medium"
    ],
    "Executive Impact":[
        "Reduced adoption",
        "Delayed execution",
        "Poor decision quality",
        "Program slowdown",
        "Reduced accountability"
    ],
    "Mitigation":[
        "Change management program",
        "Workforce development",
        "Data quality framework",
        "Value-based investment model",
        "Enterprise governance office"
    ]
})

st.dataframe(
    risk_df,
    use_container_width=True,
    hide_index=True,
    height=280
)

# =====================================================
# Strategic Transformation Roadmap
# =====================================================

st.markdown('<div class="section-title">Strategic Transformation Roadmap</div>', unsafe_allow_html=True)

roadmap_df = pd.DataFrame({
    "Year":[
        "2026",
        "2027",
        "2028",
        "2029",
        "2030"
    ],
    "Strategic Focus":[
        "Governance Foundation",
        "Interoperability Expansion",
        "Enterprise AI Scale-Up",
        "Learning Health System",
        "Intelligent Enterprise"
    ],
    "Expected Outcome":[
        "Trusted enterprise governance",
        "Connected healthcare ecosystem",
        "Responsible AI at scale",
        "Continuous learning and improvement",
        "AI-enabled health system"
    ]
})

st.dataframe(
    roadmap_df,
    use_container_width=True,
    hide_index=True,
    height=260
)

# =====================================================
# Executive Interpretation
# =====================================================

st.markdown('<div class="section-title">Executive Interpretation</div>', unsafe_allow_html=True)

st.success("""
The Digital Health Transformation Office provides executive visibility into
transformation programs, value realization, strategic risks, maturity,
and organizational readiness.

This capability enables healthcare leaders to govern transformation
as a portfolio of measurable investments rather than isolated projects.
""")