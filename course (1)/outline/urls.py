from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("course/<str:title>", views.topic_page, name="topic_page"),
    path("search/", views.search, name="search"),
    path("new/", views.new_page, name="new_page"),
    path("edit/<str:title>", views.edit_page, name="edit_page"),
    path("random/", views.random_page, name="random_page"),
]
