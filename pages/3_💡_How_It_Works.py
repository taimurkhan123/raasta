import streamlit as st
from components.styles import inject_custom_css

st.set_page_config(page_title="How It Works | Raasta")
inject_custom_css()

st.title("💡 How Raasta Works")

st.markdown("""
### The AI Pipeline
Raasta uses a secure, verified pipeline to ensure you never get hallucinated government instructions.

1. **Voice / Text Input**: You speak or type your problem naturally.
2. **Speech-to-Text**: Groq Whisper models transcribe your voice accurately.
3. **Situation Engine**: An LLM extracts your true intent, language, and context.
4. **Service Matching**: Your intent is matched to our hardcoded, verified JSON knowledge base.
5. **Rule Processing**: Required documents, exact fees, and application modes are extracted.
6. **Personalized Guide**: The AI formats this strict data into an easy-to-read, language-matched roadmap.
7. **Next Best Action**: You receive ONE clear instruction on what to do today.
""")
