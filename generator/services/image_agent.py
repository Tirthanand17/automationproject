from django.conf import settings

from .gemini_client import gemini_image, gemini_text
from .github_models_client import github_chat


SYSTEM_PROMPT = """
You are Image Agent.
Create a detailed text-to-image prompt for a social media post visual.
The prompt should be safe, professional, and visually clear.
"""


def generate_image_prompt(topic: str, platform: str, image_style: str) -> str:
    user_prompt = f"""
Create one detailed image generation prompt.

Topic: {topic}
Platform: {platform}
Image style: {image_style}

Rules:
- Return only the prompt.
- Do not include markdown.
- Mention composition, lighting, mood, and details.
"""

    try:
        if settings.AI_PROVIDER == "gemini":
            return gemini_text(SYSTEM_PROMPT + "\n" + user_prompt)
        return github_chat(SYSTEM_PROMPT, user_prompt)
    except Exception:
        return (
            f"A {image_style} social media visual about {topic}, clean modern composition, "
            "professional lighting, high detail, suitable for digital marketing, no text overlay."
        )


def generate_image_file(image_prompt: str):
    """Try to generate an actual image. Returns Django ImageField-compatible file or None."""
    if settings.AI_PROVIDER != "gemini":
        return None

    try:
        generated = gemini_image(image_prompt)
        if generated:
            filename, content_file = generated
            return filename, content_file
    except Exception:
        return None

    return None
