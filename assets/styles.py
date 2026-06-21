import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .block-container {
        padding-top: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1250px;
    }

    .main-title {
        font-size: 46px;
        font-weight: 900;
        color: #0b1f3a;
        margin-bottom: 8px;
        line-height: 1.15;
    }

    .blue-line {
        width: 80px;
        height: 5px;
        background: #0066ff;
        border-radius: 10px;
        margin: 12px 0 25px 0;
    }

    .subtitle {
        font-size: 18px;
        color: #475569;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 800;
        color: #0b1f3a;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    div[data-testid="stTextInput"] input {
        border: 1px solid #d1d5db !important;
        border-radius: 12px !important;
        background-color: #f8fafc !important;
        color: #0b1f3a !important;
        height: 52px !important;
        font-size: 16px !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border: 2px solid #0066ff !important;
        box-shadow: 0 0 0 2px rgba(0, 102, 255, 0.12) !important;
    }

    div[data-baseweb="select"] > div {
        border: 1px solid #d1d5db !important;
        border-radius: 12px !important;
        background-color: #f8fafc !important;
        min-height: 52px !important;
    }

    div[data-baseweb="select"] > div:focus-within {
        border: 2px solid #0066ff !important;
        box-shadow: 0 0 0 2px rgba(0, 102, 255, 0.12) !important;
    }

    label {
        font-weight: 600 !important;
        color: #334155 !important;
    }
    </style>
    """, unsafe_allow_html=True)


def page_header(icon, title, subtitle=None):
    st.markdown(f"""
    <div class="main-title">{icon} {title}</div>
    <div class="blue-line"></div>
    """, unsafe_allow_html=True)

    if subtitle:
        st.markdown(f"""
        <div class="subtitle">{subtitle}</div>
        """, unsafe_allow_html=True)