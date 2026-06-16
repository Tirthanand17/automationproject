from django.urls import path
from . import views

app_name = "generator"

urlpatterns = [
    path("", views.home, name="home"),
    path("generate/", views.generate_post, name="generate_post"),
]
