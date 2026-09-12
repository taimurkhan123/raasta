import json
import re
import streamlit as st
from services.llm import call_llm

# Keyword fallback so we don't depend 100% on the LLM
KEYWORD_MAP = {
    "cnic_correction": ["cnic", "nadra", "shanaakhti", "id card", "naam ghalat",
                        "name change", "dob change", "address change"],
    "fir_filing": ["fir", "police", "chori", "stolen", "theft", "crime",
                   "report", "report karni", "gum"],
    "domicile": ["domicile", "residence", "dc office", "e-khidmat",
                 "rihaish", "baqaida"],
    "birth_certificate": ["birth", "paidaish", "newborn", "union council",
                          "b-form", "bacha"],
}


def _keyword_fallback(query: str):
    q = query.lower()
    for service_id, keywords in KEYWORD_MAP.items():
        if any(kw in q for kw in keywords):
            return service_id
    return None


def _extract_json(text: str):
    """Try hard to pull a JSON object out of the model's reply."""
    if not text:
        return None
    # 1. Direct parse
    try:
        return json.loads(text)
    except Exception:
        pass
    # 2. Strip ```json ... ``` fences
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fence:
        try:
            return json.loads(fence.group(1))
        except Exception:
            pass
    # 3. First { ... } block
    brace = re.search(r"\{.*\}", text, re.DOTALL)
    if brace:
        try:
            return json.loads(brace.group(0))
        except Exception:
            pass
    return None


def analyze_situation(user_query, preferred_language="Auto-detect"):
    system_prompt = f"""
You are the Raasta intent matching engine.

User's preferred response language: {preferred_language}
If preferred language is "Auto-detect", detect from the query itself.

Map the query to ONE of these service IDs exactly:
- "cnic_correction"  (fixing name, DOB, address on CNIC — NADRA)
- "fir_filing"       (filing a police report / FIR)
- "domicile"         (domicile certificate from DC office)
- "birth_certificate" (birth registration at union council)
- "unknown"          (only if truly none of the above)

Return ONLY a single-line valid JSON object. No markdown. No explanation.
Example output:
{{"service_id":"cnic_correction","intent_description":"User wants to fix name on CNIC","confidence":0.95,"language_detected":"mixed","rejection_mentioned":false}}

Rules for confidence:
- If the query clearly mentions CNIC/NADRA/FIR/police/domicile/birth, use confidence 0.85-0.99.
- If ambiguous, use 0.5-0.7.
- If completely unrelated, use 0.0-0.3 with service_id "unknown".
"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ]

    raw = ""
    parsed = None
    try:
        raw = call_llm(messages)  # no response_format — let the prompt do the work
        parsed = _extract_json(raw)
    except Exception as e:
        st.warning(f"LLM call failed: {e}")

    # If JSON parsing failed, try a keyword fallback
    if not parsed:
        kw = _keyword_fallback(user_query)
        if kw:
            return {
                "service_id": kw,
                "intent_description": "Matched via keyword fallback",
                "confidence": 0.8,
                "language_detected": preferred_language.lower() if preferred_language != "Auto-detect" else "english",
                "rejection_mentioned": False,
            }
        return {
            "service_id": "unknown",
            "confidence": 0.0,
            "language_detected": "english",
            "rejection_mentioned": False,
        }

    # Normalize keys
    parsed.setdefault("service_id", "unknown")
    parsed.setdefault("confidence", 0.0)
    parsed.setdefault("language_detected", "english")
    parsed.setdefault("rejection_mentioned", False)
    parsed.setdefault("intent_description", "")

    # If LLM said low confidence but keywords clearly match, boost it
    if parsed["confidence"] < 0.7:
        kw = _keyword_fallback(user_query)
        if kw and kw == parsed.get("service_id"):
            parsed["confidence"] = max(parsed["confidence"], 0.8)

    return parsed
