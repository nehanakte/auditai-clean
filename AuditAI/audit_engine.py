import os
import streamlit as st
from groq import Groq

api_key = st.secrets["API_KEY"]

client = Groq(api_key=api_key)

def audit_model(description):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": description}
            ]
        )
        reply = response.choices[0].message.content
        return f"📝 Let’s take a quick look at the scorecard:\n\n{reply}"
    except Exception as e:
        return f"❌ API Error: {str(e)}"

