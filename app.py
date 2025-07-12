import streamlit as st
from audit_engine import audit_model


st.write("API KEY FOUND:", "API_KEY" in st.secrets)


st.set_page_config(page_title="AuditAI – Ethics Scorecard", layout="centered")

st.title("🔍 AuditAI – AI Ethics & Transparency Scorecard")

st.markdown("Enter a brief description of the AI system or use case:")

# Text input area
description = st.text_area("✏️ AI System Description", height=200, placeholder="e.g. Facial recognition used in public surveillance...")

# Run the audit
if st.button("Run Ethics Audit"):
    if not description.strip():
        st.warning("Please enter a description first.")
    else:
        with st.spinner("🧠 Auditing..."):
            result = audit_model(description)



        st.success("✅ Audit Complete")
        st.markdown("### 🧾 Ethics Scorecard")
        st.code(result, language="markdown")
