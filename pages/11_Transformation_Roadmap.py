import streamlit as st
from assets.styles import load_css, page_header

load_css()

page_header(
    "🗺️",
    "Transformation Roadmap",
    "Generate a consulting-grade roadmap using the HealthDataIQ™ Healthcare Informatics Maturity Model (HI2M)."
)

levels = [
    "Level 1 — Fragmented",
    "Level 2 — Governed",
    "Level 3 — Connected",
    "Level 4 — Intelligent",
    "Level 5 — Transformational"
]

current = st.selectbox(
    "Current Maturity Level",
    levels[:-1]
)

target = st.selectbox(
    "Target Maturity Level",
    levels[1:],
    index=2
)

st.info(
    "HI2M is inspired by HIMSS digital maturity thinking, DAMA-DMBOK data governance principles, CMMI capability maturity concepts, and modern digital health transformation frameworks."
)

st.markdown('<div class="section-title">Recommended Transformation Roadmap</div>', unsafe_allow_html=True)

roadmap = {
    "Level 1 — Fragmented": {
        "Governance": [
            "Establish Data Governance Office",
            "Define data owners and data stewards",
            "Approve enterprise data governance policy"
        ],
        "Metadata": [
            "Create enterprise data dictionary",
            "Develop business glossary",
            "Document priority data assets"
        ],
        "Interoperability": [
            "Assess current HL7/FHIR readiness",
            "Identify priority integration gaps"
        ],
        "Analytics": [
            "Define executive KPI catalog",
            "Standardize clinical and operational metrics"
        ],
        "AI Governance": [
            "Create AI model inventory",
            "Define responsible AI governance principles"
        ]
    },
    "Level 2 — Governed": {
        "Governance": [
            "Expand governance coverage across domains",
            "Implement data quality monitoring",
            "Create governance reporting dashboard"
        ],
        "Metadata": [
            "Deploy metadata repository",
            "Implement lineage documentation",
            "Certify critical data elements"
        ],
        "Interoperability": [
            "Develop FHIR mapping repository",
            "Standardize terminology crosswalks",
            "Prioritize API-enabled integration"
        ],
        "Analytics": [
            "Deploy operational and clinical dashboards",
            "Implement KPI ownership and review cycles"
        ],
        "AI Governance": [
            "Develop AI model registry",
            "Define bias and explainability review process"
        ]
    },
    "Level 3 — Connected": {
        "Governance": [
            "Integrate governance into analytics and AI workflows",
            "Monitor compliance and accountability metrics"
        ],
        "Metadata": [
            "Expand metadata coverage enterprise-wide",
            "Connect metadata to dashboards and AI models"
        ],
        "Interoperability": [
            "Scale FHIR APIs",
            "Implement terminology services",
            "Monitor interoperability performance"
        ],
        "Analytics": [
            "Deploy executive intelligence dashboards",
            "Enable predictive analytics use cases"
        ],
        "AI Governance": [
            "Operationalize AI risk classification",
            "Implement drift monitoring",
            "Deploy explainability reporting"
        ]
    },
    "Level 4 — Intelligent": {
        "Governance": [
            "Institutionalize continuous governance improvement",
            "Link governance performance to executive scorecards"
        ],
        "Metadata": [
            "Develop knowledge graph capabilities",
            "Implement semantic asset relationships"
        ],
        "Interoperability": [
            "Optimize FHIR-enabled ecosystem exchange",
            "Expand national or regional interoperability readiness"
        ],
        "Analytics": [
            "Deploy advanced decision intelligence",
            "Implement scenario modeling and forecasting"
        ],
        "AI Governance": [
            "Scale responsible AI across enterprise",
            "Integrate clinical AI safety monitoring",
            "Track AI value realization"
        ]
    }
}

selected_plan = roadmap.get(current, {})

for domain, initiatives in selected_plan.items():
    st.markdown(f"### {domain}")
    for item in initiatives:
        st.success(item)

st.divider()

c1, c2 = st.columns(2)

c1.metric("Current State", current)
c2.metric("Target State", target)

st.markdown("### Strategic Positioning")

st.write(
    "This roadmap supports the transition from fragmented healthcare data environments toward governed, connected, intelligent, and transformational healthcare informatics capability."
)