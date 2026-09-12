import json
import re
import streamlit as st
from services.llm import call_llm

SERVICE_KEYWORDS = {
    "cnic_correction": [
        # English / Roman
        "cnic", "nadra", "id card", "identity card", "shanaakhti",
        "naam ghalat", "name change", "dob", "date of birth",
        "address change", "cnic correction", "cnic theek",
        # Urdu script
        "سینے سی", "شناختی", "شناختی کارڈ", "نادرا", "کارڈ",
        "نام غلط", "نام تبدیل", "تاریخ پیدائش", "پتہ تبدیل",
    ],
    "fir_filing": [
        # English / Roman
        "fir", "police", "chori", "stolen", "theft", "crime",
        "report karni", "gum", "lost", "robbery", "snatching",
        # Urdu script
        "ایف آئی آر", "ایف آئی", "پولیس", "چوری", "گم", "گمشدہ",
        "ڈکیتی", "سرقہ", "رپورٹ",
    ],
    "domicile": [
        # English / Roman
        "domicile", "rihaish", "residence", "dc office",
        "e-khidmat", "baqaida",
        # Urdu script
        "ڈومیسائل", "رہائش", "رہائشی", "ڈی سی",
    ],
    "birth_certificate": [
        # English / Roman
        "birth", "paidaish", "newborn", "union council",
        "b-form", "bacha",
        # Urdu script
        "پیدائش", "پیدائشی", "جनم", "بچہ", "بچے", "یونین کونسل",
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


def analyze_situation(user_query, preferred_language="Auto-detect"):
    kw_hit = _keyword_match(user_query)

    llm_result = None
    try:
        system_prompt = (
            'Reply with ONLY JSON: '
            '{"language_detected":"urdu|english|mixed","rejection_mentioned":true|false}'
        )
        raw = call_llm([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query},
        ])
        llm_result = _extract_json(raw)
    except Exception:
        llm_result = None

    lang = (llm_result or {}).get("language_detected", "english")
    rejection = bool((llm_result or {}).get("rejection_mentioned", False))

    if kw_hit:
        return {
            "service_id": kw_hit,
            "intent_description": f"Matched: {kw_hit}",
            "confidence": 0.9,
            "language_detected": lang,
            "rejection_mentioned": rejection,
        }
    return {
        "service_id": "unknown",
        "confidence": 0.0,
        "language_detected": lang,
        "rejection_mentioned": rejection,
    }
