import streamlit as st
from audit_engine import audit_model

st.set_page_config(page_title="AuditAI – Ethics Scorecard", layout="centered")

st.title("📋 AuditAI – AI Ethics & Transparency Scorecard")
st.write("Let's take a quick look at the scorecard, summary, and suggestions for your AI system.")

user_input = st.text_area(
    "🧠 Describe your AI system:",
    height=200,
    placeholder="E.g. An AI system used to screen resumes for government jobs..."
)

if st.button("🔍 Run Audit"):
    if user_input.strip() == "":
        st.warning("Please enter a description of the AI system.")
    else:
        with st.spinner("Auditing in progress..."):
            result = audit_model(user_input)

            # Split based on headings
            try:
                sections = result.split("###")
                for section in sections:
                    if "Scorecard" in section:
                        st.subheader("📊 Scorecard")
                        st.markdown(section.replace("Scorecard:", "").strip())
                    elif "Audit Summary" in section:
                        st.subheader("📝 Audit Summary")
                        st.markdown(section.replace("Audit Summary:", "").strip())
                    elif "Improvement Suggestions" in section:
                        st.subheader("🛠️ Suggestions for Improvement")
                        st.markdown(section.replace("Improvement Suggestions:", "").strip())
                    else:
                        st.markdown(section.strip())
            except Exception as e:
                st.error("Error formatting response.")
                st.code(result)





