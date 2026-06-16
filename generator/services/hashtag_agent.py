import re
from django.conf import settings

from .gemini_client import gemini_text
from .github_models_client import github_chat


SYSTEM_PROMPT = """
You are Hashtag Agent.
Generate relevant, clean, non-spammy hashtags for social media posts.
Return only hashtags separated by spaces.
"""


def _extract_hashtags(text: str):
    tags = re.findall(r"#[A-Za-z0-9_]+", text)
    clean_tags = []
    for tag in tags:
        if tag.lower() not in [t.lower() for t in clean_tags]:
            clean_tags.append(tag)
    return clean_tags[:10]


def generate_hashtags(topic: str, platform: str):
    user_prompt = f"""
Generate 6 to 10 hashtags.

Topic: {topic}
Platform: {platform}

Return only hashtags. No explanation.
"""

    try:
        if settings.AI_PROVIDER == "gemini":
            output = gemini_text(SYSTEM_PROMPT + "\n" + user_prompt)
        else:
            output = github_chat(SYSTEM_PROMPT, user_prompt)

        tags = _extract_hashtags(output)
        if tags:
            return tags
    except Exception:
        pass

    words = re.findall(r"[A-Za-z0-9]+", topic.title().replace(" ", ""))
    main_tag = "#" + ("".join(words) if words else "AI")
    return [main_tag, "#AI", "#Automation", "#ContentCreation", "#DigitalMarketing"]
