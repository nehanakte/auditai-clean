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
                        "You're an AI auditing assistant. Given a government or public-sector AI use case, "
                        "you must return an ethics audit scorecard with scores from 1 to 5 for the following principles:\n"
                        "• Fairness\n• Transparency\n• Accountability\n• Privacy\n• Inclusivity\n"
                        "For each principle, include a one-line explanation. "
                        "Always respond in this format:\n\n"
                        "**Fairness:** 4/5 – Explanation\n"
                        "**Transparency:** 3/5 – Explanation\n"
                        "... and so on."
                    ),
                },
                {"role": "user", "content": description}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ API Error: {str(e)}"


