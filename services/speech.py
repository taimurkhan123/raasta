import io
import streamlit as st
from groq import Groq


def transcribe_audio(audio_bytes):
    if not audio_bytes or len(audio_bytes) < 1000:
        st.warning("Audio too short — record again.")
        return ""

    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    file_obj = io.BytesIO(audio_bytes)
    file_obj.name = "audio.wav"

    with st.spinner("🎙️ Transcribing..."):
        try:
            resp = client.audio.transcriptions.create(
                file=file_obj,
                model="whisper-large-v3",
                language="ur",
            )
            text = resp.text.strip()
        except Exception as e:
            st.error(f"Whisper error: {e}")
            return ""

    if text:
        st.success(f"🗣️ Heard: {text}")
    else:
        st.warning("Nothing transcribed — try again.")
    return text
