import streamlit as st
import requests
import json

# --- 1. Page Configuration (Must remain at absolute line 1) ---
st.set_page_config(
    page_title="Networked Capital Infrastructure", 
    page_icon="💼", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. Executive Light Corporate Styling ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    h1 {
        color: #1e3a8a !important;
        font-weight: 800 !important;
    }
    h3 {
        color: #334155 !important;
    }
    p, label, span {
        color: #0f172a !important;
        font-weight: 500;
    }
    input {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
    }
    div.stButton > button:first-child {
        background-color: #1e40af !important;
        color: #ffffff !important;
        border-radius: 6px !important;
        border: none !important;
        width: 100% !important;
        padding: 0.75rem !important;
        font-weight: bold !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #1d4ed8 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. Persistent UI Narrative ---
st.title("Networked Capital Infrastructure")
st.subheader("Peacemedia Software Systems — Evaluation Sandbox")
st.write("Deploy deterministic capital infrastructure inside your perimeter. Request your 30-day free sandbox trial below.")

st.divider()

# --- 4. Hardcoded Notification Gateway ---
FORMSPREE_URL = "https://formspree.io/f/xojozzrr"

# --- 5. Data Ingestion Form ---
with st.form(key="sandbox_trial_form", clear_on_submit=False):
    st.markdown("### Data Ingestion Port")
    email = st.text_input("Corporate Ingestion Email", placeholder="name@institution.com")
    company = st.text_input("Target Node / Entity Name", placeholder="Enterprise Name")
    submit_button = st.form_submit_button(label="Initialize Ingestion Pipeline & Lock Blueprint")

# --- 6. Execution Block & Embedded Asset Generator ---
if submit_button:
    if "@" not in email or "." not in email:
        st.error("Please enter a valid corporate email address.")
    elif not company:
        st.error("Please enter your organization name.")
    else:
        # Task A: Transmit Lead Notification Silently to Formspree
        payload = {
            "email": email,
            "company": company,
            "tier": "30_Day_Free_Trial_Sandbox",
            "status": "Active"
        }
        
        notification_sent = False
        try:
            response = requests.post(FORMSPREE_URL, json=payload, timeout=10)
            if response.status_code == 200:
                notification_sent = True
            else:
                st.warning("Telemetry synchronization delay. Proceeding with local asset generation.")
        except Exception as e:
            st.warning("Perimeter transmission offline. Proceeding with local asset generation.")

        # Task B: Dynamically Generate the Master Blueprint Data Asset locally
        master_asset = {
            "organization": "Peacemedia Software Systems",
            "document_control": {
                "reference": "PSS-NCI-2026-V1",
                "classification": "COMMERCIAL IN CONFIDENCE",
                "evaluation_window_days": 30
            },
            "corporate_briefing": [
                "1. SYSTEM ARCHITECTURE OVERVIEW: Peacemedia Software Systems delivers deterministic, rule-based automation engines designed to minimize operational risk and liability for enterprise environments.",
                "2. SECURITY GATEWAYS: The evaluation sandbox operates a strict Bring Your Own Key (BYOK) security protocol. No credentials are saved to external disks.",
                "3. DETERMINISTIC GUARDRAIL: The engine calculates exactly 30 calendar days of operational lifespan. Upon reaching Day 31, the processing gate cleanly refuses further transaction processing."
            ],
            "infrastructure_deployment_template": {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Description": "Peacemedia Software Systems - 30-Day Sandbox Environment",
                "Parameters": {
                    "TargetEntityName": { "Type": "String", "Default": company },
                    "IngestionEmail": { "Type": "String", "Default": email }
                },
                "Resources": {
                    "SandboxRuntime": {
                        "Type": "AWS::Lambda::Function",
                        "Properties": {
                            "Runtime": "python3.11",
                            "Timeout": 10,
                            "Environment": {
                                "Variables": {
                                    "DEPLOYMENT_TARGET": company,
                                    "ADMIN_EMAIL": email,
                                    "STATE_CONTROL": "DETERMINISTIC_BYOK"
                                }
                            }
                        }
                    }
                }
            }
        }
        
        # Format the compiled system blueprint into a string
        json_string = json.dumps(master_asset, indent=2)
        
        # Display Success Feedback
        st.success("Success! Ingestion pipeline completed. Your 30-day sandbox trial environment is locked.")
        
        # Task C: Present the On-Screen Download Button instantly
        st.download_button(
            label="📥 Download Secure Sandbox Blueprint (.json)",
            data=json_string,
            file_name="peacemedia_sandbox_blueprint.json",
            mime="application/json"
        )
