import base64
from pathlib import Path
from uuid import uuid4

from django.conf import settings
from django.core.files.base import ContentFile
from google import genai


def gemini_text(prompt: str) -> str:
    """Generate text using Gemini."""
    if not settings.GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it in your .env file.")

    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model=settings.GEMINI_TEXT_MODEL,
        contents=prompt,
    )
    return (response.text or "").strip()


def gemini_image(prompt: str):
    """Generate an image using a Gemini image-capable model.

    Returns a Django ContentFile name/content tuple or None if no image bytes are returned.
    """
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

        image_bytes = inline_data.data
        if isinstance(image_bytes, str):
            image_bytes = base64.b64decode(image_bytes)

        extension = "png"
        mime_type = getattr(inline_data, "mime_type", "") or ""
        if "jpeg" in mime_type or "jpg" in mime_type:
            extension = "jpg"
        elif "webp" in mime_type:
            extension = "webp"

        filename = f"generated_{uuid4().hex}.{extension}"
        return filename, ContentFile(image_bytes)

    return None
