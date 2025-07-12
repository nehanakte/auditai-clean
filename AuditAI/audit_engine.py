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
                        "You are conducting an AI ethics audit. "
                        "Respond in the following format:\n\n"
                        "### Scorecard:\n"
                        "- Fairness: [Rating] – [Reason]\n"
                        "- Transparency: [Rating] – [Reason]\n"
                        "- Accountability: [Rating] – [Reason]\n"
                        "- Privacy: [Rating] – [Reason]\n"
                        "- Safety: [Rating] – [Reason]\n\n"
                        "### Audit Summary:\n"
                        "(One paragraph summary of the system's ethical standing.)\n\n"
                        "### Improvement Suggestions:\n"
                        "(Actionable recommendations to improve the system ethically.)"
                    )
                },
                {"role": "user", "content": description}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ API Error: {str(e)}"





        

