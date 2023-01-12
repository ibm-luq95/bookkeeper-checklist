# -*- coding: utf-8 -*-#

from django.urls import path
from manager.views import (
    UserCreateView,
    UserDetailsView,
    UserUpdateView,
)

app_name = "users"

urlpatterns = [
    path("create", UserCreateView.as_view(), name="create"),
    path("details/<uuid:pk>", UserDetailsView.as_view(), name="detail"),
    path("update/", UserUpdateView.as_view(), name="update"),
]
