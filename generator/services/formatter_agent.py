def format_final_post(topic, platform, tone, image_style, caption, hashtags, image_prompt, image_file_name=None):
    """Create a consistent final response shape for frontend and database."""
    return {
        "topic": topic,
        "platform": platform,
        "tone": tone,
        "image_style": image_style,
        "caption": caption.strip(),
        "hashtags": hashtags,
        "image_prompt": image_prompt.strip(),
        "image_file_name": image_file_name,
    }
