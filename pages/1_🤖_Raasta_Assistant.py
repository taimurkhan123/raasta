import streamlit as st
from audio_recorder_streamlit import audio_recorder
from components.styles import inject_custom_css
from utils.helpers import check_api_key
from services.speech import transcribe_audio
from services.matcher import analyze_situation
from services.retrieval import get_service_data
from services.response import generate_response

st.set_page_config(page_title="Raasta Assistant", page_icon="🤖")
inject_custom_css()
check_api_key()

st.title("🤖 Raasta Assistant")
st.markdown("Describe your situation in text or voice. I’ll help you find the right next step.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    css_class = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-ai"
    st.markdown(f"<div class='{css_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# Input area
st.markdown("---")
col1, col2 = st.columns([0.85, 0.15])

with col2:
    st.markdown("<div style='margin-top:25px;'>", unsafe_allow_html=True)
    audio_bytes = audio_recorder(text="", icon_size="2x", icon_name="microphone")
    st.markdown("</div>", unsafe_allow_html=True)

with col1:
    user_input = st.chat_input("Type your problem here... (e.g., 'Meri CNIC mein naam ghalat hai')")

query_to_process = None

if audio_bytes:
    try:
        transcription = transcribe_audio(audio_bytes)
        if transcription:
            query_to_process = transcription
            st.success(f"🗣️ Heard: {transcription}")
    except Exception as e:
        st.error(f"Audio Error: {str(e)}")

if user_input:
    query_to_process = user_input

if query_to_process:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query_to_process})
    st.markdown(f"<div class='chat-bubble-user'>{query_to_process}</div>", unsafe_allow_html=True)
    
    with st.spinner("Understanding your situation..."):
        try:
            situation = analyze_situation(query_to_process)
            
            if situation['confidence'] >= 0.7 and situation['service_id'] != 'unknown':
                st.toast(f"Matched Service: {situation['service_id']} (Confidence: {situation['confidence']})")
                service_data = get_service_data(situation['service_id'])
            else:
                service_data = None
                
            response = generate_response(query_to_process, situation, service_data)
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.markdown(f"<div class='chat-bubble-ai'>{response}</div>", unsafe_allow_html=True)
            
        except Exception as e:
            # THIS NOW SHOWS THE REAL ERROR
            st.error(f"SYSTEM ERROR: {str(e)}")
