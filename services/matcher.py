import json
import re
import streamlit as st
from services.llm import call_llm

SERVICE_KEYWORDS = {
    "cnic_correction": [
        "cnic", "nadra", "id card", "identity card", "shanaakhti",
        "naam ghalat", "name change", "dob", "date of birth",
        "address change", "cnic correction", "cnic theek",
        "سینے سی", "سینی سی", "شناختی", "شناختی کارڈ", "نادرا", "کارڈ",
        "نام غلط", "نام تبدیل", "تاریخ پیدائش", "پتہ تبدیل",
    ],
    "fir_filing": [
        "fir", "police", "chori", "stolen", "theft", "crime",
        "report karni", "gum", "lost", "robbery", "snatching",
        "ایف آئی آر", "پولیس", "چوری", "گم", "گمشدہ", "ڈکیتی", "رپورٹ",
    ],
    "domicile": [
        "domicile", "rihaish", "residence", "dc office",
        "e-khidmat", "baqaida", "ڈومیسائل", "رہائش", "رہائشی",
    ],
    "birth_certificate": [
        "birth", "paidaish", "newborn", "union council",
        "b-form", "bacha", "پیدائش", "پیدائشی", "بچہ", "بچے", "یونین کونسل",
    ],
}


def _keyword_match(query):
    q = query.lower()
    best, score = None, 0
    for service_id, keywords in SERVICE_KEYWORDS.items():
        hits = sum(1 for kw in keywords if kw in q)
        if hits > score:
            best, score = service_id, hits
    return best if score > 0 else None


def _extract_json(text):
    if not text:
        return None
    try:
        return json.loads(text)
    except Exception:
        pass
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fence:
        try:
            return json.loads(fence.group(1))
        except Exception:
            pass
    brace = re.search(r"\{.*\}", text, re.DOTALL)
    if brace:
        try:
            return json.loads(brace.group(0))
        except Exception:
            pass
    return None


def _llm_classify(user_query):
    system_prompt = """
You are Raasta's intent classifier. The user is a Pakistani citizen.
They may write in English, Roman Urdu, or Urdu script.

Classify their query into EXACTLY ONE of:
- "cnic_correction"  (fix name/DOB/address on existing CNIC, NADRA)
- "fir_filing"       (police report, FIR, stolen/lost items, crime)
- "domicile"         (domicile certificate, DC office, residence proof)
- "birth_certificate" (birth registration, newborn, union council)
- "unknown"          (only if truly none)

Return ONLY valid JSON, nothing else:
{"service_id":"...","confidence":0.9,"language_detected":"urdu|english|mixed","rejection_mentioned":false}
"""
    raw = call_llm([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ])
    return _extract_json(raw)


def analyze_situation(user_query, preferred_language="Auto-detect"):
    kw_hit = _keyword_match(user_query)
    if kw_hit:
        return {
            "service_id": kw_hit,
            "intent_description": f"Matched: {kw_hit}",
            "confidence": 0.9,
            "language_detected": "mixed",
            "rejection_mentioned": False,
        }

    try:
        result = _llm_classify(user_query)
        if result and result.get("service_id") in (
            "cnic_correction", "fir_filing", "domicile", "birth_certificate"
        ):
            result.setdefault("confidence", 0.85)
            result.setdefault("language_detected", "mixed")
            result.setdefault("rejection_mentioned", False)
            return result
    except Exception as e:
        st.warning(f"Classifier error: {e}")

    return {
        "service_id": "unknown",
        "confidence": 0.0,
        "language_detected": "english",
        "rejection_mentioned": False,
    }
