# Generated manually for the PostPilot AI MVP.

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GeneratedPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("topic", models.CharField(max_length=255)),
                ("platform", models.CharField(choices=[("linkedin", "LinkedIn"), ("instagram", "Instagram"), ("facebook", "Facebook"), ("x", "X"), ("general", "General")], default="general", max_length=30)),
                ("tone", models.CharField(choices=[("professional", "Professional"), ("friendly", "Friendly"), ("motivational", "Motivational"), ("funny", "Funny"), ("educational", "Educational")], default="professional", max_length=30)),
                ("image_style", models.CharField(default="realistic", max_length=100)),
                ("caption", models.TextField(blank=True)),
                ("hashtags", models.TextField(blank=True, help_text="Space-separated hashtags")),
                ("image_prompt", models.TextField(blank=True)),
                ("image_file", models.ImageField(blank=True, null=True, upload_to="generated_images/")),
                ("raw_response", models.JSONField(blank=True, default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
