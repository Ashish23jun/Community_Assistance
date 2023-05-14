from django.contrib import admin
from django.urls import path, include
from knowledge_hub import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index, name="home"),
    path("query", views.query, name="query"),
    path("ngo", views.ngo, name="ngo"),
]