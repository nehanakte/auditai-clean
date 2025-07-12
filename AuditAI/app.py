import streamlit as st
from audit_engine import audit_model

st.set_page_config(page_title="AuditAI Scorecard", layout="centered")
st.title("🤖 AuditAI – AI Ethics Scorecard")

st.markdown(
    "Let's take a quick look at the scorecard evaluating your AI system on ethical principles."
)

description = st.text_area("📝 Describe the AI use case (e.g., facial recognition in public surveillance):")

if st.button("🔍 Run Audit"):
    if description:
        result = audit_model(description)
        st.subheader("📊 Scorecard")
        st.markdown(result)
    else:
        st.warning("Please enter a use case description.")

