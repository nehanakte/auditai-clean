import openai
import streamlit as st

client = openai.OpenAI(
    api_key=st.secrets["API_KEY"], 
    base_url="https://openrouter.ai/api/v1"
)

def audit_model(description):
    prompt = f"""
    You're an AI ethics auditor. Evaluate this AI system:
    ---
    {description}
    ---
    Score each: Fairness, Transparency, Accountability, Privacy, Safety, Data Governance (0–10).
    End with: Final Risk Level: Low / Medium / High.
    """

    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",  # ✅ simple safe model
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ API Error: {str(e)}"







