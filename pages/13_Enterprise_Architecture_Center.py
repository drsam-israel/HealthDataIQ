import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "🏛️",
    "Enterprise Architecture Center",
    "Visualize business, data, application, integration, AI, technology, and executive intelligence architectures."
)

# =====================================================
# Executive Architecture Blueprint
# =====================================================

st.markdown('<div class="section-title">Executive Architecture Blueprint</div>', unsafe_allow_html=True)

st.info("""
Business Architecture
        ↓
Data Architecture
        ↓
Application Architecture
        ↓
Integration Layer (FHIR • HL7 • APIs • ETL)
        ↓
Analytics & AI Layer
        ↓
Executive Intelligence Layer
""")

# =====================================================
# Architecture Domains
# =====================================================

st.markdown('<div class="section-title">Enterprise Architecture Domains</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Business Architecture",
    "Data Architecture",
    "Application Architecture",
    "Integration Architecture",
    "AI Architecture",
    "Technology Architecture"
])

with tab1:
    business_df = pd.DataFrame({
        "Capability": [
            "Patient Care",
            "Population Health",
            "Revenue Cycle",
            "Quality Management",
            "Digital Transformation"
        ],
        "Owner": [
            "Clinical Operations",
            "Population Health",
            "Finance",
            "Quality Office",
            "Executive Office"
        ],
        "Strategic Purpose": [
            "Deliver safe and effective patient care",
            "Improve community and population outcomes",
            "Optimize claims, billing, and reimbursement",
            "Monitor quality, safety, and clinical performance",
            "Drive enterprise digital transformation"
        ]
    })

    st.dataframe(
        business_df,
        use_container_width=True,
        hide_index=True,
        height=300
    )

with tab2:
    data_df = pd.DataFrame({
        "Data Domain": [
            "Demographics",
            "Clinical",
            "Laboratory",
            "Operations",
            "Financial",
            "Quality"
        ],
        "Data Steward": [
            "Health Information Management",
            "Clinical Informatics",
            "Laboratory Services",
            "Operations",
            "Finance",
            "Quality Management"
        ],
        "Governance Focus": [
            "Identity, attribution, and patient matching",
            "Clinical documentation and outcomes",
            "Lab quality, results, and terminology mapping",
            "Capacity, flow, utilization, and efficiency",
            "Revenue, cost, claims, and financial performance",
            "Safety, readmissions, mortality, and improvement"
        ]
    })

    st.dataframe(
        data_df,
        use_container_width=True,
        hide_index=True,
        height=300
    )

with tab3:
    application_df = pd.DataFrame({
        "Application": [
            "Electronic Health Record",
            "Laboratory Information System",
            "Enterprise Resource Planning",
            "Business Intelligence Platform",
            "HealthDataIQ™"
        ],
        "Category": [
            "Clinical",
            "Laboratory",
            "Enterprise",
            "Analytics",
            "Healthcare Informatics"
        ],
        "Role in Architecture": [
            "Primary clinical documentation and care delivery system",
            "Laboratory ordering, results, and diagnostics workflow",
            "Finance, HR, supply chain, and enterprise operations",
            "Executive reporting and performance intelligence",
            "Governance, metadata, interoperability, AI governance, and transformation intelligence"
        ]
    })

    st.dataframe(
        application_df,
        use_container_width=True,
        hide_index=True,
        height=300
    )

with tab4:
    integration_df = pd.DataFrame({
        "Integration Service": [
            "FHIR APIs",
            "HL7 Interfaces",
            "Master Patient Index",
            "Terminology Service",
            "API Gateway"
        ],
        "Standard / Pattern": [
            "FHIR R4",
            "HL7 v2",
            "Enterprise Patient Identity",
            "SNOMED CT / LOINC / ICD / RxNorm",
            "REST API"
        ],
        "Purpose": [
            "Enable modern healthcare data exchange",
            "Support legacy clinical system messaging",
            "Resolve patient identity across systems",
            "Standardize clinical meaning and semantic interoperability",
            "Manage secure API access and integration orchestration"
        ]
    })

    st.dataframe(
        integration_df,
        use_container_width=True,
        hide_index=True,
        height=300
    )

