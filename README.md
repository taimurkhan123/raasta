# Raasta — Voice-First Bureaucracy Assistant

**“Apni problem batayein. Raasta aapko agla qadam bataye.”**

Raasta is a voice-first AI government-service navigation assistant for citizens in Pakistan. It simplifies bureaucratic processes by understanding a citizen's situation (in Urdu, English, or mixed language), matching it to the correct service, and providing verified, structured guidance on required documents, official fees, and exact next steps.

## Features
- **Voice & Text Input**: Describe your problem naturally in Urdu or English.
- **Situation Engine**: Extracts intent, language, and context automatically.
- **Verified Knowledge Base**: Powered by static JSON rules, not LLM hallucinations.
- **Fee Transparency**: Displays verified fees and warns against overcharging.
- **Rejection Navigator**: Guides citizens on what to do if an application is rejected.

## Supported Services (MVP)
1. CNIC Correction
2. FIR Filing
3. Domicile Certificate
4. Birth Certificate

## AI & RAG Architecture
- **Speech-to-Text**: Groq Whisper API for lightning-fast Urdu/English transcription.
- **LLM Engine**: Groq LLaMA-3 (Fast inference for real-time hackathon demos).
- **RAG**: Structured JSON retrieval. The LLM only receives verified JSON data to formulate its answer.
- **Anti-Hallucination**: Strict confidence thresholds, fallback to clarification, and hardcoded fee/source mappings.

## Deployment (Streamlit Cloud)
1. Push this repository to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Create a new app and select this repository.
4. Set the Main file path to `app.py`.
5. Go to Advanced Settings -> Secrets and add your Groq API key:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_key_here"
