import json
from services.llm import call_llm


def analyze_situation(user_query, preferred_language="Auto-detect"):
    system_prompt = f"""
    You are the Raasta intent matching engine. Analyze the citizen's query.
    User's preferred response language: {preferred_language}
    If preferred language is "Auto-detect", detect from the query itself.

    Map the query to ONE of these service IDs exactly:
    - "cnic_correction"
    - "fir_filing"
    - "domicile"
    - "birth_certificate"
    - "unknown" (if none match)

    Return a valid JSON object ONLY (no markdown, no explanation):
    {{
      "service_id": "...",
      "intent_description": "...",
      "confidence": 0.0,
      "language_detected": "urdu/english/mixed",
      "rejection_mentioned": false
    }}
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ]

    response = call_llm(messages, response_format={"type": "json_object"})
    try:
        data = json.loads(response)
        data.setdefault("confidence", 0.0)
        data.setdefault("language_detected", "english")
        data.setdefault("rejection_mentioned", False)
        data.setdefault("service_id", "unknown")
        return data
    except Exception:
        return {
            "service_id": "unknown",
            "confidence": 0.0,
            "language_detected": "english",
            "rejection_mentioned": False,
        }