with tab5:
    ai_df = pd.DataFrame({
        "AI Service": [
            "SepsisIntel AI",
            "Clinical NLP",
            "Readmission Prediction",
            "Executive Copilot",
            "Responsible AI Monitor"
        ],
        "Purpose": [
            "Clinical early warning and risk prediction",
            "Clinical documentation and unstructured text intelligence",
            "Quality improvement and care transition risk identification",
            "Executive decision support and strategic intelligence",
            "Bias, drift, explainability, and AI governance monitoring"
        ],
        "Governance Requirement": [
            "High-risk clinical AI governance",
            "Privacy, accuracy, and clinical validation",
            "Bias monitoring and outcome review",
            "Human oversight and accountability",
            "Continuous monitoring and risk management"
        ]
    })

    st.dataframe(
        ai_df,
        use_container_width=True,
        hide_index=True,
        height=300
    )

with tab6:
    technology_df = pd.DataFrame({
        "Technology Layer": [
            "Cloud Platform",
            "Data Lake",
            "Database",
            "Analytics Platform",
            "AI Platform",
            "Security Layer"
        ],
        "Representative Technology": [
            "Azure / AWS / GCP",
            "Enterprise Data Lake",
            "SQL Server / PostgreSQL",
            "Power BI / Tableau / Streamlit",
            "Azure ML / Vertex AI / SageMaker",
            "IAM, RBAC, Audit Logging"
        ],
        "Enterprise Role": [
            "Scalable hosting and enterprise infrastructure",
            "Centralized storage for structured and unstructured data",
            "Governed relational data and metadata persistence",
            "Dashboards, reporting, and decision intelligence",
            "Model development, deployment, and monitoring",
            "Privacy, compliance, access control, and trust"
        ]
    })

    st.dataframe(
        technology_df,
        use_container_width=True,
        hide_index=True,
        height=300
    )

# =====================================================
# Executive Interpretation
# =====================================================

st.markdown('<div class="section-title">Executive Interpretation</div>', unsafe_allow_html=True)

st.info("""
HealthDataIQ™ Enterprise Architecture demonstrates alignment between business capabilities,
governed data assets, enterprise applications, interoperability services, AI platforms,
technology infrastructure, and executive intelligence capabilities.

This architecture provides a foundation for enterprise digital health transformation,
responsible AI adoption, healthcare interoperability, metadata governance, and
data-driven decision-making.
""")

# =====================================================
# Strategic Architecture Assessment
# =====================================================

st.markdown('<div class="section-title">Strategic Architecture Assessment</div>', unsafe_allow_html=True)

assessment_df = pd.DataFrame({
    "Architecture Domain": [
        "Business Architecture",
        "Data Architecture",
        "Application Architecture",
        "Interoperability Architecture",
        "AI Architecture",
        "Executive Intelligence"
    ],
    "Current Assessment": [
        "Established",
        "Mature",
        "Integrated",
        "Advanced",
        "Emerging",
        "Advanced"
    ],
    "Strategic Priority": [
        "Align transformation goals with care delivery priorities",
        "Strengthen enterprise metadata, data quality, and stewardship",
        "Rationalize application portfolio and reduce fragmentation",
        "Scale FHIR APIs, terminology services, and integration governance",
        "Operationalize responsible AI governance and clinical safety monitoring",
        "Expand decision intelligence and transformation value tracking"
    ]
})

st.dataframe(
    assessment_df,
    use_container_width=True,
    hide_index=True,
    height=300
)

st.success("""
Overall Architecture Readiness: HIGH

HealthDataIQ™ provides a consulting-grade enterprise architecture foundation
for healthcare informatics, interoperability, responsible AI governance,
executive intelligence, and digital health transformation.
""")