
import streamlit as st
from components.styles import inject_custom_css

st.set_page_config(
    page_title="Raasta | Apni Problem Batayein",
    page_icon="🛣️",
    layout="centered",
    initial_sidebar_state="expanded"
)

inject_custom_css()

def main():
    st.markdown("""
        <div class="hero-section">
            <h1 style='color: #006600; font-size: 2.8rem;'>Raasta</h1>
            <h3 style='color: #475569; font-weight: 500;'>Government processes shouldn’t feel complicated.</h3>
            <p style='font-size: 1.2rem; margin-top: 15px; color: #334155;'>
                Tell Raasta your problem in Urdu or English and get a clear, verified roadmap for what to do next.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([1, 0.2, 1, 0.2, 1])
    with col1:
        st.markdown("<div class='step-card'>🗣️ Your Problem</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align:center; margin-top:15px;'>→</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='step-card'>🔎 Right Service</div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div style='text-align:center; margin-top:15px;'>→</div>", unsafe_allow_html=True)
    with col5:
        st.markdown("<div class='step-card'>✅ Next Step</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### How we can help today:")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class='service-card'>
            <h4>🪪 CNIC Correction</h4>
            <p>Fix name, address, or DOB issues.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='service-card'>
            <h4>📜 Domicile Certificate</h4>
            <p>Apply for university or job requirements.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='service-card'>
            <h4>🚨 FIR Filing</h4>
            <p>Report a crime or lost items correctly.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='service-card'>
            <h4>👶 Birth Certificate</h4>
            <p>Register a newborn or get a delayed certificate.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Tell Raasta Your Problem ➔", type="primary", use_container_width=True):
        st.switch_page("pages/1_🤖_Raasta_Assistant.py")

if __name__ == "__main__":
    main()
