import streamlit as st
from components.styles import inject_custom_css

st.set_page_config(page_title="Trust & Sources | Raasta")
inject_custom_css()

st.title("🔎 Trust & Sources")

st.markdown("""
### 🛑 Our Anti-Hallucination Strategy
Large Language Models (LLMs) are great at talking, but terrible at facts. **Raasta's AI is explicitly forbidden from inventing government procedures.**

* **No Retrieved Source = No Procedure:** If our JSON database doesn't have it, Raasta won't guess.
* **Low Confidence = Clarification:** If the AI isn't 70%+ sure of what you need, it asks clarifying questions.
* **Fee Transparency:** Fees are hardcoded from official portals. We actively warn against overcharging.

### 📚 Knowledge Base Status
* **NADRA (CNIC):** Verified against `id.nadra.gov.pk`
* **Punjab Police (FIR):** Verified against `punjabpolice.gov.pk`
* **Local Govt (Birth/Domicile):** Base federal/provincial guidelines.

*Disclaimer: The AI is not the source of government truth. Always cross-check with official counters.*
""")
