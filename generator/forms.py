from django import forms
from .models import GeneratedPost


class PostGenerationForm(forms.ModelForm):
    class Meta:
        model = GeneratedPost
        fields = ["topic", "platform", "tone", "image_style"]
        widgets = {
            "topic": forms.TextInput(attrs={
                "placeholder": "Example: AI tools for students",
                "class": "form-control",
            }),
            "platform": forms.Select(attrs={"class": "form-control"}),
            "tone": forms.Select(attrs={"class": "form-control"}),
            "image_style": forms.TextInput(attrs={
                "placeholder": "Example: realistic, poster, minimal, cinematic",
                "class": "form-control",
            }),
        }
