import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Health Shield — Insurance Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* Remove all default padding and scrollbars */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        height: 100vh;
        overflow: hidden;
        background-color: #0D1B2A;
        color: #E8EAF0;
    }

    [data-testid="stAppViewContainer"] {
        padding: 0;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
        height: 100vh;
        overflow: hidden;
    }

    /* Hide Streamlit chrome */
    #MainMenu, header, footer { visibility: hidden; }

    /* Tab bar */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background-color: #0A1628;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding: 0 1.5rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: #8FA3BC;
        border-radius: 0;
        border: none;
        border-bottom: 3px solid transparent;
        padding: 12px 24px;
        font-size: 14px;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background-color: transparent !important;
        color: #ffffff !important;
        border-bottom: 3px solid #2563EB !important;
    }
    .stTabs [data-baseweb="tab-panel"] {
        padding: 0 !important;
        height: calc(100vh - 95px);
        overflow: hidden;
    }

    /* Inputs */
    [data-testid="stNumberInput"] input {
        background-color: #162233 !important;
        color: #E8EAF0 !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 6px !important;
    }

    /* Button */
    .stButton > button {
        background-color: #2563EB !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        width: 100% !important;
        padding: 10px !important;
    }
    .stButton > button:hover {
        background-color: #1D4ED8 !important;
    }

    /* Metric */
    [data-testid="stMetric"] {
        background-color: #162233;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 8px;
        padding: 0.75rem 1rem;
    }
    [data-testid="stMetricValue"] { color: #93C5FD !important; }

    /* Labels and text */
    label { color: #8FA3BC !important; font-size: 0.82rem !important; }
    h1, h2, h3 { color: #FFFFFF !important; margin-bottom: 0.4rem !important; }
    p, .stMarkdown { color: #C8D6E5; }
    hr { border-color: rgba(255,255,255,0.08); margin: 0.6rem 0 !important; }

    /* Progress bar */
    .stProgress > div > div { background-color: #2563EB; }

    /* Prediction tab inner layout */
    .pred-layout {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        height: calc(100vh - 100px);
        padding: 20px 28px;
        align-items: start;
    }

    /* Left panel */
    .left-panel {
        background: #111f31;
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 12px;
        padding: 20px;
    }

    /* Right result panel */
    .right-panel {
        background: #111f31;
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 12px;
        padding: 20px;
        min-height: 340px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    /* App header bar */
    .app-header {
        background: #0A1628;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding: 10px 24px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Reduce number input spacing */
    [data-testid="stNumberInput"] {
        margin-bottom: 2px !important;
    }
    .stMarkdown p { margin-bottom: 2px !important; }

    /* Remove extra gaps in columns */
    [data-testid="column"] { padding: 0 8px !important; }
</style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <span style="font-size:22px">🛡️</span>
    <span style="font-size:16px;font-weight:600;color:#ffffff">Health Shield</span>
    <span style="font-size:13px;color:#4a6280;margin-left:4px">— Insurance Fraud Detection</span>
</div>
""", unsafe_allow_html=True)

# ── Load model ───────────────────────────────────────────────────
model  = joblib.load("models/fraud_model.pkl")
scaler = joblib.load("models/scaler.pkl")
features = joblib.load("models/features.pkl")

# ── Tabs  (Dashboard first = landing page) ───────────────────────
tab2, tab1 = st.tabs(["📊 Dashboard", "🔍 Fraud Prediction"])

# ════════════════════════════════════════════════════════════════
# TAB 1  ▸  POWER BI  (landing page)
# ════════════════════════════════════════════════════════════════
with tab2:
    st.markdown(
        """
        <iframe
            title="Health Shield Power BI Dashboard"
            src="https://app.powerbi.com/view?r=eyJrIjoiNDBmOTM5NmUtODliNy00ZWNiLWE2YjEtYTY2NTg3N2I3MWQ0IiwidCI6IjQ0MWRiNzQ0LWY5NzUtNGI2Ny04YzU3LTA1NDFkMTI3NjM2MyJ9"
            style="width:100%; height:calc(100vh - 95px); border:none; display:block;"
            allowFullScreen="true">
        </iframe>
        """,
        unsafe_allow_html=True
    )

# ════════════════════════════════════════════════════════════════
# TAB 2  ▸  FRAUD PREDICTION
# ════════════════════════════════════════════════════════════════
with tab1:

    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown("#### Claim Information")
        st.markdown("<hr>", unsafe_allow_html=True)

        age            = st.number_input("Age",            min_value=18,  max_value=100, value=35)
        monthly_income = st.number_input("Monthly Income", min_value=0.0, value=25000.0)
        premium_amount = st.number_input("Premium Amount", min_value=0.0, value=5000.0)
        claim_amount   = st.number_input("Claim Amount",   min_value=0.0, value=10000.0)

        st.markdown("<div style='margin-top:8px'></div>", unsafe_allow_html=True)
        predict_btn = st.button("🔍 Predict Fraud")

    with right:
        st.markdown("#### Prediction Result")
        st.markdown("<hr>", unsafe_allow_html=True)

        if predict_btn:
            input_df = pd.DataFrame({
                "Age":            [age],
                "Monthly_Income": [monthly_income],
                "Premium_Amount": [premium_amount],
                "Claim_Amount":   [claim_amount]
            })
            input_df     = input_df.reindex(columns=features, fill_value=0)
            input_scaled = scaler.transform(input_df)
            prediction   = model.predict(input_scaled)[0]
            probability  = model.predict_proba(input_scaled)[0][1]

            if prediction == 1:
                st.error("🚨 Fraudulent Claim Detected")
            else:
                st.success("✅ Legitimate Claim")

            st.metric("Fraud Probability", f"{probability * 100:.2f}%")

            if probability < 0.30:
                st.success("🟢 Risk Level: LOW")
            elif probability < 0.70:
                st.warning("🟡 Risk Level: MEDIUM")
            else:
                st.error("🔴 Risk Level: HIGH")

            st.progress(float(probability))

        else:
            st.markdown(
                """
                <div style="
                    background:#162233;
                    border:1px solid rgba(255,255,255,0.07);
                    border-radius:10px;
                    padding:2.5rem 1.5rem;
                    text-align:center;
                    color:#4a6280;
                ">
                    <div style="font-size:2rem;margin-bottom:0.6rem">🔍</div>
                    <p style="color:#4a6280;margin:0;font-size:13px">
                        Fill in the claim details on the left<br>and click
                        <strong style="color:#2563EB">Predict Fraud</strong>.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
