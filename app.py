import streamlit as st
import requests

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Networked Capital Infrastructure", 
    page_icon="💼", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. Premium Light Corporate Style Injection ---
st.markdown("""
    <style>
    /* Global App Background */
    [data-testid="stAppViewContainer"] {
        background-color: #f8fafc !important; /* Soft premium off-white */
        color: #0f172a !important; /* Deep charcoal/slate for maximum readability */
    }
    
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    /* Text Elements Layer */
    h1 {
        color: #1e3a8a !important; /* Deep Navy Blue for the primary title */
        font-weight: 800 !important;
    }
    h3 {
        color: #334155 !important; /* Slate gray subheaders */
    }
    p, label, span {
        color: #0f172a !important;
        font-weight: 500;
    }
    
    /* Clean Input Fields Styling */
    input {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
    }
    
    /* High-Contrast Corporate Action Button */
    div.stButton > button:first-child {
        background-color: #1e40af !important; /* Premium Navy Button */
        color: #ffffff !important;
        border-radius: 6px !important;
        border: none !important;
        width: 100% !important;
        padding: 0.75rem !important;
        font-weight: bold !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #1d4ed8 !important; /* Vibrant blue hover state */
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. Unified Layout ---
st.title("Networked Capital Infrastructure")
st.subheader("Peacemedia Software Systems — Evaluation Sandbox")
st.write("Deploy deterministic capital infrastructure inside your perimeter. Request your 30-day free sandbox trial below.")

st.divider()

# --- 4. Formspree Endpoint ---
FORMSPREE_URL = "https://formspree.io/f/xojozzrr"

# --- 5. Clean Form Layout ---
with st.form(key="sandbox_trial_form", clear_on_submit=True):
    email = st.text_input("Corporate Email Address", placeholder="name@institution.com")
    company = st.text_input("Company / Family Office", placeholder="Enterprise Name")
    submit_button = st.form_submit_button(label="Generate Activation Blueprint")

# --- 6. Form Webhook Processing ---
if submit_button:
    if "@" not in email or "." not in email:
        st.error("Please enter a valid corporate email address.")
    elif not company:
        st.error("Please enter your organization name.")
    else:
        payload = {
            "email": email,
            "company": company,
            "tier": "30_Day_Free_Trial_Sandbox",
            "status": "Active"
        }
        try:
            response = requests.post(FORMSPREE_URL, json=payload, timeout=10)
            if response.status_code == 200:
                st.success("Success! Your 30-day sandbox trial has been provisioned. Check your corporate directory email.")
            else:
                st.error(f"Ingestion communication lag. Server responded with status code: {response.status_code}")
        except Exception as e:
            st.error("Network execution failure. Could not reach routing gateway.")
