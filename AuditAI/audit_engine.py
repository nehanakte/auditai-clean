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
                        "You're an ethical AI auditor. When given a description of an AI system, "
                        "respond with a scorecard (principle, rating, reason), an overall audit summary, "
                        "and suggestions for improvement."
                    )
                },
                {"role": "user", "content": description}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ API Error: {str(e)}"




