import streamlit as st
from components.styles import inject_custom_css
from utils.helpers import check_api_key
from services.speech import transcribe_audio
from services.matcher import analyze_situation
from services.retrieval import get_service_data
from services.response import generate_response

st.set_page_config(
    page_title="Raasta Assistant",
    page_icon="🛣️",
    layout="centered",
    initial_sidebar_state="expanded",
)
inject_custom_css()
check_api_key()

with st.sidebar:
    st.markdown("## 🛣️ Raasta")
    st.caption("Government navigation, simplified.")
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    language = st.radio(
        "Preferred Language",
        options=["Auto-detect", "English", "اردو (Urdu)", "Roman Urdu"],
        index=0,
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("### 📎 Upload Document")
    uploaded_file = st.file_uploader(
        "Attach a photo or PDF (optional)",
        type=["pdf", "png", "jpg", "jpeg"],
        label_visibility="collapsed",
    )
    if uploaded_file is not None:
        st.success(f"✅ {uploaded_file.name}")
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending_query = None
        st.rerun()

st.markdown("""
<div class="raasta-hero">
    <h1>🤖 Raasta Assistant</h1>
    <p>Describe your situation in text or voice — I'll give you the verified next step.</p>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_query" not in st.session_state:
    st.session_state.pending_query = None

if not st.session_state.messages:
    st.markdown('<div class="chip-label">Try one of these:</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🪪 Meri CNIC mein naam ghalat hai", use_container_width=True):
            st.session_state.pending_query = "Meri CNIC mein naam ghalat hai, kaise theek karun?"
            st.rerun()
        if st.button("📜 Mujhe domicile chahiye", use_container_width=True):
            st.session_state.pending_query = "Mujhe domicile certificate chahiye, kya process hai?"
            st.rerun()
    with c2:
        if st.button("🚨 I want to file an FIR", use_container_width=True):
            st.session_state.pending_query = "I want to file an FIR for a stolen bike."
            st.rerun()
        if st.button("👶 Birth certificate kaise banayein", use_container_width=True):
            st.session_state.pending_query = "Naye bache ka birth certificate kaise banwayein?"
            st.rerun()

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="chat-row user">
            <div class="chat-avatar user">👤</div>
            <div class="chat-bubble-user">{msg['content']}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-row">
            <div class="chat-avatar ai">🛣️</div>
            <div class="chat-bubble-ai">{msg['content']}</div>
        </div>
        """, unsafe_allow_html=True)

with st.expander("🎙️ Voice Input — click to record", expanded=False):
    audio_value = st.audio_input("Record your problem")
    if audio_value is not None:
        if st.button("📤 Transcribe & Send", use_container_width=True):
            transcription = transcribe_audio(audio_value.getvalue())
            if transcription:
                st.session_state.pending_query = transcription
                st.rerun()
            else:
                st.error("Nothing transcribed — please try again.")

user_input = st.chat_input("Type your problem here...")

query_to_process = None
if st.session_state.pending_query:
    query_to_process = st.session_state.pending_query
    st.session_state.pending_query = None
elif user_input:
    query_to_process = user_input

if query_to_process:
    display_query = query_to_process
    if uploaded_file is not None:
        display_query = f"📎 [{uploaded_file.name}] {query_to_process}"

    st.session_state.messages.append({"role": "user", "content": display_query})
    st.markdown(f"""
    <div class="chat-row user">
        <div class="chat-avatar user">👤</div>
        <div class="chat-bubble-user">{display_query}</div>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("Understanding your situation..."):
        try:
            augmented_query = query_to_process
            if uploaded_file is not None:
                augmented_query = f"[User attached: {uploaded_file.name}] " + query_to_process

            situation = analyze_situation(augmented_query, preferred_language=language)

            if situation.get("confidence", 0) >= 0.7 and situation.get("service_id") != "unknown":
                service_data = get_service_data(situation["service_id"])
            else:
                service_data = None

            response = generate_response(augmented_query, situation, service_data, preferred_language=language)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.markdown(f"""
            <div class="chat-row">
                <div class="chat-avatar ai">🛣️</div>
                <div class="chat-bubble-ai">{response}</div>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Connection error: {e}")
