import streamlit as st
from assets.styles import load_css, page_header

load_css()

page_header(
    "📈",
    "Maturity Assessment",
    "HealthDataIQ™ Healthcare Informatics Maturity Model (HI2M), inspired by HIMSS, DAMA-DMBOK, CMMI, and Digital Health Transformation frameworks."
)

st.info(
    "HI2M is a HealthDataIQ™ custom maturity model designed to assess healthcare informatics readiness across governance, metadata, interoperability, analytics, AI governance, and executive intelligence."
)

st.markdown("### HI2M Maturity Levels")

levels = {
    1: "Level 1 — Fragmented",
    2: "Level 2 — Governed",
    3: "Level 3 — Connected",
    4: "Level 4 — Intelligent",
    5: "Level 5 — Transformational"
}

descriptions = {
    1: "Siloed data, limited governance, manual reporting, low interoperability.",
    2: "Data governance established, policies defined, ownership and stewardship assigned.",
    3: "FHIR interoperability, terminology standardization, metadata repository, connected data assets.",
    4: "Analytics, executive dashboards, AI-enabled decision support, intelligence-driven operations.",
    5: "Responsible AI at scale, knowledge graphs, learning health system, continuous transformation."
}

for key, value in levels.items():
    st.markdown(f"**{value}:** {descriptions[key]}")

st.divider()

st.markdown("### Assess Organizational Maturity")

governance = st.slider("Data Governance", 1, 5, 3)
metadata = st.slider("Metadata Management", 1, 5, 3)
interop = st.slider("FHIR & Interoperability", 1, 5, 3)
terminology = st.slider("Terminology Standardization", 1, 5, 3)
analytics = st.slider("Analytics & Executive Intelligence", 1, 5, 3)
ai = st.slider("Responsible AI Governance", 1, 5, 3)

score = round(
    (governance + metadata + interop + terminology + analytics + ai) / 6,
    1
)

if score < 1.8:
    level_num = 1
elif score < 2.6:
    level_num = 2
elif score < 3.4:
    level_num = 3
elif score < 4.3:
    level_num = 4
else:
    level_num = 5

level = levels[level_num]

st.markdown('<div class="section-title">Assessment Result</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

c1.metric("Overall HI2M Score", score)
c2.metric("Maturity Level", level)

st.success(f"Current maturity classification: {level}")

st.markdown("### Interpretation")

st.write(descriptions[level_num])

st.markdown("### Recommended Focus Areas")

if level_num == 1:
    recommendations = [
        "Establish enterprise data governance structure",
        "Define data ownership and stewardship",
        "Create enterprise data dictionary and business glossary",
        "Standardize key clinical and operational KPIs"
    ]
elif level_num == 2:
    recommendations = [
        "Expand metadata management capabilities",
        "Implement FHIR readiness assessment",
        "Standardize terminology mappings using SNOMED CT, ICD, LOINC, and RxNorm",
        "Deploy data quality monitoring"
    ]
elif level_num == 3:
    recommendations = [
        "Deploy executive intelligence dashboards",
        "Strengthen AI governance controls",
        "Implement model registry and explainability workflows",
        "Improve interoperability monitoring"
    ]
elif level_num == 4:
    recommendations = [
        "Scale responsible AI governance",
        "Develop healthcare knowledge graph capabilities",
        "Implement transformation value tracking",
        "Move toward learning health system capabilities"
    ]
else:
    recommendations = [
        "Continuously optimize transformation performance",
        "Scale semantic intelligence and knowledge graph adoption",
        "Advance responsible AI operations",
        "Benchmark against global digital health maturity frameworks"
    ]

for item in recommendations:
    st.success(item)