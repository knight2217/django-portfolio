# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path("", views.hobby_index, name="hobby_index"),
    path("<int:pk>/", views.hobby_detail, name="hobby_detail"),
]
