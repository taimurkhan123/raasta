import streamlit as st
from groq import Groq
import io

def transcribe_audio(audio_bytes):
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    # Groq whisper requires a file-like object with a name
    file_obj = io.BytesIO(audio_bytes)
    file_obj.name = "audio.wav"
    
    with st.spinner("🎙️ Listening and transcribing..."):
        transcription = client.audio.transcriptions.create(
            file=file_obj,
            model="whisper-large-v3",
            prompt="The language might be Urdu, English, or mixed (Roman Urdu)."
        )
    return transcription.text
