import io
import re


def extract_text_from_upload(uploaded_file):
    if uploaded_file is None:
        return "", ""

    name = uploaded_file.name.lower()
    raw = uploaded_file.read()

    if name.endswith(".pdf"):
        try:
            from pypdf import PdfReader
            reader = PdfReader(io.BytesIO(raw))
            pages = [p.extract_text() or "" for p in reader.pages]
            text = "\n".join(pages).strip()
            if text:
                return text, f"Extracted {len(text)} chars from {len(reader.pages)} pages."
            return "", "PDF has no text layer (scanned image)."
        except Exception as e:
            return "", f"Could not read PDF: {e}"

    if name.endswith((".png", ".jpg", ".jpeg")):
        return "", "Image uploaded. OCR not supported — try a PDF or describe it in chat."

    return "", "Unsupported file type."


def chunk_text(text, chunk_size=500, overlap=50):
    if not text:
        return []
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks


def _score_chunk(chunk, query_terms):
    chunk_lower = chunk.lower()
    return sum(1 for term in query_terms if term in chunk_lower)


def retrieve_relevant_chunks(text, query, top_k=3):
    if not text or not query:
        return text[:2000] if text else ""

    chunks = chunk_text(text)
    if not chunks:
        return ""

    query_terms = re.findall(r"\w+", query.lower())
    query_terms = [t for t in query_terms if len(t) > 2]
    if not query_terms:
        return chunks[0]

    scored = [(chunk, _score_chunk(chunk, query_terms)) for chunk in chunks]
    scored.sort(key=lambda x: x[1], reverse=True)

    top = [chunk for chunk, score in scored[:top_k] if score > 0]
    if not top:
        top = [chunk for chunk, _ in scored[:top_k]]
    return "\n\n---\n\n".join(top)
