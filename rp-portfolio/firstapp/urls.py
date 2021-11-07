# -*- coding: utf-8 -*-
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.firstapp, name='firstapp'),
]

