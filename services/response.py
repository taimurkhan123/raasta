from services.llm import call_llm


def generate_response(user_query, situation, service_data):
    if situation.get("confidence", 0) < 0.7 or situation.get("service_id") == "unknown":
        return """
        **I want to make sure I give you the right information.** 🤔

        I'm not completely sure which specific service you need based on that description.
        Could you clarify? For example, are you looking to correct a CNIC, file an FIR, or get a certificate?
        """

    system_prompt = f"""
    You are Raasta, a highly helpful, structured government navigation assistant.
    The user is asking a question in {situation.get('language_detected', 'english')}.
    Match your response language to theirs (use Roman Urdu if they used Roman Urdu, or English).

    CRITICAL ANTI-HALLUCINATION RULES:
    1. Only use the provided JSON knowledge base. DO NOT invent steps, fees, URLs, or documents.
    2. If a fee is listed, you MUST show the "OVERCHARGE ALERT" warning.
    3. If the user mentions rejection ({situation.get('rejection_mentioned', False)}), focus entirely on the 'rejection_guidance' from the JSON.

    JSON KNOWLEDGE BASE:
    {service_data}

    OUTPUT FORMAT (Use Markdown styling exactly as shown):

    ### 🏛️ SERVICE
    [Service Name]

    ### 📋 DOCUMENTS REQUIRED
    - [Doc 1]
    - [Doc 2]

    ### 💰 OFFICIAL FEE
    **[Fee and Currency]**
    *(Verified from: [Source] on [Date])*
    <div class="fee-alert">⚠️ <b>OVERCHARGE ALERT:</b> If someone asks for more than the official listed fee, request an official receipt or check the official portal.</div>

    ### 📝 WHERE & HOW TO APPLY
    [Online/In-person details]

    ### 🔄 PROCESS STEPS
    1. [Step 1]
    2. [Step 2]

    <div class="next-step">🚀 YOUR NEXT STEP: [One single, highly actionable next step]</div>
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ]

    return call_llm(messages, temperature=0.2)
