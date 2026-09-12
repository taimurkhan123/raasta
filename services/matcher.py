import json
from services.llm import call_llm

def analyze_situation(user_query):
    system_prompt = """
    You are the Raasta intent matching engine. Analyze the citizen's query.
    Map it to one of these service IDs exactly:
    - "cnic_correction"
    - "fir_filing"
    - "domicile"
    - "birth_certificate"
    - "unknown" (if none match)
    
    Return a valid JSON object ONLY:
    {
      "service_id": "...",
      "intent_description": "...",
      "confidence": 0.0 to 1.0,
      "language_detected": "urdu/english/mixed",
      "rejection_mentioned": true/false
    }
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]
    
    response = call_llm(messages, response_format={"type": "json_object"})
    try:
        return json.loads(response)
    except Exception:
        return {"service_id": "unknown", "confidence": 0.0}
