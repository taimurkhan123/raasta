import streamlit as st
from components.styles import inject_custom_css

st.set_page_config(page_title="Services | Raasta", page_icon="📋")
inject_custom_css()

st.title("📋 Supported Services (V1)")
st.markdown("Currently, Raasta guides citizens through the following verified government processes.")

services = [
    {"icon": "🪪", "name": "CNIC Correction", "desc": "Modify name, DOB, or address via NADRA.", "mode": "In-person / Online (Pak Identity)"},
    {"icon": "🚨", "name": "FIR Filing", "desc": "Report lost documents or file a criminal complaint.", "mode": "In-person (Police Station)"},
    {"icon": "📜", "name": "Domicile Certificate", "desc": "Establish residency for education or employment.", "mode": "In-person (DC Office) / Online (Selected districts)"},
    {"icon": "👶", "name": "Birth Certificate", "desc": "Register a newborn or apply for delayed registration.", "mode": "In-person (Union Council)"}
]

for s in services:
    st.markdown(f"""
    <div class='service-card'>
        <h3 style='margin-top:0;'>{s['icon']} {s['name']}</h3>
        <p><b>Description:</b> {s['desc']}</p>
        <p><b>Application Mode:</b> {s['mode']}</p>
    </div>
    """, unsafe_allow_html=True)
