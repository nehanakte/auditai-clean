import streamlit as st
from groq import Groq

api_key = st.secrets["API_KEY"]
client = Groq(api_key=api_key)

def audit_model(description):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You're an AI ethics auditor. For the user's input, return three things:\n\n"
                        "1. A scorecard of key ethical principles (Fairness, Transparency, Privacy, Accountability, Human Oversight). "
                        "For each, rate as ✅ (Good), ⚠️ (Needs Improvement), or ❌ (Poor) and add a one-line reason.\n\n"
                        "2. A short audit summary paragraph (4-5 lines) highlighting ethical strengths and risks.\n\n"
                        "3. Three actionable improvement suggestions for more ethical and responsible deployment.\n\n"
                        "Be concise and professional. Start with the scorecard."
                    ),
                },
                {"role": "user", "content": description},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ API Error: {str(e)}"



