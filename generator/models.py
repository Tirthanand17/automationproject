from django.db import models


class GeneratedPost(models.Model):
    PLATFORM_CHOICES = [
        ("linkedin", "LinkedIn"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("x", "X"),
        ("general", "General"),
    ]

    TONE_CHOICES = [
        ("professional", "Professional"),
        ("friendly", "Friendly"),
        ("motivational", "Motivational"),
        ("funny", "Funny"),
        ("educational", "Educational"),
    ]

    topic = models.CharField(max_length=255)
    platform = models.CharField(max_length=30, choices=PLATFORM_CHOICES, default="general")
    tone = models.CharField(max_length=30, choices=TONE_CHOICES, default="professional")
    image_style = models.CharField(max_length=100, default="realistic")

    caption = models.TextField(blank=True)
    hashtags = models.TextField(blank=True, help_text="Space-separated hashtags")
    image_prompt = models.TextField(blank=True)
    image_file = models.ImageField(upload_to="generated_images/", blank=True, null=True)

    raw_response = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.topic} - {self.platform}"
