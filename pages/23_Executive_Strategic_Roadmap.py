import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🧭",
    "Executive Strategic Roadmap",
    "Consulting-grade roadmap translating current maturity, capability gaps, investment priorities, and expected outcomes into an executive transformation plan."
)

# =====================================================
# Current State / Target State
# =====================================================

st.markdown('<div class="section-title">Current State to Target State</div>', unsafe_allow_html=True)

st.markdown("""
<style>
.roadmap-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 8px 22px rgba(15,23,42,0.06);
    min-height: 145px;
}
.roadmap-title {
    font-size: 16px;
    font-weight: 900;
    color: #0b1f3a;
}
.roadmap-value {
    font-size: 17px;
    font-weight: 800;
    margin-top: 10px;
    white-space: nowrap;
}
.roadmap-note {
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
    <div class="roadmap-card">
        <div class="roadmap-title">Current State</div>
        <div class="roadmap-value" style="color:#0066ff;">Level 4 — Intelligent</div>
        <div class="roadmap-note">Strong governance, interoperability, data quality, and emerging responsible AI maturity</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="roadmap-card" style="border-top-color:#16a34a;">
        <div class="roadmap-title">Target State</div>
        <div class="roadmap-value" style="color:#16a34a;">Level 5 — Transformational</div>
        <div class="roadmap-note">Learning health system capability, knowledge graph, AI at scale, and continuous intelligence</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="roadmap-card" style="border-top-color:#9333ea;">
        <div class="roadmap-title">Transformation Horizon</div>
        <div class="roadmap-value" style="color:#9333ea;">2026–2030</div>
        <div class="roadmap-note">Five-year strategic roadmap for healthcare informatics transformation</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# Strategic Gap Analysis
# =====================================================

st.markdown('<div class="section-title">Strategic Gap Analysis</div>', unsafe_allow_html=True)

gap_df = pd.DataFrame({
    "Gap Area": [
        "Metadata Lineage",
        "Healthcare Knowledge Graph",
        "Responsible AI Scale",
        "Learning Health System Capability",
        "Executive Value Tracking",
        "Workforce AI Capability"
    ],
    "Current State": [
        "Partial lineage visibility",
        "Not yet implemented",
        "Governance framework emerging",
        "Not yet operationalized",
        "Value tracked at initiative level",
        "Developing"
    ],
    "Target State": [
        "Enterprise-wide lineage and impact analysis",
        "Semantic intelligence layer connecting data, FHIR, terminology, KPIs, AI, and dashboards",
        "Responsible AI governance scaled across all clinical and operational AI models",
        "Continuous learning and improvement across clinical, operational, and AI systems",
        "Executive value realization linked to strategic investments",
        "Enterprise AI literacy and informatics capability"
    ],
    "Priority": [
        "High",
        "Medium",
        "High",
        "Medium",
        "High",
        "High"
    ]
})

st.dataframe(
    gap_df,
    use_container_width=True,
    hide_index=True,
    height=330
)

# =====================================================
# Five-Year Strategic Roadmap
# =====================================================

st.markdown('<div class="section-title">Five-Year Strategic Roadmap</div>', unsafe_allow_html=True)

roadmap_df = pd.DataFrame({
    "Year": ["2026", "2027", "2028", "2029", "2030"],
    "Strategic Focus": [
        "Governance Foundation",
        "FHIR & Interoperability Expansion",
        "Enterprise AI Enablement",
        "Learning Health System",
        "Intelligent Enterprise"
    ],
    "Key Initiatives": [
        "Strengthen governance, data quality, metadata repository, stewardship, and executive scorecards",
        "Scale FHIR APIs, terminology services, API governance, and national exchange readiness",
        "Deploy AI governance at scale, clinical AI monitoring, model registry, and AI value tracking",
        "Implement knowledge graph, continuous learning loops, real-time intelligence, and outcome monitoring",
        "Operationalize intelligent healthcare enterprise with semantic intelligence and transformation automation"
    ],
    "Expected Outcome": [
        "Trusted healthcare data foundation",
        "Connected healthcare ecosystem",
        "Responsible AI at enterprise scale",
        "Continuous learning and improvement capability",
        "AI-enabled, intelligence-driven healthcare organization"
    ]
})

st.dataframe(
    roadmap_df,
    use_container_width=True,
    hide_index=True,
    height=330
)

# =====================================================
# Investment Priorities
# =====================================================

st.markdown('<div class="section-title">Executive Investment Priorities</div>', unsafe_allow_html=True)

investment_df = pd.DataFrame({
    "Investment Priority": [
        "Data Governance",
        "Interoperability",
        "Responsible AI Governance",
        "Executive Intelligence",
        "Transformation Office",
        "Healthcare Knowledge Graph"
    ],
    "Strategic Rationale": [
        "Improves trust, accountability, compliance, and data stewardship",
        "Enables connected care, FHIR exchange, and ecosystem integration",
        "Ensures safe, explainable, monitored, and accountable AI adoption",
        "Provides executive visibility into quality, operations, AI, and transformation",
        "Coordinates transformation execution, benefits tracking, and roadmap delivery",
        "Connects metadata, terminology, FHIR, KPIs, dashboards, and AI into semantic intelligence"
    ],
    "Priority Level": [
        "High",
        "High",
        "High",
        "High",
        "High",
        "Medium"
    ]
})

st.dataframe(
    investment_df,
    use_container_width=True,
    hide_index=True,
    height=320
)

# =====================================================
# Expected Outcomes
# =====================================================

st.markdown('<div class="section-title">Expected Transformation Outcomes</div>', unsafe_allow_html=True)

outcome_df = pd.DataFrame({
    "Outcome Area": [
        "Data Trust",
        "Connected Care",
        "Responsible AI",
        "Executive Visibility",
        "Operational Efficiency",
        "Digital Health Transformation"
    ],
    "Expected Outcome": [
        "Higher trust in enterprise clinical, operational, and financial data",
        "Improved interoperability across EHR, LIS, claims, public health, and exchange networks",
        "AI models governed through risk classification, explainability, bias monitoring, and clinical safety",
        "Leadership visibility into maturity, risks, transformation value, and strategic priorities",
        "Improved workflow, throughput, automation, and resource utilization",
        "Improved ability to execute enterprise-wide healthcare transformation"
    ]
})

st.dataframe(
    outcome_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# Executive Recommendation
# =====================================================

st.markdown('<div class="section-title">Executive Recommendation</div>', unsafe_allow_html=True)

st.success("""
HealthDataIQ™ recommends a phased 2026–2030 transformation roadmap focused on governance,
FHIR interoperability expansion, responsible AI governance at scale, executive intelligence,
healthcare knowledge graph development, and learning health system capability.

This roadmap positions the organization to move from an intelligent healthcare informatics enterprise
toward transformational maturity, where data, governance, interoperability, AI, and executive intelligence
operate as one integrated healthcare transformation system.
""")