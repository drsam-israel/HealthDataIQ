import streamlit as st

st.set_page_config(
    page_title="HealthDataIQ",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 1250px;
}

.hero {
    display: flex;
    align-items: center;
    gap: 18px;
}

.hero-icon {
    font-size: 58px;
}

.hero-title {
    font-size: 54px;
    font-weight: 900;
    color: #0b1f3a;
    line-height: 1;
}

.hero-subtitle {
    font-size: 20px;
    color: #0066ff;
    font-weight: 700;
    margin-top: 8px;
}

.blue-line {
    width: 90px;
    height: 5px;
    background: #0066ff;
    border-radius: 10px;
    margin: 18px 0 28px 0;
}

.intro-text {
    font-size: 18px;
    color: #1f2937;
    margin-bottom: 22px;
}

.capability-row {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 22px;
    margin-bottom: 28px;
}

.capability {
    text-align: center;
    font-weight: 800;
    color: #0b1f3a;
    font-size: 14px;
    line-height: 1.35;
}

.capability span {
    font-size: 24px;
    display: block;
    margin-bottom: 7px;
}

.section-title {
    font-size: 31px;
    font-weight: 900;
    color: #0b1f3a;
    margin-bottom: 8px;
}

.section-line {
    width: 70px;
    height: 4px;
    background: #0066ff;
    border-radius: 10px;
    margin-bottom: 22px;
}

.metric-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #0066ff;
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
    min-height: 135px;
}

.metric-title {
    font-size: 16px;
    font-weight: 900;
    color: #0b1f3a;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 36px;
    font-weight: 900;
    color: #0066ff;
    line-height: 1.1;
}

.metric-note {
    font-size: 14px;
    color: #334155;
    margin-top: 10px;
    line-height: 1.4;
}

.green-box {
    background: #eaf8ef;
    border-radius: 12px;
    padding: 18px 22px;
    color: #0f7a3b;
    font-size: 17px;
    font-weight: 800;
    line-height: 1.55;
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-icon">🛡️</div>
    <div>
        <div class="hero-title">HealthDataIQ™</div>
        <div class="hero-subtitle">Enterprise Healthcare Informatics Operating System (HEOS)</div>
    </div>
</div>

<div class="blue-line"></div>

<div class="intro-text">
<b style="color:#0066ff;">HealthDataIQ™</b> is a Healthcare Informatics platform designed to integrate:
</div>

<div class="capability-row">
    <div class="capability"><span>🩺</span>Clinical<br>Informatics</div>
    <div class="capability"><span>🛡️</span>Data<br>Governance</div>
    <div class="capability"><span>🗄️</span>Metadata<br>Management</div>
    <div class="capability"><span>🔁</span>FHIR<br>Interoperability</div>
    <div class="capability"><span>🧬</span>Terminology<br>Services</div>
    <div class="capability"><span>🧠</span>Responsible<br>AI Governance</div>
    <div class="capability"><span>📊</span>Executive<br>Intelligence</div>
    <div class="capability"><span>🚀</span>Digital Health<br>Transformation</div>
</div>

<div class="section-title">Executive Intelligence Summary</div>
<div class="section-line"></div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">📖 Data Elements</div>
        <div class="metric-value">10</div>
        <div class="metric-note">Standardized Data Elements</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card" style="border-top-color:#16a34a;">
        <div class="metric-title">📚 Business Terms</div>
        <div class="metric-value" style="color:#16a34a;">10</div>
        <div class="metric-note">Business Glossary Terms</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card" style="border-top-color:#9333ea;">
        <div class="metric-title">🛡️ Governance Policies</div>
        <div class="metric-value" style="color:#9333ea;">10</div>
        <div class="metric-note">Active Governance Policies</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card" style="border-top-color:#f97316;">
        <div class="metric-title">🧠 AI Models</div>
        <div class="metric-value" style="color:#f97316;">5</div>
        <div class="metric-note">Approved AI Models</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

col5, col6, col7 = st.columns(3)

with col5:
    st.markdown("""
    <div class="metric-card" style="border-top-color:#14b8a6;">
        <div class="metric-title">🔁 FHIR Resources</div>
        <div class="metric-value" style="color:#14b8a6;">2</div>
        <div class="metric-note">FHIR Resources Available</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">🗄️ Metadata Assets</div>
        <div class="metric-value">12</div>
        <div class="metric-note">Total Metadata Assets</div>
    </div>
    """, unsafe_allow_html=True)

with col7:
    st.markdown("""
    <div class="metric-card" style="border-top-color:#db2777;">
        <div class="metric-title">🧬 Terminology Concepts</div>
        <div class="metric-value" style="color:#db2777;">10</div>
        <div class="metric-note">Clinical Concepts Mapped</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="green-box">
✅ HealthDataIQ™ integrates Metadata Management, Governance, FHIR Interoperability,
Terminology Services, AI Governance, and Transformation Intelligence into a unified
Healthcare Informatics Operating System.
</div>
""", unsafe_allow_html=True)