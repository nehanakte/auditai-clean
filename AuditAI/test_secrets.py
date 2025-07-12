import streamlit as st

api_key = st.secrets["API_KEY"]
print("✅ API key loaded:", bool(api_key))
