import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Insurance Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp { background-color: #0D1B2A; color: #E8EAF0; }
    .block-container { background-color: #0D1B2A; padding-top: 2rem; }
    [data-testid="stSidebar"] {
        background-color: #101F30;
        border-right: 1px solid rgba(255,255,255,0.08);
    }
    [data-testid="stNumberInput"] input {
        background-color: #162233 !important;
        color: #E8EAF0 !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 6px !important;
    }
    .stButton > button {
        background-color: #2563EB; color: white; border: none;
        border-radius: 8px; font-weight: 500; width: 100%;
    }
    .stButton > button:hover { background-color: #1D4ED8; border: none; }
    [data-testid="stMetric"] {
        background-color: #162233;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 8px; padding: 0.8rem 1rem;
    }
    [data-testid="stMetricValue"] { color: #93C5FD !important; }
    hr { border-color: rgba(255,255,255,0.08); }
    label { color: #8FA3BC !important; font-size: 0.85rem !important; }
    .stProgress > div > div { background-color: #2563EB; }
    h1, h2, h3 { color: #FFFFFF !important; }
    p, .stMarkdown { color: #C8D6E5; }
</style>
""", unsafe_allow_html=True)

model = joblib.load("Models/fraud_model.pkl")
scaler = joblib.load("Models/scaler.pkl")
features = joblib.load("Models/features.pkl")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Prediction", "About"])

if page == "Prediction":

    st.title("🛡️ Insurance Fraud Detection")
    st.write("Enter claim details — results appear instantly on the right.")
    st.markdown("---")

    left_col, right_col = st.columns([1, 1], gap="large")

    with left_col:
        st.subheader("Claim Information")

        age = st.number_input("Age", min_value=18, max_value=100, value=35)
        monthly_income = st.number_input("Monthly Income", min_value=0.0, value=25000.0)
        premium_amount = st.number_input("Premium Amount", min_value=0.0, value=5000.0)
        claim_amount = st.number_input("Claim Amount", min_value=0.0, value=10000.0)

        predict_btn = st.button("🔍 Predict Fraud")

    with right_col:
        st.subheader("Prediction Result")

        if predict_btn:
            input_df = pd.DataFrame({
                "Age": [age],
                "Monthly_Income": [monthly_income],
                "Premium_Amount": [premium_amount],
                "Claim_Amount": [claim_amount]
            })

            input_df = input_df.reindex(columns=features, fill_value=0)
            input_scaled = scaler.transform(input_df)

            prediction = model.predict(input_scaled)[0]
            probability = model.predict_proba(input_scaled)[0][1]

            if prediction == 1:
                st.error("🚨 Fraudulent Claim Detected")
            else:
                st.success("✅ Legitimate Claim")

            # Single metric — fraud probability only
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
                    border:1px solid rgba(255,255,255,0.08);
                    border-radius:10px;
                    padding:3rem 2rem;
                    text-align:center;
                    min-height:280px;
                    display:flex;
                    flex-direction:column;
                    align-items:center;
                    justify-content:center;
                ">
                    <div style="font-size:2.5rem;margin-bottom:0.75rem">🔍</div>
                    <p style="color:#4a6280;margin:0">
                        Fill in the claim details and click<br>
                        <strong style="color:#2563EB">Predict Fraud</strong> to see results here.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

if page == "About":
    st.header("About This Project")
    st.markdown("""
    ### Project
    This application predicts insurance fraud using Machine Learning.

    ### Features
    - Age
    - Monthly Income
    - Premium Amount
    - Claim Amount

    ### Developed By
    Kgobeane Mahlo
    """)
