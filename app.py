import streamlit as st
import datetime
import json
import os

# --- 1. THE ENTERPRISE INTERFACE (Dark Theme) ---
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

st.title("Networked Capital Infrastructure")
st.subheader("Peacemedia Software Systems — Evaluation Sandbox")
st.write("Deploy deterministic capital infrastructure inside your perimeter. Request your 30-day free sandbox trial below. Users remain natively on this interface.")

st.divider()

# --- 2. EMAIL & TRIAL CAPTURE FORM ---
with st.form(key="sandbox_trial_form", clear_on_submit=True):
    email = st.text_input("Corporate Email Address", placeholder="name@institution.com")
    company = st.text_input("Company / Family Office", placeholder="Enterprise Name")
    submit_button = st.form_submit_button(label="Generate Activation Blueprint")

# --- 3. THE PYTHON BACKEND LOGIC (Calculates the 30 Days) ---
if submit_button:
    if "@" not in email or "." not in email:
        st.error("Please enter a valid corporate email address.")
    elif not company:
        st.error("Please enter your organization name.")
    else:
        # Calculate precise timestamps
        start_time = datetime.datetime.now()
        expiry_time = start_time + datetime.timedelta(days=30)
        
        trial_manifest = {
            "email": email,
            "company": company,
            "tier": "Evaluation_Sandbox",
            "status": "Active",
            "activated_at": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "expires_at": expiry_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Save lead to a local JSON file database inside the workspace
        log_file = "sandbox_testers.json"
        existing_data = []
        
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []
                    
        existing_data.append(trial_manifest)
        
        with open(log_file, "w") as f:
            json.dump(existing_data, f, indent=4)
            
        # Success message displayed to user while keeping them on the page
        st.success(f"Success! Your sandbox trial has been provisioned. Expiration set for: {trial_manifest['expires_at']}.")
