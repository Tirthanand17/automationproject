from django.contrib import admin
from .models import GeneratedPost


@admin.register(GeneratedPost)
class GeneratedPostAdmin(admin.ModelAdmin):
    list_display = ("topic", "platform", "tone", "created_at")
    list_filter = ("platform", "tone", "created_at")
    search_fields = ("topic", "caption", "hashtags")
    readonly_fields = ("created_at", "updated_at")
