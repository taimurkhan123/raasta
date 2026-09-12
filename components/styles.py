import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
        .hero-section {
            text-align: center;
            padding: 2rem 1rem;
            background: linear-gradient(180deg, #E8F5E9 0%, #FFFFFF 100%);
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }
        .step-card {
            background-color: #F1F5F9;
            padding: 15px 10px;
            border-radius: 8px;
            text-align: center;
            font-size: 0.9rem;
            font-weight: 600;
            color: #006600;
            border: 1px solid #E2E8F0;
        }
        .service-card {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            transition: transform 0.2s;
        }
        .service-card:hover {
            border-color: #006600;
            transform: translateY(-2px);
        }
        .service-card h4 {
            margin: 0 0 10px 0;
            color: #1E293B;
        }
        .service-card p {
            margin: 0;
            color: #64748B;
            font-size: 0.9rem;
        }
        .chat-bubble-user {
            background-color: #E8F5E9;
            padding: 15px;
            border-radius: 15px 15px 0px 15px;
            margin: 10px 0;
            border: 1px solid #C8E6C9;
        }
        .chat-bubble-ai {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 15px 15px 15px 0px;
            margin: 10px 0;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }
        .fee-alert {
            background-color: #FFF3CD;
            border-left: 5px solid #FFC107;
            padding: 10px 15px;
            margin: 15px 0;
            border-radius: 4px;
            color: #856404;
        }
        .next-step {
            background-color: #006600;
            color: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            margin-top: 15px;
        }
    </style>
    """, unsafe_allow_html=True)
