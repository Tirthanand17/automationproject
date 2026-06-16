from django.conf import settings

from .gemini_client import gemini_text
from .github_models_client import github_chat


SYSTEM_PROMPT = """
You are Caption Agent, an expert social media copywriter.
Create clear, engaging, human-sounding captions.
Avoid fake claims, avoid overpromising, and keep the output ready to publish.
"""


def generate_caption(topic: str, platform: str, tone: str) -> str:
    user_prompt = f"""
Generate one high-quality caption.

Topic: {topic}
Platform: {platform}
Tone: {tone}

Rules:
- Keep it natural and human.
- Do not include hashtags.
- Do not include markdown headings.
- Make it suitable for the selected platform.
"""

    try:
        if settings.AI_PROVIDER == "gemini":
            return gemini_text(SYSTEM_PROMPT + "\n" + user_prompt)
        return github_chat(SYSTEM_PROMPT, user_prompt)
    except Exception:
        return (
            f"{topic} is changing the way people think, learn, and work. "
            "With the right approach, it can save time, improve creativity, and help users take smarter action."
        )
