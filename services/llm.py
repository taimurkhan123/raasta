import streamlit as st
from groq import Groq

def get_groq_client():
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

def call_llm(messages, response_format=None, temperature=0.1):
    client = get_groq_client()
    kwargs = {
        "model": "llama3-8b-8192",  # Updated to valid Groq model string
        "messages": messages,
        "temperature": temperature
    }
    if response_format:
        kwargs["response_format"] = response_format
        
    response = client.chat.completions.create(**kwargs)
    return response.choices[0].message.content
