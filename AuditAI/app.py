import streamlit as st
from audit_engine import audit_model

st.set_page_config(page_title="AuditAI", layout="centered")

st.title("🛡️ AuditAI — AI Ethics Scorecard")

user_input = st.text_area("📝 Describe the AI system or use case you'd like to audit:")

if st.button("Run Audit"):
    if user_input.strip() == "":
        st.warning("Please enter a valid description.")
    else:
        with st.spinner("Auditing..."):
            result = audit_model(user_input)
        st.subheader("✅ Ethics Audit Report:")
        st.markdown(result)
