import streamlit as st
from assets.styles import load_css, page_header

load_css()

page_header(
    "🏥",
    "Executive Assessment Center",
    "Assess Healthcare Informatics readiness using the HealthDataIQ™ Maturity Index (HMI)."
)

st.info(
    "The Executive Assessment Center evaluates healthcare informatics maturity across governance, metadata, interoperability, analytics, AI governance, and digital transformation domains."
)

st.markdown("### Assessment Domains")

governance = st.slider(
    "Healthcare Data Governance",
    1, 5, 3,
    help="Policies, stewardship, ownership, compliance, and governance operating model."
)

metadata = st.slider(
    "Metadata Management",
    1, 5, 3,
    help="Data dictionary, glossary, lineage, metadata repository, and asset management."
)

interop = st.slider(
    "Interoperability & Standards",
    1, 5, 3,
    help="FHIR, HL7, APIs, terminology services, and information exchange."
)

analytics = st.slider(
    "Analytics & Executive Intelligence",
    1, 5, 3,
    help="KPIs, dashboards, executive reporting, predictive analytics."
)

ai = st.slider(
    "Responsible AI Governance",
    1, 5, 3,
    help="Model registry, explainability, bias monitoring, drift monitoring."
)

transformation = st.slider(
    "Digital Health Transformation",
    1, 5, 3,
    help="Transformation strategy, operating model, adoption, value realization."
)

# HMI Score

score = round(
    (
        governance +
        metadata +
        interop +
        analytics +
        ai +
        transformation
    ) / 30 * 100
)

st.markdown(
    '<div class="section-title">Executive Assessment Results</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

c1.metric("HMI Score", f"{score}/100")
c2.metric("Assessment Domains", "6")
c3.metric("Assessment Status", "Completed")

st.divider()

c1, c2, c3 = st.columns(3)

c1.metric("Governance", governance * 20)
c2.metric("Metadata", metadata * 20)
c3.metric("Interoperability", interop * 20)

c4, c5, c6 = st.columns(3)

c4.metric("Analytics", analytics * 20)
c5.metric("AI Governance", ai * 20)
c6.metric("Transformation", transformation * 20)

st.divider()

# Classification

if score < 40:
    maturity = "Level 1 — Fragmented"

elif score < 60:
    maturity = "Level 2 — Governed"

elif score < 80:
    maturity = "Level 3 — Connected"

elif score < 90:
    maturity = "Level 4 — Intelligent"

else:
    maturity = "Level 5 — Transformational"

st.success(f"Healthcare Informatics Classification: {maturity}")

# Interpretation

st.markdown("### Executive Interpretation")

if score < 40:

    st.write("""
The organization exhibits fragmented informatics capabilities.
Governance structures, metadata management, interoperability,
and executive intelligence capabilities remain immature.
""")

elif score < 60:

    st.write("""
The organization has established governance foundations and
is progressing toward enterprise-wide management of data,
metadata, and interoperability assets.
""")

elif score < 80:

    st.write("""
The organization demonstrates connected healthcare informatics
capabilities with established governance, metadata management,
and interoperability programs.
""")

elif score < 90:

    st.write("""
The organization demonstrates intelligent healthcare
informatics capabilities supported by executive intelligence,
analytics, governance, and emerging responsible AI practices.
""")

else:

    st.write("""
The organization demonstrates transformational healthcare
informatics maturity characterized by enterprise intelligence,
responsible AI, learning health system principles, and
continuous transformation.
""")

# Recommendations

st.markdown("### Strategic Recommendations")

if score < 40:

    recommendations = [
        "Establish Data Governance Office",
        "Develop Enterprise Data Dictionary",
        "Create Business Glossary",
        "Define Executive KPI Framework"
    ]

elif score < 60:

    recommendations = [
        "Deploy Metadata Repository",
        "Expand Stewardship Coverage",
        "Develop Data Quality Program",
        "Initiate FHIR Readiness Program"
    ]

elif score < 80:

    recommendations = [
        "Expand FHIR Interoperability",
        "Deploy Executive Intelligence Dashboards",
        "Implement Metadata Lineage",
        "Develop AI Governance Framework"
    ]

elif score < 90:

    recommendations = [
        "Scale Responsible AI Governance",
        "Expand Predictive Analytics",
        "Implement Enterprise Benchmarking",
        "Strengthen Transformation Management"
    ]

else:

    recommendations = [
        "Develop Healthcare Knowledge Graph",
        "Implement Learning Health System",
        "Scale Enterprise AI Governance",
        "Optimize Transformation Value Realization"
    ]

for item in recommendations:
    st.success(item)