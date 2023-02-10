# -*- coding: utf-8 -*-#
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import LoginView

app_name = "auth"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]
