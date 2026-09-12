def check_api_key():
    import streamlit as st
    if "GROQ_API_KEY" not in st.secrets:
        st.error("⚠️ GROQ_API_KEY is missing. Please add it to Streamlit Cloud Secrets.")
        st.stop()
