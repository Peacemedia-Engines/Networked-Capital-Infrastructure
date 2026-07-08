import streamlit as st
import requests

# --- 1. Page Configuration (Absolute First Streamlit Command) ---
st.set_page_config(
    page_title="Networked Capital Infrastructure", 
    page_icon="💼", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. Corrected Institutional Dark Theme Injection ---
st.markdown("""
    <style>
    /* Targets the entire app background perimeter */
    [data-testid="stAppViewContainer"] {
        background-color: #090d16 !important;
        color: #f3f4f6 !important;
    }
    
    /* Targets the top header bar to prevent color bleeding */
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    /* Locks title and subtitle colors permanently to white */
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
    }
    
    /* High-contrast custom action button */
    div.stButton > button:first-child {
        background-color: #2563eb !important;
        color: #ffffff !important;
        border-radius: 4px !important;
        border: none !important;
        width: 100% !important;
        padding: 0.75rem !important;
        font-weight: bold !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #1d4ed8 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. Persistent Visual Layout ---
st.title("Networked Capital Infrastructure")
st.subheader("Peacemedia Software Systems — Evaluation Sandbox")
st.write("Deploy deterministic capital infrastructure inside your perimeter. Request your 30-day free sandbox trial below.")

st.divider()

# --- 4. Production Webhook Target ---
FORMSPREE_URL = "https://formspree.io/f/xojozzrr"

# --- 5. Clean Input Form ---
with st.form(key="sandbox_trial_form", clear_on_submit=True):
    email = st.text_input("Corporate Email Address", placeholder="name@institution.com")
    company = st.text_input("Company / Family Office", placeholder="Enterprise Name")
    submit_button = st.form_submit_button(label="Generate Activation Blueprint")

# --- 6. Execution & Ingestion Block ---
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
