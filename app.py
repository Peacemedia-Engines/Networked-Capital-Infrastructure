import streamlit as st
import requests

# --- Page Configuration & Structural Dark Styling ---
st.set_page_config(page_title="Networked Capital Infrastructure Enterprise Sandbox", page_icon="💼", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #090d16; color: #f3f4f6; }
    h1, h2, h3 { color: #ffffff !important; }
    div.stButton > button:first-child {
        background-color: #2563eb; color: white; border-radius: 4px; border: none; width: 100%; padding: 0.75rem; font-weight: bold;
    }
    div.stButton > button:first-child:hover { background-color: #1d4ed8; }
    </style>
""", unsafe_allow_html=True)

st.title("Networked Capital Infrastructure Enterprise Sandbox")
st.subheader("Peacemedia Software Systems — Evaluation Sandbox")
st.write("Deploy deterministic capital infrastructure inside your perimeter. Request your 30-day free sandbox trial below.")

st.divider()

# --- Integrated Formspree Production Endpoint ---
FORMSPREE_URL = "https://formspree.io/f/xojozzrr"

# --- User Interface Capture Form ---
with st.form(key="sandbox_trial_form", clear_on_submit=True):
    email = st.text_input("Corporate Email Address", placeholder="name@institution.com")
    company = st.text_input("Company / Family Office", placeholder="Enterprise Name")
    submit_button = st.form_submit_button(label="Generate Activation Blueprint")

# --- Form Execution & Webhook Transmission ---
if submit_button:
    if "@" not in email or "." not in email:
        st.error("Please enter a valid corporate email address.")
    elif not company:
        st.error("Please enter your organization name.")
    else:
        # Formulate payload exactly matched to your trial parameters
        payload = {
            "email": email,
            "company": company,
            "tier": "30_Day_Free_Trial_Sandbox",
            "status": "Active"
        }
        
        try:
            # Silently route transaction details via HTTP POST to Formspree
            response = requests.post(FORMSPREE_URL, json=payload, timeout=10)
            
            if response.status_code == 200:
                st.success("Success! Your 30-day sandbox trial has been provisioned. Check your corporate directory email.")
            else:
                st.error(f"Ingestion communication lag. Server responded with status code: {response.status_code}")
        except Exception as e:
            st.error("Network execution failure. Could not reach routing gateway.")
