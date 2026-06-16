from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .forms import PostGenerationForm
from .models import GeneratedPost
from .services.orchestrator import generate_complete_post


def home(request):
    form = PostGenerationForm()
    recent_posts = GeneratedPost.objects.all()[:5]
    return render(request, "generator/home.html", {"form": form, "recent_posts": recent_posts})


@require_POST
def generate_post(request):
    form = PostGenerationForm(request.POST)

    if not form.is_valid():
        return JsonResponse({"success": False, "errors": form.errors}, status=400)

    topic = form.cleaned_data["topic"]
    platform = form.cleaned_data["platform"]
    tone = form.cleaned_data["tone"]
    image_style = form.cleaned_data["image_style"]

    result = generate_complete_post(
        topic=topic,
        platform=platform,
        tone=tone,
        image_style=image_style,
    )

    post = GeneratedPost.objects.create(
        topic=topic,
        platform=platform,
        tone=tone,
        image_style=image_style,
        caption=result.get("caption", ""),
        hashtags=" ".join(result.get("hashtags", [])),
        image_prompt=result.get("image_prompt", ""),
        image_file=result.get("image_file") or None,
        raw_response=result,
    )

    image_url = post.image_file.url if post.image_file else ""

    return JsonResponse({
        "success": True,
        "id": post.id,
        "topic": post.topic,
        "platform": post.get_platform_display(),
        "tone": post.get_tone_display(),
        "image_style": post.image_style,
        "caption": post.caption,
        "hashtags": result.get("hashtags", []),
        "image_prompt": post.image_prompt,
        "image_url": image_url,
        "provider": result.get("provider", "demo"),
    })
