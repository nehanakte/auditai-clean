import openai

client = openai.OpenAI(
    api_key="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",  # <--- your key
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







