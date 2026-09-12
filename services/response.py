from services.llm import call_llm


def generate_response(user_query, situation, service_data, preferred_language="Auto-detect"):
    if situation.get("confidence", 0) < 0.7 or situation.get("service_id") == "unknown":
        return "I want to make sure I give you the right information. I am not completely sure which service you need. Could you clarify? Are you trying to correct a CNIC, file an FIR, or get a certificate?"

    if preferred_language == "English":
        lang_rule = "Reply ONLY in English. Do not use Urdu script."
    elif preferred_language == "اردو (Urdu)":
        lang_rule = "آپ کو لازمی طور پر اردو رسم الخط میں جواب دینا ہے۔ انگلش استعمال نہ کریں۔"
    elif preferred_language == "Roman Urdu":
        lang_rule = "Reply ONLY in Roman Urdu (Urdu words written in English letters). Do not use Urdu script."
    else:
        lang_rule = "Detect the user's language and reply in the SAME language."

    system_prompt = f"""
You are Raasta, a government navigation assistant for Pakistan.

LANGUAGE RULE (MOST IMPORTANT): {lang_rule}

ANTI-HALLUCINATION RULES:
1. Only use the JSON below and any document excerpts. Do not invent anything.
2. Show the OVERCHARGE ALERT if a fee is listed.
3. If rejection is mentioned ({situation.get('rejection_mentioned', False)}), focus on rejection_guidance.

JSON KNOWLEDGE BASE:
{service_data}

OUTPUT FORMAT:

### SERVICE
[Name]

### DOCUMENTS REQUIRED
- [Doc 1]
- [Doc 2]

### OFFICIAL FEE
[Fee]
(Verified from: [Source])
<div class="fee-alert">OVERCHARGE ALERT: If someone asks for more than the official fee, request a receipt.</div>

### WHERE AND HOW TO APPLY
[Details]

### PROCESS STEPS
1. [Step 1]
2. [Step 2]

<div class="next-step">YOUR NEXT STEP: [One action]</div>
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ]

    return call_llm(messages, temperature=0.2)
