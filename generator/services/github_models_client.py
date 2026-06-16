from django.conf import settings
from openai import OpenAI


def github_chat(system_prompt: str, user_prompt: str) -> str:
    """Call GitHub Models using the OpenAI-compatible client."""
    if not settings.GITHUB_TOKEN:
        raise RuntimeError("GITHUB_TOKEN is missing. Add it in your .env file.")

    client = OpenAI(
        base_url=settings.GITHUB_MODELS_BASE_URL,
        api_key=settings.GITHUB_TOKEN,
    )

    response = client.chat.completions.create(
        model=settings.GITHUB_MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.8,
        max_tokens=700,
    )

    return response.choices[0].message.content.strip()
