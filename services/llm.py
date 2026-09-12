import streamlit as st
from groq import Groq


def get_groq_client():
    return Groq(api_key=st.secrets["GROQ_API_KEY"])


def call_llm(messages, temperature=0.1):
    client = get_groq_client()
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content
