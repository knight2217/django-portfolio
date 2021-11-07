# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:10:07 2021

@author: vader227
"""

from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    
]