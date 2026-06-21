import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🔗",
    "Interoperability Command Center",
    "Executive view of healthcare system connectivity, FHIR adoption, integration maturity, and interoperability risk."
)

# =====================================================
# Executive Interoperability Scorecard
# =====================================================

st.markdown('<div class="section-title">Executive Interoperability Scorecard</div>', unsafe_allow_html=True)

st.markdown("""
<style>
.interop-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
    min-height: 145px;
}
.interop-title {
    font-size: 16px;
    font-weight: 900;
    color: #0b1f3a;
}
.interop-value {
    font-size: 38px;
    font-weight: 900;
    margin-top: 10px;
}
.interop-note {
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
    <div class="interop-card">
        <div class="interop-title">🔄 FHIR APIs</div>
        <div class="interop-value" style="color:#0066ff;">15</div>
        <div class="interop-note">FHIR-enabled exchange services</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="interop-card" style="border-top-color:#16a34a;">
        <div class="interop-title">🔗 Connected Systems</div>
        <div class="interop-value" style="color:#16a34a;">12</div>
        <div class="interop-note">Enterprise systems connected</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="interop-card" style="border-top-color:#9333ea;">
        <div class="interop-title">📡 Daily Transactions</div>
        <div class="interop-value" style="color:#9333ea;">2.5M</div>
        <div class="interop-note">Healthcare exchange transactions</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="interop-card" style="border-top-color:#f97316;">
        <div class="interop-title">📊 Interoperability Score</div>
        <div class="interop-value" style="color:#f97316;">88%</div>
        <div class="interop-note">Enterprise interoperability readiness</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# System Connectivity Matrix
# =====================================================

st.markdown('<div class="section-title">System Connectivity Matrix</div>', unsafe_allow_html=True)

connectivity_df = pd.DataFrame({
    "System": [
        "Electronic Health Record",
        "Laboratory Information System",
        "Radiology / PACS",
        "Claims Platform",
        "ERP / Finance",
        "National Health Information Exchange"
    ],
    "Connection Status": [
        "Connected",
        "Connected",
        "Connected",
        "Connected",
        "Partially Connected",
        "Connected"
    ],
    "Standard": [
        "FHIR",
        "HL7 v2",
        "DICOM",
        "API / X12",
        "API",
        "FHIR"
    ],
    "Strategic Value": [
        "Enables clinical data exchange and longitudinal patient view",
        "Supports laboratory result interoperability",
        "Enables diagnostic imaging access and reporting",
        "Supports claims, billing, and payer exchange",
        "Connects financial and operational intelligence",
        "Enables ecosystem-level data sharing"
    ]
})

st.dataframe(
    connectivity_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# Interoperability Maturity
# =====================================================

st.markdown('<div class="section-title">Interoperability Maturity</div>', unsafe_allow_html=True)

st.success("Current Interoperability Maturity: Level 4 — Connected Enterprise")

st.progress(0.88)

st.write("""
**Interpretation:** The organization demonstrates strong interoperability capability with connected clinical,
laboratory, claims, and health information exchange systems. Remaining priorities include API governance,
terminology normalization, and real-time event streaming.
""")

# =====================================================
# FHIR Resource Adoption
# =====================================================

st.markdown('<div class="section-title">FHIR Resource Adoption</div>', unsafe_allow_html=True)

fhir_df = pd.DataFrame({
    "FHIR Resource": [
        "Patient",
        "Encounter",
        "Observation",
        "Condition",
        "MedicationRequest",
        "Procedure",
        "CarePlan"
    ],
    "Adoption Status": [
        "Implemented",
        "Implemented",
        "Implemented",
        "Implemented",
        "Planned",
        "Planned",
        "Future"
    ],
    "Use Case": [
        "Patient identity and demographic exchange",
        "Encounter and admission-level data exchange",
        "Vital signs, labs, and clinical observations",
        "Diagnosis and problem list interoperability",
        "Medication workflow interoperability",
        "Procedure documentation and exchange",
        "Care coordination and longitudinal planning"
    ]
})

st.dataframe(
    fhir_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# Interoperability Risk Register
# =====================================================

st.markdown('<div class="section-title">Executive Interoperability Risk Register</div>', unsafe_allow_html=True)

risk_df = pd.DataFrame({
    "Risk": [
        "Legacy HL7 Interface Dependency",
        "Incomplete Terminology Mapping",
        "API Version Drift",
        "Duplicate Patient Records",
        "Limited Real-Time Event Streaming"
    ],
    "Severity": [
        "High",
        "Medium",
        "Medium",
        "High",
        "Medium"
    ],
    "Executive Impact": [
        "Increases maintenance burden and integration fragility",
        "Reduces semantic consistency and analytics reliability",
        "Creates technical debt and interoperability instability",
        "Creates safety, reporting, and identity management risks",
        "Limits real-time clinical intelligence and alerting"
    ],
    "Recommended Control": [
        "FHIR migration roadmap",
        "Terminology services layer",
        "API governance framework",
        "Enterprise Master Patient Index",
        "Event streaming architecture"
    ]
})

st.dataframe(
    risk_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

# =====================================================
# Strategic Recommendations
# =====================================================

st.markdown('<div class="section-title">Strategic Interoperability Recommendations</div>', unsafe_allow_html=True)

recommendations = [
    "Expand FHIR APIs to priority external partners and national exchange networks.",
    "Implement Enterprise Master Patient Index to reduce duplicate patient records.",
    "Deploy terminology services for SNOMED CT, LOINC, ICD, and RxNorm normalization.",
    "Establish API governance and version control across integration services.",
    "Enable real-time clinical event streaming for advanced decision support and AI workflows."
]

for item in recommendations:
    st.success(item)

st.divider()

# =====================================================
# Executive Interpretation
# =====================================================

st.markdown('<div class="section-title">Executive Interpretation</div>', unsafe_allow_html=True)

st.info("""
The Interoperability Command Center demonstrates that HealthDataIQ™ can assess how healthcare systems,
standards, APIs, terminology services, and information exchanges connect across the enterprise.

This capability supports digital health transformation, national health data exchange readiness,
FHIR adoption, executive intelligence, and responsible AI enablement.
""")