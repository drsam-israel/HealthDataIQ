import streamlit as st
import pandas as pd
from assets.styles import load_css, page_header

load_css()

page_header(
    "📌",
    "Executive Insights, Recommendations & Conclusion",
    "Final executive synthesis of HealthDataIQ™ strategic insights, recommendations, and transformation conclusion."
)

# =====================================================
# Executive Insight Summary
# =====================================================

st.markdown(
    '<div class="section-title">Executive Insight Summary</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#FFFFFF;
padding:30px;
border-radius:14px;
border-left:8px solid #1E66F5;
box-shadow:0px 6px 18px rgba(0,0,0,0.06);
margin-bottom:20px;
">

<h3 style="
color:#0B1F3A;
margin-top:0px;
margin-bottom:20px;
">
Executive Perspective
</h3>

<p style="
font-size:18px;
line-height:1.8;
color:#334155;
">
HealthDataIQ™ demonstrates that healthcare transformation is not achieved through dashboards,
AI models, or technology platforms alone.
</p>

<p style="
font-size:18px;
line-height:1.8;
color:#334155;
">
Sustainable transformation requires governed data, trusted metadata,
high-quality information, interoperable systems, responsible AI governance,
executive intelligence, and measurable value realization.
</p>

<p style="
font-size:18px;
line-height:1.8;
font-weight:700;
color:#0B1F3A;
margin-bottom:0px;
">
Data → Information → Intelligence → Decisions → Business Value
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# Key Strategic Insights
# =====================================================

st.markdown('<div class="section-title">Key Strategic Insights</div>', unsafe_allow_html=True)

insights_df = pd.DataFrame({
    "Strategic Insight": [
        "Healthcare organizations do not simply need more data; they need trusted, governed, and usable data.",
        "Metadata management is a foundational capability for analytics, interoperability, and AI.",
        "Interoperability is not only a technical priority; it is a care coordination and transformation priority.",
        "Responsible AI governance must be established before healthcare AI is scaled.",
        "Executive intelligence requires integration across governance, data quality, interoperability, AI, and transformation domains.",
        "Value realization must be measured to sustain digital health transformation investments."
    ],
    "Executive Implication": [
        "Leadership must invest in governance, stewardship, and accountability.",
        "Organizations need clear definitions, ownership, lineage, and metadata visibility.",
        "FHIR, terminology services, and API governance are strategic enterprise capabilities.",
        "Clinical safety, explainability, monitoring, and accountability must be embedded into AI programs.",
        "Executives need integrated decision intelligence rather than isolated dashboards.",
        "Transformation must be tied to ROI, cost avoidance, operational efficiency, and outcomes."
    ]
})

for _, row in insights_df.iterrows():

    st.markdown(f"""
    <div style="
        background:#FFFFFF;
        padding:20px;
        border-radius:12px;
        border-left:6px solid #1E66F5;
        margin-bottom:15px;
        box-shadow:0px 4px 12px rgba(0,0,0,0.05);
    ">

    <h4 style="color:#0B1F3A;">
    Strategic Insight
    </h4>

    <p style="font-size:17px;">
    {row['Strategic Insight']}
    </p>

    <h4 style="color:#0B1F3A;">
    Executive Implication
    </h4>

    <p style="font-size:17px;">
    {row['Executive Implication']}
    </p>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# Executive Recommendations
# =====================================================

st.markdown(
    '<div class="section-title">Executive Recommendations</div>',
    unsafe_allow_html=True
)

recommendations = [
    "Establish enterprise-wide healthcare data governance and stewardship structures.",
    "Develop and maintain a standardized data dictionary, business glossary, and metadata repository.",
    "Implement continuous data quality monitoring across clinical, operational, financial, and AI domains.",
    "Expand FHIR interoperability, terminology services, and API governance capabilities.",
    "Operationalize responsible AI governance before scaling clinical and operational AI models.",
    "Create an executive intelligence layer that connects data quality, governance, interoperability, AI, and transformation performance.",
    "Track transformation value through ROI, cost avoidance, operational efficiency, and measurable outcomes.",
    "Build toward a learning health system supported by semantic intelligence, responsible AI, and continuous improvement."
]

for item in recommendations:

    st.markdown(f"""
    <div style="
    background:#FFFFFF;
    padding:24px;
    border-radius:14px;
    border-left:8px solid #16A34A;
    box-shadow:0px 6px 18px rgba(0,0,0,0.06);
    margin-bottom:15px;
    ">

    <p style="
    font-size:18px;
    line-height:1.8;
    color:#334155;
    margin-bottom:0px;
    ">
    ✅ {item}
    </p>

    </div>
    """, unsafe_allow_html=True)
# =====================================================
# HealthDataIQ Strategic Positioning
# =====================================================

st.markdown('<div class="section-title">HealthDataIQ™ Strategic Positioning</div>', unsafe_allow_html=True)

positioning_df = pd.DataFrame({
    "Capability Area": [
        "Governance",
        "Metadata",
        "Data Quality",
        "Interoperability",
        "Responsible AI",
        "Executive Intelligence",
        "Transformation",
        "Value Realization"
    ],
    "HealthDataIQ™ Positioning": [
        "Defines ownership, accountability, stewardship, policies, and governance maturity.",
        "Provides visibility into data definitions, business terms, metadata assets, and lineage readiness.",
        "Assesses trust readiness across completeness, accuracy, consistency, timeliness, and validity.",
        "Evaluates FHIR readiness, terminology mapping, API governance, and healthcare data exchange.",
        "Structures AI model oversight, risk classification, explainability, bias monitoring, and clinical safety.",
        "Provides executive visibility into maturity, risks, priorities, and transformation performance.",
        "Connects strategic roadmap, operating model, governance, and execution.",
        "Measures ROI, business value, cost avoidance, productivity gains, and enterprise outcomes."
    ]
})


for _, row in positioning_df.iterrows():

    st.markdown(f"""
    <div style="
    background:#FFFFFF;
    padding:25px;
    border-radius:14px;
    border-left:8px solid #9333EA;
    box-shadow:0px 6px 18px rgba(0,0,0,0.06);
    margin-bottom:15px;
    ">

    <h3 style="
    color:#9333EA;
    margin-top:0px;
    ">
    {row['Capability Area']}
    </h3>

    <p style="
    font-size:18px;
    line-height:1.7;
    color:#334155;
    margin-bottom:0px;
    ">
    {row['HealthDataIQ™ Positioning']}
    </p>

    </div>
    """, unsafe_allow_html=True)
# =====================================================
# Conclusion
# =====================================================

st.markdown('<div class="section-title">Conclusion</div>', unsafe_allow_html=True)

st.markdown("""
<div style="
background:#FFFFFF;
padding:35px;
border-radius:14px;
border-left:8px solid #F59E0B;
box-shadow:0px 6px 18px rgba(0,0,0,0.06);
margin-bottom:20px;
">

<h3 style="
color:#F59E0B;
margin-top:0px;
">
Executive Conclusion
</h3>

<p style="
font-size:18px;
line-height:1.8;
color:#334155;
">
HealthDataIQ™ positions healthcare informatics as an enterprise transformation capability,
rather than merely a technical function.
</p>

<p style="
font-size:18px;
line-height:1.8;
color:#334155;
">
By integrating governance, metadata management, data quality,
interoperability, terminology services, responsible AI governance,
enterprise architecture, executive intelligence, transformation management,
and value realization, HealthDataIQ™ provides a strategic blueprint
for the AI-enabled, interoperable, and intelligence-driven healthcare organization.
</p>

<p style="
font-size:18px;
line-height:1.8;
font-weight:700;
color:#0B1F3A;
margin-bottom:0px;
">
Governed Data → Connected Knowledge → Trusted AI → Executive Intelligence → Business Value
</p>

</div>
""", unsafe_allow_html=True)
# =====================================================
# Author & Professional Profile
# =====================================================
st.markdown("""
<div style="
background:#FFFFFF;
padding:25px;
border-radius:14px;
border-left:8px solid #1E66F5;
box-shadow:0px 6px 18px rgba(0,0,0,0.06);
margin-bottom:15px;
">

<h3 style="color:#1E66F5;">
Author
</h3>

<h2 style="color:#0B1F3A;">
Samuel Israel, MD
</h2>

<p style="font-size:18px;color:#334155;">
Master of Information Technology (AI Specialization)
</p>

<p style="font-size:17px;color:#475569;">
Healthcare AI • Clinical Informatics • Digital Health Transformation •
Responsible AI Governance • Healthcare Interoperability •
Executive Intelligence • Enterprise Healthcare Architecture
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:#FFFFFF;
padding:25px;
border-radius:14px;
border-left:8px solid #16A34A;
box-shadow:0px 6px 18px rgba(0,0,0,0.06);
margin-bottom:15px;
">

<h3 style="color:#16A34A;">
Professional Career Path
</h3>

<p style="
font-size:18px;
line-height:1.8;
color:#334155;
">

Healthcare AI Specialist

→ Clinical Informatics Specialist

→ Healthcare AI Governance Lead

→ Digital Health Transformation Consultant

→ Enterprise Healthcare Intelligence Leader

→ Chief Data & AI Officer (Healthcare)

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:#FFFFFF;
padding:25px;
border-radius:14px;
border-left:8px solid #9333EA;
box-shadow:0px 6px 18px rgba(0,0,0,0.06);
margin-bottom:15px;
">

<h3 style="color:#9333EA;">
HealthDataIQ™ Executive Statement
</h3>

<p style="
font-size:18px;
line-height:1.8;
color:#334155;
">

HealthDataIQ™ was developed as a consulting-grade
Healthcare Informatics Operating System (HEOS)
demonstrating how healthcare organizations can transform
governed data into trusted knowledge, responsible AI,
executive intelligence, and measurable business value.

</p>

<p style="
font-size:18px;
font-weight:700;
color:#0B1F3A;
">

Governed Data → Connected Knowledge → Trusted AI →
Executive Intelligence → Business Value

</p>

</div>
""", unsafe_allow_html=True)