import streamlit as st


def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #F0FDF4 0%, #F8FAFC 400px, #F8FAFC 100%);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #064E3B 0%, #065F46 100%);
        border-right: none;
    }
    section[data-testid="stSidebar"] * { color: #ECFDF5; }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
        font-weight: 700;
    }
    section[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.15); }

    /* LANGUAGE SELECTBOX — white box, green text */
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] > label {
        color: rgba(255,255,255,0.85) !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 2px solid #10B981 !important;
        border-radius: 10px !important;
    }
    section[data-testid="stSidebar"] [data-baseweb="select"] *,
    section[data-testid="stSidebar"] [data-baseweb="select"] input,
    section[data-testid="stSidebar"] [data-baseweb="select"] span,
    section[data-testid="stSidebar"] [data-baseweb="select"] div {
        color: #064E3B !important;
        -webkit-text-fill-color: #064E3B !important;
        background-color: transparent !important;
    }
    section[data-testid="stSidebar"] [data-baseweb="select"] svg {
        fill: #064E3B !important;
    }
    section[data-testid="stSidebar"] [data-baseweb="select"] input::placeholder {
        color: #64748B !important;
    }
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] *,
    div[data-baseweb="menu"],
    div[data-baseweb="menu"] * {
        background-color: #FFFFFF !important;
        color: #1E293B !important;
    }
    div[data-baseweb="popover"] ul li:hover,
    div[data-baseweb="popover"] ul li[aria-selected="true"] {
        background-color: #ECFDF5 !important;
        color: #047857 !important;
    }

    section[data-testid="stSidebar"] .stFileUploader section {
        background-color: rgba(255,255,255,0.08) !important;
        border: 1px solid rgba(255,255,255,0.22) !important;
        border-radius: 10px !important;
    }
    section[data-testid="stSidebar"] .stFileUploader section * {
        color: #FFFFFF !important;
    }
    section[data-testid="stSidebar"] button {
        background: rgba(255,255,255,0.1) !important;
        color: #FFF !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    section[data-testid="stSidebar"] button:hover {
        background: rgba(255,255,255,0.2) !important;
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
        border-radius: 10px;
        padding: 8px 12px;
        margin: 2px 0;
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
        background: rgba(255,255,255,0.12) !important;
    }

    .raasta-hero { text-align: center; padding: 1.2rem 1rem 0.5rem; }
    .raasta-hero h1 {
        font-size: 2.4rem; font-weight: 800; letter-spacing: -0.8px;
        background: linear-gradient(90deg, #059669 0%, #047857 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }
    .raasta-hero p { color: #475569; font-size: 1.05rem; margin-top: 0; }

    .chat-row { display: flex; margin: 14px 0; align-items: flex-start; gap: 10px; }
    .chat-row.user { flex-direction: row-reverse; }
    .chat-avatar {
        width: 36px; height: 36px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 18px; flex-shrink: 0;
    }
    .chat-avatar.user { background: #DCFCE7; }
    .chat-avatar.ai { background: #064E3B; color: white; }
    .chat-bubble-user, .chat-bubble-ai {
        padding: 14px 18px; border-radius: 16px;
        max-width: 82%; line-height: 1.55; font-size: 0.97rem;
    }
    .chat-bubble-user {
        background: linear-gradient(135deg, #DCFCE7 0%, #BBF7D0 100%);
        color: #064E3B; border: 1px solid #86EFAC;
        border-top-right-radius: 4px;
    }
    .chat-bubble-ai {
        background: #FFFFFF; color: #1E293B;
        border: 1px solid #E2E8F0; border-top-left-radius: 4px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }
    .chat-bubble-ai h3 { margin-top: 14px; margin-bottom: 6px; color: #047857; }
    .chat-bubble-ai h3:first-child { margin-top: 0; }
    .chat-bubble-ai ul { margin: 6px 0 6px 18px; }

    .chip-label {
        color: #64748B; font-size: 0.85rem; font-weight: 600;
        text-transform: uppercase; letter-spacing: 0.6px;
        margin: 1.5rem 0 0.6rem 0;
    }

    div[data-testid="stExpander"] {
        border: 1px solid #E2E8F0 !important;
        border-radius: 14px !important;
        background: #FFFFFF !important;
    }
    div[data-testid="stExpander"] summary { font-weight: 600; color: #047857; }

    .stButton > button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        padding: 0.55rem 1.1rem !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(5, 150, 105, 0.25) !important;
    }

    div[data-testid="stChatInput"] {
        border-radius: 14px;
        border: 1.5px solid #E2E8F0;
        background: #FFFFFF;
    }
    div[data-testid="stChatInput"]:focus-within {
        border-color: #10B981;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.15);
    }

    .fee-alert {
        background-color: #FEF3C7;
        border-left: 4px solid #F59E0B;
        padding: 10px 14px; margin: 12px 0;
        border-radius: 8px; color: #78350F;
    }
    .next-step {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white; padding: 14px 18px;
        border-radius: 12px; font-weight: 600; margin-top: 14px;
    }

    .service-card {
        background: #FFFFFF; padding: 20px; border-radius: 14px;
        border: 1px solid #E2E8F0; margin-bottom: 12px;
    }
    .service-card h4 { margin: 0 0 8px 0; color: #064E3B; }
    .service-card p { margin: 0; color: #64748B; font-size: 0.9rem; }
    .step-card {
        background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
        padding: 16px 12px; border-radius: 12px; text-align: center;
        font-size: 0.9rem; font-weight: 600; color: #047857;
        border: 1px solid #A7F3D0;
    }
    .hero-section {
        text-align: center; padding: 2rem 1rem;
        background: linear-gradient(180deg, #ECFDF5 0%, #FFFFFF 100%);
        border-radius: 18px; margin-bottom: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)
