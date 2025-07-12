import streamlit as st
from audit_engine import audit_model

st.set_page_config(page_title="AuditAI – AI Ethics Scorecard", layout="centered")

st.title("🧾 AuditAI – Ethics & Transparency Scorecard")
st.markdown("Let's take a quick look at the AI system's ethical performance...")

# Input Section
description = st.text_area("🔍 Describe the AI use case to audit:", height=200, placeholder="e.g. AI for predicting student dropout in public schools")

if st.button("Run Audit"):
    if not description.strip():
        st.warning("Please enter a description of the AI system.")
    else:
        with st.spinner("Running ethical audit..."):
            result = audit_model(description)
        st.markdown("### 📊 Scorecard & Summary")
        st.markdown(result)


