import base64
from uuid import uuid4

from django.conf import settings
from django.core.files.base import ContentFile
from google import genai


def gemini_text(prompt: str) -> str:
    if not settings.GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it in your .env file.")

    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model=settings.GEMINI_TEXT_MODEL,
        contents=prompt,
    )
    return (response.text or "").strip()


def gemini_image(prompt: str):
    if not settings.GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it in your .env file.")

    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model=settings.GEMINI_IMAGE_MODEL,
        contents=prompt,
    )

    candidates = getattr(response, "candidates", []) or []
    if not candidates:
        return None

    parts = getattr(candidates[0].content, "parts", []) or []
    for part in parts:
        inline_data = getattr(part, "inline_data", None)
        if not inline_data:
            continue

        file_bytes = inline_data.data
        if isinstance(file_bytes, str):
            file_bytes = base64.b64decode(file_bytes)

        extension = "png"
        mime_type = getattr(inline_data, "mime_type", "") or ""
        if "jpeg" in mime_type or "jpg" in mime_type:
            extension = "jpg"
        elif "webp" in mime_type:
            extension = "webp"

        filename = f"generated_{uuid4().hex}.{extension}"
        return filename, ContentFile(file_bytes, name=filename)

    return None
