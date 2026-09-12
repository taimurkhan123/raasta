import json
import os
import streamlit as st

@st.cache_data
def get_service_data(service_id):
    filepath = os.path.join("data", f"{service_id}.json")
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
