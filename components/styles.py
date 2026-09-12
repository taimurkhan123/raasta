import streamlit as st


def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background: #F8FAFC;
    }

    /* ============ SIDEBAR — light with green accents ============ */
    section[data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E2E8F0;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #064E3B !important;
        font-weight: 700;
        letter-spacing: -0.3px;
    }
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span {
        color: #334155;
    }
    section[data-testid="stSidebar"] hr {
        border-color: #E2E8F0;
        margin: 1rem 0;
    }

    /* Sidebar nav links */
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
        border-radius: 8px;
        padding: 8px 12px;
        margin: 2px 0;
        color: #334155 !important;
        transition: background 0.15s;
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
        background: #ECFDF5 !important;
        color: #047857 !important;
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] * {
        color: #FFFFFF !important;
    }

    /* Language selectbox — native, clean */
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] > label {
        display: none !important;
    }
    section[data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #F1F5F9 !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        color: #064E3B !important;
    }
    section[data-testid="stSidebar"] [data-baseweb="select"] > div:hover {
        border-color: #10B981 !important;
        background-color: #ECFDF5 !important;
    }
    section[data-testid="stSidebar"] [data-baseweb="select"] * {
        color: #064E3B !important;
    }

    /* File uploader */
    section[data-testid="stSidebar"] .stFileUploader > label {
        display: none !important;
    }
    section[data-testid="stSidebar"] .stFileUploader section {
        background-color: #F1F5F9 !important;
        border: 1.5px dashed #CBD5E1 !important;
        border-radius: 10px !important;
    }
    section[data-testid="stSidebar"] .stFileUploader section:hover {
        border-color: #10B981 !important;
        background-color: #ECFDF5 !important;
    }

    /* Buttons in sidebar */
    section[data-testid="stSidebar"] .stButton > button {
        background: #FFFFFF !important;
        color: #B91C1C !important;
        border: 1px solid #FECACA !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        background: #FEF2F2 !important;
        border-color: #EF4444 !important;
    }

    /* ============ HERO ============ */
    .raasta-hero {
        text-align: center;
        padding: 1.5rem 1rem 0.5rem 1rem;
    }
    .raasta-hero h1 {
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: -0.8px;
        background: linear-gradient(90deg, #059669 0%, #047857 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }
    .raasta-hero p {
        color: #475569;
        font-size: 1.05rem;
        margin-top: 0;
    }

    /* ============ CHAT BUBBLES ============ */
    .chat-row {
        display: flex;
        margin: 14px 0;
        align-items: flex-start;
        gap: 10px;
    }
    .chat-row.user { flex-direction: row-reverse; }
    .chat-avatar {
        width: 36px; height: 36px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 18px;
        flex-shrink: 0;
    }
    .chat-avatar.user { background: #DCFCE7; }
    .chat-avatar.ai   { background: #064E3B; color: white; }

    .chat-bubble-user, .chat-bubble-ai {
        padding: 14px 18px;
        border-radius: 16px;
        max-width: 82%;
        line-height: 1.55;
        font-size: 0.97rem;
    }
    .chat-bubble-user {
        background: linear-gradient(135deg, #DCFCE7 0%, #BBF7D0 100%);
        color: #064E3B;
        border: 1px solid #86EFAC;
        border-top-right-radius: 4px;
    }
    .chat-bubble-ai {
        background: #FFFFFF;
        color: #1E293B;
        border: 1px solid #E2E8F0;
        border-top-left-radius: 4px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }
    .chat-bubble-ai h3 {
        margin-top: 14px;
        margin-bottom: 6px;
        font-size: 1.02rem;
        color: #047857;
    }
    .chat-bubble-ai h3:first-child { margin-top: 0; }
    .chat-bubble-ai ul { margin: 6px 0 6px 18px; }
    .chat-bubble-ai li { margin: 3px 0; }

    .chip-label {
        color: #64748B;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        margin: 1.5rem 0 0.6rem 0;
    }

    /* ============ EXPANDER ============ */
    div[data-testid="stExpander"] {
        border: 1px solid #E2E8F0 !important;
        border-radius: 14px !important;
        background: #FFFFFF !important;
        box-shadow: 0 1px 3px rgba(15,23,42,0.03);
    }
    div[data-testid="stExpander"] summary {
        font-weight: 600;
        color: #047857;
    }

    /* ============ BUTTONS ============ */
    .stButton > button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        padding: 0.55rem 1.1rem !important;
        transition: all 0.15s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(5, 150, 105, 0.25) !important;
        color: white !important;
    }

    /* ============ CHAT INPUT ============ */
    div[data-testid="stChatInput"] {
        border-radius: 14px;
        border: 1.5px solid #E2E8F0;
        background: #FFFFFF;
        box-shadow: 0 4px 14px rgba(15,23,42,0.04);
    }
    div[data-testid="stChatInput"]:focus-within {
        border-color: #10B981;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.15);
    }

    /* ============ FEE ALERT & NEXT STEP ============ */
    .fee-alert {
        background-color: #FEF3C7;
        border-left: 4px solid #F59E0B;
        padding: 10px 14px;
        margin: 12px 0;
        border-radius: 8px;
        color: #78350F;
        font-size: 0.92rem;
    }
    .next-step {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white;
        padding: 14px 18px;
        border-radius: 12px;
        font-weight: 600;
        margin-top: 14px;
        box-shadow: 0 4px 12px rgba(5,150,105,0.2);
    }

    /* ============ CARDS ============ */
    .service-card {
        background: #FFFFFF;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(15,23,42,0.04);
        transition: transform 0.15s, border-color 0.15s, box-shadow 0.15s;
    }
    .service-card:hover {
        border-color: #10B981;
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(16,185,129,0.08);
    }
    .service-card h4 {
        margin: 0 0 8px 0;
        color: #064E3B;
        font-size: 1.05rem;
    }
    .service-card p {
        margin: 0;
        color: #64748B;
        font-size: 0.9rem;
    }
    .step-card {
        background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
        padding: 16px 12px;
        border-radius: 12px;
        text-align: center;
        font-size: 0.9rem;
        font-weight: 600;
        color: #047857;
        border: 1px solid #A7F3D0;
    }
    .hero-section {
        text-align: center;
        padding: 2rem 1rem;
        background: linear-gradient(180deg, #ECFDF5 0%, #FFFFFF 100%);
        border-radius: 18px;
        margin-bottom: 1.5rem;
        border: 1px solid #D1FAE5;
    }
    </style>
    """, unsafe_allow_html=True)
