from .caption_agent import generate_caption
from .formatter_agent import format_final_post
from .hashtag_agent import generate_hashtags
from .image_agent import generate_image_file, generate_image_prompt


def generate_complete_post(topic: str, platform: str, tone: str, image_style: str):
    caption = generate_caption(topic=topic, platform=platform, tone=tone)
    hashtags = generate_hashtags(topic=topic, platform=platform)
    image_prompt = generate_image_prompt(topic=topic, platform=platform, image_style=image_style)
    image_output = generate_image_file(image_prompt=image_prompt)

    image_field_file = None
    image_file_name = None
    if image_output:
        image_file_name, image_field_file = image_output

    result = format_final_post(
        topic=topic,
        platform=platform,
        tone=tone,
        image_style=image_style,
        caption=caption,
        hashtags=hashtags,
        image_prompt=image_prompt,
        image_file_name=image_file_name,
    )

    result["image_file"] = image_field_file
    result["provider"] = "gemini" if image_field_file else "github_or_demo"
    return result
