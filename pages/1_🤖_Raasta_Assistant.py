import streamlit as st
from components.styles import inject_custom_css
from utils.helpers import check_api_key
from services.speech import transcribe_audio
from services.matcher import analyze_situation
from services.retrieval import get_service_data
from services.response import generate_response

st.set_page_config(page_title="Raasta Assistant", page_icon="🤖", layout="centered")
inject_custom_css()
check_api_key()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Settings / ترتیبات")
    language = st.selectbox(
        "Preferred Language / پسندیدہ زبان",
        options=["Auto-detect", "English", "اردو (Urdu)", "Roman Urdu"],
        index=0,
        help="Choose how you want Raasta to respond.",
    )

    st.markdown("---")
    st.header("📎 Upload Document / دستاویز")
    uploaded_file = st.file_uploader(
        "Attach a photo or PDF (optional)",
        type=["pdf", "png", "jpg", "jpeg"],
        help="Upload CNIC, domicile, FIR copy, etc.",
    )
    if uploaded_file is not None:
        size_kb = max(1, uploaded_file.size // 1024)
        st.success(f"✅ {uploaded_file.name} ({size_kb} KB)")

    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ---------------- HEADER ----------------
st.title("🤖 Raasta Assistant")
st.markdown("Describe your situation in text or voice. I'll help you find the right next step.")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_query" not in st.session_state:
    st.session_state.pending_query = None

# ---------------- HISTORY ----------------
for msg in st.session_state.messages:
    css_class = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-ai"
    st.markdown(f"<div class='{css_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# ---------------- VOICE INPUT ----------------
with st.expander("🎙️ Voice Input / آواز سے بتائیں", expanded=False):
    audio_value = st.audio_input("Record your problem")
    if audio_value is not None:
        if st.button("📤 Transcribe & Send", type="secondary"):
            try:
                with st.spinner("🎧 Transcribing audio..."):
                    transcription = transcribe_audio(audio_value.getvalue())
                if transcription:
                    st.session_state.pending_query = transcription
                    st.rerun()
            except Exception as e:
                st.error(f"Could not process audio: {e}")

# ---------------- TEXT INPUT ----------------
user_input = st.chat_input(
    "Type your problem here... (e.g., 'Meri CNIC mein naam ghalat hai')"
)

query_to_process = None
if st.session_state.pending_query:
    query_to_process = st.session_state.pending_query
    st.session_state.pending_query = None
elif user_input:
    query_to_process = user_input

# ---------------- PROCESS ----------------
if query_to_process:
    display_query = query_to_process
    if uploaded_file is not None:
        display_query = f"📎 [{uploaded_file.name}] {query_to_process}"

    st.session_state.messages.append({"role": "user", "content": display_query})
    st.markdown(f"<div class='chat-bubble-user'>{display_query}</div>", unsafe_allow_html=True)

    with st.spinner("Understanding your situation..."):
        try:
            augmented_query = query_to_process
            if uploaded_file is not None:
                augmented_query = (
                    f"[User attached a document: {uploaded_file.name}. "
                    f"Consider that they may be referencing this document.] "
                    + query_to_process
                )

            situation = analyze_situation(
                augmented_query, preferred_language=language
            )

            if (
                situation.get("confidence", 0) >= 0.7
                and situation.get("service_id") != "unknown"
            ):
                st.toast(
                    f"Matched: {situation['service_id']} "
                    f"(Confidence: {situation['confidence']})"
                )
                service_data = get_service_data(situation["service_id"])
            else:
                service_data = None

            response = generate_response(augmented_query, situation, service_data)

            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )
            st.markdown(f"<div class='chat-bubble-ai'>{response}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Connection error: {e}")
